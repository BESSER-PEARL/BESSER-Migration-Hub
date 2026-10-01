"""Audit generated ServiceNow TypeScript declarations, without executing them."""
import ast
from collections import Counter
from pathlib import Path
import re

from migrator.generators.service_now.service_now_generator import ServiceNowGenerator


TOKEN = re.compile(r"//[^\n]*|/\*[\s\S]*?\*/|'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"|[A-Za-z_$][\w$]*|\d+|[^\s]")


def split_properties(stream):
    """Read top-level object properties, respecting nested constructors and strings."""
    if not stream or stream[0] != '{':
        raise ValueError('Expected a TypeScript object')
    properties, start, depth = [], 1, 0
    for index, token in enumerate(stream[1:], start=1):
        if token in {'(', '{', '['}:
            depth += 1
        elif token in {')', '}', ']'}:
            if token == '}' and depth == 0:
                properties.append(stream[start:index])
                break
            depth -= 1
        elif token == ',' and depth == 0:
            properties.append(stream[start:index])
            start = index + 1
    result = {}
    for property_tokens in properties:
        if not property_tokens:
            continue
        if len(property_tokens) < 3 or property_tokens[1] != ':':
            raise ValueError(f'Unsupported property: {property_tokens}')
        key = property_tokens[0]
        if key[:1] in {"'", '"'}:
            key = ast.literal_eval(key)
        if key in result:
            raise ValueError(f'Duplicate generated property: {key}')
        result[key] = property_tokens[2:]
    return result


def literal(tokens):
    return ast.literal_eval(tokens[0]) if tokens else None


def typescript_inventory(text):
    stream = [token for token in TOKEN.findall(text) if not token.startswith(('//', '/*'))]
    tables, related_lists = {}, set()
    for index, token in enumerate(stream[:-2]):
        if token not in {'Table', 'Record'} or stream[index + 1:index + 3] != ['(', '{']:
            continue
        properties = split_properties(stream[index + 2:])
        if token == 'Table':
            name = literal(properties['name'])
            if name in tables:
                raise ValueError(f'Duplicate generated table: {name}')
            columns = {}
            for column, expression in split_properties(properties['schema']).items():
                constructor = expression[0]
                options = split_properties(expression[2:])
                columns[column] = {'kind': constructor}
                if constructor == 'ReferenceColumn':
                    columns[column]['reference_table'] = literal(options['referenceTable'])
            tables[name] = columns
        elif literal(properties.get('table')) == 'sys_ui_related_list_entry':
            data = split_properties(properties['data'])
            related_lists.add(literal(data['related_list']))
    # Duplicate const identifiers can make an otherwise countable export invalid.
    declarations = re.findall(r'\b(?:export\s+)?const\s+([\w$]+)\s*=', text)
    duplicates = sorted(name for name, count in Counter(declarations).items() if count > 1)
    return {'tables': tables, 'related_lists': sorted(related_lists), 'duplicate_declarations': duplicates}


def service_now_output(domain, gui, folder, scenario):
    output = folder / 'buml_generator_result'
    generator = ServiceNowGenerator(domain, output_dir=str(output))
    generator.generate()
    path = output / 'tables.now.ts'
    audit = typescript_inventory(path.read_text(encoding='utf-8'))
    tables = audit['tables']
    attributes = []
    for cls in domain.get_classes():
        table = generator.get_table_name(cls.name)
        for attribute in cls.attributes:
            column = tables.get(table, {}).get(attribute.name)
            if column and column['kind'] != 'ReferenceColumn':
                attributes.append({'table': table, 'column': attribute.name, 'kind': column['kind']})
    relationships, associations, ends = [], 0, 0
    for association in domain.associations:
        represented = []
        for end in association.ends:
            if end.multiplicity.max != 1:
                continue
            other = next(other for other in association.ends if other is not end)
            child, parent = generator.get_table_name(other.type.name), generator.get_table_name(end.type.name)
            column = tables.get(child, {}).get(end.name, {})
            reference = column.get('kind') == 'ReferenceColumn' and column.get('reference_table') == parent
            related = f'{child}.{end.name}' in audit['related_lists']
            if reference:
                represented.append(end.name)
                ends += 1
                if other.multiplicity.max > 1 and related:
                    ends += 1
            relationships.append({'association': association.name, 'child': child, 'column': end.name,
                                  'parent': parent, 'reference_present': reference,
                                  'related_list_present': related})
        associations += bool(represented)
    counts = {'Entities': len(tables), 'Attributes': len(attributes), 'Associations': associations,
              'Multiplicities': ends, 'Generalizations': 0, 'Enumerations': 0}
    audit.update(counts=counts, matched_attributes=attributes, relationships=relationships,
                 generated_file=str(path),
                 counting_rule='Input scalar columns; association ends represented by reference columns and related lists. '
                               'This does not verify cardinality bounds or live platform execution.')
    return counts, {'data': audit}
