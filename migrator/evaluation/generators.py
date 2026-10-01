"""Rebuild parser-derived B-UML references and evaluate APEX/ReTool/ServiceNow exports.

Run with --rebuild-reference to reparse the five available APEX SQL examples.
Without that flag, generators consume the saved, shared reference models.
"""
import argparse
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import pickle
import re
import runpy
import sys

from .oracle_apex_parser import ROOT, DATA_KEYS, GUI_KEYS, calls, ddl_inventory, gui_source_inventory, data_inventory
from .oracle_apex_inventory import inventory
from .service_now import service_now_output

from .retool_parser import audit_gui, csv_inventory, serialize, tags
from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui
from migrator.generators.retool import RetoolGenerator
from migrator.generators.sql.oracle_apex_app_generator import OracleApexFullAppGenerator

SCENARIOS = [f'example{number}' for number in range(1, 6)]
REFERENCE_ROOT = ROOT / 'evaluation_replication/generator_evaluation/buml_ground_truth'
OUTPUT_ROOT = ROOT / 'evaluation_replication/generator_evaluation'
PLATFORM_FOLDERS = {'APEX': 'oracle_apex', 'ReTool': 'retool', 'ServiceNow': 'servicenow'}
PLATFORM_NAMES = {'APEX': 'Oracle APEX', 'ReTool': 'ReTool', 'ServiceNow': 'ServiceNow'}


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


def rebuild(scenario):
    source = ROOT / 'evaluation_replication/examples/oracle_apex' / scenario
    folder = REFERENCE_ROOT / scenario
    folder.mkdir(parents=True, exist_ok=True)
    log = io.StringIO()
    with redirect_stdout(log):
        domain = oracle_apex_to_buml(str(source / 'data'), module_name=scenario)
        gui = oracle_apex_to_gui(str(source / 'screens'), module_name=scenario, domain_model=domain)
    source_data = ddl_inventory(source / 'data')
    audit = data_inventory(domain, source_data)
    # The coverage convention excludes identities and FK columns at every stage.
    for cls in domain.get_classes():
        cls.attributes = {attribute for attribute in cls.attributes if attribute.name in audit['classes'][cls.name]}
    serialize(domain, gui, folder)
    reloaded = runpy.run_path(str(folder / 'project.py'))
    if inventory(gui) != inventory(reloaded['gui_model']):
        raise AssertionError(f'GUI serialization changed the reference for {scenario}')
    (folder / 'models.pkl').write_bytes(pickle.dumps({'domain': domain, 'gui': gui}))
    (folder / 'parser.log').write_text(log.getvalue(), encoding='utf-8')
    provenance = {'scenario': scenario, 'origin': 'improved Oracle APEX parser; not independently authored',
                  'source': source.relative_to(ROOT).as_posix(), 'excluded_attributes': audit['excluded_attributes'],
                  'source_files': {file.relative_to(source).as_posix(): hashlib.sha256(file.read_bytes()).hexdigest()
                                   for file in sorted(source.rglob('*.sql'))}}
    dump(folder / 'reference.json', provenance)
    dump(folder / 'inventory.json', {'data': audit, 'gui': inventory(gui)})
    (folder / 'README.md').write_text(
        '# Recreated B-UML reference\n\nParser-derived from the five current APEX SQL examples. '
        'This is not an independently authored oracle. `project.py` is executable and checked '
        'against the original model inventory; `models.pkl` preserves the exact shared graph. '
        'Platform identity and misclassified FK attributes are excluded consistently.\n', encoding='utf-8')


def reference_counts(domain, gui):
    return {'Entities': len(domain.get_classes()),
            'Attributes': sum(len(cls.attributes) for cls in domain.get_classes()),
            'Associations': len(domain.associations),
            'Multiplicities': sum(len(association.ends) for association in domain.associations),
            'Generalizations': len(domain.generalizations),
            'Enumerations': sum(type(element).__name__ == 'Enumeration' for element in domain.types),
            **inventory(gui)['counts']}


def retool_output(domain, gui, folder, scenario):
    generator = RetoolGenerator(domain, gui_model=gui, app_name=scenario,
                                output_dir=str(folder / 'buml_generator_result'), include_sample_data=True)
    generator.generate()
    output = folder / 'buml_generator_result'
    schema = json.loads((output / 'csv/schema.json').read_text())
    data, _ = csv_inventory(output / 'csv',
        synthetic_columns={table['name']: {column['name'] for column in table['columns'] if column['synthetic']}
                           for table in schema['tables']},
        known_fk_columns={table['name']: {column['name'] for column in table['columns'] if column['references']}
                          for table in schema['tables']})
    gui_audit = audit_gui(output / scenario, {table['table'] for table in data['tables']})
    # RetoolGenerator exports events, but does not export Button.actionType.
    # Caption guesses are not generated action semantics and cannot earn coverage.
    gui_audit['caption_inferred_action_type_count'] = gui_audit['counts']['Action types']
    gui_audit['counts']['Action types'] = 0
    # Count exported captions directly; equality to widget ID is not evidence of a synthetic caption.
    captions = [record['attributes'].get('text') or record['attributes'].get('label')
                for file in (output / scenario / 'src').glob('*.rsx')
                for record in tags(file.read_text(encoding='utf-8')) if record['tag'] == 'Button']
    counts = data['counts'] | gui_audit['counts']
    counts.update(Generalizations=0, Enumerations=0, Labels=sum(bool(caption) for caption in captions))
    return counts, {'data': data, 'gui': gui_audit, 'captions': captions, 'warnings': generator.warnings}


def apex_output(domain, gui, folder, scenario):
    app = OracleApexFullAppGenerator(domain, gui_model=gui, output_dir=str(folder / 'buml_generator_result'),
                                    app_name=scenario, app_id=8000 + int(scenario[-1]))
    path = Path(app.generate())
    text = path.read_text(encoding='utf-8')
    # Audit the actual embedded Supporting Objects SQL, decoded from export assignments.
    ddl = supporting_objects_sql(text)
    ddl_folder = folder / 'audit/ddl'
    ddl_folder.mkdir(parents=True, exist_ok=True)
    (ddl_folder / 'embedded.sql').write_text(ddl, encoding='utf-8')
    data = ddl_inventory(ddl_folder)
    # Match input scalar attributes to exported columns; generated identities/FKs are excluded.
    matched = sum(app._ddl._col_name(attribute.name).lower() in data['tables'].get(
        app._ddl._table_name(cls.name).lower(), {}) for cls in domain.get_classes() for attribute in cls.attributes)
    data['counts']['Attributes'] = matched
    pages = folder / 'audit/pages'
    pages.mkdir(parents=True, exist_ok=True)
    for old_page in pages.glob('page_*.sql'):
        old_page.unlink()
    markers = list(re.finditer(r'^prompt\s+--application/pages/page_\d+\s*$', text, re.MULTILINE))
    scaffolding = []
    for index, marker in enumerate(markers):
        section = text[marker.start():markers[index + 1].start() if index + 1 < len(markers) else len(text)]
        declarations = calls(section).get('create_page', [])
        if not declarations:
            continue
        page = declarations[0]
        if page.get('id') in {'0', '1', '101', '9999'}:
            scaffolding.append(page)
            continue
        (pages / f"page_{int(page['id']):05}.sql").write_text(section, encoding='utf-8')
    gui_audit = gui_source_inventory(pages, data['tables'])
    return data['counts'] | gui_audit['counts'], {'data': data, 'gui': gui_audit,
                                                'excluded_platform_pages': scaffolding,
                                                'warnings': app.warnings}


def supporting_objects_sql(text):
    """Read assignments without treating semicolons inside SQL strings as terminators."""
    return '\n'.join(value.replace("''", "'") for block in re.findall(
        r"wwv_flow_imp\.g_varchar2_table\(\d+\)\s*:=\s*((?:'(?:''|[^'])*'|[^';])*);", text)
        for value in re.findall(r"'((?:''|[^'])*)'", block))


def report(results, platforms):
    lines = ['# Generator evaluation from recreated APEX B-UML references', '',
             'All platforms use the same saved input models, derived from the improved APEX parser '
             'on `export_to_buml/example1–5`. These are parser-derived references, not independent ground truth.', '',
             'Counts describe exported structure, not execution in a live platform. Attributes exclude '
             'platform identity/FK columns. Generated APEX global/home/login scaffolding is excluded. '
             'APEX uses `OracleApexFullAppGenerator`, the generator selected by the web application. '
             'APEX action types are reconstructed classifications from exported button evidence; their ratio '
             'does not establish preservation of action semantics. ReTool action types count as zero because '
             'the generator does not export Button.actionType; caption guesses do not count as generated actions. '
             'Retool captions are counted directly from RSX. ServiceNow is evaluated for data models only, '
             'using exported Table, scalar column, ReferenceColumn, and related-list declarations. '
             'Association-end counts do not verify cardinality bounds.', '']
    lines += ['The APEX application generator renders each B-UML screen and its Form, Button, '
              'InputField, and class-backed DataList widgets directly. Unbound forms have no '
              'invented persistence. Unsupported behavior is recorded in the target inventories.', '']
    latex = []
    for model, keys in [('Data model', DATA_KEYS), ('GUI model', GUI_KEYS)]:
        model_platforms = [platform for platform in platforms if model == 'Data model' or platform != 'ServiceNow']
        lines += [f'## {model}', '', '| Platform | Element | Input B-UML | Generated |', '|---|---|---:|---:|']
        for platform in model_platforms:
            for key in keys:
                reference = sum(result['reference'][key] for result in results if result['platform'] == platform)
                generated = sum(result['generated'][key] for result in results if result['platform'] == platform)
                lines.append(f'| {PLATFORM_NAMES[platform]} | {key} | {reference} | {generated} |')
        lines.append('')
        latex += [f'% {model}', r'\begin{tabular}{l' + 'r' * len(keys) + '}', r'\toprule',
                  'Platform & ' + ' & '.join(keys) + r' \\', r'\midrule']
        for platform in model_platforms:
            cells = []
            for key in keys:
                reference = sum(result['reference'][key] for result in results if result['platform'] == platform)
                generated = sum(result['generated'][key] for result in results if result['platform'] == platform)
                percent = '--' if reference == 0 or (key == 'Action types' and platform == 'APEX') else f'{generated / reference * 100:.1f}\\%'
                cells.append(r'\makecell{' + f'{generated}/{reference}' + r' \\ (' + percent + ')}')
            latex.append(PLATFORM_NAMES[platform] + ' & ' + ' & '.join(cells) + r' \\')
        latex += [r'\bottomrule', r'\end{tabular}', '']
    lines += ['## By application', '', '| Platform | Application | Element | Input B-UML | Generated |', '|---|---|---|---:|---:|']
    for result in results:
        lines.extend(f"| {PLATFORM_NAMES[result['platform']]} | {result['scenario']} | {key} | {result['reference'][key]} | {result['generated'][key]} |"
                     for key in DATA_KEYS + (GUI_KEYS if result['platform'] != 'ServiceNow' else []))
    output = OUTPUT_ROOT / 'recreated_reference_results.md'
    output.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    (OUTPUT_ROOT / 'recreated_reference_tables.tex').write_text('\n'.join(latex), encoding='utf-8')
    data_table = [r'\begin{table}[t]', r'\centering',
                  r'\caption{Aggregate data-model generator fidelity. Values are reported as',
                  r'generated/input B-UML elements.}', r'\label{tab:generator-data-model}',
                  r'\scriptsize', r'\setlength{\tabcolsep}{4pt}', r'\renewcommand{\arraystretch}{1.05}',
                  r'\begin{tabular}{lrrrr}', r'\toprule',
                  r'Platform & Ent. & Attr. & Assoc. & Mult. \\', r'\midrule']
    for platform in ['ReTool', 'APEX', 'ServiceNow']:
        if platform not in platforms:
            continue
        data_table.append(PLATFORM_NAMES[platform])
        for index, key in enumerate(DATA_KEYS[:4]):
            reference = sum(result['reference'][key] for result in results if result['platform'] == platform)
            generated = sum(result['generated'][key] for result in results if result['platform'] == platform)
            percentage = f'{100 * generated / reference:g}\\%' if reference else 'N/A'
            data_table.append(f'& {generated}/{reference} ({percentage})' + (r' \\' if index == 3 else ''))
    data_table += [r'\bottomrule', r'\end{tabular}', r'\vspace{0.3em}',
                   r'\begin{minipage}{0.95\linewidth}', r'\footnotesize',
                   r'\textit{Note:} Ent. = entities; Attr. = attributes; Assoc. = associations;',
                   r'Mult. = multiplicities.', r'\end{minipage}', r'\end{table}']
    (OUTPUT_ROOT / 'recreated_reference_data_table.tex').write_text('\n'.join(data_table) + '\n', encoding='utf-8')
    for platform in platforms:
        platform_results = [result for result in results if result['platform'] == platform]
        dump(OUTPUT_ROOT / PLATFORM_FOLDERS[platform] / 'results.json', platform_results)
        path = OUTPUT_ROOT / PLATFORM_FOLDERS[platform] / 'results.md'
        path.parent.mkdir(parents=True, exist_ok=True)
        platform_lines = lines
        if platform == 'ServiceNow':
            platform_lines = lines[:lines.index('## GUI model')] + lines[lines.index('## By application'):]
        path.write_text('\n'.join(line for line in platform_lines if not line.startswith('| ') or
                                  line.startswith('| Platform') or line.startswith(f'| {PLATFORM_NAMES[platform]} |')) + '\n', encoding='utf-8')
    print(f'Saved combined results: {output}')
    for platform in platforms:
        keys = DATA_KEYS if platform == 'ServiceNow' else GUI_KEYS
        print(platform, {key: (sum(result['generated'][key] for result in results if result['platform'] == platform),
                               sum(result['reference'][key] for result in results if result['platform'] == platform))
                         for key in keys})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--rebuild-reference', action='store_true')
    parser.add_argument('--platform', choices=list(PLATFORM_NAMES), nargs='+', default=list(PLATFORM_NAMES))
    args = parser.parse_args()
    args.platform = list(dict.fromkeys(args.platform))
    results = []
    for scenario in SCENARIOS:
        if args.rebuild_reference:
            rebuild(scenario)
        for platform in args.platform:
            # Fresh graph for each platform; one generator cannot mutate the other's input.
            reference_bytes = (REFERENCE_ROOT / scenario / 'models.pkl').read_bytes()
            models = pickle.loads(reference_bytes)
            domain, gui = models['domain'], models['gui']
            folder = OUTPUT_ROOT / PLATFORM_FOLDERS[platform] / scenario
            folder.mkdir(parents=True, exist_ok=True)
            reference = reference_counts(domain, gui)
            log = io.StringIO()
            with redirect_stdout(log):
                generated, audit = {'APEX': apex_output, 'ReTool': retool_output,
                                    'ServiceNow': service_now_output}[platform](domain, gui, folder, scenario)
            result = {'scenario': scenario, 'platform': platform, 'reference': reference, 'generated': generated,
                      'reference_sha256': hashlib.sha256(reference_bytes).hexdigest()}
            dump(folder / 'results.json', result)
            dump(folder / 'oracle_inventory.json', {'counts': reference, 'gui': inventory(gui)})
            dump(folder / 'target_inventory.json', audit)
            (folder / 'generator.log').write_text(log.getvalue(), encoding='utf-8')
            results.append(result)
    if len(args.platform) > 1:
        for scenario in SCENARIOS:
            pair = [result['reference'] for result in results if result['scenario'] == scenario]
            assert all(reference == pair[0] for reference in pair), f'Different platform denominators for {scenario}'
    # A single-platform rerun must retain the other platform's compatible results.
    platforms = list(args.platform)
    for platform in PLATFORM_NAMES:
        if platform in platforms:
            continue
        saved = OUTPUT_ROOT / PLATFORM_FOLDERS[platform] / 'results.json'
        if saved.exists():
            previous = json.loads(saved.read_text(encoding='utf-8'))
            expected = {result['scenario']: result['reference_sha256'] for result in results}
            if len(previous) == len(SCENARIOS) and all(
                    result.get('reference_sha256') == expected.get(result['scenario']) for result in previous):
                results.extend(previous)
                platforms.append(platform)
    report(results, [platform for platform in PLATFORM_NAMES if platform in platforms])


if __name__ == '__main__':
    main()
