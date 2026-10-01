# Generator evaluation from recreated APEX B-UML references

All platforms use the same saved input models, derived from the improved APEX parser on `export_to_buml/example1–5`. These are parser-derived references, not independent ground truth.

Counts describe exported structure, not execution in a live platform. Attributes exclude platform identity/FK columns. Generated APEX global/home/login scaffolding is excluded. APEX uses `OracleApexFullAppGenerator`, the generator selected by the web application. APEX action types are reconstructed classifications from exported button evidence; their ratio does not establish preservation of action semantics. ReTool action types count as zero because the generator does not export Button.actionType; caption guesses do not count as generated actions. Retool captions are counted directly from RSX. ServiceNow is evaluated for data models only, using exported Table, scalar column, ReferenceColumn, and related-list declarations. Association-end counts do not verify cardinality bounds.

The APEX application generator renders each B-UML screen and its Form, Button, InputField, and class-backed DataList widgets directly. Unbound forms have no invented persistence. Unsupported behavior is recorded in the target inventories.

## Data model

| Platform | Element | Input B-UML | Generated |
|---|---|---:|---:|
| Oracle APEX | Entities | 20 | 20 |
| Oracle APEX | Attributes | 151 | 151 |
| Oracle APEX | Associations | 11 | 11 |
| Oracle APEX | Multiplicities | 22 | 22 |
| Oracle APEX | Generalizations | 0 | 0 |
| Oracle APEX | Enumerations | 0 | 0 |

## GUI model

| Platform | Element | Input B-UML | Generated |
|---|---|---:|---:|
| Oracle APEX | Screens | 63 | 63 |
| Oracle APEX | Bound entities | 6 | 6 |
| Oracle APEX | Buttons | 105 | 105 |
| Oracle APEX | Action types | 11 | 11 |
| Oracle APEX | Navigation | 0 | 0 |
| Oracle APEX | Forms | 25 | 25 |
| Oracle APEX | Labels | 105 | 105 |

## By application

| Platform | Application | Element | Input B-UML | Generated |
|---|---|---|---:|---:|
| Oracle APEX | example1 | Entities | 1 | 1 |
| Oracle APEX | example1 | Attributes | 8 | 8 |
| Oracle APEX | example1 | Associations | 0 | 0 |
| Oracle APEX | example1 | Multiplicities | 0 | 0 |
| Oracle APEX | example1 | Generalizations | 0 | 0 |
| Oracle APEX | example1 | Enumerations | 0 | 0 |
| Oracle APEX | example1 | Screens | 12 | 12 |
| Oracle APEX | example1 | Bound entities | 0 | 0 |
| Oracle APEX | example1 | Buttons | 26 | 26 |
| Oracle APEX | example1 | Action types | 3 | 3 |
| Oracle APEX | example1 | Navigation | 0 | 0 |
| Oracle APEX | example1 | Forms | 6 | 6 |
| Oracle APEX | example1 | Labels | 26 | 26 |
| Oracle APEX | example2 | Entities | 3 | 3 |
| Oracle APEX | example2 | Attributes | 27 | 27 |
| Oracle APEX | example2 | Associations | 2 | 2 |
| Oracle APEX | example2 | Multiplicities | 4 | 4 |
| Oracle APEX | example2 | Generalizations | 0 | 0 |
| Oracle APEX | example2 | Enumerations | 0 | 0 |
| Oracle APEX | example2 | Screens | 16 | 16 |
| Oracle APEX | example2 | Bound entities | 1 | 1 |
| Oracle APEX | example2 | Buttons | 24 | 24 |
| Oracle APEX | example2 | Action types | 2 | 2 |
| Oracle APEX | example2 | Navigation | 0 | 0 |
| Oracle APEX | example2 | Forms | 7 | 7 |
| Oracle APEX | example2 | Labels | 24 | 24 |
| Oracle APEX | example3 | Entities | 6 | 6 |
| Oracle APEX | example3 | Attributes | 20 | 20 |
| Oracle APEX | example3 | Associations | 5 | 5 |
| Oracle APEX | example3 | Multiplicities | 10 | 10 |
| Oracle APEX | example3 | Generalizations | 0 | 0 |
| Oracle APEX | example3 | Enumerations | 0 | 0 |
| Oracle APEX | example3 | Screens | 1 | 1 |
| Oracle APEX | example3 | Bound entities | 0 | 0 |
| Oracle APEX | example3 | Buttons | 0 | 0 |
| Oracle APEX | example3 | Action types | 0 | 0 |
| Oracle APEX | example3 | Navigation | 0 | 0 |
| Oracle APEX | example3 | Forms | 0 | 0 |
| Oracle APEX | example3 | Labels | 0 | 0 |
| Oracle APEX | example4 | Entities | 8 | 8 |
| Oracle APEX | example4 | Attributes | 87 | 87 |
| Oracle APEX | example4 | Associations | 2 | 2 |
| Oracle APEX | example4 | Multiplicities | 4 | 4 |
| Oracle APEX | example4 | Generalizations | 0 | 0 |
| Oracle APEX | example4 | Enumerations | 0 | 0 |
| Oracle APEX | example4 | Screens | 9 | 9 |
| Oracle APEX | example4 | Bound entities | 3 | 3 |
| Oracle APEX | example4 | Buttons | 23 | 23 |
| Oracle APEX | example4 | Action types | 4 | 4 |
| Oracle APEX | example4 | Navigation | 0 | 0 |
| Oracle APEX | example4 | Forms | 4 | 4 |
| Oracle APEX | example4 | Labels | 23 | 23 |
| Oracle APEX | example5 | Entities | 2 | 2 |
| Oracle APEX | example5 | Attributes | 9 | 9 |
| Oracle APEX | example5 | Associations | 2 | 2 |
| Oracle APEX | example5 | Multiplicities | 4 | 4 |
| Oracle APEX | example5 | Generalizations | 0 | 0 |
| Oracle APEX | example5 | Enumerations | 0 | 0 |
| Oracle APEX | example5 | Screens | 25 | 25 |
| Oracle APEX | example5 | Bound entities | 2 | 2 |
| Oracle APEX | example5 | Buttons | 32 | 32 |
| Oracle APEX | example5 | Action types | 2 | 2 |
| Oracle APEX | example5 | Navigation | 0 | 0 |
| Oracle APEX | example5 | Forms | 8 | 8 |
| Oracle APEX | example5 | Labels | 32 | 32 |
