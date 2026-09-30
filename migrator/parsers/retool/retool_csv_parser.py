"""Retool CSV export -> BESSER B-UML DomainModel parser.

Reads CSV files exported from a Retool DB (one file per table).
CSV headers define column names; the `id` column becomes the class's
primary-key attribute instead of being dropped.
Columns ending in `_id` whose prefix matches another CSV entity name
(allowing simple singular/plural variation, e.g. `book_id` -> `books`)
are converted to BinaryAssociation objects instead of plain attributes.

Column types are inferred from sampled cell values first (int / float /
bool / date / datetime), falling back to a column-name heuristic only when
a column has no sampled values to look at.

CSV filename normalisation: common export suffixes (_example, _data, _test,
_sample, _demo, _export, _table, _db) are stripped when deriving entity
class names, but the full stem is still used for FK cross-reference
matching so that e.g. `author_id` → `author_example` works correctly.

Optionally, when an RSX Toolscript export directory/zip is also supplied
via `rsx_dir`, its `lib/*.sql` query files are mined for `JOIN ... ON`
clauses, which are unambiguous ground truth for foreign keys and can
confirm or supplement what the CSV-only heuristic finds.
"""

import csv
import os
import re
from datetime import date, datetime

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

from migrator.parsers.retool._rsx_source import load_rsx_source
from migrator.parsers.retool._sql_source import IDENTIFIER, clean_identifier, sql_tables

# Suffixes stripped from CSV filename stems when deriving entity class names
_DROP_SUFFIXES = (
    '_example', '_data', '_test', '_sample',
    '_demo', '_export', '_table', '_db',
)

_SAMPLE_ROWS = 20

_BOOL_LITERALS = {'true', 'false'}
_INT_RE = re.compile(r'^[+-]?\d+$')
_FLOAT_RE = re.compile(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$')
_DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
_DATETIME_RE = re.compile(r'^\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}')


def _normalize_stem(stem: str) -> str:
    """Strip common export suffixes from a CSV filename stem (lowercase)."""
    lower = stem.lower()
    for suffix in _DROP_SUFFIXES:
        if lower.endswith(suffix):
            return lower[: -len(suffix)]
    return lower


def _to_pascal(name: str) -> str:
    """Convert snake_case / lower-case identifier to PascalCase class name."""
    result = "".join(word.capitalize() for word in name.replace('-', '_').split('_'))
    if result and result[0].isdigit():
        result = "_" + result
    return result


def _stems_match(a: str, b: str) -> bool:
    """True if two identifier stems refer to the same entity, tolerating
    simple English singular/plural variation (book <-> books,
    discount_code <-> discount_codes, category <-> categories).
    """
    if a == b:
        return True
    for x, y in ((a, b), (b, a)):
        if x + 's' == y or x + 'es' == y or (x.endswith('y') and x[:-1] + 'ies' == y):
            return True
    return False


def _infer_type_from_name(col_name: str):
    """Heuristic B-UML type from a column name (fallback when no sampled
    values are available)."""
    lower = col_name.lower()
    if lower == 'id' or lower.endswith('_id'):
        return IntegerType
    if re.search(r'(^date$|_date$|_at$|_on$|birth|^start$|^end$)', lower):
        return DateType
    if re.search(r'(time|timestamp)', lower):
        return DateTimeType
    if re.search(r'(^is_|^has_|^can_|enabled$|active$|^flag)', lower):
        return BooleanType
    if re.search(r'(^pages$|^count$|quantity|qty|^age$|^year$|^num$|^total$|^size$)', lower):
        return IntegerType
    return StringType


def _infer_type_from_values(values: list, col_name: str):
    """Infer a B-UML type by inspecting sampled non-empty cell values.
    Falls back to the column-name heuristic when there is nothing to
    sample.
    """
    non_empty = [v.strip() for v in values if v is not None and v.strip() != '']
    if not non_empty:
        return _infer_type_from_name(col_name)

    lowered = [v.lower() for v in non_empty]
    if all(v in _BOOL_LITERALS for v in lowered):
        return BooleanType
    def valid_iso(value, parser):
        try:
            parser(value)
            return True
        except ValueError:
            return False

    if all(_DATETIME_RE.match(v) and valid_iso(v, datetime.fromisoformat) for v in non_empty):
        return DateTimeType
    if all(_DATE_RE.match(v) and valid_iso(v, date.fromisoformat) for v in non_empty):
        return DateType
    if all(_INT_RE.match(v) for v in non_empty):
        return IntegerType
    if all(_FLOAT_RE.match(v) or _INT_RE.match(v) for v in non_empty):
        return FloatType
    return StringType


def _mine_sql_joins(rsx_dir: str, norm_to_raw: dict) -> list:
    """Scan lib/*.sql files from an RSX export for `JOIN ... ON t1.c1 =
    t2.c2` clauses and resolve them into (from_raw, fk_col_lower, to_raw)
    tuples, matching table names against known CSV stems (singular/plural
    tolerant).

    Resolve aliases and quoted/schema-qualified tables. A side named
    ``id`` or ``<table>_id`` is treated as the referenced primary key;
    equalities with no clear primary-key side are ignored.
    """
    source = load_rsx_source(rsx_dir)
    sql_files = {k: v for k, v in source.items() if k.startswith('lib/') and k.lower().endswith('.sql')}

    def resolve_table(name: str):
        name = name.strip().strip('"').strip('`').lower()
        for raw in norm_to_raw.values():
            if _stems_match(name, raw):
                return raw
        for norm, raw in norm_to_raw.items():
            if _stems_match(name, norm):
                return raw
        return None

    fk_tuples = []
    equality = re.compile(
        rf'({IDENTIFIER})\s*\.\s*({IDENTIFIER})\s*=\s*'
        rf'({IDENTIFIER})\s*\.\s*({IDENTIFIER})', re.IGNORECASE,
    )
    for text in sql_files.values():
        _primary, aliases, sql = sql_tables(text)
        for on in re.finditer(r'\bON\b(.*?)(?=\b(?:JOIN|WHERE|GROUP|ORDER|LIMIT|UNION)\b|;|$)',
                              sql, re.IGNORECASE | re.DOTALL):
            for match in equality.finditer(on[1]):
                t1, c1, t2, c2 = map(clean_identifier, match.groups())
                t1, t2 = aliases.get(t1, t1), aliases.get(t2, t2)
                raw1, raw2 = resolve_table(t1), resolve_table(t2)
                if not raw1 or not raw2:
                    continue
                pk1 = c1 == 'id' or (c1.endswith('_id') and _stems_match(c1[:-3], t1))
                pk2 = c2 == 'id' or (c2.endswith('_id') and _stems_match(c2[:-3], t2))
                if pk1 and not pk2:
                    fk_tuples.append((raw2, c2, raw1))
                elif pk2 and not pk1:
                    fk_tuples.append((raw1, c1, raw2))
    return fk_tuples


def retool_csv_to_buml(csv_dir: str, module_name: str = None, rsx_dir: str = None) -> DomainModel:
    """Parse Retool CSV files from a directory and return a B-UML DomainModel.

    Args:
        csv_dir:     Directory containing .csv files exported from Retool DB.
        module_name: Optional name for the resulting DomainModel.
        rsx_dir:     Optional path to a Retool RSX export (zip or directory)
            whose lib/*.sql queries are mined for JOIN-based FK evidence.

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
    # raw_stem_lower → {headers, rows, path, norm_stem, class_name}
    table_info: dict = {}
    for fname in csv_files:
        raw_stem = os.path.splitext(fname)[0]
        norm_stem = _normalize_stem(raw_stem)
        class_name = _to_pascal(norm_stem)
        path = os.path.join(csv_dir, fname)
        with open(path, 'r', encoding='utf-8-sig', newline='') as fh:
            reader = csv.reader(fh)
            headers = [h.strip() for h in next(reader, [])]
            if not headers:
                print(f"  Skipping empty CSV: {fname}")
                continue
            if any(not h for h in headers) or len({h.lower() for h in headers}) != len(headers):
                raise ValueError(f"CSV {fname!r} has empty or duplicate column names")
            rows = []
            for i, row in enumerate(reader):
                if i >= _SAMPLE_ROWS:
                    break
                rows.append(row)
        table_info[raw_stem.lower()] = {
            'headers':    headers,
            'rows':       rows,
            'path':       path,
            'norm_stem':  norm_stem,
            'class_name': class_name,
        }

    if not table_info:
        return None

    # Build norm_stem → raw_stem mapping for FK resolution
    norm_to_raw: dict = {info['norm_stem']: raw for raw, info in table_info.items()}
    if len(norm_to_raw) != len(table_info):
        raise ValueError('CSV filenames normalize to duplicate entity names')
    sql_fks = {(f, c): t for f, c, t in _mine_sql_joins(rsx_dir, norm_to_raw)} if rsx_dir else {}

    name = module_name or 'RetoolApp'
    domain_model = DomainModel(name=name)
    classes: dict = {}      # raw_stem_lower → Class
    pending_fks: list = []  # (from_raw, fk_col_lower, to_raw)

    # ── Second pass: build Class objects ──────────────────────────────────
    for raw_stem, info in table_info.items():
        headers    = info['headers']
        rows       = info['rows']
        class_name = info['class_name']

        # Detect FK columns (ending in _id whose prefix maps to another table,
        # tolerating simple singular/plural variation).
        fk_cols: dict = {}  # col_lower → to_raw_stem
        pk_col = next((c.lower() for c in headers if c.lower() == 'id'), None)
        if pk_col is None:
            pk_col = next((c.lower() for c in headers if c.lower().endswith('_id')
                           and _stems_match(c.lower()[:-3], info['norm_stem'])), None)
        for col in headers:
            col_lower = col.lower()
            if col_lower == pk_col:
                continue
            if (raw_stem, col_lower) in sql_fks:
                target = sql_fks[(raw_stem, col_lower)]
                fk_cols[col_lower] = target
                pending_fks.append((raw_stem, col_lower, target))
                continue
            if not col_lower.endswith('_id'):
                continue
            fk_prefix = col_lower[:-3]  # strip trailing _id

            # Priority 1: match on normalised stem (singular/plural tolerant)
            matched_raw = None
            for norm_stem, to_raw in norm_to_raw.items():
                if _stems_match(fk_prefix, norm_stem):
                    matched_raw = to_raw
                    break

            # Priority 2: raw stem starts with fk_prefix (+ optional '_'),
            # also singular/plural tolerant.
            if matched_raw is None:
                for candidate_raw in table_info:
                    stripped = candidate_raw[:-1] if candidate_raw.endswith('s') else candidate_raw
                    if (candidate_raw == fk_prefix
                            or candidate_raw.startswith(fk_prefix + '_')
                            or _stems_match(fk_prefix, stripped)):
                        matched_raw = candidate_raw
                        break

            if matched_raw is not None and matched_raw != raw_stem:
                fk_cols[col_lower] = matched_raw
                pending_fks.append((raw_stem, col_lower, matched_raw))

        # Build domain attributes: real primary key for id, inferred type
        # (from sampled values, falling back to name heuristic) for the rest.
        properties: set = set()
        for col_idx, col in enumerate(headers):
            col_lower = col.lower()
            if col_lower in fk_cols:
                continue
            values = [row[col_idx] for row in rows if col_idx < len(row)]
            buml_type = _infer_type_from_values(values, col_lower)
            properties.add(Property(
                name=col_lower,
                type=buml_type,
                multiplicity=Multiplicity(1, 1) if col_lower == pk_col else Multiplicity(0, 1),
                is_id=col_lower == pk_col,
            ))

        cls = Class(name=class_name, attributes=properties)
        classes[raw_stem] = cls
        domain_model.types.add(cls)
        print(f"  Class '{class_name}': {sorted(p.name for p in properties)}")

    # ── Fourth pass: build BinaryAssociation objects from FK edges ──────────
    print(f"  Building {len(pending_fks)} association(s) from FK columns...")
    seen_assocs = set()
    used_assoc_names = set()
    for from_raw, fk_col, to_raw in pending_fks:
        if from_raw not in classes or to_raw not in classes:
            print(f"  Skipping FK '{from_raw}.{fk_col}' -> unknown table '{to_raw}'")
            continue
        if (from_raw, fk_col, to_raw) in seen_assocs:
            continue
        seen_assocs.add((from_raw, fk_col, to_raw))
        from_cls = classes[from_raw]
        to_cls   = classes[to_raw]
        inverse_name = from_cls.name.lower()
        existing_roles = {e.name for e in to_cls.all_association_ends()}
        if inverse_name in existing_roles:
            inverse_name += f'_{fk_col}'
        end_many = Property(
            name=inverse_name,
            type=from_cls,
            multiplicity=Multiplicity(0, '*'),
        )
        end_one = Property(
            name=to_cls.name.lower(),
            type=to_cls,
            multiplicity=Multiplicity(0, 1),
        )
        assoc_name = f"{from_cls.name}_{to_cls.name}"
        if assoc_name in used_assoc_names:
            assoc_name += f"_{fk_col}"
        used_assoc_names.add(assoc_name)
        end_one.name = fk_col[:-3] if fk_col.endswith('_id') else fk_col
        assoc = BinaryAssociation(
            name=assoc_name,
            ends={end_many, end_one},
        )
        domain_model.associations.add(assoc)
        print(f"  Association: {from_cls.name} -> {to_cls.name}  (FK: {fk_col})")

    print(
        f"  Total: {len(classes)} class(es), "
        f"{len(domain_model.associations)} association(s)"
    )
    return domain_model
