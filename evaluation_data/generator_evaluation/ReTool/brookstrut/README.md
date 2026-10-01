# brookstrut: generator evaluation (RQ2, oracle BUML ground truth)

**17 non-Screen object(s) found in the oracle's `Module.screens`** (a known authoring bug in this oracle file - see `load_oracle`'s docstring in `evaluate_generator.py`): `Product_Availability_List` (DataList), `Transaction_Summary_by_Minute_List` (DataList), `Sales_History_Generation_Log_List` (DataList), `Recent_Sales_List` (DataList), `Sales_by_Product_and_Store_by_Week_List` (DataList), `Transaction_Log_List` (DataList), `Sales_by_Store_by_Week_List` (DataList), `Transaction_Summary_by_Hour_List` (DataList), `Store_Regions_List` (DataList), `Region_Stores_List` (DataList), `Configuration_Options_List` (DataList), `Sales_History_Interactive_Report_List` (DataList), `Page_Views_List` (DataList), `Products_List` (DataList), `Generate_Transaction` (Button), `Top_Users_List` (DataList), `Event_Log_List` (DataList). These were dropped before generation, so Screens/related widget counts for this scenario undercount the true oracle.

## BUML (oracle) → Retool (RQ2)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 5 | 5 | 100.0% |
| Attributes | 31 | 31 | 100.0% |
| Associations | 5 | 5 | 100.0% |
| Multiplicities | 10 | 10 | 100.0% |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Modules | 1 | 1 | 100.0% |
| Screens | 29 | 29 | 100.0% |
| Bound entities | 0 | 0 | N/A |
| Buttons | 57 | 57 | 100.0% |
| Action types | 4 | 5 | 125.0% |
| Navigation | 0 | 0 | N/A |
| Forms | 0 | 0 | N/A |
| Labels | 57 | 57 | 100.0% |
| DataLists | 0 | 0 | N/A |
| DataSources | 0 | 0 | N/A |
| Input fields | 0 | 0 | N/A |

## Generator warnings

- Button 'Refresh_Page' has no executable action binding.
- Button 'Up' has no executable action binding.
- Button 'Refresh' has no executable action binding.
- Button 'Reload' has no executable action binding.
- Button 'Cancel' has no executable action binding.
- Button 'Remove_Transactions' has no executable action binding.
- Button 'Generate_Transaction' has no executable action binding.
- Button 'Reset' has no executable action binding.
- Button 'Edit_Store' has no executable action binding.
- Button 'Create' has no executable action binding.
- Button 'Delete' has no executable action binding.
- Button 'Save' has no executable action binding.
- Button 'Reset_Report' has no executable action binding.
