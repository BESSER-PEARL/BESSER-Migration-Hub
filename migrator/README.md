# Migration library

All parsers, generators, shared helpers and evaluation scripts live here. The webapp calls this library.

## Parse and generate

```python
from pathlib import Path
from migrator.api import parse_source
from migrator.pipeline import generate_target

base = Path("evaluation_replication/examples/oracle_apex/example1")
domain, gui = parse_source(
    "oracle_apex", base / "data", base / "screens", module_name="Example1"
)
warnings = generate_target(
    "retool", None, domain, Path("output/example1"), gui_model=gui
)
```

`parse_source(source, data_path, gui_path=None, module_name=None)` returns the domain and optional GUI model. Supported sources are `mendix`, `oracle_apex`, and `retool`. A Mendix module name is required. Passing the domain model to the GUI parser resolves bindings to real classes.

`generate_target(target_generator, sql_dialect, model, output_dir, gui_model=None)` writes target artifacts and returns warnings. Targets are `oracle_apex`, `retool`, `service_now`, `sql`, and `spreadsheet`. SQL dialects are `mysql` and `postgres`.

```bash
python -m migrator.converters.migrate --source oracle_apex --data evaluation_replication/examples/oracle_apex/example1/data --gui evaluation_replication/examples/oracle_apex/example1/screens --module Example1 --target retool --output output/example1
```

## Platform parsers

| Function | Call |
|---|---|
| Mendix data | `mendix_to_buml(json_path, module_name, encoding="utf-16")` |
| Mendix GUI | `mendix_to_gui(json_path, module_name, domain_model=domain)` |
| Mendix modules | `list_modules(json_path)` |
| APEX data | `oracle_apex_to_buml(ddl_path, module_name=None)` |
| APEX GUI directory | `oracle_apex_to_gui(pages_dir, module_name=None, domain_model=domain)` |
| APEX combined SQL | `oracle_apex_gui_from_sql(sql_path, module_name=None, domain_model=domain)` |
| ReTool data | `retool_csv_to_buml(csv_dir, module_name=None, rsx_dir=gui_path)` |
| ReTool GUI | `retool_rsx_to_gui(zip_path, module_name=None, domain_model=domain)` |
| Experimental Power Apps data | `powerapps_to_buml(image_path, csv_paths, openai_token)` |

Import these functions from:

```python
from migrator.parsers.mendix.mendix import mendix_to_buml
from migrator.parsers.mendix.mendix_gui import mendix_to_gui
from migrator.parsers.mendix.inspection import list_modules
from migrator.parsers.oracle_apex.oracle_apex import oracle_apex_to_buml
from migrator.parsers.oracle_apex.oracle_apex_gui import oracle_apex_to_gui, oracle_apex_gui_from_sql
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui
from migrator.parsers.powerapps import powerapps_to_buml
```

`ModelMigrator(lcp, model_path, module_name, openai_token).domain_model()` and `GUIModelMigrator(lcp, model_path, module_name, openai_token, domain_model=None).gui_model()` provide the existing parser facades. Use `parse_source` for joint data/GUI extraction, including ReTool SQL join evidence.

## Platform generators

Instantiate a generator, then call `.generate()`:

```python
from migrator.generators.sql.oracle_apex_app_generator import OracleApexFullAppGenerator
from migrator.generators.sql.oracle_apex_sql_generator import OracleApexSQLGenerator
from migrator.generators.retool import RetoolGenerator, RetoolCSVGenerator, RetoolRsxAppGenerator
from migrator.generators.service_now.service_now_generator import ServiceNowGenerator
from migrator.generators.sql.sql_generator import SQLGenerator
from migrator.generators.spreadsheet.spreadsheet_generator import SpreadSheetGenerator

OracleApexFullAppGenerator(domain, gui_model=gui, output_dir="output/apex").generate()
OracleApexSQLGenerator(domain, output_dir="output/apex_data").generate()
RetoolGenerator(domain, gui_model=gui, app_name="Example", output_dir="output/retool").generate()
RetoolCSVGenerator(domain, output_dir="output/csv").generate()
RetoolRsxAppGenerator(gui_model=gui, domain_model=domain, output_dir="output/rsx").generate()
ServiceNowGenerator(domain, output_dir="output/servicenow").generate()
SQLGenerator(domain, output_dir="output/sql", sql_dialect="postgres").generate()
SpreadSheetGenerator(domain, output_dir="output/spreadsheet").generate()
```

ReTool supports explicit rows, optional sample data and a database resource ID; see its [generator documentation](generators/retool/README.md). It also exposes `RetoolGenerator.generate_json()` for the legacy JSON format.

For incremental APEX pages within an existing split export, call `generate_pages_for_gui_model(apex_export_dir, gui_model, library_model, workspace_name, user_name, output_dir=...)` from `migrator.converters.besser_to_apex`. `UIPagesSQLGenerator` in `migrator.generators.sql.sql_generator_ui` provides the underlying page template.

## Serialization and inspection

- `migrator.serialization.serialize_domain(model, pivot_dir)` writes the domain Python file.
- `migrator.serialization.serialize_gui(model, pivot_dir)` writes GUI Python or a readable fallback; returns the filename and any fallback message.
- `migrator.evaluation.retool_parser.serialize(domain, gui, folder)` writes checked `data_model.py`, `gui_model.py`, `project.py`, and a trusted local snapshot. The evaluation uses this serializer to repair omissions in the installed BESSER code builder.
- `migrator.inspection.domain_summary(model)`, `gui_summary(model)` and `classify_files(directory)` expose the inspection helpers used by the interface.

## Evaluation commands

```bash
python -m migrator.evaluation.oracle_apex_parser
python -m migrator.evaluation.retool_parser
python -m migrator.evaluation.generators
python -m migrator.evaluation.generators --platform ServiceNow
python -m migrator.evaluation.generators --rebuild-reference
python -m migrator.converters.retool_example --example 3 --output output/retool_example3
```

The [replication guide](../evaluation_replication/README.md) explains the inputs and saved outputs. Run `python -m <module> --help` for evaluation options.

## Limitations

- Mendix: runtime microflows and unsupported widgets can leave extraction gaps.
- APEX: page filters and navigation extraction limit parsing. Unbound forms have no invented persistence; unsupported generated actions are reported.
- ReTool: CSV relationships use SQL evidence and naming conventions. The generator does not preserve button action types and preserves only part of the evaluated entity bindings.
- ServiceNow: data models only. Reference/related-list counts do not establish exact cardinality enforcement.
- Power Apps: experimental screenshot/CSV extraction requires an OpenAI key and is outside the paper benchmark.
