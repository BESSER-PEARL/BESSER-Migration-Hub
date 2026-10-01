"""BUML -> Retool generation and round-trip regression coverage."""
import csv
from datetime import date
import json
from pathlib import Path
import zipfile
import subprocess
import sys

import pytest
from besser.BUML.metamodel.structural import (
    BinaryAssociation, BooleanType, Class, DateType, DomainModel, FloatType,
    Generalization, IntegerType, Multiplicity, Property, StringType,
)
from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType, DataList, DataSourceElement, Form, GUIModel,
    InputField, InputFieldType, Module, Screen, SelectOption, Text,
)
from besser.BUML.metamodel.gui.events_actions import Event, Transition

from migrator.generators.retool import RetoolCSVGenerator, RetoolGenerator, RetoolRsxAppGenerator
from migrator.parsers.retool._rsx_source import load_rsx_source
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui

EXAMPLES = Path(__file__).resolve().parents[1] / 'evaluation_replication' / 'examples' / 'retool'
BASE_EXAMPLES = EXAMPLES


def example(number):
    root = BASE_EXAMPLES / f'example{number}'
    data = next(p for p in root.iterdir() if p.name.lower() == 'data')
    source = next(p for p in root.iterdir() if p.name.lower() == 'gui')
    domain = retool_csv_to_buml(str(data), rsx_dir=str(source))
    return domain, retool_rsx_to_gui(str(source), domain_model=domain)


def screens(model):
    return {screen.name: screen for module in model.modules for screen in module.screens}


def widgets(model):
    return [widget for screen in screens(model).values() for widget in screen.view_elements]


@pytest.mark.parametrize('number', [1, 2, 3, 4, 5])
def test_examples_preserve_screens_widgets_and_bindings(number, tmp_path):
    domain, gui = example(number)
    generator = RetoolGenerator(domain, gui_model=gui, output_dir=tmp_path, app_name='roundtrip')
    csv_paths, archive = generator.generate()
    assert len(csv_paths) == len(domain.get_classes())
    for path in csv_paths:
        with open(path, encoding='utf-8', newline='') as fh:
            rows = list(csv.reader(fh))
        assert len(rows) == 1  # No fake records in a schema export.
        assert len(rows[0]) == len(set(rows[0]))
    reloaded = retool_rsx_to_gui(archive, domain_model=domain)
    assert set(screens(reloaded)) == set(screens(gui))
    for name, screen in screens(gui).items():
        assert screens(reloaded)[name].is_main_page == screen.is_main_page
    for kind in [Form, DataList, Button, InputField]:
        assert sum(isinstance(w, kind) for w in widgets(reloaded)) == sum(isinstance(w, kind) for w in widgets(gui))
    originals = {w.name: w for w in widgets(gui) if isinstance(w, Form)}
    forms = {w.name: w for w in widgets(reloaded) if isinstance(w, Form)}
    for name, original in originals.items():
        assert forms[name].submit_label == original.submit_label
        assert {f.name for f in forms[name].inputFields} == {f.name for f in original.inputFields}
    # The folder and ZIP contain identical source text, with no stale files included.
    source = load_rsx_source(archive)
    assert source == load_rsx_source(str(tmp_path / 'roundtrip'))
    report = json.loads(source['generation_report.json'])
    assert report['warnings'] == generator.warnings
    assert set(report['screens']) == set(screens(gui))
    text_values = {w.content for w in widgets(reloaded) if isinstance(w, Text)}
    assert {w.content for w in widgets(gui) if isinstance(w, Text)} <= text_values


def simple_domain():
    properties = {
        Property(name='uuid', type=StringType, is_id=True, multiplicity=Multiplicity(1, 1)),
        Property(name='unitPrice', type=FloatType), Property(name='enabled', type=BooleanType),
        Property(name='releaseDate', type=DateType), Property(name='description', type=StringType),
    }
    return DomainModel(name='Catalog', types={Class(name='Product', attributes=properties)})


def test_supplied_rows_preserve_values_and_named_string_primary_key(tmp_path):
    domain = simple_domain()
    rows = {'Product': [{'uuid': 'product-1', 'unitPrice': 12.5, 'enabled': True,
                         'releaseDate': date(2024, 3, 1), 'description': 'A, "quoted"\nproduct'}]}
    files = RetoolCSVGenerator(domain, output_dir=tmp_path, rows=rows).generate()
    with open(files[0], encoding='utf-8', newline='') as fh:
        reader = csv.DictReader(fh)
        assert reader.fieldnames == ['uuid', 'description', 'enabled', 'release_date', 'unit_price']
        row = next(reader)
    assert row == {'uuid': 'product-1', 'description': 'A, "quoted"\nproduct', 'enabled': 'true',
                   'release_date': '2024-03-01', 'unit_price': '12.5'}
    schema = json.loads((tmp_path / 'csv' / 'schema.json').read_text())
    columns = {c['name']: c for c in schema['tables'][0]['columns']}
    assert columns['uuid']['primary_key'] and columns['uuid']['type'] == 'str'
    assert 'id' not in columns
    assert not schema['sample_data']


def test_explicit_sample_data_preserves_scalar_types(tmp_path):
    domain = simple_domain()
    RetoolCSVGenerator(domain, output_dir=tmp_path, include_sample_data=True).generate()
    parsed = retool_csv_to_buml(str(tmp_path / 'csv'))
    fields = {a.name: a.type for a in parsed.get_class_by_name('Product').attributes}
    assert fields['unit_price'] is FloatType
    assert fields['enabled'] is BooleanType
    assert fields['release_date'] is DateType
    schema = json.loads((tmp_path / 'csv' / 'schema.json').read_text())
    assert schema['sample_data']


def test_foreign_keys_and_junction_tables_share_csv_and_gui_schema(tmp_path):
    student = Class(name='Student', attributes={Property(name='student_id', type=IntegerType, is_id=True)})
    course = Class(name='Course', attributes={Property(name='id', type=StringType, is_id=True)})
    enrollment = BinaryAssociation(name='Enrollment', ends={
        Property(name='students', type=student, multiplicity=Multiplicity(0, '*')),
        Property(name='courses', type=course, multiplicity=Multiplicity(0, '*')),
    })
    favorite = BinaryAssociation(name='Favorite', ends={
        Property(name='fans', type=student, multiplicity=Multiplicity(0, '*')),
        Property(name='favorite', type=course, multiplicity=Multiplicity(0, 1)),
    })
    domain = DomainModel(name='School', types={student, course}, associations={enrollment, favorite})
    paths, archive = RetoolGenerator(domain, output_dir=tmp_path).generate()
    assert {Path(p).stem for p in paths} == {'student', 'course', 'enrollment'}
    schema = json.loads((tmp_path / 'csv' / 'schema.json').read_text())
    tables = {table['name']: table for table in schema['tables']}
    student_columns = {c['name']: c for c in tables['student']['columns']}
    assert student_columns['favorite_id']['type'] == 'str'
    assert student_columns['favorite_id']['references'] == {'table': 'course', 'column': 'id'}
    junction = tables['enrollment']
    assert junction['junction']
    assert {c['references']['table'] for c in junction['columns'] if c['references']} == {'student', 'course'}
    rsx = load_rsx_source(archive)
    assert 'SELECT * FROM "enrollment";' in rsx['lib/get_enrollment.sql']
    assert 'key="favorite_id"' in rsx['src/Student.rsx']
    assert 'key="student_id"' in rsx['src/Student.rsx']
    assert 'key="id"' not in rsx['src/Student.rsx']


def test_inherited_properties_and_existing_ids_are_not_duplicated(tmp_path):
    parent = Class(name='Base', attributes={Property(name='id', type=IntegerType, is_id=True), Property(name='name', type=StringType)})
    child = Class(name='Child', attributes={Property(name='extra', type=StringType)})
    generalization = Generalization(general=parent, specific=child)
    domain = DomainModel(name='Inherited', types={parent, child}, generalizations={generalization})
    paths = RetoolCSVGenerator(domain, output_dir=tmp_path).generate()
    child_file = next(p for p in paths if Path(p).stem == 'child')
    with open(child_file, encoding='utf-8', newline='') as fh:
        assert next(csv.reader(fh)) == ['id', 'extra', 'name']


def test_gui_only_escaping_fields_and_explicit_dialog_transition(tmp_path):
    field = InputField(name='category', description='', field_type=InputFieldType.Dropdown,
                       label='A "quoted" label', required=True,
                       options=[SelectOption(label='A & B', value='a<b')])
    form = Form(name='Edit', description='', inputFields={field}, title='Edit item', submit_label='Apply')
    modal = Screen(name='editModal', description='', view_elements={form}, is_main_page=False)
    button = Button(name='open', description='', label='Open > details',
                    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Cancel)
    button.events = {Event(name='show', actions={Transition(name='openDetails', target_screen=modal)})}
    main = Screen(name='Home', description='', view_elements={button, Text(name='intro', content='A & B\n<hello>')}, is_main_page=True)
    gui = GUIModel(name='Demo', package='', versionCode='', versionName='', description='', modules={Module(name='Demo', screens={main, modal})})
    generator = RetoolRsxAppGenerator(gui_model=gui, output_dir=tmp_path)
    archive = generator.generate()
    source = load_rsx_source(archive)
    assert 'method="show"' in source['src/Home.rsx']
    assert 'pluginId="editModal"' in source['src/Home.rsx']
    assert not any(path.endswith('.sql') for path in source)
    parsed = retool_rsx_to_gui(archive)
    assert set(screens(parsed)) == {'Home', 'editModal'}
    parsed_form = next(w for w in widgets(parsed) if isinstance(w, Form))
    parsed_field = next(iter(parsed_form.inputFields))
    assert parsed_field.label == 'A "quoted" label'
    assert parsed_field.required
    assert [(o.label, o.value) for o in parsed_field.options] == [('A & B', 'a<b')]
    assert parsed_form.submit_label == 'Apply'
    assert any(w.content == 'A & B\n<hello>' for w in widgets(parsed) if isinstance(w, Text))
    assert not any('open' in warning for warning in generator.warnings)
    parsed_button = next(w for w in widgets(parsed) if isinstance(w, Button) and w.name == 'open')
    assert next(iter(next(iter(parsed_button.events)).actions)).target_screen is screens(parsed)['editModal']


def test_empty_wrapper_is_preserved_without_becoming_landing_page(tmp_path):
    wrapper = Screen(name='AWrapper', description='', view_elements=set(), is_main_page=True)
    body = Screen(name='ZBody', description='', view_elements={Text(name='message', content='Hello')}, is_main_page=True)
    gui = GUIModel(name='Demo', package='', versionCode='', versionName='', description='',
                   modules={Module(name='Demo', screens={wrapper, body})})
    archive = RetoolRsxAppGenerator(gui_model=gui, output_dir=tmp_path).generate()
    source = load_rsx_source(archive)
    assert json.loads(source['metadata.json'])['appTemplate']['rootScreen'] == 'ZBody'
    assert set(screens(retool_rsx_to_gui(archive))) == {'AWrapper', 'ZBody'}


def test_regeneration_keeps_user_files_and_excludes_stale_output_from_zip(tmp_path):
    domain = simple_domain()
    folder = tmp_path / 'app'
    folder.mkdir()
    custom = folder / 'notes.txt'
    custom.write_text('keep me')
    stale = folder / 'stale.rsx'
    stale.write_text('<Text id="stale" value="old" />')
    generator = RetoolRsxAppGenerator(domain, app_name='app', output_dir=tmp_path)
    archive = generator.generate()
    assert custom.read_text() == 'keep me' and stale.exists()
    with zipfile.ZipFile(archive) as zf:
        assert 'app/stale.rsx' not in zf.namelist()
        assert 'app/notes.txt' not in zf.namelist()
    first = load_rsx_source(archive)
    generator.generate()
    assert load_rsx_source(archive) == first


@pytest.mark.parametrize('bad_name', ['../outside', '.', '..', 'a/b', 'a\\b'])
def test_app_name_cannot_escape_output_directory(bad_name, tmp_path):
    with pytest.raises(ValueError, match='folder name'):
        RetoolRsxAppGenerator(simple_domain(), app_name=bad_name, output_dir=tmp_path)


def test_normalized_name_collisions_are_reported(tmp_path):
    domain = DomainModel(name='Collision', types={Class(name='FooBar', attributes=set()), Class(name='foo_bar', attributes=set())})
    with pytest.raises(ValueError, match='Duplicate generated table'):
        RetoolCSVGenerator(domain, output_dir=tmp_path).generate()


def test_invalid_row_columns_fail_before_writing(tmp_path):
    with pytest.raises(ValueError, match='Unknown columns'):
        RetoolCSVGenerator(simple_domain(), output_dir=tmp_path, rows={'Product': [{'typo': 1}]}).generate()
    assert not (tmp_path / 'csv').exists()


def test_synthetic_keys_are_assigned_only_for_supplied_rows(tmp_path):
    cls = Class(name='Note', attributes={Property(name='text', type=StringType)})
    domain = DomainModel(name='Notes', types={cls})
    paths = RetoolCSVGenerator(domain, output_dir=tmp_path, rows={'Note': [{'text': 'first'}, {'text': 'second'}]}).generate()
    with open(paths[0], encoding='utf-8', newline='') as fh:
        assert list(csv.DictReader(fh)) == [{'id': '1', 'text': 'first'}, {'id': '2', 'text': 'second'}]


def test_one_to_one_foreign_keys_are_unique_in_manifest(tmp_path):
    person = Class(name='Person', attributes={Property(name='id', type=IntegerType, is_id=True)})
    passport = Class(name='Passport', attributes={Property(name='id', type=IntegerType, is_id=True)})
    association = BinaryAssociation(name='Identity', ends={
        Property(name='person', type=person, multiplicity=Multiplicity(1, 1)),
        Property(name='passport', type=passport, multiplicity=Multiplicity(0, 1)),
    })
    domain = DomainModel(name='Identity', types={person, passport}, associations={association})
    RetoolCSVGenerator(domain, output_dir=tmp_path).generate()
    manifest = json.loads((tmp_path / 'csv' / 'schema.json').read_text())
    foreign = [c for t in manifest['tables'] for c in t['columns'] if c['references']]
    assert len(foreign) == 1
    assert foreign[0]['unique'] and not foreign[0]['nullable']


def test_legacy_json_generation_remains_available(tmp_path):
    output = RetoolGenerator(simple_domain(), output_dir=tmp_path).generate_json()
    payload = json.loads(Path(output).read_text(encoding='utf-8'))
    assert isinstance(json.loads(payload['page']['data']['appState']), list)


@pytest.mark.parametrize('number', [1, 2, 3, 4])
def test_example_script_exports_original_records(number, tmp_path):
    result = subprocess.run([sys.executable, '-m', 'migrator.converters.retool_example', '--example', str(number),
                             '--output', str(tmp_path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert (tmp_path / f'example{number}.zip').exists()
    data = next(p for p in (BASE_EXAMPLES / f'example{number}').iterdir() if p.name.lower() == 'data')
    for original in data.glob('*.csv'):
        with original.open(encoding='utf-8-sig', newline='') as fh:
            expected = list(csv.DictReader(fh))
        with (tmp_path / 'csv' / original.name).open(encoding='utf-8', newline='') as fh:
            actual = list(csv.DictReader(fh))
        assert len(actual) == len(expected)
        for input_row, output_row in zip(expected, actual):
            assert all(output_row[name] == value for name, value in input_row.items())


@pytest.mark.parametrize('gui_only', [False, True])
def test_webapp_dispatches_gui_model_and_registers_artifacts(gui_only, tmp_path):
    from webapp.backend.app.services.generate import generate_artifacts
    from webapp.backend.app.sessions import Session
    from webapp.backend.app.platforms import get_target
    domain, gui = example(3)
    session = Session(id='test', work_dir=tmp_path, domain_model=None if gui_only else domain, gui_model=gui)
    result = generate_artifacts(session, 'retool')
    assert get_target('retool').supports_gui
    names = {a['name'] for a in result['artifacts']}
    assert any(name.endswith('.zip') for name in names)
    assert any(name.endswith('generation_report.json') for name in names)
    assert any(name.endswith('.csv') for name in names) is not gui_only
    assert result['warnings']
