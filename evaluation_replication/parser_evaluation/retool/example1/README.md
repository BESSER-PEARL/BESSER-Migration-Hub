# example1: current parser evaluation (RQ1 only)

Generator evaluation (RQ2) is not measured here: see `python -m migrator.evaluation.generators`, which grades the generator against the shared parser-derived APEX B-UML references instead of this script's own parser output.

## Retool → BUML (RQ1)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 3 | 3 | 100.0% |
| Attributes | 14 | 14 | 100.0% |
| Associations | 2 | 2 | 100.0% |
| Multiplicities | 4 | 4 | 100.0% |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Screens | 10 | 10 | 100.0% |
| Bound entities | 3 | 3 | 100.0% |
| Buttons | 11 | 11 | 100.0% |
| Action types | 4 | 4 | 100.0% |
| Navigation | 1 | 0 | 0.0% |
| Forms | 3 | 3 | 100.0% |
| Labels | 11 | 11 | 100.0% |

Source/pivot event declarations: **19 / 0**. Button classifications are naming heuristics; they do not establish executable CRUD behavior.

Records present in source CSV (not instances recovered from BUML): `{'books': 20, 'discount_codes': 5, 'orders': 10}`.

## Artifacts

- `source_inventory.json`: file hashes, independent tag/header counts and source evidence.
- `project.py`: executable combined model, with documented serializer repairs.
- `pivot.pkl`: exact locally produced reference model (load only trusted local snapshots).
- `inventory.json`: classes, relationships, screens, widgets, bindings.
- `pipeline.log`, `results.json`: diagnostics and machine-readable results.

