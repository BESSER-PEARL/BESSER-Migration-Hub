# example3: current parser evaluation (RQ1 only)

Generator evaluation (RQ2) is not measured here: see `python -m migrator.evaluation.generators`, which grades the generator against the shared parser-derived APEX B-UML references instead of this script's own parser output.

## Retool → BUML (RQ1)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 1 | 1 | 100.0% |
| Attributes | 6 | 6 | 100.0% |
| Associations | 0 | 0 | N/A |
| Multiplicities | 0 | 0 | N/A |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Screens | 4 | 4 | 100.0% |
| Bound entities | 1 | 1 | 100.0% |
| Buttons | 7 | 7 | 100.0% |
| Action types | 5 | 5 | 100.0% |
| Navigation | 4 | 1 | 25.0% |
| Forms | 2 | 2 | 100.0% |
| Labels | 7 | 7 | 100.0% |

Source/pivot event declarations: **14 / 1**. Button classifications are naming heuristics; they do not establish executable CRUD behavior.

Records present in source CSV (not instances recovered from BUML): `{'products': 3}`.

## Artifacts

- `source_inventory.json`: file hashes, independent tag/header counts and source evidence.
- `project.py`: executable combined model, with documented serializer repairs.
- `pivot.pkl`: exact locally produced reference model (load only trusted local snapshots).
- `inventory.json`: classes, relationships, screens, widgets, bindings.
- `pipeline.log`, `results.json`: diagnostics and machine-readable results.

