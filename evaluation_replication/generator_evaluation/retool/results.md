# Generator evaluation from recreated APEX B-UML references

All platforms use the same saved input models, derived from the improved APEX parser on `export_to_buml/example1–5`. These are parser-derived references, not independent ground truth.

Counts describe exported structure, not execution in a live platform. Attributes exclude platform identity/FK columns. Generated APEX global/home/login scaffolding is excluded. APEX uses `OracleApexFullAppGenerator`, the generator selected by the web application. APEX action types are reconstructed classifications from exported button evidence; their ratio does not establish preservation of action semantics. ReTool action types count as zero because the generator does not export Button.actionType; caption guesses do not count as generated actions. Retool captions are counted directly from RSX. ServiceNow is evaluated for data models only, using exported Table, scalar column, ReferenceColumn, and related-list declarations. Association-end counts do not verify cardinality bounds.

The APEX application generator renders each B-UML screen and its Form, Button, InputField, and class-backed DataList widgets directly. Unbound forms have no invented persistence. Unsupported behavior is recorded in the target inventories.

## Data model

| Platform | Element | Input B-UML | Generated |
|---|---|---:|---:|
| ReTool | Entities | 20 | 20 |
| ReTool | Attributes | 151 | 151 |
| ReTool | Associations | 11 | 11 |
| ReTool | Multiplicities | 22 | 22 |
| ReTool | Generalizations | 0 | 0 |
| ReTool | Enumerations | 0 | 0 |

## GUI model

| Platform | Element | Input B-UML | Generated |
|---|---|---:|---:|
| ReTool | Screens | 63 | 63 |
| ReTool | Bound entities | 6 | 3 |
| ReTool | Buttons | 105 | 105 |
| ReTool | Action types | 11 | 0 |
| ReTool | Navigation | 0 | 0 |
| ReTool | Forms | 25 | 25 |
| ReTool | Labels | 105 | 105 |

## By application

| Platform | Application | Element | Input B-UML | Generated |
|---|---|---|---:|---:|
| ReTool | example1 | Entities | 1 | 1 |
| ReTool | example1 | Attributes | 8 | 8 |
| ReTool | example1 | Associations | 0 | 0 |
| ReTool | example1 | Multiplicities | 0 | 0 |
| ReTool | example1 | Generalizations | 0 | 0 |
| ReTool | example1 | Enumerations | 0 | 0 |
| ReTool | example1 | Screens | 12 | 12 |
| ReTool | example1 | Bound entities | 0 | 0 |
| ReTool | example1 | Buttons | 26 | 26 |
| ReTool | example1 | Action types | 3 | 0 |
| ReTool | example1 | Navigation | 0 | 0 |
| ReTool | example1 | Forms | 6 | 6 |
| ReTool | example1 | Labels | 26 | 26 |
| ReTool | example2 | Entities | 3 | 3 |
| ReTool | example2 | Attributes | 27 | 27 |
| ReTool | example2 | Associations | 2 | 2 |
| ReTool | example2 | Multiplicities | 4 | 4 |
| ReTool | example2 | Generalizations | 0 | 0 |
| ReTool | example2 | Enumerations | 0 | 0 |
| ReTool | example2 | Screens | 16 | 16 |
| ReTool | example2 | Bound entities | 1 | 1 |
| ReTool | example2 | Buttons | 24 | 24 |
| ReTool | example2 | Action types | 2 | 0 |
| ReTool | example2 | Navigation | 0 | 0 |
| ReTool | example2 | Forms | 7 | 7 |
| ReTool | example2 | Labels | 24 | 24 |
| ReTool | example3 | Entities | 6 | 6 |
| ReTool | example3 | Attributes | 20 | 20 |
| ReTool | example3 | Associations | 5 | 5 |
| ReTool | example3 | Multiplicities | 10 | 10 |
| ReTool | example3 | Generalizations | 0 | 0 |
| ReTool | example3 | Enumerations | 0 | 0 |
| ReTool | example3 | Screens | 1 | 1 |
| ReTool | example3 | Bound entities | 0 | 0 |
| ReTool | example3 | Buttons | 0 | 0 |
| ReTool | example3 | Action types | 0 | 0 |
| ReTool | example3 | Navigation | 0 | 0 |
| ReTool | example3 | Forms | 0 | 0 |
| ReTool | example3 | Labels | 0 | 0 |
| ReTool | example4 | Entities | 8 | 8 |
| ReTool | example4 | Attributes | 87 | 87 |
| ReTool | example4 | Associations | 2 | 2 |
| ReTool | example4 | Multiplicities | 4 | 4 |
| ReTool | example4 | Generalizations | 0 | 0 |
| ReTool | example4 | Enumerations | 0 | 0 |
| ReTool | example4 | Screens | 9 | 9 |
| ReTool | example4 | Bound entities | 3 | 0 |
| ReTool | example4 | Buttons | 23 | 23 |
| ReTool | example4 | Action types | 4 | 0 |
| ReTool | example4 | Navigation | 0 | 0 |
| ReTool | example4 | Forms | 4 | 4 |
| ReTool | example4 | Labels | 23 | 23 |
| ReTool | example5 | Entities | 2 | 2 |
| ReTool | example5 | Attributes | 9 | 9 |
| ReTool | example5 | Associations | 2 | 2 |
| ReTool | example5 | Multiplicities | 4 | 4 |
| ReTool | example5 | Generalizations | 0 | 0 |
| ReTool | example5 | Enumerations | 0 | 0 |
| ReTool | example5 | Screens | 25 | 25 |
| ReTool | example5 | Bound entities | 2 | 2 |
| ReTool | example5 | Buttons | 32 | 32 |
| ReTool | example5 | Action types | 2 | 0 |
| ReTool | example5 | Navigation | 0 | 0 |
| ReTool | example5 | Forms | 8 | 8 |
| ReTool | example5 | Labels | 32 | 32 |
