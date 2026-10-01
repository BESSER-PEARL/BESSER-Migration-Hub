"""Verify that ServiceNow coverage follows exported declarations."""
from pathlib import Path
import sys

import pytest
from migrator.evaluation.service_now import service_now_output, typescript_inventory
from migrator.generators.service_now.service_now_generator import ServiceNowGenerator
from besser.BUML.metamodel.structural import BinaryAssociation, Class, DomainModel, Multiplicity, Property, StringType


@pytest.mark.parametrize('remove_inverse', [False, True])
def test_reference_and_inverse_are_audited_from_actual_export(tmp_path, monkeypatch, remove_inverse):
    parent = Class(name='Parent', attributes={Property(name='name', type=StringType)})
    child = Class(name='Child', attributes={Property(name='title', type=StringType)})
    association = BinaryAssociation(name='Family', ends={
        Property(name='parent', type=parent, multiplicity=Multiplicity(0, 1)),
        Property(name='children', type=child, multiplicity=Multiplicity(0, '*'))})
    domain = DomainModel(name='App', types={parent, child}, associations={association})
    original = ServiceNowGenerator.generate
    def generate(instance):
        original(instance)
        if remove_inverse:
            path = Path(instance.output_dir) / 'tables.now.ts'
            path.write_text(path.read_text(encoding='utf-8').replace(
                "related_list: 'u_child.parent'", "related_list: 'u_child.missing'"), encoding='utf-8')
    monkeypatch.setattr(ServiceNowGenerator, 'generate', generate)
    counts, audit = service_now_output(domain, None, tmp_path, 'example')
    assert counts['Entities'] == 2
    assert counts['Attributes'] == 2  # The generated reference is counted separately.
    assert counts['Associations'] == 1
    assert counts['Multiplicities'] == (1 if remove_inverse else 2)
    assert audit['data']['relationships'][0]['reference_present']


def test_inventory_ignores_comments_and_handles_nested_literals():
    result = typescript_inventory("""
// Table({ name: 'fake', schema: {} });
export const items = Table({name: 'u_items', schema: {
  title: StringColumn({ label: 'Text, with {braces}' }),
  parent: ReferenceColumn({ referenceTable: 'u_parent', label: 'Parent' }),
}});
""")
    assert set(result['tables']) == {'u_items'}
    assert result['tables']['u_items']['parent']['reference_table'] == 'u_parent'


def test_inventory_rejects_duplicate_schema_columns():
    with pytest.raises(ValueError, match='Duplicate generated property: title'):
        typescript_inventory("Table({name:'u_items', schema:{title:StringColumn({}), title:IntegerColumn({})}})")
