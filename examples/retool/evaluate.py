"""Reproduce the five-example Retool evaluation (paper section 6).

The source/target auditor deliberately does not call the migration parser.
Run from the repository: python examples/retool/evaluate.py
Only the counts table is retained; pipeline artifacts use a temporary directory.
"""
import argparse
import ast
from collections import Counter
import contextlib
import csv
import hashlib
import html
import importlib.metadata
import io
import json
from pathlib import Path
import pickle
import re
import runpy
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui
from migrator.generators.retool import RetoolGenerator
from besser.utilities.buml_code_builder import domain_model_to_code, gui_model_to_code
from besser.BUML.metamodel.gui.graphical_ui import Button, Form, DataList, InputField

EXAMPLES = Path(__file__).resolve().parent
INPUTS = {'TextInput', 'TextArea', 'RichText', 'Password', 'NumberInput', 'Slider',
          'Checkbox', 'Switch', 'Select', 'RadioGroup', 'MultiSelect', 'Date',
          'DateTime', 'Time', 'FileButton', 'FileUpload', 'DateRange', 'Tags'}
DATA_KEYS = ['Entities', 'Attributes', 'Associations', 'Multiplicities', 'Generalizations', 'Enumerations']
GUI_KEYS = ['Modules', 'Screens', 'Bound entities', 'Buttons', 'Action types', 'Navigation',
            'Forms', 'Labels', 'DataLists', 'DataSources', 'Input fields']


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def tags(text):
    """Independent lexical audit; retain raw evidence and source line numbers.

    No JavaScript is evaluated. Quoted and brace-delimited attributes may
    contain angle brackets. This auditor is intentionally not the parser API.
    """
    position = 0
    stack = []
    while position < len(text):
        match = re.search(r'<(/?)([A-Za-z][\w.$]*)\b', text[position:])
        if not match:
            return
        begin = position + match.start()
        end = position + match.end()
        quote = None
        braces = 0
        while end < len(text):
            char = text[end]
            if quote:
                if char == '\\':
                    end += 2
                    continue
                if char == quote:
                    quote = None
            elif char in '\"\'`':
                quote = char
            elif char == '{':
                braces += 1
            elif char == '}':
                braces -= 1
            elif char == '>' and braces == 0:
                break
            end += 1
        raw = text[begin:end + 1]
        name = match[2]
        if match[1]:
            if stack and stack[-1] == name:
                stack.pop()
        else:
            attrs = {}
            # Literal strings/booleans needed by the counting policy only.
            for prop in re.finditer(r'([\w]+)\s*=\s*("(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'|\{(?:true|false)\})', raw):
                value = prop[2]
                attrs[prop[1]] = html.unescape(value[1:-1])
            yield {'tag': name, 'attributes': attrs, 'raw': raw,
                   'line': text.count('\n', 0, begin) + 1, 'parents': list(stack)}
            if not raw.rstrip().endswith('/>'):
                stack.append(name)
        position = end + 1


def audit_gui(folder, table_names):
    records = []
    visited = []
    def visit(file, ancestors=()):
        relative = file.relative_to(folder).as_posix()
        if relative in ancestors:
            raise ValueError('Include cycle in audit: ' + relative)
        visited.append(relative)
        for record in tags(file.read_text(encoding='utf-8-sig')):
            record['file'] = relative
            if record['tag'] == 'Include':
                target = (file.parent / record['attributes']['src']).resolve()
                if not target.is_relative_to(folder.resolve()):
                    raise ValueError('Include outside GUI folder')
                visit(target, ancestors + (relative,))
            else:
                records.append(record)
    visit(folder / 'main.rsx')
    count = Counter(r['tag'] for r in records)
    buttons = [r for r in records if r['tag'] in {'Button', 'Action'}]
    legacy_labels = [label for r in records for label in re.findall(r'actionButtonText:\s*"([^"]*)"', r['raw'])]
    screens = [r for r in records if r['tag'] in {'Screen', 'Modal', 'ModalFrame'} or
               (r['tag'] == 'View' and not re.fullmatch(r'View\s+\d+', r['attributes'].get('viewKey', r['attributes'].get('id', ''))))]
    navigation = [r for r in records if r['tag'] == 'Event' and
                  r['attributes'].get('method') in {'show', 'hide', 'open', 'close', 'navigateTo', 'setCurrentView'}]
    tables = [r for r in records if r['tag'] in {'Table', 'TableLegacy'}]
    sql_tables = {}
    for file in sorted((folder / 'lib').glob('*.sql')):
        match = re.search(r'\bFROM\s+([\w."`\[\]]+)', file.read_text(encoding='utf-8-sig'), re.I)
        if match:
            sql_tables[file.stem] = match[1].split('.')[-1].strip('"`[]').lower()
    bound = set()
    for r in records:
        if r['tag'] in {'Table', 'TableLegacy', 'Chart', 'PlotlyChart', 'Series', 'Select'}:
            for query, table in sql_tables.items():
                if re.search(r'\b' + re.escape(query) + r'\b', r['raw']) and table in table_names:
                    bound.add(table)
    # Binding coverage uses CSV-backed SQL tables, not missing external tables.
    def authored_caption(r):
        # Icon-only buttons without a source caption get an ID-derived one (parser
        # fallback and generator re-serialization); exclude that boilerplate here.
        caption = r['attributes'].get('text') or r['attributes'].get('label')
        return caption if caption and caption != r['attributes'].get('id') else None
    metrics = {'Modules': 1, 'Screens': len(screens) + (0 if count['Screen'] else 1),
               'Bound entities': len(bound), 'Buttons': len(buttons) + len(legacy_labels),
               'Action types': None, 'Navigation': len(navigation), 'Forms': count['Form'],
               'Labels': sum(bool(authored_caption(r)) for r in buttons) + sum(bool(v) for v in legacy_labels),
               'DataLists': len(tables), 'DataSources': len(tables),
               'Input fields': sum(count[t] for t in INPUTS)}
    ids = {r['attributes'].get('id') for r in records}
    unresolved = []
    for record in records:
        for key, value in record['attributes'].items():
            if '{{' not in value:
                continue
            for symbol in sorted(set(re.findall(r'\b([A-Za-z_$][\w$]*)\.(?:data|value|selectedRow)\b', value)) - ids):
                if symbol not in {'self', 'item', 'currentSourceRow', 'currentRow', 'i', 'utils', 'localStorage', 'retoolContext'}:
                    unresolved.append({'file': record['file'], 'line': record['line'],
                                       'widget': record['attributes'].get('id'), 'property': key, 'symbol': symbol})
    return {'counts': metrics, 'tag_counts': dict(sorted(count.items())), 'elements': records,
            'screen_evidence': screens, 'navigation_evidence': navigation,
            'bound_tables': sorted(bound), 'sql_primary_tables': sql_tables,
            'visited_files': visited, 'events': count['Event'],
            'unresolved_expression_references': unresolved}


def _stems_match(a, b):
    """Singular/plural tolerant match between two lower-case table stems
    (mirrors migrator.parsers.retool.retool_csv_parser._stems_match)."""
    if a == b:
        return True
    for x, y in ((a, b), (b, a)):
        if x + 's' == y or x + 'es' == y or (x.endswith('y') and x[:-1] + 'ies' == y):
            return True
    return False


def _fk_columns(tables):
    """Columns ending in `_id` whose prefix names another table in this same
    export are an implicit (naming-convention) association, not a plain
    scalar attribute - independently of whether the parser recognises them.
    This mirrors the parser's own FK heuristic so the Base/BUML/Target counts
    classify the same column the same way."""
    stems = {t['table'].lower() for t in tables}
    fk = {}
    for t in tables:
        own = t['table'].lower()
        pk = next((c for c in t['columns'] if c.lower() == 'id'), None)
        if pk is None:
            pk = next((c for c in t['columns'] if c.lower().endswith('_id')
                       and _stems_match(c.lower()[:-3], own)), None)
        for c in t['columns']:
            lower = c.lower()
            if lower == (pk or '').lower() or not lower.endswith('_id'):
                continue
            prefix = lower[:-3]
            if any(_stems_match(prefix, s) for s in stems if s != own):
                fk.setdefault(t['table'], set()).add(c)
    return fk


def csv_inventory(folder, synthetic_columns=None):
    """synthetic_columns maps table name -> column names the generator added as
    boilerplate (e.g. a primary key for a table with no natural key); these are
    excluded from the Attributes count so it isn't inflated by generator output
    that was never present in, or derived from, the model.

    FK-shaped columns (see _fk_columns) are implicit associations: they are
    counted as Associations/Multiplicities, not Attributes, at every stage
    (Base, BUML, Target) so a column isn't an "attribute" in the source export
    and an "association" once parsed."""
    synthetic_columns = synthetic_columns or {}
    tables = []
    rows = {}
    for file in sorted(folder.glob('*.csv')):
        with file.open(encoding='utf-8-sig', newline='') as stream:
            reader = csv.DictReader(stream)
            records = list(reader)
            tables.append({'table': file.stem, 'columns': reader.fieldnames, 'rows': len(records), 'file': file.name})
            rows[file.stem] = records
    boilerplate = sum(len(synthetic_columns.get(t['table'], ())) for t in tables)
    fk = _fk_columns(tables)
    fk_count = sum(len(cols) for cols in fk.values())
    return {'tables': tables, 'counts': {'Entities': len(tables),
            'Attributes': sum(len(t['columns']) for t in tables) - boilerplate - fk_count,
            'Associations': fk_count, 'Multiplicities': fk_count * 2,
            'Generalizations': 0, 'Enumerations': 0}}, rows


def pivot_inventory(domain, gui):
    def field_details(field):
        return {'name': field.name, 'type': field.field_type.name, 'label': field.label,
                'default': field.default_value, 'required': field.required,
                'options': [{'label': o.label, 'value': o.value} for o in (field.options or [])]}
    classes = [{'name': c.name, 'attributes': [{'name': a.name, 'type': a.type.name, 'id': a.is_id}
                for a in sorted(c.attributes, key=lambda a: a.name)]} for c in sorted(domain.get_classes(), key=lambda c: c.name)]
    associations = [{'name': a.name, 'ends': [{'name': e.name, 'type': e.type.name,
                     'multiplicity': str(e.multiplicity)} for e in sorted(a.ends, key=lambda e: e.name)]}
                    for a in sorted(domain.associations, key=lambda a: a.name)]
    screens, widgets, bindings, action_types = [], [], set(), set()
    event_count = navigation_count = 0
    for module in sorted(gui.modules, key=lambda m: m.name):
        for screen in sorted(module.screens, key=lambda s: s.name):
            screens.append({'module': module.name, 'name': screen.name, 'main': screen.is_main_page})
            for widget in sorted(screen.view_elements, key=lambda w: w.name):
                record = {'screen': screen.name, 'name': widget.name, 'kind': type(widget).__name__}
                record['events'] = []
                for event in sorted(getattr(widget, 'events', set()), key=lambda e: e.name):
                    event_count += 1
                    actions = []
                    for action in sorted(event.actions, key=lambda a: a.name):
                        target = getattr(action, 'target_screen', None)
                        actions.append({'name': action.name, 'kind': type(action).__name__,
                                        'target': target.name if target else None})
                        navigation_count += type(action).__name__ == 'Transition'
                    record['events'].append({'name': event.name, 'type': event.event_type.name, 'actions': actions})
                if isinstance(widget, Button):
                    record.update(label=widget.label, action_type=widget.actionType.name)
                    action_types.add(widget.actionType.name)
                if isinstance(widget, Form):
                    record.update(title=widget.title, submit_label=widget.submit_label,
                                  fields=[f.name for f in sorted(widget.inputFields, key=lambda f: f.name)],
                                  field_details=[field_details(f) for f in sorted(widget.inputFields, key=lambda f: f.name)])
                if isinstance(widget, InputField):
                    record['field_details'] = field_details(widget)
                if type(widget).__name__ == 'Text':
                    record['content'] = widget.content
                if isinstance(widget, DataList):
                    record['sources'] = [{'name': s.name, 'fields': list(s.field_names or [])}
                                         for s in sorted(widget.list_sources, key=lambda s: s.name)]
                binding = getattr(widget, 'data_binding', None)
                concept = getattr(binding, 'domain_concept', None)
                if concept:
                    record['binding'] = concept.name
                    bindings.add(concept.name)
                widgets.append(record)
    count = Counter(w['kind'] for w in widgets)
    counts = {'Entities': len(classes), 'Attributes': sum(len(c['attributes']) for c in classes),
              'Associations': len(associations), 'Multiplicities': sum(len(a['ends']) for a in associations),
              'Generalizations': len(domain.generalizations),
              'Enumerations': sum(type(t).__name__ == 'Enumeration' for t in domain.types),
              'Modules': len(gui.modules), 'Screens': len(screens), 'Bound entities': len(bindings),
              # Each Form's submit control renders as a standalone <Button> in the
              # export (Base/Target), but BUML models it as Form.submit_label, not
              # a separate Button widget - count it here too so Buttons isn't an
              # artifact of that bucketing (no example form sets show_cancel, so
              # one implicit button per Form is exact, not an approximation).
              'Buttons': count['Button'] + count['Form'], 'Action types': len(action_types), 'Navigation': navigation_count,
              'Forms': count['Form'], 'Labels': sum(bool(w.get('label')) and w.get('label') != w.get('name') for w in widgets if w['kind'] == 'Button') + sum(bool(w.get('submit_label')) for w in widgets if w['kind'] == 'Form'),
              'DataLists': count['DataList'], 'DataSources': sum(len(w.get('sources', [])) for w in widgets),
              'Input fields': count['InputField'] + sum(len(w.get('fields', [])) for w in widgets)}
    return {'counts': counts, 'classes': classes, 'associations': associations,
            'screens': screens, 'widgets': widgets, 'bound_entities': sorted(bindings),
            'action_types': sorted(action_types), 'native_events': event_count}


def serialize(domain, gui, folder):
    """Store exact pivot and readable Python; transparently repair builder losses."""
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'pivot.pkl').write_bytes(pickle.dumps((domain, gui)))
    domain_model_to_code(domain, str(folder / 'domain_model.py'))
    gui_model_to_code(gui, str(folder / 'gui_model.py'), domain_model=domain)
    content = (folder / 'domain_model.py').read_text(encoding='utf-8') + '\n' + (folder / 'gui_model.py').read_text(encoding='utf-8')
    tree = ast.parse(content)
    variables = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            for kw in node.value.keywords:
                if kw.arg == 'name' and isinstance(kw.value, ast.Constant):
                    variables.setdefault(kw.value.value, []).append(node.targets[0].id)
    repairs = []
    for module in sorted(gui.modules, key=lambda m: m.name):
        for screen in sorted(module.screens, key=lambda s: s.name):
            for widget in sorted(screen.view_elements, key=lambda w: w.name):
                candidates = variables.get(widget.name, [])
                if not candidates:
                    continue
                variable = candidates.pop(0)
                if isinstance(widget, Form):
                    for key in ('title', 'submit_label'):
                        repairs.append(f'{variable}.{key} = {getattr(widget, key)!r}')
                if isinstance(widget, (Form, DataList)) and getattr(widget, 'data_binding', None):
                    cls = widget.data_binding.domain_concept
                    repairs.append(f'{variable}.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name({cls.name!r}))')
                if isinstance(widget, DataList):
                    for source in widget.list_sources:
                        repairs.append(f'next(s for s in {variable}.list_sources if s.name == {source.name!r}).field_names = {list(source.field_names or [])!r}')
                events = sorted(getattr(widget, 'events', set()), key=lambda e: e.name)
                if events:
                    repairs.append(f'{variable}.events = set()')
                    for event in events:
                        actions = []
                        for action in sorted(event.actions, key=lambda a: a.name):
                            target = action.target_screen.name
                            actions.append(f'Transition(name={action.name!r}, target_screen=next(s for m in gui_model.modules for s in m.screens if s.name == {target!r}), triggered_by={variable})')
                        repairs.append(f'{variable}.events.add(Event(name={event.name!r}, event_type=EventType.{event.event_type.name}, actions={{{", ".join(actions)}}}))')
    content += '\nfrom besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition\n'
    content += '\n# Restore fields omitted by the installed BESSER code builder.\n' + '\n'.join(repairs) + '\n'
    (folder / 'project.py').write_text(content, encoding='utf-8')
    namespace = runpy.run_path(str(folder / 'project.py'))
    equal = pivot_inventory(domain, gui) == pivot_inventory(namespace['domain_model'], namespace['gui_model'])
    dump(folder / 'serialization.json', {'builder_repairs': repairs, 'inventory_equal_after_python_reload': equal,
                                        'generator_reference': 'project.py reloaded and inventory checked'})
    if not equal:
        raise AssertionError('Python pivot inventory changed on reload')


def ratios(reference, output, keys):
    return {key: {'reference': reference.get(key), 'output': output.get(key),
                  'percent': round(100 * output[key] / reference[key], 2)
                  if reference.get(key) and output.get(key) is not None else None} for key in keys}


def table(metrics):
    return '\n'.join(['| Element | Reference | Output | Coverage |', '|---|---:|---:|---:|'] +
                     [f"| {k} | {v['reference'] if v['reference'] is not None else 'unknown'} | {v['output'] if v['output'] is not None else 'unknown'} | {str(v['percent']) + '%' if v['percent'] is not None else 'N/A'} |" for k, v in metrics.items()])


def run_example(number, run, from_snapshots=False, output_root=None):
    name = f'example{number}'
    root = EXAMPLES / name
    data_dir = next(p for p in root.iterdir() if p.name.lower() == 'data')
    gui_dir = next(p for p in root.iterdir() if p.name.lower() == 'gui')
    out = Path(output_root) / name if output_root else root / 'evaluation' / run
    out.mkdir(parents=True, exist_ok=True)
    data, rows = csv_inventory(data_dir)
    source = audit_gui(gui_dir, {t['table'] for t in data['tables']})
    dump(out / 'source_inventory.json', {'data': data, 'gui': source,
        'sha256': {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for folder in (data_dir, gui_dir) for p in sorted(folder.rglob('*')) if p.is_file()}})
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        if from_snapshots:
            domain, gui = pickle.loads((out / 'retool_to_buml' / 'pivot.pkl').read_bytes())
            print('Recomputed audit from frozen baseline pivot; parser not rerun.')
        else:
            domain = retool_csv_to_buml(str(data_dir), module_name=name, rsx_dir=str(gui_dir))
            gui = retool_rsx_to_gui(str(gui_dir), module_name=name, domain_model=domain)
        pivot = pivot_inventory(domain, gui)
        serialize(domain, gui, out / 'retool_to_buml')
        namespace = runpy.run_path(str(out / 'retool_to_buml' / 'project.py'))
        domain, gui = namespace['domain_model'], namespace['gui_model']
        generator = RetoolGenerator(domain, gui_model=gui, app_name=name,
                                    output_dir=str(out / 'buml_to_retool'), rows=rows)
        paths, archive = generator.generate()
        schema_manifest = json.loads((out / 'buml_to_retool' / 'csv' / 'schema.json').read_text())
        synthetic_columns = {t['name']: {c['name'] for c in t['columns'] if c['synthetic']} for t in schema_manifest['tables']}
        target_data, target_rows = csv_inventory(out / 'buml_to_retool' / 'csv', synthetic_columns=synthetic_columns)
        target_gui = audit_gui(out / 'buml_to_retool' / name, {t['table'] for t in target_data['tables']})
        roundtrip = retool_rsx_to_gui(archive, module_name=name, domain_model=domain)
    (out / ('audit_refresh.log' if from_snapshots else 'pipeline.log')).write_text(log.getvalue(), encoding='utf-8')
    dump(out / 'retool_to_buml' / 'inventory.json', pivot)
    dump(out / 'buml_to_retool' / 'inventory.json', {'data': target_data, 'gui': target_gui})
    dump(out / 'roundtrip_inventory.json', pivot_inventory(domain, roundtrip))
    parser_reference = data['counts'] | source['counts']
    target_counts = target_data['counts'] | target_gui['counts']
    # Associations/Multiplicities now come from the same FK-naming heuristic
    # csv_inventory applies to Base and BUML (see _fk_columns), so they are
    # genuine counts here too, not forced zeros. CSV has no native
    # generalization/enum declarations, so those stay zero.
    target_counts.update(Generalizations=0, Enumerations=0, **{'Action types': 0})
    result = {'example': name, 'run': run, 'parser': ratios(parser_reference, pivot['counts'], DATA_KEYS + GUI_KEYS),
              'generator': ratios(pivot['counts'], target_counts, DATA_KEYS + GUI_KEYS),
              'warnings': generator.warnings, 'source_events': source['events'],
              'pivot_events': pivot['native_events'], 'generated_events': target_gui['events'],
              'row_counts': {'source': {k: len(v) for k, v in rows.items()}, 'target': {k: len(v) for k, v in target_rows.items()}},
              'source_tag_counts': source['tag_counts'], 'serialization_passed': True}
    result['generated_unresolved_expression_references'] = target_gui['unresolved_expression_references']
    result['frozen_baseline_reference'] = from_snapshots
    source_cells = retained_cells = 0
    missing_cells = []
    for name_, records in rows.items():
        target_records = target_rows[name_]
        for row_number, record in enumerate(records):
            for column, value in record.items():
                source_cells += 1
                if row_number < len(target_records) and target_records[row_number].get(column) == value:
                    retained_cells += 1
                else:
                    missing_cells.append({'table': name_, 'row': row_number + 1, 'column': column})
    result['supplementary'] = {'source_cells': source_cells, 'retained_cells': retained_cells,
                               'changed_or_missing_cells': missing_cells,
                               'csv_schema_manifest_references': sum(bool(c['references']) for t in schema_manifest['tables'] for c in t['columns'])}
    dump(out / 'results.json', result)
    (out.parent / 'README.md').write_text(
        f'# {name}: saved pipeline evaluations\n\n'
        'Start with [the updated evaluation](improved/README.md). '
        'It includes both migration directions and links to the generated artifacts.\n\n'
        '- [Baseline](baseline/README.md)\n'
        '- [Updated pipeline](improved/README.md)\n'
        '- [Shared protocol and aggregate findings](../../evaluation/README.md)\n', encoding='utf-8')
    report = f'# {name}: {run} pipeline evaluation\n\n'
    report += 'Method and limitations: [shared evaluation protocol](../../../evaluation/README.md).\n\n'
    report += '## Retool → BUML (RQ1)\n\n' + table(result['parser']) + '\n\n'
    report += '## BUML → Retool (RQ2)\n\n' + table(result['generator']) + '\n\n'
    report += f"Source/pivot/generated event declarations: **{source['events']} / {pivot['native_events']} / {target_gui['events']}**. Button classifications are naming heuristics; they do not establish executable CRUD behavior.\n\n"
    report += f"Records supplied separately from CSV: `{result['row_counts']}`. These are not instances recovered from BUML.\n\n"
    report += f"Supplementary accounting: **{retained_cells}/{source_cells}** original CSV cells retained exactly. The schema manifest contains **{result['supplementary']['csv_schema_manifest_references']}** FK references, without enforcing them in CSV.\n\n"
    report += '## Artifacts\n\n- `source_inventory.json`: file hashes, independent tag/header counts and source evidence.\n- `retool_to_buml/project.py`: executable combined model, with documented serializer repairs.\n- `retool_to_buml/pivot.pkl`: exact locally produced reference model (load only trusted local snapshots).\n- `retool_to_buml/inventory.json`: classes, relationships, screens, widgets, bindings.\n- `buml_to_retool/csv/`: generated records and supplementary schema manifest.\n- `buml_to_retool/' + name + '.zip`: generated Toolscript archive; matching folder alongside it.\n- `roundtrip_inventory.json`: supplementary reparse check; not the generator ground truth.\n- `pipeline.log`, `results.json`: diagnostics and machine-readable results.\n\n'
    report += '## Generator warnings\n\n' + '\n'.join('- ' + w for w in generator.warnings) + '\n'
    report += '\n## Unresolved generated expressions\n\n'
    report += ('\n'.join(f"- `{r['file']}:{r['line']}`: `{r['widget']}.{r['property']}` refers to undeclared `{r['symbol']}`." for r in target_gui['unresolved_expression_references'])
               or 'No unresolved references found by the limited `.data` / `.value` / `.selectedRow` identifier audit.') + '\n'
    (out / 'README.md').write_text(report, encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=EXAMPLES / 'evaluation' / 'results.md')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='retool-evaluation-') as workdir:
        results = [run_example(number, 'current', output_root=workdir) for number in range(1, 6)]
    lines = ['# Retool pipeline element counts', '',
             'Base = original Retool CSV/GUI exports; BUML = parsed pivot supplied to the generator; '
             'Target = generated Retool CSV/GUI exports. Counts use the current parser and generator.', '',
             '| Example | Element | Base | BUML | Target |',
             '|---|---|---:|---:|---:|']
    display = lambda value: 'N/A' if value is None else str(value)
    for result in results:
        for key in DATA_KEYS + GUI_KEYS:
            source = result['parser'][key]['reference']
            pivot = result['parser'][key]['output']
            target = result['generator'][key]['output']
            lines.append(f"| {result['example']} | {key} | {display(source)} | {display(pivot)} | {display(target)} |")
    lines += ['', 'Counting notes:', '',
              '- N/A means the source export does not declare a comparable element (e.g. CSV has no '
              'generalization/enumeration syntax). Associations/Multiplicities are not N/A: a `*_id` '
              'column whose prefix names another table in the same export is counted as an implicit '
              'association at every stage (Base, BUML, Target), via the same naming convention the '
              'parser itself uses to build associations - not just once the parser has run. Target '
              'counts exclude supplementary `schema.json` constraints.',
              '- Attributes count scalar properties/columns, excluding columns classified as an implicit '
              'association (see above). Two source FK columns are counted as associations at every stage, '
              'not as attributes anywhere, so Base/BUML/Target no longer disagree on their classification. '
              'Synthetic primary-key columns the generator adds for tables with no natural key are also '
              'excluded from the Attributes count, since they are generator boilerplate, not model- or '
              'source-derived data.',
              '- Buttons include each Form\'s submit control: BUML models it as `Form.submit_label`, not a '
              'separate Button widget, but it renders as a standalone `<Button>` in the export, so it is '
              'counted here at every stage (no example form sets `show_cancel`, so this is exact, not an '
              'approximation). Labels count authored button/submit captions only; ID-derived captions '
              'synthesized for icon-only buttons are excluded from these counts rather than inflating '
              'BUML/Target.',
              '- Screens include named views/wrappers, dialogs, and implicit main pages. Navigation counts '
              'explicit operations, excluding script-inferred navigation. Action types is a genuine, '
              'one-directional gap, not a counting artifact: the parser classifies each button\'s CRUD/'
              'navigation intent into a BUML enum from its query/label text (`N/A` in Base because the '
              'source export has no such field to classify from), but the generator never serializes '
              '`Button.actionType` back into the output - the generated RSX carries the button\'s executable '
              'event/plugin wiring, but not this classification, so Target is always 0.',
              '- This follows the separate parser/generator measurements in paper section 6. It measures '
              'export structure, not live Retool execution or layout equivalence.', '',
              'Regenerate: `python examples/retool/evaluate.py`. Only this table is saved; intermediate '
              'models and exports are temporary.', '']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Saved counts for five examples to {args.output}')


if __name__ == '__main__':
    main()
