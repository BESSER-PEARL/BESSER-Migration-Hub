# sample_reporting: generator evaluation (RQ2, oracle BUML ground truth)

**18 non-Screen object(s) found in the oracle's `Module.screens`** (a known authoring bug in this oracle file - see `load_oracle`'s docstring in `evaluate_generator.py`): `RANK_and_DENSE_RANK_List` (DataList), `Format_Masks_List` (DataList), `ROW_NUMBER_List` (DataList), `Bind_Variables_List` (DataList), `Top_N_Queries_List` (DataList), `Regular_Expressions_List` (DataList), `Report_from_Collection_List` (DataList), `CASE_Statement_List` (DataList), `Linking_to_Interactive_Reports_List` (DataList), `LEAD_and_LAG_List` (DataList), `LISTAGG_List` (DataList), `RATIO_TO_REPORT_List` (DataList), `Inline_Views_List` (DataList), `Custom_Buttons_List` (DataList), `Interactive_Report_List` (DataList), `Highlighting_List` (DataList), `Drill_Down_IR_List` (DataList), `Pipelined_Functions_List` (DataList). These were dropped before generation, so Screens/related widget counts for this scenario undercount the true oracle.

## BUML (oracle) → Retool (RQ2)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 2 | 2 | 100.0% |
| Attributes | 10 | 10 | 100.0% |
| Associations | 1 | 1 | 100.0% |
| Multiplicities | 2 | 2 | 100.0% |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Modules | 1 | 1 | 100.0% |
| Screens | 21 | 21 | 100.0% |
| Bound entities | 0 | 0 | N/A |
| Buttons | 15 | 15 | 100.0% |
| Action types | 4 | 5 | 125.0% |
| Navigation | 0 | 0 | N/A |
| Forms | 0 | 0 | N/A |
| Labels | 15 | 15 | 100.0% |
| DataLists | 0 | 0 | N/A |
| DataSources | 0 | 0 | N/A |
| Input fields | 0 | 0 | N/A |

## Generator warnings

- Button 'Cancel' has no executable action binding.
- Button 'Save' has no executable action binding.
- Button 'Reset_Report' has no executable action binding.
- Button 'Reset' has no executable action binding.
- Button 'Reset_Data' has no executable action binding.
- Button 'Create' has no executable action binding.
- Button 'Delete' has no executable action binding.
