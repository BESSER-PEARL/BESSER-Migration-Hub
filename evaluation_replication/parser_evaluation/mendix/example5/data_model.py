####################
# STRUCTURAL MODEL #
####################

####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata, MethodImplementationType
)

# Classes
DemoItemRevision = Class(name="DemoItemRevision")
DemoItem = Class(name="DemoItem")
DemoItemCreateInput = Class(name="DemoItemCreateInput")
DemoItemRevisionCompoundCreateInput = Class(name="DemoItemRevisionCompoundCreateInput")
DemoWorkspaceObject = Class(name="DemoWorkspaceObject")
DemoBOMLine = Class(name="DemoBOMLine")
SelectedBOMLineHelper = Class(name="SelectedBOMLineHelper")
StructureHelper = Class(name="StructureHelper")
BomWindowPropFlagMap = Class(name="BomWindowPropFlagMap")
ItemRevision = Class(name="ItemRevision")
ItemRevisionSearchCriteria = Class(name="ItemRevisionSearchCriteria")
GeneralQuery = Class(name="GeneralQuery")
Item = Class(name="Item")
SearchInput = Class(name="SearchInput")
ModelObject = Class(name="ModelObject")
WorkspaceObject = Class(name="WorkspaceObject")
ItemCreateInput = Class(name="ItemCreateInput")
ItemRevisionCompoundCreateInput = Class(name="ItemRevisionCompoundCreateInput")
BOMLine = Class(name="BOMLine")
SearchCriteria_SavedQuery = Class(name="SearchCriteria_SavedQuery")
POM_application_object = Class(name="POM_application_object")
CreateInput = Class(name="CreateInput")
CompndCreateInput = Class(name="CompndCreateInput")
BOMLine = Class(name="BOMLine")
SearchCriteriaInput = Class(name="SearchCriteriaInput")
BaseCreateInput = Class(name="BaseCreateInput")

# DemoItemRevision class attributes and methods

# DemoItem class attributes and methods

# DemoItemCreateInput class attributes and methods

# DemoItemRevisionCompoundCreateInput class attributes and methods

# DemoWorkspaceObject class attributes and methods

# DemoBOMLine class attributes and methods

# SelectedBOMLineHelper class attributes and methods

# StructureHelper class attributes and methods
StructureHelper_WithVariantRule: Property = Property(name="WithVariantRule", type=BooleanType)
StructureHelper.attributes={StructureHelper_WithVariantRule}

# BomWindowPropFlagMap class attributes and methods
BomWindowPropFlagMap_show_unconfigured_variants: Property = Property(name="show_unconfigured_variants", type=BooleanType)
BomWindowPropFlagMap_show_unconfigured_changes: Property = Property(name="show_unconfigured_changes", type=BooleanType)
BomWindowPropFlagMap_show_suppressed_occurrences: Property = Property(name="show_suppressed_occurrences", type=BooleanType)
BomWindowPropFlagMap_is_packed_by_default: Property = Property(name="is_packed_by_default", type=BooleanType)
BomWindowPropFlagMap_show_out_of_context_lines: Property = Property(name="show_out_of_context_lines", type=BooleanType)
BomWindowPropFlagMap_fnd0show_uncnf_occ_eff: Property = Property(name="fnd0show_uncnf_occ_eff", type=BooleanType)
BomWindowPropFlagMap_fnd0bw_in_cv_cfg_to_load_md: Property = Property(name="fnd0bw_in_cv_cfg_to_load_md", type=BooleanType)
BomWindowPropFlagMap.attributes={BomWindowPropFlagMap_fnd0bw_in_cv_cfg_to_load_md, BomWindowPropFlagMap_fnd0show_uncnf_occ_eff, BomWindowPropFlagMap_is_packed_by_default, BomWindowPropFlagMap_show_out_of_context_lines, BomWindowPropFlagMap_show_suppressed_occurrences, BomWindowPropFlagMap_show_unconfigured_changes, BomWindowPropFlagMap_show_unconfigured_variants}

# ItemRevision class attributes and methods
ItemRevision_item_id: Property = Property(name="item_id", type=StringType)
ItemRevision_item_revision_id: Property = Property(name="item_revision_id", type=StringType)
ItemRevision.attributes={ItemRevision_item_id, ItemRevision_item_revision_id}

# ItemRevisionSearchCriteria class attributes and methods
ItemRevisionSearchCriteria_Name: Property = Property(name="Name", type=StringType)
ItemRevisionSearchCriteria_ItemID: Property = Property(name="ItemID", type=StringType)
ItemRevisionSearchCriteria__Type: Property = Property(name="_Type", type=StringType)
ItemRevisionSearchCriteria.attributes={ItemRevisionSearchCriteria_ItemID, ItemRevisionSearchCriteria_Name, ItemRevisionSearchCriteria__Type}

# GeneralQuery class attributes and methods
GeneralQuery_Name: Property = Property(name="Name", type=StringType)
GeneralQuery_Description: Property = Property(name="Description", type=StringType)
GeneralQuery__Type: Property = Property(name="_Type", type=StringType)
GeneralQuery_OwningUser: Property = Property(name="OwningUser", type=StringType)
GeneralQuery_OwningGroup: Property = Property(name="OwningGroup", type=StringType)
GeneralQuery_CreatedAfter: Property = Property(name="CreatedAfter", type=DateType)
GeneralQuery_CreatedBefore: Property = Property(name="CreatedBefore", type=DateType)
GeneralQuery_ModifiedAfter: Property = Property(name="ModifiedAfter", type=DateType)
GeneralQuery_ModifiedBefore: Property = Property(name="ModifiedBefore", type=DateType)
GeneralQuery_ReleasedAfter: Property = Property(name="ReleasedAfter", type=DateType)
GeneralQuery_ReleasedBefore: Property = Property(name="ReleasedBefore", type=DateType)
GeneralQuery_WorkflowTemplateName: Property = Property(name="WorkflowTemplateName", type=StringType)
GeneralQuery_CurrentTask: Property = Property(name="CurrentTask", type=StringType)
GeneralQuery.attributes={GeneralQuery_CreatedAfter, GeneralQuery_CreatedBefore, GeneralQuery_CurrentTask, GeneralQuery_Description, GeneralQuery_ModifiedAfter, GeneralQuery_ModifiedBefore, GeneralQuery_Name, GeneralQuery_OwningGroup, GeneralQuery_OwningUser, GeneralQuery_ReleasedAfter, GeneralQuery_ReleasedBefore, GeneralQuery_WorkflowTemplateName, GeneralQuery__Type}

# Item class attributes and methods
Item_item_id: Property = Property(name="item_id", type=StringType)
Item.attributes={Item_item_id}

# SearchInput class attributes and methods
SearchInput_providerName: Property = Property(name="providerName", type=StringType)
SearchInput_startIndex: Property = Property(name="startIndex", type=IntegerType)
SearchInput_maxToLoad: Property = Property(name="maxToLoad", type=IntegerType)
SearchInput_internalPropertyName: Property = Property(name="internalPropertyName", type=StringType)
SearchInput_maxToReturn: Property = Property(name="maxToReturn", type=IntegerType)
SearchInput_searchFilterFieldSortType: Property = Property(name="searchFilterFieldSortType", type=StringType)
SearchInput.attributes={SearchInput_internalPropertyName, SearchInput_maxToLoad, SearchInput_maxToReturn, SearchInput_providerName, SearchInput_searchFilterFieldSortType, SearchInput_startIndex}

# ModelObject class attributes and methods
ModelObject_UID: Property = Property(name="UID", type=StringType)
ModelObject__Type: Property = Property(name="_Type", type=StringType)
ModelObject_ClassName: Property = Property(name="ClassName", type=StringType)
ModelObject.attributes={ModelObject_ClassName, ModelObject_UID, ModelObject__Type}

# WorkspaceObject class attributes and methods
WorkspaceObject_object_name: Property = Property(name="object_name", type=StringType)
WorkspaceObject_object_desc: Property = Property(name="object_desc", type=StringType)
WorkspaceObject_date_released: Property = Property(name="date_released", type=DateType)
WorkspaceObject_checked_out: Property = Property(name="checked_out", type=StringType)
WorkspaceObject_checked_out_date: Property = Property(name="checked_out_date", type=DateType)
WorkspaceObject.attributes={WorkspaceObject_checked_out, WorkspaceObject_checked_out_date, WorkspaceObject_date_released, WorkspaceObject_object_desc, WorkspaceObject_object_name}

# ItemCreateInput class attributes and methods
ItemCreateInput_item_id: Property = Property(name="item_id", type=StringType)
ItemCreateInput.attributes={ItemCreateInput_item_id}

# ItemRevisionCompoundCreateInput class attributes and methods
ItemRevisionCompoundCreateInput_item_revision_id: Property = Property(name="item_revision_id", type=StringType)
ItemRevisionCompoundCreateInput.attributes={ItemRevisionCompoundCreateInput_item_revision_id}

# BOMLine class attributes and methods

# SearchCriteria_SavedQuery class attributes and methods
SearchCriteria_SavedQuery_utcOffset: Property = Property(name="utcOffset", type=StringType)
SearchCriteria_SavedQuery_searchID: Property = Property(name="searchID", type=StringType)
SearchCriteria_SavedQuery_totalObjectsFoundReportedToClient: Property = Property(name="totalObjectsFoundReportedToClient", type=StringType)
SearchCriteria_SavedQuery_lastEndIndex: Property = Property(name="lastEndIndex", type=StringType)
SearchCriteria_SavedQuery_typeOfSearch: Property = Property(name="typeOfSearch", type=StringType)
SearchCriteria_SavedQuery_queryUID: Property = Property(name="queryUID", type=StringType)
SearchCriteria_SavedQuery.attributes={SearchCriteria_SavedQuery_lastEndIndex, SearchCriteria_SavedQuery_queryUID, SearchCriteria_SavedQuery_searchID, SearchCriteria_SavedQuery_totalObjectsFoundReportedToClient, SearchCriteria_SavedQuery_typeOfSearch, SearchCriteria_SavedQuery_utcOffset}

# POM_application_object class attributes and methods
POM_application_object_creation_date: Property = Property(name="creation_date", type=DateType)
POM_application_object_last_mod_date: Property = Property(name="last_mod_date", type=DateType)
POM_application_object_object_string: Property = Property(name="object_string", type=StringType)
POM_application_object.attributes={POM_application_object_creation_date, POM_application_object_last_mod_date, POM_application_object_object_string}

# CreateInput class attributes and methods

# CompndCreateInput class attributes and methods
CompndCreateInput___referencePropName: Property = Property(name="__referencePropName", type=StringType)
CompndCreateInput.attributes={CompndCreateInput___referencePropName}

# BOMLine class attributes and methods
BOMLine_object_string: Property = Property(name="object_string", type=StringType)
BOMLine_bl_rev_object_name: Property = Property(name="bl_rev_object_name", type=StringType)
BOMLine_bl_has_children: Property = Property(name="bl_has_children", type=BooleanType)
BOMLine_bl_quantity: Property = Property(name="bl_quantity", type=StringType)
BOMLine_bl_variant_state: Property = Property(name="bl_variant_state", type=StringType)
BOMLine_bl_plmxml_abs_xform: Property = Property(name="bl_plmxml_abs_xform", type=StringType)
BOMLine_bl_item_item_revision: Property = Property(name="bl_item_item_revision", type=StringType)
BOMLine.attributes={BOMLine_bl_has_children, BOMLine_bl_item_item_revision, BOMLine_bl_plmxml_abs_xform, BOMLine_bl_quantity, BOMLine_bl_rev_object_name, BOMLine_bl_variant_state, BOMLine_object_string}

# SearchCriteriaInput class attributes and methods

# BaseCreateInput class attributes and methods
BaseCreateInput___boName: Property = Property(name="__boName", type=StringType)
BaseCreateInput_object_name: Property = Property(name="object_name", type=StringType)
BaseCreateInput_object_desc: Property = Property(name="object_desc", type=StringType)
BaseCreateInput.attributes={BaseCreateInput___boName, BaseCreateInput_object_desc, BaseCreateInput_object_name}

# Relationships
SelectedBOMLineHelper_DemoBOMLine: BinaryAssociation = BinaryAssociation(
    name="SelectedBOMLineHelper_DemoBOMLine",
    ends={
        Property(name="selectedbomlinehelper", type=SelectedBOMLineHelper, multiplicity=Multiplicity(0, 9999)),
        Property(name="demobomline", type=DemoBOMLine, multiplicity=Multiplicity(1, 1))
    }
)
StructureHelper_DemoItemRevision: BinaryAssociation = BinaryAssociation(
    name="StructureHelper_DemoItemRevision",
    ends={
        Property(name="structurehelper", type=StructureHelper, multiplicity=Multiplicity(0, 9999)),
        Property(name="demoitemrevision", type=DemoItemRevision, multiplicity=Multiplicity(1, 1))
    }
)
StructureHelper_BomWindowPropFlagMap: BinaryAssociation = BinaryAssociation(
    name="StructureHelper_BomWindowPropFlagMap",
    ends={
        Property(name="structurehelper", type=StructureHelper, multiplicity=Multiplicity(0, 9999)),
        Property(name="bomwindowpropflagmap", type=BomWindowPropFlagMap, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DemoItemRevision_ItemRevision = Generalization(general=ItemRevision, specific=DemoItemRevision)
gen_DemoItem_Item = Generalization(general=Item, specific=DemoItem)
gen_DemoItemCreateInput_ItemCreateInput = Generalization(general=ItemCreateInput, specific=DemoItemCreateInput)
gen_DemoItemRevisionCompoundCreateInput_ItemRevisionCompoundCreateInput = Generalization(general=ItemRevisionCompoundCreateInput, specific=DemoItemRevisionCompoundCreateInput)
gen_DemoWorkspaceObject_WorkspaceObject = Generalization(general=WorkspaceObject, specific=DemoWorkspaceObject)
gen_DemoBOMLine_BOMLine = Generalization(general=BOMLine, specific=DemoBOMLine)
gen_ItemRevision_WorkspaceObject = Generalization(general=WorkspaceObject, specific=ItemRevision)
gen_GeneralQuery_SearchCriteria_SavedQuery = Generalization(general=SearchCriteria_SavedQuery, specific=GeneralQuery)
gen_Item_WorkspaceObject = Generalization(general=WorkspaceObject, specific=Item)
gen_WorkspaceObject_POM_application_object = Generalization(general=POM_application_object, specific=WorkspaceObject)
gen_ItemCreateInput_CreateInput = Generalization(general=CreateInput, specific=ItemCreateInput)
gen_ItemRevisionCompoundCreateInput_CompndCreateInput = Generalization(general=CompndCreateInput, specific=ItemRevisionCompoundCreateInput)
gen_SearchCriteria_SavedQuery_SearchCriteriaInput = Generalization(general=SearchCriteriaInput, specific=SearchCriteria_SavedQuery)
gen_POM_application_object_ModelObject = Generalization(general=ModelObject, specific=POM_application_object)
gen_CreateInput_BaseCreateInput = Generalization(general=BaseCreateInput, specific=CreateInput)
gen_CompndCreateInput_BaseCreateInput = Generalization(general=BaseCreateInput, specific=CompndCreateInput)
gen_BOMLine_ModelObject = Generalization(general=ModelObject, specific=BOMLine)

# Domain Model
domain_model = DomainModel(
    name="SampleApp",
    types={DemoItemRevision, DemoItem, DemoItemCreateInput, DemoItemRevisionCompoundCreateInput, DemoWorkspaceObject, DemoBOMLine, SelectedBOMLineHelper, StructureHelper, BomWindowPropFlagMap, ItemRevision, ItemRevisionSearchCriteria, GeneralQuery, Item, SearchInput, ModelObject, WorkspaceObject, ItemCreateInput, ItemRevisionCompoundCreateInput, BOMLine, SearchCriteria_SavedQuery, POM_application_object, CreateInput, CompndCreateInput, BOMLine, SearchCriteriaInput, BaseCreateInput},
    associations={SelectedBOMLineHelper_DemoBOMLine, StructureHelper_DemoItemRevision, StructureHelper_BomWindowPropFlagMap},
    generalizations={gen_DemoItemRevision_ItemRevision, gen_DemoItem_Item, gen_DemoItemCreateInput_ItemCreateInput, gen_DemoItemRevisionCompoundCreateInput_ItemRevisionCompoundCreateInput, gen_DemoWorkspaceObject_WorkspaceObject, gen_DemoBOMLine_BOMLine, gen_ItemRevision_WorkspaceObject, gen_GeneralQuery_SearchCriteria_SavedQuery, gen_Item_WorkspaceObject, gen_WorkspaceObject_POM_application_object, gen_ItemCreateInput_CreateInput, gen_ItemRevisionCompoundCreateInput_CompndCreateInput, gen_SearchCriteria_SavedQuery_SearchCriteriaInput, gen_POM_application_object_ModelObject, gen_CreateInput_BaseCreateInput, gen_CompndCreateInput_BaseCreateInput, gen_BOMLine_ModelObject},
    metadata=None
)


###############
#  GUI MODEL  #
###############

###############
#  GUI MODEL  #
###############

