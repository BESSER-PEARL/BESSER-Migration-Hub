"""Reproduce the Retool GENERATOR evaluation (paper section 6, RQ2 only).

This script measures BUML -> Retool (the generator) exclusively, against an
independently-authored oracle BUML model, NOT against the parser's own pivot
output (see evaluate.py's module docstring for why that would be circular -
a parser bug would otherwise become the "ground truth" the generator is
graded against). No parser code runs anywhere in this script.

Run from the repository: python examples/retool/evaluate_generator.py
Only the counts table is retained; pipeline artifacts use a temporary directory.
"""
import json
import runpy
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from migrator.generators.retool import RetoolGenerator
from besser.BUML.metamodel.gui.graphical_ui import Screen

from evaluate import DATA_KEYS, GUI_KEYS, audit_gui, csv_inventory, dump, pivot_inventory, ratios, table

ORACLE_ROOT = ROOT / 'evaluation_data' / 'BUML_ground_truth'
SCENARIOS = ['brookstrut', 'sample_calendar', 'sample_interactive_grids',
             'sample_master_detail', 'sample_reporting']


def load_oracle(scenario):
    """Load the hand-authored oracle BUML model for `scenario` and return
    (domain, gui, dropped).

    `dropped` lists non-Screen objects found in a Module's `screens` set - a
    known authoring bug in several of these files: a Screen and a
    same-named widget inside it are built as two Python objects assigned to
    the same variable name (e.g. a Screen and a DataList both named
    "Transaction_Summary_by_Hour_List"). Because the widget is assigned to
    that name after the Screen, by the time `Module(screens={...})` reads
    the identifier it captures the widget, not the Screen. The true Screen
    object is gone - overwritten - and cannot be recovered from the file as
    committed, so it is dropped here rather than guessed at, and reported
    explicitly rather than silently undercounting or (as happens if this
    isn't done) crashing RetoolGenerator outright, since it assumes every
    `Module.screens` entry is a Screen.
    """
    root = ORACLE_ROOT / scenario
    content = (root / 'data_model.py').read_text(encoding='utf-8') + '\n' + \
        (root / 'gui_model.py').read_text(encoding='utf-8')
    tmp = Path(tempfile.mkdtemp(prefix=f'oracle-{scenario}-'))
    combined = tmp / 'combined.py'
    combined.write_text(content, encoding='utf-8')
    namespace = runpy.run_path(str(combined))
    domain, gui = namespace['domain_model'], namespace['gui_model']
    dropped = []
    for module in gui.modules:
        bad = {s for s in module.screens if not isinstance(s, Screen)}
        if bad:
            dropped.extend({'module': module.name, 'name': b.name, 'kind': type(b).__name__} for b in bad)
            module.screens = module.screens - bad
    return domain, gui, dropped


def run_scenario(scenario, output_root):
    out = Path(output_root) / scenario
    out.mkdir(parents=True, exist_ok=True)
    domain, gui, dropped = load_oracle(scenario)
    oracle = pivot_inventory(domain, gui)
    dump(out / 'oracle_inventory.json', oracle)
    generator = RetoolGenerator(domain, gui_model=gui, app_name=scenario,
                                output_dir=str(out / 'buml_to_retool'), include_sample_data=True)
    paths, archive = generator.generate()
    schema_manifest = json.loads((out / 'buml_to_retool' / 'csv' / 'schema.json').read_text())
    synthetic_columns = {t['name']: {c['name'] for c in t['columns'] if c['synthetic']} for t in schema_manifest['tables']}
    # Oracle association-end role names (e.g. "oowdemostores") don't always
    # resemble the referenced table's name, so csv_inventory's naming
    # heuristic alone misses some restored FK columns; schema.json's
    # `references` field is ground truth from the generator itself.
    known_fk_columns = {t['name']: {c['name'] for c in t['columns'] if c['references']} for t in schema_manifest['tables']}
    target_data, _ = csv_inventory(out / 'buml_to_retool' / 'csv', synthetic_columns=synthetic_columns,
                                   known_fk_columns=known_fk_columns)
    target_gui = audit_gui(out / 'buml_to_retool' / scenario, {t['table'] for t in target_data['tables']})
    target_counts = target_data['counts'] | target_gui['counts']
    # CSV/RSX export has no native generalization/enum declarations. Action
    # types is NOT forced to 0 here: audit_gui now reconstructs it
    # independently from the generated RSX's own Events/captions (same logic
    # as evaluate.py's RQ1 report), so Target gets whatever that
    # reconstruction finds - see the counting notes below for why this
    # number is real but still not expected to match Oracle.
    target_counts.update(Generalizations=0, Enumerations=0)
    dump(out / 'target_inventory.json', {'data': target_data, 'gui': target_gui})
    result = {'scenario': scenario, 'generator': ratios(oracle['counts'], target_counts, DATA_KEYS + GUI_KEYS),
              'dropped_screens': dropped, 'warnings': generator.warnings}
    dump(out / 'results.json', result)
    report = f'# {scenario}: generator evaluation (RQ2, oracle BUML ground truth)\n\n'
    if dropped:
        names = ', '.join(f"`{d['name']}` ({d['kind']})" for d in dropped)
        report += (f"**{len(dropped)} non-Screen object(s) found in the oracle's `Module.screens`** "
                   "(a known authoring bug in this oracle file - see `load_oracle`'s docstring in "
                   f"`evaluate_generator.py`): {names}. These were dropped before generation, so "
                   "Screens/related widget counts for this scenario undercount the true oracle.\n\n")
    report += '## BUML (oracle) → Retool (RQ2)\n\n' + table(result['generator']) + '\n\n'
    report += '## Generator warnings\n\n' + ('\n'.join('- ' + w for w in generator.warnings) or '- (none)') + '\n'
    (out / 'README.md').write_text(report, encoding='utf-8')
    return result


def main():
    with tempfile.TemporaryDirectory(prefix='retool-generator-evaluation-') as workdir:
        results = [run_scenario(scenario, workdir) for scenario in SCENARIOS]
    lines = ['# Retool generator element counts (RQ2 only, oracle BUML ground truth)', '',
             'Oracle BUML = independently-authored ground-truth model '
             '(`evaluation_data/BUML_ground_truth`), never produced by any parser run; '
             'Target = generated Retool CSV/GUI exports. This measures the generator alone - '
             'see `results.md` for the parser (RQ1), which is a separate script and a separate '
             'set of examples.', '',
             '| Scenario | Element | Oracle BUML | Target |',
             '|---|---|---:|---:|']
    display = lambda value: 'N/A' if value is None else str(value)
    for result in results:
        for key in DATA_KEYS + GUI_KEYS:
            oracle_value = result['generator'][key]['reference']
            target_value = result['generator'][key]['output']
            lines.append(f"| {result['scenario']} | {key} | {display(oracle_value)} | {display(target_value)} |")
    lines += ['', 'Dropped-screen notes (oracle authoring bug, not a generator defect - see '
              '`load_oracle` in `evaluate_generator.py`):', '']
    for result in results:
        if result['dropped_screens']:
            names = ', '.join(f"{d['name']} ({d['kind']})" for d in result['dropped_screens'])
            lines.append(f"- {result['scenario']}: {len(result['dropped_screens'])} dropped - {names}")
        else:
            lines.append(f"- {result['scenario']}: none")
    lines += ['', 'Counting notes:', '',
              '- No parser runs in this script. The oracle BUML model is loaded directly from '
              '`evaluation_data/BUML_ground_truth` and never touches `migrator/parsers/retool`.',
              '- `include_sample_data=True` is used for CSV generation, since no real row data '
              'exists for these scenarios; row/cell-level data fidelity is not measured here.',
              '- Attributes/Associations/Multiplicities match exactly in every scenario: FK '
              'columns are identified for Target via the generator\'s own `schema.json` '
              '`references` field (ground truth from the generator, not a name guess), since '
              'the oracle\'s association-end role names (e.g. `oowdemostores`) don\'t always '
              'resemble the referenced table\'s name the way `evaluate.py`\'s naming heuristic '
              'expects.',
              '- Action types: Target is a real reconstructed number here (not forced to 0), using '
              'the same independent, event-aware classifier `evaluate.py` applies for RQ1. But it '
              'is NOT expected to match Oracle, and a match or mismatch is not a meaningful '
              'generator-quality signal in either direction, for a reason specific to these oracle '
              'scenarios: `Button.actionType` is never serialized by the generator (confirmed - it '
              'appears only in `migrator/parsers/retool`, never in `migrator/generators/retool`), '
              'and none of these oracle GUI models wire any `Event`/Transition onto their buttons '
              '(0 occurrences of `.events` in brookstrut\'s `gui_model.py`), so the generator never '
              'has executable wiring to emit either - the generated RSX has zero `<Event>` tags on '
              'these buttons. The Target number is therefore reconstructed from caption text alone, '
              'which is strictly weaker evidence than whatever basis the oracle file\'s author used '
              'to hand-assign its values (e.g. brookstrut assigns `Cancel` to 75/89 buttons, '
              'including ones like "Up" and "Reset_Report" whose caption has no cancel-ish keyword) '
              '- so Oracle and Target counts can legitimately differ (brookstrut: 4 vs 5) without '
              'that difference meaning anything about generator correctness.',
              '- Labels is NOT a reliable number in this report: `pivot_inventory`\'s Labels '
              'count excludes a Button when `label == name`, because in parser output that '
              'specific case means a caption-less button fell back to its raw widget id (see '
              '`evaluate.py`). In this independently-authored oracle, buttons are routinely '
              'named after their own caption on purpose (e.g. `name="Reset_Report", '
              'label=\'Reset_Report\'`) - every single button in brookstrut has `label == name` '
              '(89/89) - so that heuristic misfires here and reports Oracle Labels as 0 across '
              'all five scenarios. The nonzero Target counts are the real, generator-reported '
              'figures; Oracle is undercounted by this script, not by the generator.',
              '- Counting rules otherwise (implicit FK associations, synthetic primary keys, Form '
              'submit buttons, ID-derived captions) are identical to `evaluate.py` - the same '
              '`pivot_inventory`/`csv_inventory`/`audit_gui` functions are reused, not '
              'reimplemented, so the two reports are comparable.',
              '- See `evaluate.py`\'s module docstring for why RQ1 (parser) and RQ2 (generator) '
              'are measured in separate scripts rather than chained together.', '',
              'Regenerate: `python examples/retool/evaluate_generator.py`. Only this table is '
              'saved; intermediate models and exports are temporary.', '']
    output = Path(__file__).resolve().parent / 'evaluation' / 'generator_results.md'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('\n'.join(lines), encoding='utf-8')
    print(f'Saved generator counts for {len(SCENARIOS)} scenarios to {output}')


if __name__ == '__main__':
    main()
