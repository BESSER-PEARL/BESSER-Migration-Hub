"""Export an example through BUML to Retool CSV and Toolscript artifacts."""
import argparse
import csv
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from migrator.generators.retool import RetoolGenerator
from migrator.parsers.retool.retool_csv_parser import retool_csv_to_buml
from migrator.parsers.retool.retool_rsx_parser import retool_rsx_to_gui


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--example', type=int, choices=[1, 2, 3, 4, 5], default=3)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--resource-id', help='Retool DB resource UUID; defaults to a placeholder')
    args = parser.parse_args()
    name = f'example{args.example}'
    root = Path(__file__).resolve().parent / 'base_examples' / name
    data_dir = next(path for path in root.iterdir() if path.name.lower() == 'data')
    gui_dir = next(path for path in root.iterdir() if path.name.lower() == 'gui')
    domain = retool_csv_to_buml(str(data_dir), module_name=name, rsx_dir=str(gui_dir))
    gui = retool_rsx_to_gui(str(gui_dir), module_name=name, domain_model=domain)
    rows = {}
    for path in sorted(data_dir.glob('*.csv')):
        with path.open(encoding='utf-8-sig', newline='') as fh:
            rows[path.stem] = list(csv.DictReader(fh))
    output = args.output or PROJECT_ROOT / 'output' / 'retool' / name
    generator = RetoolGenerator(model=domain, gui_model=gui, app_name=name,
                                output_dir=str(output), rows=rows, resource_id=args.resource_id)
    csv_files, archive = generator.generate()
    print(f'Generated {len(csv_files)} CSV tables and {archive}')
    for warning in generator.warnings:
        print(f'  Review: {warning}')


if __name__ == '__main__':
    main()
