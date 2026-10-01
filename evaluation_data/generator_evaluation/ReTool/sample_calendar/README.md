# sample_calendar: generator evaluation (RQ2, oracle BUML ground truth)

**2 non-Screen object(s) found in the oracle's `Module.screens`** (a known authoring bug in this oracle file - see `load_oracle`'s docstring in `evaluate_generator.py`): `Report_List` (DataList), `Date_Reporting_List` (DataList). These were dropped before generation, so Screens/related widget counts for this scenario undercount the true oracle.

## BUML (oracle) → Retool (RQ2)

| Element | Reference | Output | Coverage |
|---|---:|---:|---:|
| Entities | 3 | 3 | 100.0% |
| Attributes | 26 | 26 | 100.0% |
| Associations | 0 | 0 | N/A |
| Multiplicities | 0 | 0 | N/A |
| Generalizations | 0 | 0 | N/A |
| Enumerations | 0 | 0 | N/A |
| Modules | 1 | 1 | 100.0% |
| Screens | 33 | 33 | 100.0% |
| Bound entities | 0 | 0 | N/A |
| Buttons | 27 | 27 | 100.0% |
| Action types | 4 | 5 | 125.0% |
| Navigation | 0 | 0 | N/A |
| Forms | 0 | 0 | N/A |
| Labels | 27 | 27 | 100.0% |
| DataLists | 1 | 1 | 100.0% |
| DataSources | 1 | 1 | 100.0% |
| Input fields | 0 | 0 | N/A |

## Generator warnings

- Button 'Cancel' has no executable action binding.
- Button 'Reset_Data' has no executable action binding.
- Button 'View_Report' has no executable action binding.
- Button 'Save' has no executable action binding.
- Button 'Save_In_Database' has no executable action binding.
- Button 'Show_In_Calendar' has no executable action binding.
- Button 'Next' has no executable action binding.
- Button 'Prev' has no executable action binding.
- Button 'Today' has no executable action binding.
- Table 'Report_List' has no domain class; data binding needs manual wiring.
- Button 'Reset_Report' has no executable action binding.
- Button 'Clear' has no executable action binding.
- Button 'Create' has no executable action binding.
- Button 'Delete' has no executable action binding.
