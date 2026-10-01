# example5: current parser evaluation (RQ1 only)

Generator evaluation (RQ2) is not measured here: see `evaluate_generator.py` / `generator_results.md`, which grades the generator against an independently-authored oracle BUML model instead of this script's own parser output.

## Retool → BUML (RQ1)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 1 | 1 | 100.0% |
| Attributes | 8 | 8 | 100.0% |
| Associations | 0 | 0 | N/A |
| Multiplicities | 0 | 0 | N/A |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Modules | 1 | 1 | 100.0% |
| Screens | 5 | 5 | 100.0% |
| Bound entities | 1 | 1 | 100.0% |
| Buttons | 9 | 9 | 100.0% |
| Action types | 5 | 5 | 100.0% |
| Navigation | 6 | 1 | 16.67% |
| Forms | 1 | 1 | 100.0% |
| Labels | 7 | 7 | 100.0% |
| DataLists | 1 | 1 | 100.0% |
| DataSources | 1 | 1 | 100.0% |
| Input fields | 12 | 12 | 100.0% |

Source/pivot event declarations: **29 / 1**. Button classifications are naming heuristics; they do not establish executable CRUD behavior.

Records present in source CSV (not instances recovered from BUML): `{'team_members': 3}`.

## Artifacts

- `source_inventory.json`: file hashes, independent tag/header counts and source evidence.
- `project.py`: executable combined model, with documented serializer repairs.
- `pivot.pkl`: exact locally produced reference model (load only trusted local snapshots).
- `inventory.json`: classes, relationships, screens, widgets, bindings.
- `pipeline.log`, `results.json`: diagnostics and machine-readable results.

