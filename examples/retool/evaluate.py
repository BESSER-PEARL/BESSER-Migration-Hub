"""Reproduce the five-example Retool PARSER evaluation (paper section 6, RQ1 only).

This script measures Retool -> BUML (the parser) exclusively: Base (the raw
Retool CSV/GUI export) vs BUML (the parsed pivot). It does not run the
generator and does not measure BUML -> Retool (RQ2) at all - that is a
separate question, answered by `evaluate_generator.py` against an
independently-authored oracle BUML model, not against this script's own
parser output. Grading the generator against the parser's own pivot would
let a parser bug silently become the "ground truth" the generator is judged
against, so RQ1 and RQ2 are intentionally kept apart as separate scripts.

The source auditor deliberately does not call the migration parser.
Run from the repository: python examples/retool/evaluate.py
Base examples live under examples/retool/base_examples/exampleN/{data,gui}/.
The aggregate table is saved to evaluation/results.md; each example's own
parsed BUML pivot (project.py, pivot.pkl, inventory.json) is kept on disk
under examples/retool/buml_parser_result/exampleN/ for manual inspection/
comparison, not discarded in a temp dir.
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

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui
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


# Keyword -> action category, independently mirroring (not importing) the
# priority _BUTTON_MAP in migrator.parsers.retool.retool_rsx_parser, so the
# raw-export auditor can classify a button's CRUD/navigation intent the same
# way the parser does, without calling the parser.
_ACTION_KEYWORDS = [
    ('add', 'Add'), ('create', 'Add'), ('new', 'Add'), ('insert', 'Add'),
    ('save', 'Save'), ('edit', 'Save'), ('update', 'Save'), ('checkout', 'Save'), ('submit', 'Save'),
    ('delete', 'Delete'), ('remove', 'Delete'),
    ('back', 'Cancel'), ('cancel', 'Cancel'), ('close', 'Cancel'),
]


def _keyword_action(text):
    if not text:
        return None
    words = re.sub(r'([a-z])([A-Z])', r'\1 \2', text).lower()
    for keyword, action in _ACTION_KEYWORDS:
        if re.search(rf'(?<![a-z]){keyword}(?![a-z])', words):
            return action
    return None


def _owned_events(records, index):
    """Direct-child `Event` records of `records[index]`, found via each
    record's own `parents` ancestor-name list (already tracked by `tags()`'s
    nesting stack) rather than re-scanning raw text spans."""
    owner = records[index]
    depth = len(owner['parents'])
    events = []
    for record in records[index + 1:]:
        if len(record['parents']) <= depth:
            break
        if len(record['parents']) == depth + 1 and record['parents'][-1] == owner['tag'] and record['tag'] == 'Event':
            events.append(record)
    return events


def _button_action_type(records, index):
    """Classify a Button/Action tag's CRUD/navigation intent independently
    of the parser, mirroring its event-first priority (see
    retool_rsx_parser._event_signal/_classify_best): a triggered datasource
    query name is ground truth for CRUD intent, a widget show/hide event is
    structural, and only then does the caption get a keyword guess. Falls
    back to 'RunMethod' - the parser's own default for "no signal matched" -
    rather than None, so an unclassified button here and an unclassified
    button in the parsed pivot count as the same category."""
    owner = records[index]
    caption = owner['attributes'].get('text') or owner['attributes'].get('label')
    trigger_plugin_id = None
    widget_methods = []
    for event in _owned_events(records, index):
        ev_type = event['attributes'].get('type')
        method = event['attributes'].get('method')
        if ev_type == 'datasource' and method == 'trigger' and trigger_plugin_id is None:
            trigger_plugin_id = event['attributes'].get('pluginId')
        elif ev_type == 'widget':
            widget_methods.append(method)
    if trigger_plugin_id:
        action = _keyword_action(trigger_plugin_id)
        if action:
            return action
    if any(method in ('hide', 'close') for method in widget_methods):
        return 'Cancel'
    if any(method in ('show', 'open') for method in widget_methods):
        return 'Navigate'
    return _keyword_action(caption) or 'RunMethod'


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
    button_indices = [i for i, r in enumerate(records) if r['tag'] in {'Button', 'Action'}]
    buttons = [records[i] for i in button_indices]
    legacy_labels = [label for r in records for label in re.findall(r'actionButtonText:\s*"([^"]*)"', r['raw'])]
    legacy_actions = [(label, query) for r in records for label, query in
                      re.findall(r'\{\s*actionButtonText:\s*"([^"]*)".*?actionButtonQuery:\s*"([^"]*)"', r['raw'], re.DOTALL)]
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
    # Action types: no field in the raw export is literally named "action
    # type", but the information isn't absent either - a triggered query's
    # pluginId (e.g. "deleteProduct") and a widget show/hide Event's method
    # are both literal source attributes, and are the exact same evidence
    # the parser classifies from (see _button_action_type). So this is
    # computed here too, independently of the parser, rather than left N/A.
    # A Form's submit button (submit={true}) is excluded here even though
    # it's counted in Buttons/Labels above: the parser never classifies it
    # at all (_build_button returns None for it; it becomes Form.submit_label,
    # which has no actionType field), so Action types is specifically about
    # standalone Button widgets, and including submit buttons here would
    # compare against something BUML structurally cannot produce.
    classifiable = [i for i in button_indices if records[i]['attributes'].get('submit') != 'true']
    action_type_names = {_button_action_type(records, i) for i in classifiable}
    action_type_names |= {_keyword_action(query) or _keyword_action(label) or 'RunMethod'
                          for label, query in legacy_actions}
    metrics = {'Modules': 1, 'Screens': len(screens) + (0 if count['Screen'] else 1),
               'Bound entities': len(bound), 'Buttons': len(buttons) + len(legacy_labels),
               'Action types': len(action_type_names), 'Navigation': len(navigation), 'Forms': count['Form'],
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


def csv_inventory(folder, synthetic_columns=None, known_fk_columns=None):
    """synthetic_columns maps table name -> column names the generator added as
    boilerplate (e.g. a primary key for a table with no natural key); these are
    excluded from the Attributes count so it isn't inflated by generator output
    that was never present in, or derived from, the model.

    FK-shaped columns (see _fk_columns) are implicit associations: they are
    counted as Associations/Multiplicities, not Attributes, at every stage
    (Base, BUML, Target) so a column isn't an "attribute" in the source export
    and an "association" once parsed. `_fk_columns`'s naming-convention
    heuristic is the only option for raw source CSVs, but it can miss FK
    columns whose name doesn't resemble the referenced table's name (e.g. an
    association end role name that isn't just the class name). For generated
    output, the generator's own `schema.json` manifest marks `references`
    authoritatively; pass that in as `known_fk_columns` (table name -> column
    names) to use ground truth instead of re-guessing from column names."""
    synthetic_columns = synthetic_columns or {}
    known_fk_columns = known_fk_columns or {}
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
    for table_name, columns in known_fk_columns.items():
        fk.setdefault(table_name, set()).update(columns)
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
                    # Trust the parser's own marker (set at the one place that
                    # actually knows) for whether this label is a genuine
                    # source caption or an invented raw-id fallback, rather
                    # than guessing from label == name - that guess is
                    # specific to this parser's fallback shape and misfires
                    # on BUML models built any other way (e.g. an
                    # independently-authored oracle model, where routinely
                    # naming a button after its own label is not a sign of a
                    # missing caption). Absent on any non-parser-built Button.
                    record.update(label=widget.label, action_type=widget.actionType.name,
                                  synthetic_label=getattr(widget, '_synthetic_label', False))
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
              'Forms': count['Form'], 'Labels': sum(bool(w.get('label')) and not w.get('synthetic_label') for w in widgets if w['kind'] == 'Button') + sum(bool(w.get('submit_label')) for w in widgets if w['kind'] == 'Form'),
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
                if isinstance(widget, Button) and getattr(widget, '_synthetic_label', False):
                    # Non-metamodel marker (see retool_rsx_parser._build_button);
                    # the code builder has no field for it, so it must be
                    # reattached explicitly or Labels' count would silently
                    # change after this round-trip.
                    repairs.append(f'{variable}._synthetic_label = True')
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


def run_example(number, run, from_snapshots=False):
    name = f'example{number}'
    root = EXAMPLES / 'base_examples' / name
    data_dir = next(p for p in root.iterdir() if p.name.lower() == 'data')
    gui_dir = next(p for p in root.iterdir() if p.name.lower() == 'gui')
    out = EXAMPLES / 'buml_parser_result' / name
    out.mkdir(parents=True, exist_ok=True)
    data, rows = csv_inventory(data_dir)
    source = audit_gui(gui_dir, {t['table'] for t in data['tables']})
    dump(out / 'source_inventory.json', {'data': data, 'gui': source,
        'sha256': {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for folder in (data_dir, gui_dir) for p in sorted(folder.rglob('*')) if p.is_file()}})
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        if from_snapshots:
            domain, gui = pickle.loads((out / 'pivot.pkl').read_bytes())
            print('Recomputed audit from frozen baseline pivot; parser not rerun.')
        else:
            domain = retool_csv_to_buml(str(data_dir), module_name=name, rsx_dir=str(gui_dir))
            gui = retool_rsx_to_gui(str(gui_dir), module_name=name, domain_model=domain)
        pivot = pivot_inventory(domain, gui)
        serialize(domain, gui, out)
    (out / ('audit_refresh.log' if from_snapshots else 'pipeline.log')).write_text(log.getvalue(), encoding='utf-8')
    dump(out / 'inventory.json', pivot)
    parser_reference = data['counts'] | source['counts']
    result = {'example': name, 'run': run, 'parser': ratios(parser_reference, pivot['counts'], DATA_KEYS + GUI_KEYS),
              'source_events': source['events'], 'pivot_events': pivot['native_events'],
              'row_counts': {'source': {k: len(v) for k, v in rows.items()}},
              'source_tag_counts': source['tag_counts'], 'serialization_passed': True}
    result['frozen_baseline_reference'] = from_snapshots
    dump(out / 'results.json', result)
    report = f'# {name}: {run} parser evaluation (RQ1 only)\n\n'
    report += ('Generator evaluation (RQ2) is not measured here: see '
               '`evaluate_generator.py` / `generator_results.md`, which grades the '
               'generator against an independently-authored oracle BUML model '
               'instead of this script\'s own parser output.\n\n')
    report += '## Retool → BUML (RQ1)\n\n' + table(result['parser']) + '\n\n'
    report += f"Source/pivot event declarations: **{source['events']} / {pivot['native_events']}**. Button classifications are naming heuristics; they do not establish executable CRUD behavior.\n\n"
    report += f"Records present in source CSV (not instances recovered from BUML): `{result['row_counts']['source']}`.\n\n"
    report += '## Artifacts\n\n- `source_inventory.json`: file hashes, independent tag/header counts and source evidence.\n- `project.py`: executable combined model, with documented serializer repairs.\n- `pivot.pkl`: exact locally produced reference model (load only trusted local snapshots).\n- `inventory.json`: classes, relationships, screens, widgets, bindings.\n- `pipeline.log`, `results.json`: diagnostics and machine-readable results.\n\n'
    (out / 'README.md').write_text(report, encoding='utf-8')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=EXAMPLES / 'evaluation' / 'results.md')
    args = parser.parse_args()
    # Each example writes to buml_parser_result/exampleN/ (not a temp dir), so
    # the parsed BUML pivot (project.py, pivot.pkl, inventory.json) is kept
    # on disk for manual comparison.
    results = [run_example(number, 'current') for number in range(1, 6)]
    lines = ['# Retool parser element counts (RQ1 only)', '',
             'Base = original Retool CSV/GUI exports; BUML = parsed pivot (output of the '
             'migration parser). Counts use the current parser. This file does not measure '
             'the generator (BUML -> Retool, RQ2): see `generator_results.md`, which grades '
             'the generator against an independently-authored oracle BUML model rather than '
             'the parser\'s own output measured here.', '',
             '| Example | Element | Base | BUML |',
             '|---|---|---:|---:|']
    display = lambda value: 'N/A' if value is None else str(value)
    for result in results:
        for key in DATA_KEYS + GUI_KEYS:
            source = result['parser'][key]['reference']
            pivot = result['parser'][key]['output']
            lines.append(f"| {result['example']} | {key} | {display(source)} | {display(pivot)} |")
    lines += ['', 'Counting notes:', '',
              '- N/A means the source export does not declare a comparable element (e.g. CSV has no '
              'generalization/enumeration syntax). Associations/Multiplicities are not N/A: a `*_id` '
              'column whose prefix names another table in the same export is counted as an implicit '
              'association at every stage (Base, BUML), via the same naming convention the '
              'parser itself uses to build associations - not just once the parser has run.',
              '- Attributes count scalar properties/columns, excluding columns classified as an implicit '
              'association (see above). Two source FK columns are counted as associations at every stage, '
              'not as attributes anywhere, so Base and BUML no longer disagree on their classification.',
              '- Buttons include each Form\'s submit control: BUML models it as `Form.submit_label`, not a '
              'separate Button widget, but it renders as a standalone `<Button>` in the source export, so '
              'it is counted here at every stage (no example form sets `show_cancel`, so this is exact, '
              'not an approximation). Labels count authored button/submit captions only; ID-derived '
              'captions synthesized for icon-only buttons are excluded from these counts.',
              '- Screens include named views/wrappers, dialogs, and implicit main pages. Navigation counts '
              'explicit operations, excluding script-inferred navigation. Action types count distinct '
              'CRUD/navigation categories classified from a button\'s wired-up Events first (a triggered '
              'query name like `deleteProduct`, or a widget `show`/`hide` event) and only falling back to '
              'its caption text when no event is conclusive. No field in the raw export is literally named '
              '"action type", but the evidence it is classified from (a query name, an event method) is '
              'real, literal source data, so Base computes this independently of the parser (same keyword '
              'map, applied directly to the raw tags) rather than reporting `N/A` - it is not a parser-only '
              'concept, just a parser-only field name. Whether the generator preserves this classification '
              'is a generator question, not measured here - see `generator_results.md`.',
              '- This follows the parser measurement in paper section 6. It measures export structure, not '
              'live Retool execution or layout equivalence.', '',
              'Regenerate: `python examples/retool/evaluate.py`. This table is saved here; each '
              'example\'s own parsed BUML pivot is kept under '
              '`buml_parser_result/exampleN/` for manual comparison.', '']
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Saved counts for five examples to {args.output}')


if __name__ == '__main__':
    main()
