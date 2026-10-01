# Oracle APEX parser coverage

Input dataset: `evaluation_replication/examples/oracle_apex`.

Values are extracted/source. These five applications also supply the shared generator references.

Source counts are audited independently from SQL declarations; extracted counts come from actual model objects.

Attributes exclude FK columns and identity columns, including multiline and ON NULL identity declarations. Extracted attributes count only matching source scalar columns; retained platform identities, misclassified FK columns, and attributes absent from the source are excluded and recorded separately in the inventories. Associations count declared FKs; multiplicities count their two ends. SQL checks are not B-UML enum declarations.

GUI source counts include skipped pages. Bound entities count distinct declared schema tables referenced by region SQL/table metadata or native form-process table metadata; explanatory HTML and displayed code samples are excluded. Extracted bound entities include real class references on widgets and their data sources. Navigation counts explicit in-app button redirects and branches, including parameterized page targets; script-inferred navigation is excluded. Forms count native form regions or legacy/custom form pages with form-process or editable/submit evidence. Labels count button/submit captions, with button-name fallbacks. Action types count distinct classified button categories per app; a Form submit control has no Button.actionType in B-UML.

## Data model

| Application | Entities | Attributes | Associations | Multiplicities | Generalizations | Enumerations |
|---|---:|---:|---:|---:|---:|---:|
| example1 | 1/1 | 8/8 | 0/0 | 0/0 | 0/0 | 0/0 |
| example2 | 3/3 | 27/27 | 2/2 | 4/4 | 0/0 | 0/0 |
| example3 | 6/6 | 20/20 | 5/5 | 10/10 | 0/0 | 0/0 |
| example4 | 8/8 | 87/88 | 2/3 | 4/6 | 0/0 | 0/0 |
| example5 | 2/2 | 9/9 | 2/2 | 4/4 | 0/0 | 0/0 |
| Total | 100.0% | 99.3% | 91.7% | 91.7% | -- | -- |

## Gui model

| Application | Screens | Bound entities | Buttons | Action types | Navigation | Forms | Labels |
|---|---:|---:|---:|---:|---:|---:|---:|
| example1 | 12/14 | 0/0 | 26/29 | 3/4 | 0/15 | 6/6 | 26/29 |
| example2 | 16/18 | 1/1 | 24/25 | 2/2 | 0/12 | 7/8 | 24/25 |
| example3 | 1/4 | 0/0 | 0/1 | 0/1 | 0/0 | 0/1 | 0/1 |
| example4 | 9/11 | 3/3 | 23/24 | 4/4 | 0/9 | 4/5 | 23/24 |
| example5 | 25/27 | 2/2 | 32/33 | 2/2 | 0/30 | 8/9 | 32/33 |
| Total | 85.1% | 100.0% | 93.8% | 84.6% | 0.0% | 86.2% | 93.8% |
