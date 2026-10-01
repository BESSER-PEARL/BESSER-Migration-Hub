# Generator evaluation from recreated APEX B-UML references

All platforms use the same saved input models, derived from the improved APEX parser on `export_to_buml/example1–5`. These are parser-derived references, not independent ground truth.

Counts describe exported structure, not execution in a live platform. Attributes exclude platform identity/FK columns. Generated APEX global/home/login scaffolding is excluded. APEX uses `OracleApexFullAppGenerator`, the generator selected by the web application. APEX action types are reconstructed classifications from exported button evidence; their ratio does not establish preservation of action semantics. ReTool action types count as zero because the generator does not export Button.actionType; caption guesses do not count as generated actions. Retool captions are counted directly from RSX. ServiceNow is evaluated for data models only, using exported Table, scalar column, ReferenceColumn, and related-list declarations. Association-end counts do not verify cardinality bounds.

The APEX application generator renders each B-UML screen and its Form, Button, InputField, and class-backed DataList widgets directly. Unbound forms have no invented persistence. Unsupported behavior is recorded in the target inventories.

## Data model

| Platform | Element | Input B-UML | Generated |
|---|---|---:|---:|
| ServiceNow | Entities | 20 | 20 |
| ServiceNow | Attributes | 151 | 151 |
| ServiceNow | Associations | 11 | 11 |
| ServiceNow | Multiplicities | 22 | 22 |
| ServiceNow | Generalizations | 0 | 0 |
| ServiceNow | Enumerations | 0 | 0 |

## By application

| Platform | Application | Element | Input B-UML | Generated |
|---|---|---|---:|---:|
| ServiceNow | example1 | Entities | 1 | 1 |
| ServiceNow | example1 | Attributes | 8 | 8 |
| ServiceNow | example1 | Associations | 0 | 0 |
| ServiceNow | example1 | Multiplicities | 0 | 0 |
| ServiceNow | example1 | Generalizations | 0 | 0 |
| ServiceNow | example1 | Enumerations | 0 | 0 |
| ServiceNow | example2 | Entities | 3 | 3 |
| ServiceNow | example2 | Attributes | 27 | 27 |
| ServiceNow | example2 | Associations | 2 | 2 |
| ServiceNow | example2 | Multiplicities | 4 | 4 |
| ServiceNow | example2 | Generalizations | 0 | 0 |
| ServiceNow | example2 | Enumerations | 0 | 0 |
| ServiceNow | example3 | Entities | 6 | 6 |
| ServiceNow | example3 | Attributes | 20 | 20 |
| ServiceNow | example3 | Associations | 5 | 5 |
| ServiceNow | example3 | Multiplicities | 10 | 10 |
| ServiceNow | example3 | Generalizations | 0 | 0 |
| ServiceNow | example3 | Enumerations | 0 | 0 |
| ServiceNow | example4 | Entities | 8 | 8 |
| ServiceNow | example4 | Attributes | 87 | 87 |
| ServiceNow | example4 | Associations | 2 | 2 |
| ServiceNow | example4 | Multiplicities | 4 | 4 |
| ServiceNow | example4 | Generalizations | 0 | 0 |
| ServiceNow | example4 | Enumerations | 0 | 0 |
| ServiceNow | example5 | Entities | 2 | 2 |
| ServiceNow | example5 | Attributes | 9 | 9 |
| ServiceNow | example5 | Associations | 2 | 2 |
| ServiceNow | example5 | Multiplicities | 4 | 4 |
| ServiceNow | example5 | Generalizations | 0 | 0 |
| ServiceNow | example5 | Enumerations | 0 | 0 |
