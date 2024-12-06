import json
import os
from besser.BUML.metamodel.structural import *

def primitive_data_types() -> set[PrimitiveDataType]:
    return {PrimitiveDataType("int"), PrimitiveDataType("str"), PrimitiveDataType("datetime")}

def build_enums(enums: list[dict[str, Any]]) -> set[Enumeration]:
    """Builds enumerations from Mendix JSON data."""
    enumerations = set()
    for enum in enums:
        literals = {EnumerationLiteral(name=literal.get("name")) for literal in enum.get("values", [])}
        enumerations.add(Enumeration(name=enum.get("name"), literals=literals))
    return enumerations

def mendix_to_buml_datatype(mendix_datetype: str) -> str:
    """Converts Mendix data type to B-UML data type."""
    type_mapping = {
        "DomainModels$StringAttributeType": StringType,
        "DomainModels$IntegerAttributeType": IntegerType,
        "DomainModels$DateTimeAttributeType": DateType
    }
    return type_mapping.get(mendix_datetype, "")

def build_classes(entities: list, buml_model: DomainModel) -> set[Class]:
    """Builds classes with attributes from Mendix JSON data."""
    classes = set()
    for entity in entities:
        attributes = set()
        for attr in entity.get("attributes", []):
            attr_type = attr["type"].get("$Type", "")
            if attr_type == "DomainModels$EnumerationAttributeType":
                enum_name = attr["type"]["enumeration"].split('.')[1]
                new_attr = Property(name=attr.get("name"), type=buml_model.get_type_by_name(enum_name))
            else:
                prim_data_type = mendix_to_buml_datatype(attr_type)
                new_attr = Property(name=attr.get("name"), type=prim_data_type)
            attributes.add(new_attr)
        classes.add(Class(name=entity.get("name"), attributes=attributes))
    return classes

def build_associations(associations: list[dict], entities: list[dict], buml_model: DomainModel) -> set[Association]:
    """Builds associations between classes from Mendix JSON data."""
    result_associations = set()

    for association in associations:
        parent_property = None
        child_property = None
        # cardinality
        mul1 = Multiplicity(0, "*")
        mul2 = Multiplicity(1, 1)

        if association.get("type") == "ReferenceSet":
            mul2 = Multiplicity(0, "*")
        elif association.get("type") == "Reference" and association.get("owner") == "Both":
            mul1 = Multiplicity(1, 1)

        for entity in entities:
            class_name = entity.get("name")
            if entity.get("$ID") == association.get("parent"):
                comp_1 = association.get("deleteBehavior", {}).get("parentDeleteBehavior") == "DeleteMeAndReferences"
                parent_property = Property(name=class_name.lower(), type=buml_model.get_class_by_name(class_name), multiplicity=mul1, is_composite=comp_1)
            elif entity.get("$ID") == association.get("child"):
                comp_2 = association.get("deleteBehavior", {}).get("childDeleteBehavior") == "DeleteMeAndReferences"
                child_property = Property(name=class_name.lower(), type=buml_model.get_class_by_name(class_name), multiplicity=mul2, is_composite=comp_2)

        # Check if both ends are defined before creating the association
        if parent_property and child_property:
            new_association = BinaryAssociation(name=association.get("name"), ends={parent_property, child_property})
            result_associations.add(new_association)
        else:
            print(f"Warning: Association '{association.get('name')}' is missing a valid end.")

    return result_associations

def build_generalizations(entities: list[dict], buml_model: DomainModel) -> set[Generalization]:
    """Builds generalizations from Mendix JSON data."""
    result_generalizations = set()

    for entity in entities:
        if entity.get("generalization").get("generalization"):
            general = buml_model.get_class_by_name(entity.get("generalization").get("generalization").split(".")[1])
            specific = buml_model.get_class_by_name(entity.get("name"))
            new_generalization: Generalization = Generalization(general, specific)
            print(entity.get("generalization").get("generalization"))
            result_generalizations.add(new_generalization)
    return result_generalizations

def mendix_to_buml(json_path: str, module_name: str, encoding: str = "utf-16") -> DomainModel:
    """Converts a Mendix JSON model to a B-UML domain model."""
    if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
        print("The JSON file is empty or does not exist.")
        return None

    try:
        with open(json_path, "r", encoding=encoding) as json_file:
            data = json.load(json_file)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Error reading JSON file: {e}")
        return None

    mx_model, enums = {}, []
    for unit in data.get("units", []):
        if unit.get("$Type") == "DomainModels$DomainModel" and unit.get("entities"):
            if unit["entities"][0].get("$QualifiedName", "").split('.')[0] == module_name:
                mx_model = unit
        if unit.get("$Type") == "Enumerations$Enumeration" and unit.get("$QualifiedName", "").split('.')[0] == module_name:
            enums.append(unit)

    if not mx_model:
        print(f'The module "{module_name}" does not exist.')
        return None

    b_uml_model = DomainModel(name=module_name)
    #b_uml_model.types = primitive_data_types()
    b_uml_model.types.update(build_enums(enums))
    b_uml_model.types.update(build_classes(mx_model.get("entities"),
                            buml_model=b_uml_model))
    b_uml_model.associations = build_associations(mx_model.get("associations"),
                            mx_model.get("entities"), buml_model=b_uml_model)
    b_uml_model.generalizations = build_generalizations(mx_model.get("entities"),
                            buml_model=b_uml_model)

    return b_uml_model
