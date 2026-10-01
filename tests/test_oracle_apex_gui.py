"""APEX form regions and legacy form pages become B-UML Form widgets."""
from pathlib import Path

import pytest
from besser.BUML.metamodel.gui.graphical_ui import Button, DataList, Form, InputFieldType, Screen
from besser.BUML.metamodel.structural import Class, DomainModel

from migrator.parsers.oracle_apex.oracle_apex_gui import (
    _parse_page_file, oracle_apex_gui_from_sql, oracle_apex_to_gui,
)
from migrator.generators.retool import RetoolRsxAppGenerator
from migrator.parsers.retool._rsx_source import load_rsx_source
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui

ROOT = Path(__file__).resolve().parents[1]


def parse(tmp_path, sql, domain_model=None):
    path = tmp_path / 'page_00002.sql'
    path.write_text(sql, encoding='utf-8')
    return _parse_page_file(str(path), domain_model=domain_model)[1]


def test_native_form_after_report_preserves_fields_and_submit(tmp_path):
    screen = parse(tmp_path, """
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Editor');
wwv_flow_imp_page.create_page_plug(p_id=>wwv_flow_imp.id(10),p_plug_source_type=>'NATIVE_IR');
wwv_flow_imp_page.create_page_plug(p_id=>wwv_flow_imp.id(20),p_plug_name=>'Author''s details (',p_plug_source_type=>'NATIVE_FORM');
wwv_flow_imp_page.create_page_item(p_name=>'P2_NAME',p_item_plug_id=>wwv_flow_imp.id(20),p_display_as=>'NATIVE_TEXT_FIELD',p_prompt=>'Author''s name',p_is_required=>true);
wwv_flow_imp_page.create_page_item(p_name=>'P2_ID',p_item_plug_id=>wwv_flow_imp.id(20),p_display_as=>'NATIVE_HIDDEN');
wwv_flow_imp_page.create_page_item(p_name=>'P2_FILTER',p_item_plug_id=>wwv_flow_imp.id(10),p_display_as=>'NATIVE_TEXT_FIELD');
wwv_flow_imp_page.create_page_button(p_button_name=>'SAVE',p_button_action=>'SUBMIT',p_button_image_alt=>'Apply changes');
wwv_flow_imp_page.create_page_button(p_button_name=>'CANCEL',p_button_action=>'REDIRECT_PAGE');
""")
    assert isinstance(screen, Screen)
    assert any(isinstance(widget, DataList) for widget in screen.view_elements)
    form = next(widget for widget in screen.view_elements if isinstance(widget, Form))
    assert form.title == "Author's details ("
    assert form.submit_label == 'Apply changes'
    fields = {field.name: field for field in form.inputFields}
    assert set(fields) == {'P2_NAME', 'P2_ID'}
    assert fields['P2_NAME'].required
    assert fields['P2_NAME'].label == "Author's name"
    assert fields['P2_ID'].field_type == InputFieldType.Hidden
    assert [widget.name for widget in screen.view_elements if isinstance(widget, Button)] == ['Cancel']


def test_multiple_native_regions_keep_their_own_items(tmp_path):
    screen = parse(tmp_path, """
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Two forms');
wwv_flow_imp_page.create_page_plug(p_id=>10,p_plug_name=>'First',p_plug_source_type=>'NATIVE_FORM');
wwv_flow_imp_page.create_page_plug(p_id=>20,p_plug_name=>'Second',p_plug_source_type=>'NATIVE_FORM');
wwv_flow_imp_page.create_page_item(p_name=>'P2_FIRST',p_item_plug_id=>10,p_display_as=>'NATIVE_NUMBER_FIELD');
wwv_flow_imp_page.create_page_item(p_name=>'P2_SECOND',p_item_plug_id=>20,p_display_as=>'NATIVE_DATE_PICKER_APEX');
""")
    forms = {widget.title: widget for widget in screen.view_elements if isinstance(widget, Form)}
    assert {field.name for field in forms['First'].inputFields} == {'P2_FIRST'}
    assert {field.name for field in forms['Second'].inputFields} == {'P2_SECOND'}
    assert next(iter(forms['First'].inputFields)).field_type == InputFieldType.Number
    assert next(iter(forms['Second'].inputFields)).field_type == InputFieldType.Date


@pytest.mark.parametrize('modal', [False, True])
def test_report_and_empty_dialog_do_not_become_forms(tmp_path, modal):
    screen = parse(tmp_path, f"""
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Help',p_page_mode=>'{"MODAL" if modal else "NORMAL"}');
wwv_flow_imp_page.create_page_plug(p_plug_source_type=>'NATIVE_IR');
""")
    assert not any(isinstance(widget, Form) for widget in screen.view_elements)


def test_legacy_nonmodal_form_process(tmp_path):
    screen = parse(tmp_path, """
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Employee');
wwv_flow_imp_page.create_page_item(p_name=>'P2_NAME',p_display_as=>'NATIVE_TEXT_FIELD',p_source_type=>'DB_COLUMN');
wwv_flow_imp_page.create_page_process(p_process_type=>'NATIVE_FORM_FETCH');
wwv_flow_imp_page.create_page_button(p_button_name=>'SAVE',p_button_action=>'SUBMIT');
""")
    assert len([widget for widget in screen.view_elements if isinstance(widget, Form)]) == 1


def test_real_custom_form_directory_monolithic_and_retool_export(tmp_path):
    source = ROOT / 'evaluation_replication/examples/oracle_apex/example1/screens/page_00002.sql'
    (tmp_path / source.name).write_text(source.read_text(encoding='utf-8'), encoding='utf-8')
    gui = oracle_apex_to_gui(str(tmp_path), 'CustomForm')
    screen = next(iter(next(iter(gui.modules)).screens))
    form = next(widget for widget in screen.view_elements if isinstance(widget, Form))
    assert {field.name for field in form.inputFields} == {'P2_NAME'}
    assert next(iter(form.inputFields)).required
    assert sum(isinstance(widget, Button) for widget in screen.view_elements) + 1 == 3

    monolithic = oracle_apex_gui_from_sql(str(tmp_path / source.name), 'CustomForm')
    mono_screen = next(iter(next(iter(monolithic.modules)).screens))
    assert len([widget for widget in mono_screen.view_elements if isinstance(widget, Form)]) == 1

    archive = RetoolRsxAppGenerator(gui_model=gui, output_dir=str(tmp_path / 'retool')).generate()
    exported = load_rsx_source(archive)
    assert sum(text.count('<Form') for text in exported.values()) == 1
    assert sum(text.count('<Button') for text in exported.values()) == 3
    reloaded = retool_rsx_to_gui(archive)
    reloaded_form = next(widget for module in reloaded.modules for screen in module.screens
                         for widget in screen.view_elements if isinstance(widget, Form))
    assert {field.name for field in reloaded_form.inputFields} == {'P2_NAME'}
    assert reloaded_form.submit_label == form.submit_label


def test_native_form_and_report_resolve_declared_tables(tmp_path):
    employee, department = Class(name='Employees'), Class(name='Departments')
    domain = DomainModel(name='App', types={employee, department})
    sql = '''prompt --application/pages/page_00002
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Editor');
wwv_flow_imp_page.create_page_plug(p_id=>10,p_plug_source_type=>'NATIVE_IR',p_query_table=>'"OWNER"."DEPARTMENTS"');
wwv_flow_imp_page.create_page_plug(p_id=>20,p_plug_source_type=>'NATIVE_FORM',p_query_table=>'employees');
wwv_flow_imp_page.create_page_item(p_name=>'P2_NAME',p_item_plug_id=>20,p_display_as=>'NATIVE_TEXT_FIELD');
'''
    screen = parse(tmp_path, sql, domain)
    form = next(widget for widget in screen.view_elements if isinstance(widget, Form))
    report = next(widget for widget in screen.view_elements if isinstance(widget, DataList))
    assert form.data_binding.domain_concept is employee
    assert report.data_binding.domain_concept is department
    assert next(iter(report.list_sources)).dataSourceClass is department
    # Both public entry points receive the exact domain model, not reconstructed classes.
    gui = oracle_apex_gui_from_sql(str(tmp_path / 'page_00002.sql'), domain_model=domain)
    form = next(widget for module in gui.modules for screen in module.screens
                for widget in screen.view_elements if isinstance(widget, Form))
    assert form.data_binding.domain_concept is employee


@pytest.mark.parametrize('modern', [False, True])
def test_legacy_form_process_resolves_table_metadata(tmp_path, modern):
    employee = Class(name='EbaDemoEmp')
    domain = DomainModel(name='App', types={employee})
    metadata = ("p_attributes=>wwv_flow_t_plugin_attributes(wwv_flow_t_varchar2('table_name', 'EBA_DEMO_EMP')).to_clob"
                if modern else "p_attribute_02=>'EBA_DEMO_EMP'")
    screen = parse(tmp_path, f'''
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Employee');
wwv_flow_imp_page.create_page_item(p_name=>'P2_NAME',p_display_as=>'NATIVE_TEXT_FIELD');
wwv_flow_imp_page.create_page_process(p_process_type=>'NATIVE_FORM_FETCH',{metadata});
''', domain)
    form = next(widget for widget in screen.view_elements if isinstance(widget, Form))
    assert form.data_binding.domain_concept is employee


def test_joined_report_preserves_each_declared_source_class(tmp_path):
    employee, department = Class(name='Emp'), Class(name='Dept')
    domain = DomainModel(name='App', types={employee, department})
    screen = parse(tmp_path, '''
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Employees');
wwv_flow_imp_page.create_page_plug(p_plug_source_type=>'NATIVE_IR',
p_plug_source=>wwv_flow_string.join(wwv_flow_t_varchar2(
'select e.name, d.name', 'from "OWNER"."EMP" e, DEPT d', 'where e.dept_id=d.id')));
''', domain)
    report = next(widget for widget in screen.view_elements if isinstance(widget, DataList))
    assert report.data_binding.domain_concept is employee
    assert {source.dataSourceClass for source in report.list_sources} == {employee, department}


@pytest.mark.parametrize('query', ["select 'FROM EMP' from UNKNOWN", 'with EMP as (select 1 from dual) select * from EMP'])
def test_unknown_or_derived_tables_do_not_get_guessed_bindings(tmp_path, query):
    domain = DomainModel(name='App', types={Class(name='Emp')})
    screen = parse(tmp_path, f"""
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'EMP');
wwv_flow_imp_page.create_page_plug(p_plug_source_type=>'NATIVE_IR',p_plug_source=>'{query.replace("'", "''")}');
""", domain)
    report = next(widget for widget in screen.view_elements if isinstance(widget, DataList))
    assert report.data_binding is None
    assert all(source.dataSourceClass is None for source in report.list_sources)


def test_migration_facade_passes_domain_model_to_apex_parser(tmp_path):
    from migrator.model_migrator_gui import GUIModelMigrator
    employee = Class(name='Emp')
    domain = DomainModel(name='App', types={employee})
    parse(tmp_path, """
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Employees');
wwv_flow_imp_page.create_page_plug(p_plug_source_type=>'NATIVE_IR',p_query_table=>'EMP');
""")
    gui = GUIModelMigrator('oracle_apex', str(tmp_path), 'App', '', domain_model=domain).gui_model()
    report = next(widget for module in gui.modules for screen in module.screens
                  for widget in screen.view_elements if isinstance(widget, DataList))
    assert report.data_binding.domain_concept is employee
