# sample_master_detail: generator evaluation (RQ2, oracle BUML ground truth)

**3 non-Screen object(s) found in the oracle's `Module.screens`** (a known authoring bug in this oracle file - see `load_oracle`'s docstring in `evaluate_generator.py`): `Top_Users_List` (DataList), `Drill_Down_List` (DataList), `Page_Views_List` (DataList). These were dropped before generation, so Screens/related widget counts for this scenario undercount the true oracle.

## BUML (oracle) → Retool (RQ2)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 8 | 8 | 100.0% |
| Attributes | 66 | 66 | 100.0% |
| Associations | 12 | 12 | 100.0% |
| Multiplicities | 24 | 24 | 100.0% |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Modules | 1 | 1 | 100.0% |
| Screens | 29 | 29 | 100.0% |
| Bound entities | 0 | 0 | N/A |
| Buttons | 81 | 81 | 100.0% |
| Action types | 4 | 5 | 125.0% |
| Navigation | 0 | 0 | N/A |
| Forms | 0 | 0 | N/A |
| Labels | 81 | 81 | 100.0% |
| DataLists | 0 | 0 | N/A |
| DataSources | 0 | 0 | N/A |
| Input fields | 0 | 0 | N/A |

## Generator warnings

- Button 'Cancel' has no executable action binding.
- Button 'Save' has no executable action binding.
- Button 'Add_Comment' has no executable action binding.
- Button 'Create' has no executable action binding.
- Button 'Delete' has no executable action binding.
- Button 'Get_Next_Rowid' has no executable action binding.
- Button 'Get_Previous_Rowid' has no executable action binding.
- Button 'Login' has no executable action binding.
- Button 'Load_Sample_Data' has no executable action binding.
- Button 'Remove_Sample_Data' has no executable action binding.
- Button 'Reset_Data' has no executable action binding.
- Button 'Apply_Changes' has no executable action binding.
- Button 'Add_Milestone' has no executable action binding.
- Button 'Add_Task' has no executable action binding.
- Button 'Edit_Project' has no executable action binding.
- Button 'Edit' has no executable action binding.
- Button 'Pop_Eba_Demo_Md_Comments' has no executable action binding.
- Button 'Pop_Eba_Demo_Md_Milestones' has no executable action binding.
- Button 'Pop_Eba_Demo_Md_Tasks' has no executable action binding.
- Button 'Reset' has no executable action binding.
- Button 'Calendar' has no executable action binding.
- Button 'Add_Link' has no executable action binding.
- Button 'Add_Todo' has no executable action binding.
- Button 'Edit_Task' has no executable action binding.
- Button 'Add' has no executable action binding.
- Button 'Submit' has no executable action binding.
