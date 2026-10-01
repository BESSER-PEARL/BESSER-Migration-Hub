# Retool parser element counts (RQ1 only)

Base = original Retool CSV/GUI exports; BUML = parsed pivot (output of the migration parser). Counts use the current parser. This file does not measure the generator (BUML -> Retool, RQ2): see `generator_results.md`, which grades the generator against an independently-authored oracle BUML model rather than the parser's own output measured here.

| Example | Element | Base | BUML |
|---|---|---:|---:|
| example1 | Entities | 3 | 3 |
| example1 | Attributes | 14 | 14 |
| example1 | Associations | 2 | 2 |
| example1 | Multiplicities | 4 | 4 |
| example1 | Generalizations | 0 | 0 |
| example1 | Enumerations | 0 | 0 |
| example1 | Modules | 1 | 1 |
| example1 | Screens | 10 | 10 |
| example1 | Bound entities | 3 | 3 |
| example1 | Buttons | 11 | 11 |
| example1 | Action types | 4 | 4 |
| example1 | Navigation | 1 | 0 |
| example1 | Forms | 3 | 3 |
| example1 | Labels | 11 | 11 |
| example1 | DataLists | 8 | 8 |
| example1 | DataSources | 8 | 8 |
| example1 | Input fields | 32 | 32 |
| example2 | Entities | 1 | 1 |
| example2 | Attributes | 9 | 9 |
| example2 | Associations | 0 | 0 |
| example2 | Multiplicities | 0 | 0 |
| example2 | Generalizations | 0 | 0 |
| example2 | Enumerations | 0 | 0 |
| example2 | Modules | 1 | 1 |
| example2 | Screens | 4 | 4 |
| example2 | Bound entities | 1 | 1 |
| example2 | Buttons | 1 | 1 |
| example2 | Action types | 0 | 0 |
| example2 | Navigation | 0 | 0 |
| example2 | Forms | 1 | 1 |
| example2 | Labels | 1 | 1 |
| example2 | DataLists | 1 | 1 |
| example2 | DataSources | 1 | 1 |
| example2 | Input fields | 6 | 6 |
| example3 | Entities | 1 | 1 |
| example3 | Attributes | 6 | 6 |
| example3 | Associations | 0 | 0 |
| example3 | Multiplicities | 0 | 0 |
| example3 | Generalizations | 0 | 0 |
| example3 | Enumerations | 0 | 0 |
| example3 | Modules | 1 | 1 |
| example3 | Screens | 4 | 4 |
| example3 | Bound entities | 1 | 1 |
| example3 | Buttons | 7 | 7 |
| example3 | Action types | 5 | 5 |
| example3 | Navigation | 4 | 1 |
| example3 | Forms | 2 | 2 |
| example3 | Labels | 7 | 7 |
| example3 | DataLists | 1 | 1 |
| example3 | DataSources | 1 | 1 |
| example3 | Input fields | 6 | 6 |
| example4 | Entities | 2 | 2 |
| example4 | Attributes | 6 | 6 |
| example4 | Associations | 0 | 0 |
| example4 | Multiplicities | 0 | 0 |
| example4 | Generalizations | 0 | 0 |
| example4 | Enumerations | 0 | 0 |
| example4 | Modules | 1 | 1 |
| example4 | Screens | 2 | 2 |
| example4 | Bound entities | 2 | 2 |
| example4 | Buttons | 1 | 1 |
| example4 | Action types | 1 | 1 |
| example4 | Navigation | 1 | 1 |
| example4 | Forms | 0 | 0 |
| example4 | Labels | 1 | 1 |
| example4 | DataLists | 1 | 1 |
| example4 | DataSources | 1 | 1 |
| example4 | Input fields | 0 | 0 |
| example5 | Entities | 1 | 1 |
| example5 | Attributes | 8 | 8 |
| example5 | Associations | 0 | 0 |
| example5 | Multiplicities | 0 | 0 |
| example5 | Generalizations | 0 | 0 |
| example5 | Enumerations | 0 | 0 |
| example5 | Modules | 1 | 1 |
| example5 | Screens | 5 | 5 |
| example5 | Bound entities | 1 | 1 |
| example5 | Buttons | 9 | 9 |
| example5 | Action types | 5 | 5 |
| example5 | Navigation | 6 | 1 |
| example5 | Forms | 1 | 1 |
| example5 | Labels | 7 | 7 |
| example5 | DataLists | 1 | 1 |
| example5 | DataSources | 1 | 1 |
| example5 | Input fields | 12 | 12 |

Counting notes:

- N/A means the source export does not declare a comparable element (e.g. CSV has no generalization/enumeration syntax). Associations/Multiplicities are not N/A: a `*_id` column whose prefix names another table in the same export is counted as an implicit association at every stage (Base, BUML), via the same naming convention the parser itself uses to build associations - not just once the parser has run.
- Attributes count scalar properties/columns, excluding columns classified as an implicit association (see above). Two source FK columns are counted as associations at every stage, not as attributes anywhere, so Base and BUML no longer disagree on their classification.
- Buttons include each Form's submit control: BUML models it as `Form.submit_label`, not a separate Button widget, but it renders as a standalone `<Button>` in the source export, so it is counted here at every stage (no example form sets `show_cancel`, so this is exact, not an approximation). Labels count authored button/submit captions only; ID-derived captions synthesized for icon-only buttons are excluded from these counts.
- Screens include named views/wrappers, dialogs, and implicit main pages. Navigation counts explicit operations, excluding script-inferred navigation. Action types count distinct CRUD/navigation categories classified from a button's wired-up Events first (a triggered query name like `deleteProduct`, or a widget `show`/`hide` event) and only falling back to its caption text when no event is conclusive. No field in the raw export is literally named "action type", but the evidence it is classified from (a query name, an event method) is real, literal source data, so Base computes this independently of the parser (same keyword map, applied directly to the raw tags) rather than reporting `N/A` - it is not a parser-only concept, just a parser-only field name. Whether the generator preserves this classification is a generator question, not measured here - see `generator_results.md`.
- This follows the parser measurement in paper section 6. It measures export structure, not live Retool execution or layout equivalence.

Regenerate: `python examples/retool/evaluate.py`. Only this table is saved; intermediate models and exports are temporary.
