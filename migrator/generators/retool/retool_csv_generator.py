"""Generate CSV import templates or supplied rows from a BUML domain model."""
import csv
from datetime import date, datetime
import json
from pathlib import Path
from besser.BUML.metamodel.structural import Enumeration

from ._schema import collect_tables


class RetoolCSVGenerator:
    """Export one CSV per relational table and a schema.json manifest.

    Domain models contain schema rather than records. CSVs are header-only by
    default. Pass rows={class_or_table_name: [dict, ...]} to export real records,
    or include_sample_data=True to explicitly request demonstration records.
    """

    def __init__(self, model, output_dir=None, rows=None, include_sample_data=False):
        if model is None:
            raise ValueError('A domain model is required for CSV generation')
        if rows is not None and include_sample_data:
            raise ValueError('Supply rows or request sample data, not both')
        self.model = model
        self.output_dir = Path(output_dir or 'retool_output')
        self.rows = rows or {}
        self.include_sample_data = include_sample_data

    def generate(self):
        tables = collect_tables(self.model)
        known = {t.name for t in tables} | {t.entity.name for t in tables if t.entity}
        unknown = set(self.rows) - known
        if unknown:
            raise ValueError(f'Rows supplied for unknown entities: {sorted(unknown)}')
        prepared = []
        for table in tables:
            records = self.rows.get(table.name, self.rows.get(table.entity.name, []) if table.entity else [])
            if self.include_sample_data:
                records = [{c.name: c.sample() for c in table.columns}]
            aliases = {c.source_name: c.name for c in table.columns if c.source_name}
            allowed = {c.name for c in table.columns}
            normalized = []
            for row_number, record in enumerate(records, 1):
                row = {aliases.get(k, k): v for k, v in record.items()}
                if len(row) != len(record):
                    raise ValueError(f'Duplicate aliases in row {row_number} of {table.name}')
                if set(row) - allowed:
                    raise ValueError(f'Unknown columns in {table.name}: {sorted(set(row) - allowed)}')
                for column in table.columns:
                    if column.primary_key and column.synthetic and column.name not in row:
                        row[column.name] = row_number
                    if not column.nullable and row.get(column.name) is None:
                        raise ValueError(f'Missing required value in {table.name}.{column.name}, row {row_number}')
                normalized.append({k: self._value(v) for k, v in row.items()})
            prepared.append((table, normalized))
        csv_dir = self.output_dir / 'csv'
        csv_dir.mkdir(parents=True, exist_ok=True)
        written = []
        for table, records in prepared:
            path = csv_dir / f'{table.name}.csv'
            with path.open('w', encoding='utf-8', newline='') as fh:
                writer = csv.DictWriter(fh, fieldnames=[c.name for c in table.columns])
                writer.writeheader()
                writer.writerows(records)
            written.append(str(path))
        manifest = {
            'model': self.model.name, 'sample_data': self.include_sample_data,
            'tables': [{
                'name': t.name, 'entity': t.entity.name if t.entity else None, 'junction': t.junction,
                'columns': [{
                    'name': c.name, 'type': c.type.name, 'primary_key': c.primary_key,
                    'nullable': c.nullable, 'synthetic': c.synthetic, 'unique': c.primary_key or c.unique,
                    'enum_values': sorted(literal.name for literal in c.type.literals) if isinstance(c.type, Enumeration) else None,
                    'references': {'table': c.reference[0], 'column': c.reference[1]} if c.reference else None,
                } for c in t.columns],
            } for t in tables],
        }
        (csv_dir / 'schema.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding='utf-8')
        return written

    @staticmethod
    def _value(value):
        if value is None:
            return ''
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if isinstance(value, (datetime, date)):
            return value.isoformat()
        return value
