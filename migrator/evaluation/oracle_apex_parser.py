"""Reproduce APEX parser coverage with an independent SQL source inventory.

Run: python -m migrator.evaluation.oracle_apex_parser
The five native APEX examples also supply the generator reference models.
"""
import argparse
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import pickle
import re

from .oracle_apex_inventory import ROOT, GUI_KEYS, inventory
from .retool_parser import serialize
from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui

DATA_KEYS = ['Entities', 'Attributes', 'Associations', 'Multiplicities', 'Generalizations', 'Enumerations']
TOKEN = re.compile(r"--[^\n]*|/\*[\s\S]*?\*/|'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"|[A-Za-z_$#][\w$#]*|\d+|=>|[^\s]")


def tokens(text):
    return [token for token in TOKEN.findall(text) if not token.startswith(('--', '/*'))]


def identifier(token):
    return token.strip('"').lower()


def groups(stream, start):
    """Read a parenthesized list, splitting commas only at its outer depth."""
    depth, result, current = 1, [], []
    index = start + 1
    while index < len(stream):
        token = stream[index]
        if token == '(':
            depth += 1
        elif token == ')':
            depth -= 1
            if depth == 0:
                result.append(current)
                return result, index + 1
        if token == ',' and depth == 1:
            result.append(current)
            current = []
        else:
            current.append(token)
        index += 1
    raise ValueError('Unclosed SQL argument list')


def ddl_inventory(folder):
    tables, foreign_keys = {}, set()
    for path in sorted(folder.rglob('*.sql')):
        stream = tokens(path.read_text(encoding='utf-8'))
        lower = [identifier(token) for token in stream]
        for index in range(len(stream) - 3):
            if lower[index:index + 2] == ['create', 'table'] and stream[index + 3] == '(':
                table = lower[index + 2]
                definitions, _ = groups(stream, index + 3)
                columns = {}
                for definition in definitions:
                    if not definition:
                        continue
                    words = [identifier(token) for token in definition]
                    if words[0] in {'constraint', 'primary', 'foreign', 'unique', 'check'}:
                        if 'foreign' in words and 'references' in words:
                            fk = words.index('foreign')
                            cols, _ = groups(definition, fk + 2)
                            foreign_keys.add((table, tuple(identifier(col[0]) for col in cols),
                                              words[words.index('references') + 1]))
                        continue
                    columns[words[0]] = {'type': words[1], 'identity': 'identity' in words}
                    if 'references' in words:
                        foreign_keys.add((table, (words[0],), words[words.index('references') + 1]))
                if table in tables and tables[table] != columns:
                    raise ValueError(f'Conflicting CREATE TABLE definitions for {table}')
                tables[table] = columns
            if lower[index:index + 2] == ['alter', 'table']:
                table = lower[index + 2]
                end = index + 3
                while end < len(stream) and stream[end] not in {';', '/'}:
                    end += 1
                statement = stream[index:end]
                words = lower[index:end]
                if 'foreign' in words and 'references' in words:
                    fk = words.index('foreign')
                    cols, _ = groups(statement, fk + 2)
                    foreign_keys.add((table, tuple(identifier(col[0]) for col in cols),
                                      words[words.index('references') + 1]))
    fk_columns = {(table, column) for table, columns, _ in foreign_keys for column in columns}
    scalar = [(table, column) for table, columns in tables.items() for column, details in columns.items()
              if not details['identity'] and (table, column) not in fk_columns]
    return {'counts': {'Entities': len(tables), 'Attributes': len(scalar),
                       'Associations': len(foreign_keys), 'Multiplicities': 2 * len(foreign_keys),
                       'Generalizations': 0, 'Enumerations': 0},
            'tables': tables, 'scalar_columns': scalar,
            'foreign_keys': sorted(foreign_keys)}


def calls(text):
    """Read APEX declarations without calling any parser extraction helper."""
    stream = tokens(text)
    result = {}
    for index in range(len(stream) - 3):
        if stream[index].lower() != 'wwv_flow_imp_page' or stream[index + 1] != '.' or stream[index + 3] != '(':
            continue
        arguments, _ = groups(stream, index + 3)
        values = {}
        for argument in arguments:
            if len(argument) < 3 or argument[1] != '=>':
                continue
            key = argument[0].lower().removeprefix('p_')
            expression = argument[2:]
            strings = [token[1:-1].replace("''", "'") for token in expression if token.startswith("'")]
            if strings:
                values[key] = '\n'.join(strings)
                if key == 'attributes':
                    values['plugin_attributes'] = dict(zip(strings[::2], strings[1::2]))
            elif len(expression) == 1:
                values[key] = expression[0]
            elif len(expression) == 6 and expression[:4] == ['wwv_flow_imp', '.', 'id', '(']:
                values[key] = expression[4]
        result.setdefault(stream[index + 2].lower(), []).append(values)
    return result


def source_action(button):
    name = button.get('button_name', '').upper()
    action = {'CREATE': 'Add', 'SAVE': 'Save', 'DELETE': 'Delete', 'CANCEL': 'Cancel'}.get(name)
    if action:
        return action
    action = {'INSERT': 'Add', 'UPDATE': 'Save', 'DELETE': 'Delete'}.get(button.get('database_action', '').upper())
    if action:
        return action
    if 't-Button--danger' in button.get('button_template_options', ''):
        return 'Delete'
    return 'Save' if button.get('button_is_hot') == 'Y' else 'Cancel'


def gui_source_inventory(folder, table_names):
    counts = dict.fromkeys(GUI_KEYS, 0)
    pages, bound, actions = [], set(), set()
    for path in sorted(folder.glob('page_*.sql')):
        declarations = calls(path.read_text(encoding='utf-8'))
        for page in declarations.get('create_page', []):
            buttons = [button for button in declarations.get('create_page_button', []) if button.get('button_name')]
            items = declarations.get('create_page_item', [])
            plugs = declarations.get('create_page_plug', [])
            processes = declarations.get('create_page_process', [])
            editable = any(item.get('display_as') not in {None, 'NATIVE_HIDDEN', 'NATIVE_DISPLAY_ONLY'} for item in items)
            native_forms = sum(plug.get('plug_source_type') == 'NATIVE_FORM' for plug in plugs)
            form_count = native_forms or int(
                any(process.get('process_type', '').startswith('NATIVE_FORM_') for process in processes)
                or (editable and (page.get('page_mode') == 'MODAL'
                                  or any(button.get('button_action') == 'SUBMIT' for button in buttons))))
            nav = sum(button.get('button_action') == 'REDIRECT_PAGE' and
                      bool(re.search(r'f\?p=[^:]+:(?:\d+|&[\w.]+):', button.get('button_redirect_url', ''), re.I))
                      for button in buttons)
            nav += sum(branch.get('branch_type') == 'BRANCH_TO_STEP' and branch.get('branch_action', '').isdigit()
                       or bool(re.search(r'f\?p=[^:]+:(?:\d+|&[\w.]+):', branch.get('branch_action', ''), re.I))
                       for branch in declarations.get('create_page_branch', []))
            counts['Screens'] += 1
            counts['Buttons'] += len(buttons)
            counts['Forms'] += form_count
            counts['Labels'] += sum(bool(button.get('button_image_alt') or button.get('button_name')) for button in buttons)
            counts['Navigation'] += nav
            actions.update(source_action(button) for button in buttons)
            for region in plugs + processes:
                query = region.get('plug_source', '')
                # A table name in HTML documentation or a displayed SQL example
                # does not establish a region's data binding.
                if re.match(r'\s*(?:select|with)\b', query, re.I):
                    query = re.sub(r"'(?:''|[^'])*'|--[^\n]*|/\*[\s\S]*?\*/", ' ', query)
                    bound.update(table for table in table_names if
                                 re.search(r'(?<![\w$#])"?' + re.escape(table) + r'"?(?![\w$#])', query, re.I))
                declared_table = region.get('query_table') or region.get('plugin_attributes', {}).get('table_name')
                if declared_table and declared_table.lower() in table_names:
                    bound.add(declared_table.lower())
            pages.append({'file': path.name, 'id': page.get('id'), 'name': page.get('name'),
                          'buttons': len(buttons), 'forms': form_count, 'navigation': nav})
    counts['Bound entities'], counts['Action types'] = len(bound), len(actions)
    return {'counts': counts, 'pages': pages, 'bound_entities': sorted(bound), 'action_types': sorted(actions)}


def data_inventory(domain, source):
    classes = domain.get_classes()
    table_for_class = {''.join(word.capitalize() for word in table.split('_')): table
                       for table in source['tables']}
    scalar = {tuple(column) for column in source['scalar_columns']}
    fk_columns = {(table, column) for table, columns, _ in source['foreign_keys'] for column in columns}
    raw_classes, covered_classes, excluded = {}, {}, {}
    for cls in classes:
        table = table_for_class.get(cls.name)
        raw_classes[cls.name] = sorted(attribute.name for attribute in cls.attributes)
        covered_classes[cls.name] = []
        for attribute in sorted(cls.attributes, key=lambda attribute: attribute.name):
            column = attribute.name.lower()
            if (table, column) in scalar:
                covered_classes[cls.name].append(attribute.name)
                continue
            details = source['tables'].get(table, {}).get(column, {})
            reason = ('platform_identity' if details.get('identity') else
                      'foreign_key' if (table, column) in fk_columns else 'not_a_source_attribute')
            excluded.setdefault(cls.name, []).append({'name': attribute.name, 'reason': reason})
    return {'counts': {'Entities': len(classes), 'Attributes': sum(map(len, covered_classes.values())),
                       'Associations': len(domain.associations),
                       'Multiplicities': sum(len(association.ends) for association in domain.associations),
                       'Generalizations': len(domain.generalizations),
                       'Enumerations': sum(type(element).__name__ == 'Enumeration' for element in domain.types)},
            'classes': covered_classes, 'raw_classes': raw_classes, 'excluded_attributes': excluded}


def percentage(extracted, source):
    return '--' if source == 0 else f'{100 * extracted / source:.1f}%'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-root', type=Path, default=ROOT / 'evaluation_replication/examples/oracle_apex')
    parser.add_argument('--output', type=Path, default=ROOT / 'evaluation_replication/parser_evaluation/oracle_apex')
    args = parser.parse_args()
    results = []
    for number in range(1, 6):
        name = f'example{number}'
        source, output = args.input_root / name, args.output / name
        output.mkdir(parents=True, exist_ok=True)
        source_data = ddl_inventory(source / 'data')
        source_gui = gui_source_inventory(source / 'screens', source_data['tables'])
        log = io.StringIO()
        with redirect_stdout(log):
            domain = oracle_apex_to_buml(str(source / 'data'), module_name=name)
            gui = oracle_apex_to_gui(str(source / 'screens'), module_name=name, domain_model=domain)
        if domain is None or gui is None:
            raise RuntimeError(f'Missing model for {source}')
        result = {'example': name, 'input': str(source.resolve()), 'source_data': source_data,
                  'source_gui': source_gui, 'extracted_data': data_inventory(domain, source_data), 'extracted_gui': inventory(gui),
                  'source_files': {file.relative_to(source).as_posix(): hashlib.sha256(file.read_bytes()).hexdigest()
                                   for file in sorted(source.rglob('*.sql'))}}
        expected = {''.join(word.capitalize() for word in table.split('_')):
                    {column for source_table, column in source_data['scalar_columns'] if source_table == table}
                    for table in source_data['tables']}
        result['attribute_differences'] = {
            cls: {'extra': sorted(set(result['extracted_data']['classes'].get(cls, [])) - columns),
                  'missing': sorted(columns - set(result['extracted_data']['classes'].get(cls, [])))}
            for cls, columns in expected.items()
            if set(result['extracted_data']['classes'].get(cls, [])) != columns}
        (output / 'inventory.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        (output / 'parser.log').write_text(log.getvalue(), encoding='utf-8')
        (output / 'models.pkl').write_bytes(pickle.dumps({'domain': domain, 'gui': gui}))
        serialize(domain, gui, output)
        results.append(result)
    lines = ['# Oracle APEX parser coverage', '', f'Input dataset: `{args.input_root.relative_to(ROOT).as_posix() if args.input_root.is_relative_to(ROOT) else args.input_root}`.', '',
             'Values are extracted/source. These five applications also supply the shared generator references.', '',
             'Source counts are audited independently from SQL declarations; extracted counts come from actual model objects.', '',
             'Attributes exclude FK columns and identity columns, including multiline and ON NULL identity declarations. '
             'Extracted attributes count only matching source scalar columns; retained platform identities, '
             'misclassified FK columns, and attributes absent from the source are excluded and recorded separately in the inventories. '
             'Associations count declared FKs; multiplicities count their two ends. SQL checks are not B-UML enum declarations.', '',
             'GUI source counts include skipped pages. Bound entities count distinct declared schema tables referenced by '
             'region SQL/table metadata or native form-process table metadata; explanatory HTML and displayed code samples are excluded. '
             'Extracted bound entities include real class references on widgets and their data sources. Navigation counts explicit in-app button redirects '
             'and branches, including parameterized page targets; script-inferred navigation is excluded. '
             'Forms count native form regions or legacy/custom form pages with form-process or editable/submit evidence. '
             'Labels count button/submit captions, with button-name fallbacks. Action types count distinct classified button '
             'categories per app; a Form submit control has no Button.actionType in B-UML.', '']
    latex = []
    for model, keys in [('data', DATA_KEYS), ('gui', GUI_KEYS)]:
        lines += [f'## {model.capitalize()} model', '', '| Application | ' + ' | '.join(keys) + ' |',
                  '|---|' + '---:|' * len(keys)]
        latex += [r'\multirow{6}{*}{Oracle APEX}']
        for number, result in enumerate(results, 1):
            values = [f"{result['extracted_' + model]['counts'][key]}/{result['source_' + model]['counts'][key]}" for key in keys]
            lines.append('| ' + result['example'] + ' | ' + ' | '.join(values) + ' |')
            latex.append(f'& App~{number} & ' + ' & '.join(values) + r' \\')
        values = [percentage(sum(result['extracted_' + model]['counts'][key] for result in results),
                             sum(result['source_' + model]['counts'][key] for result in results)) for key in keys]
        lines += ['| Total | ' + ' | '.join(values) + ' |', '']
        latex += ['& Total & ' + ' & '.join(value.replace('%', r'\%') for value in values) + r' \\', '']
    (args.output / 'results.md').write_text('\n'.join(lines), encoding='utf-8')
    (args.output / 'oracle_apex_rows.tex').write_text('\n'.join(latex), encoding='utf-8')
    full_tables = args.output / 'parser_tables.tex'
    if full_tables.exists():
        blocks = iter('\n'.join(latex).strip().split('\n\n'))
        updated, count = re.subn(
            r'\\multirow\{6\}\{\*\}\{Oracle APEX\}[\s\S]*?(?=\\midrule|\\bottomrule)',
            lambda match: next(blocks) + '\n', full_tables.read_text(encoding='utf-8'))
        if count != 2:
            raise ValueError('Expected two Oracle APEX blocks in parser_tables.tex')
        full_tables.write_text(updated, encoding='utf-8')
    coverage = {key: percentage(sum(result['extracted_gui']['counts'][key] for result in results),
                               sum(result['source_gui']['counts'][key] for result in results)).replace('%', r'\%')
                for key in GUI_KEYS}
    omitted_screens = sum(result['source_gui']['counts']['Screens'] - result['extracted_gui']['counts']['Screens']
                          for result in results)
    paragraph = (
        f"For Oracle APEX, the parser achieves {coverage['Screens']} screen coverage, "
        f"{coverage['Buttons']} button and {coverage['Labels']} label coverage, "
        f"{coverage['Action types']} button action-type coverage, and {coverage['Forms']} form coverage "
        f"on the five evaluated SQL exports. Bound entity coverage is {coverage['Bound entities']}: "
        r'declared report tables and form-process tables are resolved to B-UML class references. '
        f"Navigation coverage is {coverage['Navigation']}, since the current parser does not construct navigation actions. "
        f'The {omitted_screens} omitted screens are excluded by the page-ID and '
        r'page-name filtering rules, which skip pages such as home, global, and login pages; '
        r'App~1 also loses its Basic Collections page because its ID is 1. '
        r'Buttons and forms on omitted pages are consequently absent from B-UML. '
        r'A primary form submit control is represented by \texttt{Form.submit\_label} '
        r'rather than a standalone \texttt{Button}, which can reduce the number of distinct '
        r'button action types retained in the model.' + '\n')
    (args.output / 'oracle_apex_gui_paragraph.tex').write_text(paragraph, encoding='utf-8')
    if full_tables.exists():
        updated = re.sub(r'For Oracle APEX,[\s\S]*?(?=\n\\begin\{table\*\})',
                         lambda match: paragraph + '\n', full_tables.read_text(encoding='utf-8'))
        full_tables.write_text(updated, encoding='utf-8')
    print('\n'.join(lines))
    print(f'Saved report, replacement LaTeX rows, and parsed models to {args.output}')


if __name__ == '__main__':
    main()
