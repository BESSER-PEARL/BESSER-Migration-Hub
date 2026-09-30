"""Small SQL identifier reader shared by the Retool parsers.

Only direct FROM/JOIN references are supported; this is not a SQL evaluator.
"""
import re

IDENTIFIER = r'(?:"[^"\n]+"|`[^`\n]+`|\[[^\]\n]+\]|[A-Za-z_][\w$]*)'
TABLE = rf'{IDENTIFIER}(?:\s*\.\s*{IDENTIFIER})*'
_RESERVED = {'on', 'where', 'join', 'inner', 'left', 'right', 'full', 'cross',
             'outer', 'order', 'group', 'limit', 'offset', 'union', 'having', 'set'}


def clean_identifier(value):
    return value.strip().strip('"`[]').lower()


def sql_tables(sql):
    """Return (primary table, alias map, SQL without comments)."""
    sql = re.sub(r"'(?:(?:'')|[^'])*'", "''", sql)
    sql = re.sub(r'--[^\n]*|/\*.*?\*/', '', sql, flags=re.DOTALL)
    aliases = {}
    primary = None
    reserved = '|'.join(sorted(_RESERVED))
    for match in re.finditer(
        rf'\b(FROM|JOIN)\s+({TABLE})(?:\s+(?:AS\s+)?(?!\b(?:{reserved})\b)({IDENTIFIER}))?',
        sql, re.IGNORECASE,
    ):
        table = clean_identifier(re.split(r'\s*\.\s*', match[2])[-1])
        aliases[table] = table
        if primary is None and match[1].lower() == 'from':
            primary = table
        if match[3] and clean_identifier(match[3]) not in _RESERVED:
            aliases[clean_identifier(match[3])] = table
    return primary, aliases, sql
