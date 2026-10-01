"""Exercise GUI exports through SQL evidence and the APEX parser."""
from pathlib import Path
import sys

from migrator.evaluation.oracle_apex_parser import calls, gui_source_inventory
from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType, DataList, DataSourceElement, Form, GUIModel,
    InputField, InputFieldType, Module, Screen,
)
from besser.BUML.metamodel.gui.binding import DataBinding
from besser.BUML.metamodel.gui.events_actions import Event, Transition
from besser.BUML.metamodel.structural import Class, DomainModel, Property, StringType
from migrator.generators.sql.oracle_apex_app_generator import OracleApexFullAppGenerator
from migrator.generators.sql.oracle_apex_gui_export import render_page
from migrator.parsers.oracle_apex.oracle_apex_gui import _parse_page_file


def gui(screens):
    return GUIModel(name='App', package='', versionCode='', versionName='', description='',
                    modules={Module(name='App', screens=set(screens))})


def form(name, label):
    return Form(name=name, description='', title="Author's details", submit_label=label,
                inputFields={InputField(name='P7_NAME', description='', field_type=InputFieldType.Text,
                                        label="Author's name", required=True)})


def test_mixed_screen_exports_form_binding_and_authored_controls(tmp_path):
    cls = Class(name='Person', attributes={Property(name='name', type=StringType)})
    domain = DomainModel(name='App', types={cls})
    editor = form('Editor', 'Apply edits')
    editor.data_binding = DataBinding(domain_concept=cls)
    report = DataList(name='People', description='', list_sources={DataSourceElement(name='Person', dataSourceClass=cls)})
    save = Button(name='Save', description='', label="Author's save", buttonType=ButtonType.RaisedButton,
                  actionType=ButtonActionType.Save)
    screen = Screen(name='Custom_Workspace', description='', view_elements={editor, report, save}, is_main_page=True)
    generator = OracleApexFullAppGenerator(domain, gui_model=gui([screen]), output_dir=str(tmp_path))
    assignments = generator._assign_gui_page_numbers()
    sql = render_page(generator, screen, assignments[0][1], assignments)
    path = tmp_path / 'page_00002.sql'
    path.write_text(sql, encoding='utf-8')
    parsed = calls(sql)
    assert parsed['create_page'][0]['name'] == 'Custom_Workspace'
    assert len(parsed['create_page_button']) == 2
    assert {region.get('plug_source_type') for region in parsed['create_page_plug']} >= {'NATIVE_FORM', 'NATIVE_IR'}
    assert gui_source_inventory(tmp_path, {'person': {}})['counts']['Bound entities'] == 1
    reloaded = _parse_page_file(str(path), domain_model=domain)[1]
    restored = next(widget for widget in reloaded.view_elements if isinstance(widget, Form))
    assert restored.submit_label == 'Apply edits'  # Standalone Save belongs to the page, not the form.
    assert restored.data_binding.domain_concept is cls
    assert any(field.label == "Author's name" and field.required for field in restored.inputFields)
    assert next(widget for widget in reloaded.view_elements if isinstance(widget, Button)).label == "Author's save"


def test_every_screen_survives_duplicate_entity_names_and_navigation(tmp_path):
    empty = Screen(name='Person_List', description='', view_elements=set(), is_main_page=True)
    another = Screen(name='Person_page', description='', view_elements=set(), is_main_page=True)
    dialog = Screen(name='Custom_Editor', description='', view_elements={form('Editor', 'Apply')}, is_main_page=False)
    button = Button(name='Open', description='', label='Open editor', buttonType=ButtonType.RaisedButton,
                    actionType=ButtonActionType.Navigate)
    button.events = {Event(name='open', actions={Transition(name='toEditor', target_screen=dialog)})}
    empty.view_elements = {button}
    generator = OracleApexFullAppGenerator(DomainModel(name='App', types=set()), gui_model=gui([empty, another, dialog]),
                                          output_dir=str(tmp_path))
    sql = Path(generator.generate()).read_text(encoding='utf-8')
    parsed = calls(sql)
    emitted = {page['name']: page for page in parsed['create_page']}
    assert {empty.name, another.name, dialog.name} <= emitted.keys()
    assert emitted[dialog.name]['page_mode'] == 'MODAL'
    assert f":{emitted[dialog.name]['id']}:" in next(
        button for button in parsed['create_page_button'] if button['button_name'] == 'OPEN')['button_redirect_url']
    native_form = next(region for region in parsed['create_page_plug'] if region.get('plug_source_type') == 'NATIVE_FORM')
    assert 'from dual' in native_form['plug_source']
    assert not any(process.get('process_type') == 'NATIVE_FORM_PROCESS' for process in parsed['create_page_process'])
    assert any('no persistence binding' in warning for warning in generator.warnings)


def test_domain_only_generation_keeps_existing_report_and_form_pages(tmp_path):
    cls = Class(name='Person', attributes={Property(name='name', type=StringType)})
    generator = OracleApexFullAppGenerator(DomainModel(name='App', types={cls}), output_dir=str(tmp_path))
    parsed = calls(Path(generator.generate()).read_text(encoding='utf-8'))
    assert {page['id'] for page in parsed['create_page']} == {'0', '1', '2', '3', '101'}
    assert any(region.get('plug_source_type') == 'NATIVE_FORM' for region in parsed['create_page_plug'])
