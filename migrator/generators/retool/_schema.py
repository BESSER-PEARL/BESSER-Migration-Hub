"""Shared relational schema for Retool CSV, SQL and GUI output."""
from dataclasses import dataclass, field
import re

from besser.BUML.metamodel.structural import Enumeration, IntegerType
from besser.generators.structural_utils import get_foreign_keys


def snake_name(name):
    value = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', name)
    value = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', value)
    value = re.sub(r'[^a-zA-Z0-9_]', '_', value).strip('_').lower()
    if not value:
        raise ValueError(f'Cannot generate an identifier for {name!r}')
    return '_' + value if value[0].isdigit() else value


def sql_identifier(name):
    return '"' + name.replace('"', '""') + '"'


def values(collection):
    return list(collection.values()) if isinstance(collection, dict) else list(collection or [])


@dataclass
class Column:
    name: str
    type: object
    source_name: str = None
    primary_key: bool = False
    nullable: bool = True
    reference: tuple = None
    synthetic: bool = False
    unique: bool = False

    @property
    def format(self):
        return {'int': 'decimal', 'float': 'decimal', 'bool': 'boolean',
                'date': 'date', 'datetime': 'datetime'}.get(self.type.name, 'string')

    def sample(self):
        if isinstance(self.type, Enumeration):
            literals = sorted(self.type.literals, key=lambda literal: literal.name)
            return literals[0].name if literals else ''
        if self.reference:
            return Column('id', self.type, primary_key=True).sample()
        return {'int': 1 if self.primary_key else 0, 'float': '0.0', 'bool': 'false',
                'date': '2024-01-01', 'datetime': '2024-01-01T00:00:00',
                'time': '00:00:00'}.get(self.type.name, 'sample_id' if self.primary_key else f'sample_{self.name}')


@dataclass
class Table:
    name: str
    entity: object = None
    columns: list = field(default_factory=list)
    junction: bool = False

    @property
    def key(self):
        return next(c for c in self.columns if c.primary_key)

    def add(self, column):
        if any(c.name == column.name for c in self.columns):
            raise ValueError(f'Duplicate generated column {self.name}.{column.name}')
        self.columns.append(column)


def _attributes(cls, visited=None):
    visited = set(visited or ())
    if cls in visited:
        raise ValueError(f'Cyclic inheritance at {cls.name}')
    visited.add(cls)
    result = {}
    for generalization in sorted(cls.generalizations, key=lambda g: g.general.name):
        if generalization.specific is cls:
            result.update(_attributes(generalization.general, visited))
    result.update({attr.name: attr for attr in cls.attributes})
    return result


def collect_tables(model):
    if model is None:
        return []
    tables, by_class = [], {}
    names = set()
    for cls in sorted(model.get_classes(), key=lambda c: c.name):
        name = snake_name(cls.name)
        if name in names:
            raise ValueError(f'Duplicate generated table name {name!r}')
        names.add(name)
        table = Table(name=name, entity=cls)
        attrs = sorted(_attributes(cls).values(), key=lambda a: (not a.is_id, a.name))
        keys = [a for a in attrs if a.is_id]
        if len(keys) > 1:
            raise ValueError(f'Composite primary keys are not supported for {cls.name}')
        if not keys:
            keys = [a for a in attrs if snake_name(a.name) == 'id']
        if not keys:
            table.add(Column('id', IntegerType, primary_key=True, nullable=False, synthetic=True))
        for attr in attrs:
            if attr.multiplicity.max > 1:
                raise ValueError(f'Multivalued attribute {cls.name}.{attr.name} cannot be stored in a CSV column')
            table.add(Column(snake_name(attr.name), attr.type, source_name=attr.name,
                             primary_key=attr in keys, nullable=attr.multiplicity.min == 0 and attr not in keys))
        # Put the existing key first without adding a second id.
        table.columns.sort(key=lambda c: (not c.primary_key, c.name))
        tables.append(table)
        by_class[cls.name] = table

    foreign_keys = get_foreign_keys(model)
    for assoc in sorted(model.associations, key=lambda a: a.name):
        ends = sorted(assoc.ends, key=lambda e: (e.type.name, e.name))
        if len(ends) != 2:
            raise ValueError(f'Only binary associations are supported: {assoc.name}')
        if all(end.multiplicity.max > 1 for end in ends):
            name = snake_name(assoc.name)
            if name in names:
                raise ValueError(f'Junction table name {name!r} conflicts with another table')
            names.add(name)
            junction = Table(name=name, junction=True)
            junction.add(Column('id', IntegerType, primary_key=True, nullable=False, synthetic=True))
            for end in ends:
                referenced = by_class[end.type.name]
                role = snake_name(end.name or end.type.name)
                column_name = role if role.endswith('_id') else role + '_id'
                junction.add(Column(column_name, referenced.key.type, nullable=False,
                                    reference=(referenced.name, referenced.key.name)))
            tables.append(junction)
            continue
        owner_name, role = foreign_keys[assoc.name]
        owner = by_class[owner_name]
        candidates = [end for end in ends if end.name == role]
        reference_end = next((end for end in candidates if end.type.name != owner_name), candidates[0])
        referenced = by_class[reference_end.type.name]
        role_name = snake_name(role)
        column_name = role_name if role_name.endswith('_id') else role_name + '_id'
        existing = next((c for c in owner.columns if c.name == column_name), None)
        if existing is not None:
            if existing.primary_key or existing.reference or existing.type != referenced.key.type:
                raise ValueError(f'Foreign key conflicts with {owner.name}.{column_name}')
            existing.reference = (referenced.name, referenced.key.name)
            existing.unique = all(end.multiplicity.max == 1 for end in ends)
        else:
            owner.add(Column(column_name, referenced.key.type, nullable=reference_end.multiplicity.min == 0,
                             reference=(referenced.name, referenced.key.name),
                             unique=all(end.multiplicity.max == 1 for end in ends)))
    return tables


def entities_info(model):
    return [(t.entity.name if t.entity else t.name, t.name, [(c.name, c.format) for c in t.columns])
            for t in collect_tables(model)]
