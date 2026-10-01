# BUML to Retool generators

`RetoolCSVGenerator` exports data tables. `RetoolRsxAppGenerator` exports a
classic Retool Toolscript GUI folder and ZIP. `RetoolGenerator` runs both.

```python
from migrator.generators.retool import RetoolGenerator

generator = RetoolGenerator(
    model=domain_model,
    gui_model=gui_model,
    app_name='catalog',
    output_dir='output/retool',
    resource_id='YOUR_RETOOL_DATABASE_RESOURCE_UUID',
)
csv_paths, gui_zip = generator.generate()
print(generator.warnings)
```

The output contains `csv/<table>.csv`, `csv/schema.json`, `catalog.zip`, and a
`catalog/` folder with `main.rsx`, `functions.rsx`, `metadata.json`, `src/`,
`lib/`, `.positions/`, and `generation_report.json`.

## Data export

A domain model contains schema, not records. The default CSVs contain headers
only, ready to fill with application data. Pass records explicitly:

```python
from migrator.generators.retool import RetoolCSVGenerator

RetoolCSVGenerator(
    model=domain_model,
    output_dir='output/retool',
    rows={'Product': [{'id': 1, 'name': 'Green tea', 'price': 12.99}]},
).generate()
```

Row mapping keys may be BUML class names or generated table names. Column keys
may be BUML property names or generated snake_case names. Dates use ISO format,
booleans use `true`/`false`, and CSV quoting preserves commas and newlines. Unknown
tables/columns, ambiguous aliases, and missing required values are rejected
before CSV files are written. Record-level type checks, key uniqueness, and
referential integrity must still be checked in the destination database.

Use `include_sample_data=True` to request one demonstration row per table;
`schema.json` marks this explicitly. Sample data cannot be combined with supplied
rows. Real records are never synthesized from a domain model. When a table has
no existing primary key, the generated schema adds a numeric `id`; supplied
records missing that synthetic key receive sequential IDs.

The shared schema preserves existing primary keys and their types, inherited
attributes, many-to-one FKs, one-to-one unique FKs, and many-to-many junction
tables. All generated identifiers use snake_case. Colliding identifiers,
composite primary keys, and multivalued attributes raise explicit errors.
Inheritance is flattened into each class's table. Junction tables have their
own generated key and two foreign keys.

CSV import does not encode database constraints or reliably retain column
types. Configure those using `schema.json`, which records types, enum values,
keys, nullability, uniqueness, and FK references. Filling header-only CSVs with
records or using explicit samples helps type inference during import.

## GUI export

```python
from migrator.generators.retool import RetoolRsxAppGenerator

generator = RetoolRsxAppGenerator(
    domain_model=domain_model, gui_model=gui_model,
    app_name='catalog', output_dir='output/retool',
)
gui_zip = generator.generate()
```

With a GUI model, the generator preserves its screens and modal dialogs and
renders tables, forms, standalone fields, static selector options, text, images,
containers, basic bar/line/pie charts, metric fields, and explicit page/dialog
transitions. Queries select from the same table names used by CSV generation.
Table columns follow their data source's field list and use the real primary
key when it is displayed. Unsupported inputs use a text field fallback;
unsupported components and action bindings are reported.

Without a GUI model, a domain model produces one table page per entity and
junction table. Without a domain model, a GUI model still exports its widgets
and static content; tables and charts need their data sources wired manually.

The output targets the **classic RSX/Toolscript format used by the repository's
Retool examples**. Import the ZIP in a compatible Retool instance and reconnect
queries to your database resource. The default resource UUID is a placeholder.
Current Retool also has a separate [React/CLI app format](https://docs.retool.com/build/apps/guides/create/cli);
this generator does not emit that format.

Layouts use a simple vertical grid rather than reproducing every source style.
Forms keep visible submit labels and field metadata. Executable page/dialog
transitions require explicit BUML `Event`/`Transition` objects. CRUD queries,
JavaScript transformations, computed columns, charts without bound x/y fields,
and arbitrary action logic need manual wiring; the generator does not infer
database writes from a button label. Review `generation_report.json` and
`generator.warnings` for the specific gaps in each export.

Generated files are overwritten on subsequent runs. Other files in the app
folder are retained, and the ZIP includes only files from the current generation.
Always import the newly generated ZIP to avoid stale files from earlier runs.

`RetoolGenerator.generate()` now returns `(csv_paths, gui_zip)`.
`generate_csv()` and `generate_gui()` run each export separately. The previous
domain-only Transit JSON scaffold remains available via `generate_json()`;
it does not export a supplied GUI model.

## Example and checks

From the repository root:

```powershell
python -m migrator.converters.retool_example --example 3 --output output/retool_example3
python -m pytest tests/test_retool_generators.py tests/test_retool_parsers.py -q
```

The example reads the fixture's data/GUI into BUML, exports its original CSV
records and generated GUI, and prints the ZIP location and generation warnings.
Tests cover all four fixtures, CSV data/types/keys, relational associations,
inheritance, GUI-only export, escaping, dialog transitions, regeneration,
legacy JSON, and the web application's Retool target integration.

Validation checks generated files and round-trips through the repository's
parsers. Live import into a Retool instance has not been verified.
