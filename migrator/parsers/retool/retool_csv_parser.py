"""Retool CSV export -> BESSER B-UML DomainModel parser.

Reads CSV files exported from a Retool DB (one file per table).
CSV headers define column names; the `id` column is always skipped.
Columns ending in `_id` whose prefix matches another CSV entity name
are converted to BinaryAssociation objects instead of plain attributes.

CSV filename normalisation: common export suffixes (_example, _data, _test,
_sample, _demo, _export, _table, _db) are stripped when deriving entity
class names, but the full stem is still used for FK cross-reference
matching so that e.g. `author_id` → `author_example` works correctly.
"""

import csv
import os
import re

from besser.BUML.metamodel.structural import (
    BinaryAssociation,
    BooleanType,
    Class,
    DateTimeType,
    DateType,
    DomainModel,
    FloatType,
    IntegerType,
    Multiplicity,
    Property,
    StringType,
)

# Suffixes stripped from CSV filename stems when deriving entity class names
_DROP_SUFFIXES = (
    '_example', '_data', '_test', '_sample',
    '_demo', '_export', '_table', '_db',
)


def _normalize_stem(stem: str) -> str:
    """Strip common export suffixes from a CSV filename stem (lowercase)."""
    lower = stem.lower()
    for suffix in _DROP_SUFFIXES:
        if lower.endswith(suffix):
            return lower[: -len(suffix)]
    return lower


def _to_pascal(name: str) -> str:
    """Convert snake_case / lower-case identifier to PascalCase class name."""
    return "".join(word.capitalize() for word in name.replace('-', '_').split('_'))


def _infer_type(col_name: str):
    """Heuristic B-UML type from a column name."""
    lower = col_name.lower()
    if re.search(r'(^date$|_date$|_at$|_on$|^created$|^updated$|birth|^start$|^end$)', lower):
        return DateType
    if re.search(r'(time|timestamp)', lower):
        return DateTimeType
    if re.search(r'(^is_|^has_|^can_|enabled$|active$|^flag)', lower):
        return BooleanType
    if re.search(r'(^pages$|^count$|quantity|qty|price|amount|^age$|^year$|^num$|^total$|^size$)', lower):
        return IntegerType
    return StringType


def retool_csv_to_buml(csv_dir: str, module_name: str = None) -> DomainModel:
    """Parse Retool CSV files from a directory and return a B-UML DomainModel.

    Args:
        csv_dir:     Directory containing .csv files exported from Retool DB.
        module_name: Optional name for the resulting DomainModel.

    Returns:
        A populated DomainModel, or None if no CSV files are found.
    """
    if not os.path.isdir(csv_dir):
        print(f"CSV directory not found: {csv_dir}")
        return None

    csv_files = sorted(f for f in os.listdir(csv_dir) if f.lower().endswith('.csv'))
    if not csv_files:
        print(f"No CSV files found in: {csv_dir}")
        return None

    print(f"Parsing {len(csv_files)} CSV file(s) in: {os.path.basename(csv_dir)}")

    # ── First pass: collect all table metadata ─────────────────────────────
    # raw_stem_lower → {headers, path, norm_stem, class_name}
    table_info: dict = {}
    for fname in csv_files:
        raw_stem = os.path.splitext(fname)[0]
        norm_stem = _normalize_stem(raw_stem)
        class_name = _to_pascal(norm_stem)
        path = os.path.join(csv_dir, fname)
        with open(path, 'r', encoding='utf-8-sig') as fh:
            headers = [h.strip() for h in next(csv.reader(fh))]
        table_info[raw_stem.lower()] = {
            'headers':    headers,
            'path':       path,
            'norm_stem':  norm_stem,
            'class_name': class_name,
        }

    # Build norm_stem → raw_stem mapping for FK resolution
    norm_to_raw: dict = {info['norm_stem']: raw for raw, info in table_info.items()}

    name = module_name or 'RetoolApp'
    domain_model = DomainModel(name=name)
    classes: dict = {}      # raw_stem_lower → Class
    pending_fks: list = []  # (from_raw, fk_col_lower, to_raw)

    # ── Second pass: build Class objects ──────────────────────────────────
    for raw_stem, info in table_info.items():
        headers    = info['headers']
        class_name = info['class_name']

        # Detect FK columns (ending in _id whose prefix maps to another table)
        fk_cols: dict = {}  # col_lower → to_raw_stem
        for col in headers:
            col_lower = col.lower()
            if col_lower == 'id':
                continue
            if not col_lower.endswith('_id'):
                continue
            fk_prefix = col_lower[:-3]  # strip trailing _id

            # Priority 1: exact match on normalised stem
            if fk_prefix in norm_to_raw:
                to_raw = norm_to_raw[fk_prefix]
                fk_cols[col_lower] = to_raw
                pending_fks.append((raw_stem, col_lower, to_raw))
                continue

            # Priority 2: raw stem starts with fk_prefix + '_'
            for candidate_raw in table_info:
                if (candidate_raw == fk_prefix
                        or candidate_raw.startswith(fk_prefix + '_')):
                    fk_cols[col_lower] = candidate_raw
                    pending_fks.append((raw_stem, col_lower, candidate_raw))
                    break

        # Build domain attributes (skip id and FK columns)
        properties: set = set()
        for col in headers:
            col_lower = col.lower()
            if col_lower == 'id':
                continue
            if col_lower in fk_cols:
                continue
            buml_type = _infer_type(col_lower)
            properties.add(Property(
                name=col_lower,
                type=buml_type,
                multiplicity=Multiplicity(0, 1),
            ))

        cls = Class(name=class_name, attributes=properties)
        classes[raw_stem] = cls
        domain_model.types.add(cls)
        print(f"  Class '{class_name}': {sorted(p.name for p in properties)}")

    # ── Third pass: build BinaryAssociation objects from FK edges ──────────
    print(f"  Building {len(pending_fks)} association(s) from FK columns…")
    for from_raw, fk_col, to_raw in pending_fks:
        if from_raw not in classes or to_raw not in classes:
            print(f"  ⚠  Skipping FK '{from_raw}.{fk_col}' → unknown table '{to_raw}'")
            continue
        from_cls = classes[from_raw]
        to_cls   = classes[to_raw]
        end_many = Property(
            name=from_cls.name.lower(),
            type=from_cls,
            multiplicity=Multiplicity(0, '*'),
        )
        end_one = Property(
            name=to_cls.name.lower(),
            type=to_cls,
            multiplicity=Multiplicity(0, 1),
        )
        assoc = BinaryAssociation(
            name=f"{from_cls.name}_{to_cls.name}",
            ends={end_many, end_one},
        )
        domain_model.associations.add(assoc)
        print(f"  Association: {from_cls.name} ──→ {to_cls.name}  (FK: {fk_col})")

    print(
        f"  Total: {len(classes)} class(es), "
        f"{len(domain_model.associations)} association(s)"
    )
    return domain_model
