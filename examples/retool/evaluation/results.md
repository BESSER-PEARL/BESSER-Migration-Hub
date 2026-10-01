# Retool pipeline element counts

Base = original Retool CSV/GUI exports; BUML = parsed pivot supplied to the generator; Target = generated Retool CSV/GUI exports. Counts use the current parser and generator.

| Example | Element | Base | BUML | Target |
|---|---|---:|---:|---:|
| example1 | Entities | 3 | 3 | 3 |
| example1 | Attributes | 16 | 14 | 16 |
| example1 | Associations | N/A | 2 | 0 |
| example1 | Multiplicities | N/A | 4 | 0 |
| example1 | Generalizations | 0 | 0 | 0 |
| example1 | Enumerations | 0 | 0 | 0 |
| example1 | Modules | 1 | 1 | 1 |
| example1 | Screens | 10 | 10 | 10 |
| example1 | Bound entities | 3 | 3 | 3 |
| example1 | Buttons | 11 | 8 | 11 |
| example1 | Action types | N/A | 4 | 0 |
| example1 | Navigation | 1 | 0 | 0 |
| example1 | Forms | 3 | 3 | 3 |
| example1 | Labels | 11 | 11 | 11 |
| example1 | DataLists | 8 | 8 | 8 |
| example1 | DataSources | 8 | 8 | 8 |
| example1 | Input fields | 32 | 32 | 32 |
| example2 | Entities | 1 | 1 | 1 |
| example2 | Attributes | 9 | 9 | 9 |
| example2 | Associations | N/A | 0 | 0 |
| example2 | Multiplicities | N/A | 0 | 0 |
| example2 | Generalizations | 0 | 0 | 0 |
| example2 | Enumerations | 0 | 0 | 0 |
| example2 | Modules | 1 | 1 | 1 |
| example2 | Screens | 4 | 4 | 4 |
| example2 | Bound entities | 1 | 1 | 1 |
| example2 | Buttons | 1 | 0 | 1 |
| example2 | Action types | N/A | 0 | 0 |
| example2 | Navigation | 0 | 0 | 0 |
| example2 | Forms | 1 | 1 | 1 |
| example2 | Labels | 1 | 1 | 1 |
| example2 | DataLists | 1 | 1 | 1 |
| example2 | DataSources | 1 | 1 | 1 |
| example2 | Input fields | 6 | 6 | 6 |
| example3 | Entities | 1 | 1 | 1 |
| example3 | Attributes | 6 | 6 | 6 |
| example3 | Associations | N/A | 0 | 0 |
| example3 | Multiplicities | N/A | 0 | 0 |
| example3 | Generalizations | 0 | 0 | 0 |
| example3 | Enumerations | 0 | 0 | 0 |
| example3 | Modules | 1 | 1 | 1 |
| example3 | Screens | 4 | 4 | 4 |
| example3 | Bound entities | 1 | 1 | 1 |
| example3 | Buttons | 7 | 5 | 7 |
| example3 | Action types | N/A | 3 | 0 |
| example3 | Navigation | 4 | 1 | 1 |
| example3 | Forms | 2 | 2 | 2 |
| example3 | Labels | 7 | 7 | 7 |
| example3 | DataLists | 1 | 1 | 1 |
| example3 | DataSources | 1 | 1 | 1 |
| example3 | Input fields | 6 | 6 | 6 |
| example4 | Entities | 2 | 2 | 2 |
| example4 | Attributes | 6 | 6 | 6 |
| example4 | Associations | N/A | 0 | 0 |
| example4 | Multiplicities | N/A | 0 | 0 |
| example4 | Generalizations | 0 | 0 | 0 |
| example4 | Enumerations | 0 | 0 | 0 |
| example4 | Modules | 1 | 1 | 1 |
| example4 | Screens | 2 | 2 | 2 |
| example4 | Bound entities | 2 | 2 | 2 |
| example4 | Buttons | 1 | 1 | 1 |
| example4 | Action types | N/A | 1 | 0 |
| example4 | Navigation | 1 | 1 | 1 |
| example4 | Forms | 0 | 0 | 0 |
| example4 | Labels | 1 | 1 | 1 |
| example4 | DataLists | 1 | 1 | 1 |
| example4 | DataSources | 1 | 1 | 1 |
| example4 | Input fields | 0 | 0 | 0 |
| example5 | Entities | 1 | 1 | 1 |
| example5 | Attributes | 8 | 8 | 8 |
| example5 | Associations | N/A | 0 | 0 |
| example5 | Multiplicities | N/A | 0 | 0 |
| example5 | Generalizations | 0 | 0 | 0 |
| example5 | Enumerations | 0 | 0 | 0 |
| example5 | Modules | 1 | 1 | 1 |
| example5 | Screens | 5 | 5 | 5 |
| example5 | Bound entities | 1 | 1 | 1 |
| example5 | Buttons | 9 | 8 | 9 |
| example5 | Action types | N/A | 3 | 0 |
| example5 | Navigation | 6 | 1 | 1 |
| example5 | Forms | 1 | 1 | 1 |
| example5 | Labels | 7 | 7 | 7 |
| example5 | DataLists | 1 | 1 | 1 |
| example5 | DataSources | 1 | 1 | 1 |
| example5 | Input fields | 12 | 12 | 12 |

Counting notes:

- N/A means the source export does not declare a comparable element. CSV relationships and cardinalities cannot be verified; the two BUML associations are inferred. Target counts exclude supplementary `schema.json` constraints.
- Attributes count scalar properties/columns. Two source FK columns become BUML association roles; generation restores them. Synthetic primary-key columns the generator adds for tables with no natural key are excluded from these counts, since they are generator boilerplate, not model- or source-derived data.
- Buttons include source/target submit controls. BUML puts seven submit controls into Forms, giving 22 standalone buttons plus seven form controls. Labels count authored button/submit captions only; ID-derived captions synthesized for icon-only buttons are excluded from these counts rather than inflating BUML/Target.
- Screens include named views/wrappers, dialogs, and implicit main pages. Navigation counts explicit operations, excluding script-inferred navigation. Action types count BUML enum intent; the target does not preserve it as explicit CRUD/cancel actions.
- This follows the separate parser/generator measurements in paper section 6. It measures export structure, not live Retool execution or layout equivalence.

Regenerate: `python examples/retool/evaluate.py`. Only this table is saved; intermediate models and exports are temporary.
