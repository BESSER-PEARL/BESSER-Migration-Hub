# BESSER Migration Hub

Migrate applications between low-code platforms through BESSER's platform-independent B-UML model. Source parsers extract data and GUI models; target generators turn those models into platform artifacts.

This repository contains the migration library, a web interface for easy use, and the replication data for the accompanying paper.

| Platform | Source parsing | Target generation |
|---|---|---|
| Mendix | Data and GUI from export JSON | -- |
| Oracle APEX | Data and GUI from SQL exports | Data and GUI as application SQL |
| ReTool | Data from CSV; GUI from Toolscript RSX/ZIP | CSV, schema metadata and Toolscript RSX/ZIP |
| ServiceNow | -- | Data model as SDK TypeScript |

## Repository

- [`migrator/`](migrator/README.md): parsers, generators, migration commands and evaluation tooling.
- [`webapp/`](webapp/README.md): web interface calling the migration library.
- [`evaluation_replication/`](evaluation_replication/README.md): paper examples, parsed B-UML models, shared generator references, generated outputs and results.
- [`tests/`](tests/): regression checks.

## Install

Use Python 3.11 or newer; Python 3.12 was used for the evaluation.

```bash
python -m venv .venv
# Activate .venv using your shell, then:
python -m pip install -e ".[test]"
```

For the interface, follow the [webapp instructions](webapp/README.md). For Python functions and command-line migrations, see the [library documentation](migrator/README.md).

## Reproduce the evaluation

```bash
python -m migrator.evaluation.oracle_apex_parser
python -m migrator.evaluation.retool_parser
python -m migrator.evaluation.generators
python -m pytest
```

Generator evaluation uses the same saved, parser-derived APEX B-UML references for all target platforms. Regeneration and counting conventions are described in the [replication guide](evaluation_replication/README.md).

## Scope

The evaluation measures structural extraction and generation. It does not establish complete visual or runtime equivalence. Platform workflows, security rules, integrations and custom code require additional migration work.

## License

[MIT](LICENSE).
