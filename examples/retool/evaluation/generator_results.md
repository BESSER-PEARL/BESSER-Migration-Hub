# Retool generator element counts (RQ2 only, oracle BUML ground truth)

Oracle BUML = independently-authored ground-truth model (`evaluation_data/BUML_ground_truth`), never produced by any parser run; Target = generated Retool CSV/GUI exports. This measures the generator alone - see `results.md` for the parser (RQ1), which is a separate script and a separate set of examples.

| Scenario | Element | Oracle BUML | Target |
|---|---|---:|---:|
| brookstrut | Entities | 5 | 5 |
| brookstrut | Attributes | 31 | 31 |
| brookstrut | Associations | 5 | 5 |
| brookstrut | Multiplicities | 10 | 10 |
| brookstrut | Generalizations | 0 | 0 |
| brookstrut | Enumerations | 0 | 0 |
| brookstrut | Modules | 1 | 1 |
| brookstrut | Screens | 29 | 29 |
| brookstrut | Bound entities | 0 | 0 |
| brookstrut | Buttons | 57 | 57 |
| brookstrut | Action types | 4 | 0 |
| brookstrut | Navigation | 0 | 0 |
| brookstrut | Forms | 0 | 0 |
| brookstrut | Labels | 0 | 44 |
| brookstrut | DataLists | 0 | 0 |
| brookstrut | DataSources | 0 | 0 |
| brookstrut | Input fields | 0 | 0 |
| sample_calendar | Entities | 3 | 3 |
| sample_calendar | Attributes | 26 | 26 |
| sample_calendar | Associations | 0 | 0 |
| sample_calendar | Multiplicities | 0 | 0 |
| sample_calendar | Generalizations | 0 | 0 |
| sample_calendar | Enumerations | 0 | 0 |
| sample_calendar | Modules | 1 | 1 |
| sample_calendar | Screens | 33 | 33 |
| sample_calendar | Bound entities | 0 | 0 |
| sample_calendar | Buttons | 27 | 27 |
| sample_calendar | Action types | 4 | 0 |
| sample_calendar | Navigation | 0 | 0 |
| sample_calendar | Forms | 0 | 0 |
| sample_calendar | Labels | 0 | 14 |
| sample_calendar | DataLists | 1 | 1 |
| sample_calendar | DataSources | 1 | 1 |
| sample_calendar | Input fields | 0 | 0 |
| sample_interactive_grids | Entities | 3 | 3 |
| sample_interactive_grids | Attributes | 29 | 29 |
| sample_interactive_grids | Associations | 2 | 2 |
| sample_interactive_grids | Multiplicities | 4 | 4 |
| sample_interactive_grids | Generalizations | 0 | 0 |
| sample_interactive_grids | Enumerations | 0 | 0 |
| sample_interactive_grids | Modules | 1 | 1 |
| sample_interactive_grids | Screens | 47 | 47 |
| sample_interactive_grids | Bound entities | 0 | 0 |
| sample_interactive_grids | Buttons | 95 | 95 |
| sample_interactive_grids | Action types | 4 | 0 |
| sample_interactive_grids | Navigation | 0 | 0 |
| sample_interactive_grids | Forms | 0 | 0 |
| sample_interactive_grids | Labels | 0 | 86 |
| sample_interactive_grids | DataLists | 0 | 0 |
| sample_interactive_grids | DataSources | 0 | 0 |
| sample_interactive_grids | Input fields | 0 | 0 |
| sample_master_detail | Entities | 8 | 8 |
| sample_master_detail | Attributes | 66 | 66 |
| sample_master_detail | Associations | 12 | 12 |
| sample_master_detail | Multiplicities | 24 | 24 |
| sample_master_detail | Generalizations | 0 | 0 |
| sample_master_detail | Enumerations | 0 | 0 |
| sample_master_detail | Modules | 1 | 1 |
| sample_master_detail | Screens | 29 | 29 |
| sample_master_detail | Bound entities | 0 | 0 |
| sample_master_detail | Buttons | 81 | 81 |
| sample_master_detail | Action types | 4 | 0 |
| sample_master_detail | Navigation | 0 | 0 |
| sample_master_detail | Forms | 0 | 0 |
| sample_master_detail | Labels | 0 | 55 |
| sample_master_detail | DataLists | 0 | 0 |
| sample_master_detail | DataSources | 0 | 0 |
| sample_master_detail | Input fields | 0 | 0 |
| sample_reporting | Entities | 2 | 2 |
| sample_reporting | Attributes | 10 | 10 |
| sample_reporting | Associations | 1 | 1 |
| sample_reporting | Multiplicities | 2 | 2 |
| sample_reporting | Generalizations | 0 | 0 |
| sample_reporting | Enumerations | 0 | 0 |
| sample_reporting | Modules | 1 | 1 |
| sample_reporting | Screens | 21 | 21 |
| sample_reporting | Bound entities | 0 | 0 |
| sample_reporting | Buttons | 15 | 15 |
| sample_reporting | Action types | 4 | 0 |
| sample_reporting | Navigation | 0 | 0 |
| sample_reporting | Forms | 0 | 0 |
| sample_reporting | Labels | 0 | 8 |
| sample_reporting | DataLists | 0 | 0 |
| sample_reporting | DataSources | 0 | 0 |
| sample_reporting | Input fields | 0 | 0 |

Dropped-screen notes (oracle authoring bug, not a generator defect - see `load_oracle` in `evaluate_generator.py`):

- brookstrut: 17 dropped - Configuration_Options_List (DataList), Sales_History_Interactive_Report_List (DataList), Page_Views_List (DataList), Transaction_Summary_by_Hour_List (DataList), Generate_Transaction (Button), Top_Users_List (DataList), Products_List (DataList), Event_Log_List (DataList), Sales_by_Store_by_Week_List (DataList), Region_Stores_List (DataList), Product_Availability_List (DataList), Transaction_Summary_by_Minute_List (DataList), Sales_History_Generation_Log_List (DataList), Recent_Sales_List (DataList), Sales_by_Product_and_Store_by_Week_List (DataList), Transaction_Log_List (DataList), Store_Regions_List (DataList)
- sample_calendar: 2 dropped - Report_List (DataList), Date_Reporting_List (DataList)
- sample_interactive_grids: none
- sample_master_detail: 3 dropped - Top_Users_List (DataList), Page_Views_List (DataList), Drill_Down_List (DataList)
- sample_reporting: 18 dropped - LISTAGG_List (DataList), Regular_Expressions_List (DataList), CASE_Statement_List (DataList), Top_N_Queries_List (DataList), RATIO_TO_REPORT_List (DataList), Pipelined_Functions_List (DataList), Drill_Down_IR_List (DataList), Custom_Buttons_List (DataList), Inline_Views_List (DataList), Format_Masks_List (DataList), Interactive_Report_List (DataList), RANK_and_DENSE_RANK_List (DataList), Linking_to_Interactive_Reports_List (DataList), Highlighting_List (DataList), LEAD_and_LAG_List (DataList), Bind_Variables_List (DataList), ROW_NUMBER_List (DataList), Report_from_Collection_List (DataList)

Counting notes:

- No parser runs in this script. The oracle BUML model is loaded directly from `evaluation_data/BUML_ground_truth` and never touches `migrator/parsers/retool`.
- `include_sample_data=True` is used for CSV generation, since no real row data exists for these scenarios; row/cell-level data fidelity is not measured here.
- Attributes/Associations/Multiplicities match exactly in every scenario: FK columns are identified for Target via the generator's own `schema.json` `references` field (ground truth from the generator, not a name guess), since the oracle's association-end role names (e.g. `oowdemostores`) don't always resemble the referenced table's name the way `evaluate.py`'s naming heuristic expects.
- Action types: Target is always 0 for the same reason as in `evaluate.py` - the generator never serializes `Button.actionType` back into the output. The oracle here has real, hand-assigned values (e.g. brookstrut: 75 Cancel, 6 Add, 5 Save, 3 Delete across 89 buttons), so this gap is not an artifact of this script's counting - it is a genuine, confirmed generator limitation.
- Labels is NOT a reliable number in this report: `pivot_inventory`'s Labels count excludes a Button when `label == name`, because in parser output that specific case means a caption-less button fell back to its raw widget id (see `evaluate.py`). In this independently-authored oracle, buttons are routinely named after their own caption on purpose (e.g. `name="Reset_Report", label='Reset_Report'`) - every single button in brookstrut has `label == name` (89/89) - so that heuristic misfires here and reports Oracle Labels as 0 across all five scenarios. The nonzero Target counts are the real, generator-reported figures; Oracle is undercounted by this script, not by the generator.
- Counting rules otherwise (implicit FK associations, synthetic primary keys, Form submit buttons, ID-derived captions) are identical to `evaluate.py` - the same `pivot_inventory`/`csv_inventory`/`audit_gui` functions are reused, not reimplemented, so the two reports are comparable.
- See `evaluate.py`'s module docstring for why RQ1 (parser) and RQ2 (generator) are measured in separate scripts rather than chained together.

Regenerate: `python examples/retool/evaluate_generator.py`. Only this table is saved; intermediate models and exports are temporary.
