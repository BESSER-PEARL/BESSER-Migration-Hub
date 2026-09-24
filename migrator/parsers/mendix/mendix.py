import json
import os
import re
from besser.BUML.metamodel.structural import *

def _safe_name(name: str | None) -> str | None:
    """Sanitize a name to be a valid B-UML/Python identifier.

    Replaces any character that is not a letter, digit or underscore
    (e.g. spaces, punctuation) with '_', and prefixes with '_' if the
    result starts with a digit.
    """
    if not name:
        return name
    safe = re.sub(r"\W", "_", name)
    if safe[0].isdigit():
        safe = "_" + safe
    return safe


def primitive_data_types() -> set[PrimitiveDataType]:
    return {PrimitiveDataType("int"), PrimitiveDataType("str"), PrimitiveDataType("datetime")}

def _get_enum_literal_name(literal: dict) -> str:
    """Extracts the display name for a Mendix enumeration literal.

    Mendix prefixes some enum values with '_' to avoid reserved-word
    conflicts (e.g. '_New').  We prefer the human-readable caption
    (English translation) when available; otherwise we strip any
    leading underscore from the internal name.
    """
    caption = literal.get("caption")
    if caption:
        for t in caption.get("translations", []):
            if t.get("languageCode") == "en_US" and t.get("text"):
                return t["text"]
    name = literal.get("name", "")
    return name.lstrip("_") if name.startswith("_") else name

def build_enums(enums: list[dict[str, Any]]) -> set[Enumeration]:
    """Builds enumerations from Mendix JSON data."""
    enumerations = set()
    for enum in enums:
        literals = {EnumerationLiteral(name=_safe_name(_get_enum_literal_name(literal))) for literal in enum.get("values", [])}
        enumerations.add(Enumeration(name=_safe_name(enum.get("name")), literals=literals))
    return enumerations

def mendix_to_buml_datatype(mendix_datetype: str) -> PrimitiveDataType:
    """Converts Mendix data type to B-UML data type.

    ``Property.type`` must be a real BUML type object (the code builder reads
    ``attr.type.name``), so any unmapped/unknown Mendix attribute type falls
    back to ``StringType`` instead of "" (an empty string previously crashed
    code generation with ``AttributeError: 'str' object has no attribute 'name'``).
    """
    type_mapping = {
        "DomainModels$StringAttributeType": StringType,
        "DomainModels$IntegerAttributeType": IntegerType,
        "DomainModels$LongAttributeType": IntegerType,
        "DomainModels$AutoNumberAttributeType": IntegerType,
        "DomainModels$DateTimeAttributeType": DateType,
        "DomainModels$BooleanAttributeType": BooleanType,
        "DomainModels$DecimalAttributeType": FloatType,
        "DomainModels$HashedStringAttributeType": StringType,
        "DomainModels$BinaryAttributeType": StringType,
    }
    return type_mapping.get(mendix_datetype, StringType)

def build_classes(entities: list, buml_model: DomainModel) -> set[Class]:
    """Builds classes with attributes from Mendix JSON data."""
    classes = set()
    for entity in entities:
        attributes = set()
        for attr in entity.get("attributes", []):
            attr_type = attr["type"].get("$Type", "")
            if attr_type == "DomainModels$EnumerationAttributeType":
                enum_name = attr["type"]["enumeration"].split('.')[1]
                enum_type = buml_model.get_type_by_name(enum_name)
                if enum_type is None:
                    # Enum not part of the migrated module (e.g. defined in a
                    # different Mendix module) -- fall back to StringType so
                    # code generation still gets a real type object instead
                    # of None ('NoneType' object has no attribute 'name').
                    print(f"Warning: Enumeration '{enum_name}' referenced by attribute "
                          f"'{attr.get('name')}' is not part of the migrated module; "
                          f"falling back to StringType.")
                    enum_type = StringType
                new_attr = Property(name=_safe_name(attr.get("name")), type=enum_type)
            else:
                prim_data_type = mendix_to_buml_datatype(attr_type)
                new_attr = Property(name=_safe_name(attr.get("name")), type=prim_data_type)
            attributes.add(new_attr)
        classes.add(Class(name=_safe_name(entity.get("name")), attributes=attributes))
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
            safe_class = _safe_name(class_name)
            if entity.get("$ID") == association.get("parent"):
                comp_1 = association.get("deleteBehavior", {}).get("parentDeleteBehavior") == "DeleteMeAndReferences"
                parent_property = Property(name=safe_class.lower(), type=buml_model.get_class_by_name(safe_class), multiplicity=mul1, is_composite=comp_1)
            elif entity.get("$ID") == association.get("child"):
                comp_2 = association.get("deleteBehavior", {}).get("childDeleteBehavior") == "DeleteMeAndReferences"
                child_property = Property(name=safe_class.lower(), type=buml_model.get_class_by_name(safe_class), multiplicity=mul2, is_composite=comp_2)

        # Check if both ends are defined before creating the association
        if parent_property and child_property:
            new_association = BinaryAssociation(name=_safe_name(association.get("name")), ends={parent_property, child_property})
            result_associations.add(new_association)
        else:
            print(f"Warning: Association '{association.get('name')}' is missing a valid end.")

    return result_associations

def _index_entities_and_enums(data: dict) -> tuple[dict[str, dict], dict[str, dict], dict[str, dict]]:
    """Index every entity/enum across *all* Mendix modules in this export.

    A Mendix export contains one ``DomainModels$DomainModel`` unit per module,
    so an entity referenced from another module (e.g. a generalization's
    parent, or an association's other endpoint) is normally invisible to a
    single-module parse. Building this index once lets the caller resolve
    those cross-module references regardless of which module they live in.

    Returns ``(entities_by_id, entities_by_qualified_name, enums_by_qualified_name)``.
    """
    entities_by_id: dict[str, dict] = {}
    entities_by_qname: dict[str, dict] = {}
    enums_by_qname: dict[str, dict] = {}
    for unit in data.get("units", []):
        if unit.get("$Type") == "DomainModels$DomainModel":
            for entity in unit.get("entities", []) or []:
                eid = entity.get("$ID")
                qname = entity.get("$QualifiedName", "")
                if eid:
                    entities_by_id[eid] = entity
                if qname:
                    entities_by_qname[qname] = entity
        elif unit.get("$Type") == "Enumerations$Enumeration":
            qname = unit.get("$QualifiedName", "")
            if qname:
                enums_by_qname[qname] = unit
    return entities_by_id, entities_by_qname, enums_by_qname


def _collect_gui_referenced_entity_qnames(data: dict, module_name: str) -> set[str]:
    """Scan this module's own pages for entity references in GUI bindings.

    A DataView/ListView/ReferenceSelector/Gallery can be bound to an entity
    from another module with no corresponding domain-model association at
    all (e.g. a ListView showing ``Administration.UserRole`` records) --
    those references only appear inside ``Pages$Page`` units, as
    ``DomainModels$DirectEntityRef.entity`` or the entity portion of a
    ``DomainModels$AttributeRef.attribute`` path. Collecting them here lets
    those classes be pulled into the same B-UML model too, instead of only
    ever considering domain-model-level references.
    """
    referenced: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            node_type = node.get("$Type")
            if node_type == "DomainModels$DirectEntityRef":
                entity_qname = node.get("entity", "")
                if entity_qname:
                    referenced.add(entity_qname)
            elif node_type == "DomainModels$AttributeRef":
                attribute = node.get("attribute", "")
                parts = attribute.split(".")
                if len(parts) >= 2:
                    referenced.add(".".join(parts[:2]))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for unit in data.get("units", []):
        if unit.get("$Type") == "Pages$Page" and unit.get("$QualifiedName", "").split(".")[0] == module_name:
            walk(unit)

    return referenced


def _collect_referenced_entities(
    primary_entities: list[dict],
    associations: list[dict],
    entities_by_id: dict[str, dict],
    entities_by_qname: dict[str, dict],
    extra_referenced_qnames: set[str] | None = None,
    max_hops: int = 10,
) -> list[dict]:
    """Expand a module's own entities with every other-module entity it
    directly depends on, so those classes exist in the same B-UML domain
    model instead of leaving generalizations/associations/GUI bindings
    unresolved.

    Three kinds of cross-module references are pulled in:
      1. Association endpoints: if this module's own associations reference
         an entity not in ``primary_entities``, that entity's module is
         imported for that single entity (one hop -- we don't also import
         everything *that* entity associates with, to avoid pulling in an
         unbounded chain of unrelated system entities).
      2. ``extra_referenced_qnames``: entities referenced only from the GUI
         layer (see ``_collect_gui_referenced_entity_qnames``), same one-hop
         treatment as association endpoints.
      3. Generalization parents: followed transitively (bounded by
         ``max_hops``) from the primary entities and anything pulled in via
         (1)/(2), since a class's ancestor chain must fully exist for the
         generalization to be buildable.
    """
    included: dict[str, dict] = {e.get("$ID"): e for e in primary_entities if e.get("$ID")}
    worklist = list(primary_entities)

    for association in associations or []:
        for key in ("parent", "child"):
            entity_id = association.get(key)
            if entity_id and entity_id not in included:
                external_entity = entities_by_id.get(entity_id)
                if external_entity is not None:
                    included[entity_id] = external_entity
                    worklist.append(external_entity)

    for qname in extra_referenced_qnames or ():
        external_entity = entities_by_qname.get(qname)
        if external_entity is None:
            continue
        entity_id = external_entity.get("$ID")
        if entity_id and entity_id not in included:
            included[entity_id] = external_entity
            worklist.append(external_entity)

    hops = 0
    while worklist and hops < max_hops:
        hops += 1
        next_worklist = []
        for entity in worklist:
            gen_qname = entity.get("generalization", {}).get("generalization")
            if not gen_qname:
                continue
            parent_entity = entities_by_qname.get(gen_qname)
            if parent_entity is None:
                continue
            parent_id = parent_entity.get("$ID")
            if parent_id and parent_id not in included:
                included[parent_id] = parent_entity
                next_worklist.append(parent_entity)
        worklist = next_worklist

    return list(included.values())


def _collect_referenced_enums(
    entities: list[dict],
    enums_by_qname: dict[str, dict],
    primary_enums: list[dict],
) -> list[dict]:
    """Expand a module's own enums with every other-module enum referenced by
    an ``EnumerationAttributeType`` attribute on any of ``entities`` (including
    entities pulled in cross-module by ``_collect_referenced_entities``)."""
    included: dict[str, dict] = {e.get("$QualifiedName", ""): e for e in primary_enums}
    for entity in entities:
        for attr in entity.get("attributes", []) or []:
            if attr.get("type", {}).get("$Type") != "DomainModels$EnumerationAttributeType":
                continue
            enum_qname = attr["type"].get("enumeration", "")
            if enum_qname and enum_qname not in included:
                enum_unit = enums_by_qname.get(enum_qname)
                if enum_unit is not None:
                    included[enum_qname] = enum_unit
    return list(included.values())


def build_generalizations(entities: list[dict], buml_model: DomainModel) -> set[Generalization]:
    """Builds generalizations from Mendix JSON data."""
    result_generalizations = set()

    for entity in entities:
        qualified_general = entity.get("generalization").get("generalization")
        if qualified_general:
            general_name = _safe_name(qualified_general.split(".")[1])
            general = buml_model.get_class_by_name(general_name)
            specific = buml_model.get_class_by_name(_safe_name(entity.get("name")))
            if general is None:
                print(f"Warning: Skipping generalization '{qualified_general}' -> "
                      f"parent class '{general_name}' is not part of the migrated module "
                      f"(likely a built-in Mendix module such as 'System').")
                continue
            new_generalization: Generalization = Generalization(general, specific)
            result_generalizations.add(new_generalization)
    return result_generalizations

def mendix_to_buml(json_path: str, module_name: str, encoding: str = "utf-16") -> DomainModel:
    """Converts a Mendix JSON model to a B-UML domain model."""
    if not os.path.exists(json_path) or os.path.getsize(json_path) == 0:
        print("The JSON file is empty or does not exist.")
        return None

    tried_encodings = ["utf-8", "utf-16", "utf-16-le", "utf-16-be"]

    data = None
    for enc in tried_encodings:
        try:
            with open(json_path, "r", encoding=enc) as json_file:
                data = json.load(json_file)
            print(f"✅ Successfully loaded JSON using encoding: {enc}")
            break
        except UnicodeDecodeError as e:
            print(f"⚠️ UnicodeDecodeError for {enc}: {e}")
        except json.JSONDecodeError as e:
            print(f"❌ JSONDecodeError with {enc}: {e}")
            return None
        except Exception as e:  # broad-exception-caught
            print(f"❌ Unknown error with {enc}: {e}")
            return None

    if data is None:
        print("❌ Failed to decode the JSON file with all tried encodings.")
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

    # A Mendix export splits entities/enums across one DomainModel unit per
    # module, so a generalization's parent or an association's other endpoint
    # that lives in a different module (e.g. Attachment -> System.FileDocument)
    # would otherwise be missing from the B-UML model entirely. Pull in the
    # specific other-module entities/enums this module actually references,
    # instead of only ever seeing the current module in isolation.
    entities_by_id, entities_by_qname, enums_by_qname = _index_entities_and_enums(data)
    gui_entity_qnames = _collect_gui_referenced_entity_qnames(data, module_name)
    all_entities = _collect_referenced_entities(
        primary_entities=mx_model.get("entities"),
        associations=mx_model.get("associations"),
        entities_by_id=entities_by_id,
        entities_by_qname=entities_by_qname,
        extra_referenced_qnames=gui_entity_qnames,
    )
    all_enums = _collect_referenced_enums(all_entities, enums_by_qname, enums)

    b_uml_model = DomainModel(name=module_name)
    #b_uml_model.types = primitive_data_types()
    b_uml_model.types.update(build_enums(all_enums))
    b_uml_model.types.update(build_classes(all_entities,
                            buml_model=b_uml_model))
    b_uml_model.associations = build_associations(mx_model.get("associations"),
                            all_entities, buml_model=b_uml_model)
    b_uml_model.generalizations = build_generalizations(all_entities,
                            buml_model=b_uml_model)

    return b_uml_model
