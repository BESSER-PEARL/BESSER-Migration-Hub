"""Check reference reloads and audits of actual generator output."""
from pathlib import Path
import json
import runpy
import sys

from migrator.evaluation.generators import serialize, supporting_objects_sql
from migrator.evaluation.oracle_apex_inventory import inventory
from migrator.evaluation.oracle_apex_parser import ddl_inventory
from besser.BUML.metamodel.structural import Class, DomainModel, Property, StringType
from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui


def test_shared_reference_reload_preserves_bound_empty_source_and_next_button(tmp_path):
    domain = DomainModel(name='Records', types={Class(name='Records', attributes={Property(name='name', type=StringType)})})
    screens = tmp_path / 'screens'
    screens.mkdir()
    (screens / 'page_00002.sql').write_text("""
wwv_flow_imp_page.create_page(p_id=>2,p_name=>'Records');
wwv_flow_imp_page.create_page_plug(p_id=>10,p_plug_source_type=>'NATIVE_IR',p_query_table=>'RECORDS');
wwv_flow_imp_page.create_page_button(p_button_name=>'NEXT',p_button_image_alt=>'next(caption)',p_button_action=>'SUBMIT');
""", encoding='utf-8')
    gui = oracle_apex_to_gui(str(screens), module_name='Records', domain_model=domain)
    folder = tmp_path / 'reference'
    serialize(domain, gui, folder)
    loaded = runpy.run_path(str(folder / 'project.py'))
    assert inventory(loaded['gui_model']) == inventory(gui)
    assert inventory(gui)['counts']['Bound entities'] == 1
    assert json.loads((folder / 'serialization.json').read_text())['inventory_equal_after_python_reload']


def test_embedded_ddl_preserves_semicolons_and_escaped_literals(tmp_path):
    exported = """
wwv_flow_imp.g_varchar2_table(1) := 'CREATE TABLE ITEMS (NAME VARCHAR2(20) DEFAULT ''a;b'');' || wwv_flow.LF;
wwv_flow_imp.g_varchar2_table(2) := 'CREATE TABLE SALES (TITLE VARCHAR2(20));' || wwv_flow.LF;
"""
    ddl = supporting_objects_sql(exported)
    assert "DEFAULT 'a;b'" in ddl
    (tmp_path / 'export.sql').write_text(ddl, encoding='utf-8')
    assert ddl_inventory(tmp_path)['counts']['Attributes'] == 2
