"""Regression coverage for Retool CSV and Toolscript -> BUML conversion."""
from pathlib import Path
import zipfile

import pytest
from besser.BUML.metamodel.gui.dashboard import BarChart, LineChart
from besser.BUML.metamodel.gui.graphical_ui import Button, DataList, Form, InputField, InputFieldType, Text
from besser.BUML.metamodel.structural import DateType, FloatType, IntegerType, StringType
from besser.utilities.buml_code_builder import domain_model_to_code, gui_model_to_code

from migrator.parsers.retool._rsx_source import load_rsx_source
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui

EXAMPLES = Path(__file__).resolve().parents[1] / 'examples' / 'retool' / 'base_examples'


def test_named_empty_pages_extended_inputs_and_direct_navigation(tmp_path):
    (tmp_path / 'main.rsx').write_text('''<App>
      <Screen id="landing"><View id="wrapper" viewKey="section">
        <View id="body" viewKey="View 1">
          <DateRange id="period" label="Period" />
          <Tags id="keywords" label="Keywords" />
          <Button id="openDialog" text="Details">
            <Event event="click" type="widget" method="show" pluginId="dialog" />
          </Button>
          <Button id="unresolved" text="Unknown">
            <Event event="click" type="widget" method="show" pluginId="missing" />
          </Button>
          <Button id="scripted" text="Script">
            <Event event="click" type="script" method="run" pluginId="dialog" />
          </Button>
        </View>
      </View></Screen><ModalFrame id="dialog" /></App>''', encoding='utf-8')
    gui = retool_rsx_to_gui(str(tmp_path))
    assert set(screens(gui)) == {'landing', 'landing_section', 'dialog'}
    widgets = elements(gui)
    assert widgets['period'].field_type is InputFieldType.DateRange
    assert widgets['keywords'].field_type is InputFieldType.Tags
    event = next(iter(widgets['openDialog'].events))
    action = next(iter(event.actions))
    assert action.target_screen is screens(gui)['dialog']
    assert action.triggered_by is widgets['openDialog']
    assert not getattr(widgets['unresolved'], 'events', set())
    assert not getattr(widgets['scripted'], 'events', set())


def example_models(number):
    root = EXAMPLES / f'example{number}'
    data = next(p for p in root.iterdir() if p.name.lower() == 'data')
    gui = next(p for p in root.iterdir() if p.name.lower() == 'gui')
    domain = retool_csv_to_buml(str(data), rsx_dir=str(gui))
    return domain, retool_rsx_to_gui(str(gui), domain_model=domain)


def screens(gui):
    return {s.name: s for m in gui.modules for s in m.screens}


def elements(gui):
    return {e.name: e for s in screens(gui).values() for e in s.view_elements}


def source_of(element):
    return next(iter(element.list_sources))


@pytest.mark.parametrize('number,class_names,association_count,screen_count', [
    (1, {'Books', 'DiscountCodes', 'Orders'}, 2, 10),
    (2, {'Inventory'}, 0, 4),
    (3, {'Products'}, 0, 4),
    (4, {'MonthlySales', 'CategorySales'}, 0, 2),
    (5, {'TeamMembers'}, 0, 5),
])
def test_examples_and_runnable_buml_export(number, class_names, association_count, screen_count, tmp_path):
    domain, gui = example_models(number)
    assert {c.name for c in domain.get_classes()} == class_names
    assert len(domain.associations) == association_count
    assert len(screens(gui)) == screen_count
    assert isinstance(gui.modules, set)  # BESSER's serializer expects modules, not dictionary keys.
    domain_file, gui_file = tmp_path / 'domain.py', tmp_path / 'gui.py'
    domain_model_to_code(domain, str(domain_file))
    gui_model_to_code(gui, str(gui_file), domain_model=domain)
    namespace = {}
    exec(domain_file.read_text(encoding='utf-8'), namespace)
    exec(gui_file.read_text(encoding='utf-8'), namespace)
    assert set(screens(namespace['gui_model'])) == set(screens(gui))
    assert set(elements(namespace['gui_model'])) == set(elements(gui))
    for name, widget in elements(gui).items():
        if isinstance(widget, DataList):
            reloaded = source_of(elements(namespace['gui_model'])[name])
            original = source_of(widget)
            if original.dataSourceClass is not None:
                assert reloaded.dataSourceClass.name == original.dataSourceClass.name
                # BESSER 7.13 resolves fields against the CSV class and drops
                # query-only columns. Check every schema-backed field survives.
                backed_fields = {a.name for a in original.dataSourceClass.attributes}
                assert set(original.field_names) & backed_fields <= set(reloaded.field_names)
            else:
                assert set(reloaded.field_names) == set(original.field_names)


def test_bookstore_bindings_and_nested_dialogs():
    domain, gui = example_models(1)
    widgets = elements(gui)
    books = source_of(widgets['booksInventoryTable_List'])
    assert books.dataSourceClass is domain.get_class_by_name('Books')
    assert {'title', 'isbn', 'price'} <= set(books.field_names)
    assert not screens(gui)['modal1'].is_main_page
    assert not screens(gui)['checkoutModal'].is_main_page
    assert 'form4' not in {e.name for e in screens(gui)['Books_Add_Books'].view_elements}
    assert isinstance(widgets['searchInventoryTextInput'], InputField)
    assert isinstance(widgets['select10'], InputField)


def test_inventory_pages_columns_and_modern_chart_series():
    domain, gui = example_models(2)
    assert set(screens(gui)) == {'inventory', 'inventory_local', 'inventory_vendor', 'addInventory'}
    widgets = elements(gui)
    source = source_of(widgets['inventoryTable_List'])
    assert source.dataSourceClass is domain.get_class_by_name('Inventory')
    assert {'sku', 'quantity', 'location'} <= set(source.field_names)
    chart = widgets['localInventoryChart']
    assert isinstance(chart, BarChart)
    assert chart.series[0].data_binding.data_field.name == 'quantity'
    assert chart.series[0].data_binding.label_field.name == 'sku'
    assert len(widgets['form1'].inputFields) == 6


def test_products_modern_actions_and_scoped_select_options():
    domain, gui = example_models(3)
    widgets = elements(gui)
    source = source_of(widgets['productsTable_List'])
    assert source.dataSourceClass is domain.get_class_by_name('Products')
    assert source.field_names == ['id', 'name', 'description', 'category', 'price', 'created_at']
    assert {e.label for e in widgets.values() if isinstance(e, Button)} >= {'Edit', 'Delete'}
    form = widgets['CreateProductForm']
    fields = {f.name: f for f in form.inputFields}
    assert [o.value for o in fields['category'].options] == ['Electronics', 'Clothing', 'Books']
    assert not fields['name'].options
    assert form.data_binding.domain_concept is domain.get_class_by_name('Products')
    assert form.submit_label == 'Create'
    assert not screens(gui)['editModal'].is_main_page


def test_reporting_charts_and_source_schema_limits():
    domain, gui = example_models(4)
    widgets = elements(gui)
    chart = widgets['revenueChart']
    assert isinstance(chart, LineChart)
    assert chart.data_binding.domain_concept is domain.get_class_by_name('MonthlySales')
    assert chart.series[0].data_binding.data_field.name == 'revenue'
    assert isinstance(widgets['categoryChart'], BarChart)
    assert {s.data_binding.data_field.name for s in widgets['categoryChart'].series} == {'revenue', 'orders'}
    assert isinstance(widgets['statRevenue'], Text)
    source = source_of(widgets['salesTable_List'])
    assert {'orders', 'conversion'} <= set(source.field_names)
    assert 'orders' not in {a.name for a in source.dataSourceClass.attributes}


def write_csv(root, name, text):
    (root / f'{name}.csv').write_text(text, encoding='utf-8')


def test_own_table_id_is_primary_key_and_uuid_ids_keep_their_type(tmp_path):
    write_csv(tmp_path, 'categories', 'category_id,name\n1,Fiction\n')
    write_csv(tmp_path, 'books', 'id,category_id\nbook-uuid,1\n')
    domain = retool_csv_to_buml(str(tmp_path))
    assert len(domain.associations) == 1
    categories = domain.get_class_by_name('Categories')
    key = next(a for a in categories.attributes if a.name == 'category_id')
    assert key.is_id and key.type is IntegerType
    key = next(a for a in domain.get_class_by_name('Books').attributes if a.name == 'id')
    assert key.is_id and key.type is StringType


def test_sql_aliases_override_name_guess_and_remove_fk_attribute(tmp_path):
    write_csv(tmp_path, 'users', 'id,name\n1,Alice\n')
    write_csv(tmp_path, 'owners', 'id,name\n1,Wrong entity\n')
    write_csv(tmp_path, 'orders', 'id,owner_id,reviewer_id\n1,1,1\n')
    gui = tmp_path / 'gui'
    (gui / 'lib').mkdir(parents=True)
    (gui / 'lib' / 'orders.sql').write_text(
        'SELECT * FROM "public"."orders" JOIN "users" AS u ON orders.owner_id = u.id '
        'LEFT JOIN users r ON orders.reviewer_id = r.id', encoding='utf-8',
    )
    domain = retool_csv_to_buml(str(tmp_path), rsx_dir=str(gui))
    assert len(domain.associations) == 2
    assert len({a.name for a in domain.associations}) == 2
    assert {e.type.name for a in domain.associations for e in a.ends} == {'Orders', 'Users'}
    assert {a.name for a in domain.get_class_by_name('Orders').attributes} == {'id'}


@pytest.mark.parametrize('value,expected', [
    ('1e3', FloatType), ('.5', FloatType), ('2024-02-29', DateType),
    ('2024-02-30', StringType), ('2024-01-01garbage', StringType),
])
def test_csv_type_inference(value, expected, tmp_path):
    write_csv(tmp_path, 'values', f'id,value\n1,{value}\n')
    domain = retool_csv_to_buml(str(tmp_path))
    assert next(a for a in domain.get_class_by_name('Values').attributes if a.name == 'value').type is expected


def test_empty_csv_is_skipped_and_duplicate_columns_rejected(tmp_path):
    write_csv(tmp_path, 'empty', '')
    assert retool_csv_to_buml(str(tmp_path)) is None
    write_csv(tmp_path, 'items', 'id,ID\n1,2\n')
    with pytest.raises(ValueError, match='duplicate column'):
        retool_csv_to_buml(str(tmp_path))


def test_rsx_expressions_includes_query_ids_and_option_scope(tmp_path):
    write_csv(tmp_path, 'products', 'id,name\n1,Product\n')
    domain = retool_csv_to_buml(str(tmp_path))
    gui = tmp_path / 'gui'
    (gui / 'lib').mkdir(parents=True)
    (gui / 'lib' / 'arbitrary_filename.sql').write_text('SELECT * FROM public.products', encoding='utf-8')
    (gui / 'main.rsx').write_text('''<App>
      <SqlQueryUnified id="fetchProducts" query={include("./lib/arbitrary_filename.sql", "string")} />
      <Table id="products" data="{{ fetchProducts.data.filter(x => x.id > 0) }}">
        <Column key="id" /><Column key="name" />
      </Table>
      <Include src="./fields.rsx" /><Include src="./fields.rsx" />
      <!-- <Text id="ignored" value="comment" /> -->
      <Button id="compare" text="A > B &amp; C" disabled={{ value > 3 }} />
    </App>''', encoding='utf-8')
    (gui / 'fields.rsx').write_text('''<Form id="filters">
      <Select id="first"><Option value="a" label="Alpha" /></Select>
      <Select id="second"><Option value="b" /></Select>
      <TextInput id="search" />
      <Include src="./fields.rsx" />
    </Form>''', encoding='utf-8')
    model = retool_rsx_to_gui(str(gui), domain_model=domain)
    widgets = elements(model)
    assert source_of(widgets['products_List']).dataSourceClass is domain.get_class_by_name('Products')
    assert widgets['compare'].label == 'A > B & C'
    assert 'ignored' not in widgets
    assert {'filters', 'filters_2'} <= widgets.keys()
    fields = {f.name: f for f in widgets['filters'].inputFields}
    assert [(o.value, o.label) for o in fields['first'].options] == [('a', 'Alpha')]
    assert [o.value for o in fields['second'].options] == ['b']
    assert not fields['search'].options


@pytest.mark.parametrize('number', [1, 2, 3, 4])
def test_nested_zip_and_directory_exports_are_equivalent(number, tmp_path):
    root = next(p for p in (EXAMPLES / f'example{number}').iterdir() if p.name.lower() == 'gui')
    archive = tmp_path / 'export.zip'
    with zipfile.ZipFile(archive, 'w') as zf:
        for path in root.rglob('*'):
            if path.is_file():
                zf.write(path, 'export/GUI/' + path.relative_to(root).as_posix())
    assert load_rsx_source(str(archive)) == load_rsx_source(str(root))
    domain, directory_model = example_models(number)
    zip_model = retool_rsx_to_gui(str(archive), domain_model=domain)
    assert set(screens(zip_model)) == set(screens(directory_model))
    assert set(elements(zip_model)) == set(elements(directory_model))


@pytest.mark.parametrize('number', [1, 2, 3, 4])
def test_gui_only_examples_export_without_a_domain_model(number, tmp_path):
    root = next(p for p in (EXAMPLES / f'example{number}').iterdir() if p.name.lower() == 'gui')
    model = retool_rsx_to_gui(str(root))
    output = tmp_path / 'gui.py'
    gui_model_to_code(model, str(output))
    namespace = {}
    exec(output.read_text(encoding='utf-8'), namespace)
    assert set(screens(namespace['gui_model'])) == set(screens(model))
    assert set(elements(namespace['gui_model'])) == set(elements(model))
