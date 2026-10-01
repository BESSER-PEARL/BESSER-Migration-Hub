"""Command-line migration through the shared B-UML pivot model."""
import argparse
from pathlib import Path

from migrator.api import parse_source
from migrator.pipeline import generate_target


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', choices=['mendix', 'oracle_apex', 'retool'], required=True)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--gui', type=Path)
    parser.add_argument('--module')
    parser.add_argument('--target', choices=['oracle_apex', 'retool', 'service_now', 'sql', 'spreadsheet'], required=True)
    parser.add_argument('--sql-dialect', choices=['mysql', 'postgres'])
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    domain, gui = parse_source(args.source, args.data, args.gui, args.module)
    warnings = generate_target(args.target, args.sql_dialect, domain, args.output, gui_model=gui)
    print(f'Generated artifacts in {args.output.resolve()}')
    for warning in warnings:
        print(f'Review: {warning}')


if __name__ == '__main__':
    main()
