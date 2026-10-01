"""Parse five APEX SQL examples and inventory the actual resulting B-UML objects.

Run with python -m migrator.evaluation.oracle_apex_inventory.
Use --input-root for another directory containing example1–5/data and screens.
This checks parser output; it does not replace the independent generator oracle.
"""
import argparse
from collections import Counter
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import pickle
import sys

ROOT = Path(__file__).resolve().parents[2]

from besser.BUML.metamodel.gui.graphical_ui import Button, Form, Screen, ViewContainer
from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
from migrator.parsers.oracle_apex.oracle_apex_gui import _all_calls, oracle_apex_to_gui

GUI_KEYS = ['Screens', 'Bound entities', 'Buttons', 'Action types',
            'Navigation', 'Forms', 'Labels']


def inventory(gui):
    modules = gui.modules.values() if isinstance(gui.modules, dict) else gui.modules
    screens = [screen for module in modules for screen in module.screens]
    assert all(isinstance(screen, Screen) for screen in screens)
    widgets = []
    visited = set()

    def visit(widget):
        if id(widget) in visited:
            return
        visited.add(id(widget))
        widgets.append(widget)
        if isinstance(widget, ViewContainer):
            for child in widget.view_elements:
                visit(child)

    for screen in screens:
        for widget in screen.view_elements:
            visit(widget)
    buttons = [widget for widget in widgets if isinstance(widget, Button)]
    forms = [widget for widget in widgets if isinstance(widget, Form)]
    bindings = set()
    navigation = 0
    for widget in screens + widgets:
        concept = getattr(getattr(widget, 'data_binding', None), 'domain_concept', None)
        if concept is not None:
            bindings.add(concept.name)
        for source in getattr(widget, 'list_sources', set()):
            if getattr(source, 'dataSourceClass', None) is not None:
                bindings.add(source.dataSourceClass.name)
        for event in getattr(widget, 'events', set()):
            navigation += sum(type(action).__name__ == 'Transition' for action in event.actions)
    action_types = sorted({button.actionType.name for button in buttons})
    counts = {
        'Screens': len(screens), 'Bound entities': len(bindings),
        'Buttons': len(buttons) + len(forms), 'Action types': len(action_types),
        'Navigation': navigation, 'Forms': len(forms),
        'Labels': sum(bool(button.label) and not getattr(button, '_synthetic_label', False)
                      for button in buttons) + sum(bool(form.submit_label) for form in forms),
    }
    return {
        'counts': counts, 'widget_types': dict(Counter(type(widget).__name__ for widget in widgets)),
        'bound_entities': sorted(bindings), 'action_types': action_types,
        'screens': [{'name': screen.name, 'widgets': [
            {'name': widget.name, 'kind': type(widget).__name__,
             'label': getattr(widget, 'label', None),
             'binding': getattr(getattr(getattr(widget, 'data_binding', None), 'domain_concept', None), 'name', None),
             'sources': [{'name': source.name, 'class': getattr(source.dataSourceClass, 'name', None)}
                         for source in sorted(getattr(widget, 'list_sources', set()), key=lambda source: source.name)],
             'action_type': getattr(getattr(widget, 'actionType', None), 'name', None),
             **({'submit_label': widget.submit_label, 'title': widget.title,
                 'fields': [{'name': field.name, 'type': field.field_type.name,
                             'label': field.label, 'required': field.required}
                            for field in sorted(widget.inputFields, key=lambda field: field.name)]}
                if isinstance(widget, Form) else {})}
            for widget in sorted(screen.view_elements, key=lambda widget: widget.name)]}
            for screen in sorted(screens, key=lambda screen: screen.name)],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input-root', type=Path, default=
                        ROOT / 'evaluation_replication/examples/oracle_apex')
    parser.add_argument('--output', type=Path, default=
                        ROOT / 'evaluation_replication/parser_evaluation/oracle_apex/gui_counts')
    args = parser.parse_args()
    results = []
    for number in range(1, 6):
        name = f'example{number}'
        source = args.input_root / name
        output = args.output / name
        output.mkdir(parents=True, exist_ok=True)
        log = io.StringIO()
        with redirect_stdout(log):
            domain = oracle_apex_to_buml(str(source / 'data'), module_name=name)
            gui = oracle_apex_to_gui(str(source / 'screens'), module_name=name, domain_model=domain)
        if domain is None or gui is None:
            raise RuntimeError(f'Parser returned no model for {source}')
        result = inventory(gui)
        result['example'] = name
        result['input'] = str(source.resolve())
        result['source_files'] = {
            file.relative_to(source).as_posix(): hashlib.sha256(file.read_bytes()).hexdigest()
            for file in sorted(source.rglob('*.sql'))}
        # Diagnostic only: these source declarations are not B-UML Form objects.
        result['source_native_form_regions'] = sum(
            plug.get('plug_source_type') == 'NATIVE_FORM'
            for file in (source / 'screens').glob('page_*.sql')
            for plug in _all_calls(file.read_text(encoding='utf-8'), 'create_page_plug'))
        (output / 'inventory.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        (output / 'parser.log').write_text(log.getvalue(), encoding='utf-8')
        # Preserve the actual model graph without the source serializer's name collisions.
        (output / 'models.pkl').write_bytes(pickle.dumps({'domain': domain, 'gui': gui}))
        results.append(result)
    lines = ['# Oracle APEX parser: actual B-UML GUI element counts', '',
             f'Input: `{args.input_root.resolve()}`.', '',
             'Counts come from freshly parsed model objects, before Python source serialization.', '',
             '| Application | ' + ' | '.join(GUI_KEYS) + ' |',
             '|---|' + '---:|' * len(GUI_KEYS)]
    for result in results:
        lines.append('| ' + result['example'] + ' | ' +
                     ' | '.join(str(result['counts'][key]) for key in GUI_KEYS) + ' |')
    lines.append('| Total | ' + ' | '.join(
        str(sum(result['counts'][key] for result in results)) for key in GUI_KEYS) + ' |')
    report = args.output / 'results.md'
    report.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('\n'.join(lines))
    print(f'\nSaved report and model inventories to {args.output}')


if __name__ == '__main__':
    main()
