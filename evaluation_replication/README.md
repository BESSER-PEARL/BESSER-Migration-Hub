# Paper replication data

This folder contains source examples, parser outputs and generator outputs. Executable tooling lives in [`migrator/evaluation`](../migrator/evaluation).

```text
evaluation_replication/
  examples/
    mendix/exampleN/          # JSON containing both data and GUI definitions
    oracle_apex/exampleN/    # data/*.sql and screens/page_*.sql
    retool/exampleN/         # CSV data and Toolscript RSX GUI exports
  parser_evaluation/
    mendix/exampleN/
    oracle_apex/exampleN/
    retool/exampleN/         # data_model.py, gui_model.py, project.py and inventories
  generator_evaluation/
    buml_ground_truth/exampleN/  # Shared Oracle-parser-derived B-UML input models
    oracle_apex/exampleN/        # Generated application SQL and audits
    retool/exampleN/             # Generated CSV/schema, RSX and ZIP artifacts
    servicenow/exampleN/         # Generated tables.now.ts and audits
```

Mendix example metadata identifies the selected module and source JSON. APEX stores table DDL separately from page SQL; ReTool stores CSV data separately from its GUI Toolscript files. Keep the original platform exports when importing examples.

## Parser evaluation

```bash
python -m migrator.evaluation.oracle_apex_parser
python -m migrator.evaluation.retool_parser
```

Each command writes the parsed data and GUI Python, a combined `project.py`, inventories, results and logs. The supplied Mendix projects are retained snapshots; separate data and GUI files are derived from those projects. Use the [Mendix parser functions](../migrator/README.md#platform-parsers) with the selected source module for extraction.

## Generator evaluation

```bash
python -m migrator.evaluation.generators
```

All three targets consume the same five saved models in `generator_evaluation/buml_ground_truth`. Each target gets a fresh model graph. Input hashes are recorded in the results, and compatible results are retained when running one target with `--platform APEX`, `--platform ReTool`, or `--platform ServiceNow`.

To recreate the references from the current APEX exports and rerun generation:

```bash
python -m migrator.evaluation.generators --rebuild-reference
```

The B-UML references are parser-derived, rather than independently authored source ground truth. `project.py` and `gui_model.py` can be loaded as Python; locally generated pickle files preserve the exact model graph used for evaluation.

## Results and counting

- [Combined generator results](generator_evaluation/recreated_reference_results.md)
- [Data-model LaTeX table](generator_evaluation/recreated_reference_data_table.tex)
- [Aggregate LaTeX tables](generator_evaluation/recreated_reference_tables.tex)
- [APEX parser results](parser_evaluation/oracle_apex/results.md)
- [ReTool parser results](parser_evaluation/retool/results.md)

Attributes count source scalar properties and exclude generated platform identities and relationship columns. GUI metrics are screens, bound entities, buttons, button action types, navigation, forms and labels. Form submit controls contribute to button and label counts. ReTool action types are zero when no action-type semantics are generated; caption guesses do not earn generator coverage.

The audits inspect exported structure. Association-end counts do not establish exact cardinality enforcement, and GUI counts do not establish visual or executable behavior. No target-platform deployment is required for these experiments.
