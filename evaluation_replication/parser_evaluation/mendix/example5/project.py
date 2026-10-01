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

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType, SelectOption,
    Alert, AlertSeverity,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: SampleApp

# Screen: CreateItem_Request
createitem_request = Screen(name="CreateItem_Request", description="", view_elements=set(), route_path="/CreateItem_Request", screen_size="Small")
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40 = Text(
    name="text40",
    content="Create Item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3, text40},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Create",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
text2 = Text(
    name="text2",
    content="Data for initial revision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea2 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox5 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container3 = ViewContainer(
    name="container3",
    description="",
    view_elements={text2, textarea2, textbox4, textbox5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview7 = ViewContainer(
    name="dataView7",
    description="",
    view_elements={actionbutton1, container3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
createitem_request.view_elements = {container1, dataview7}
createitem_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
createitem_request.layout = createitem_request_layout


# Screen: CreateItem_Response
createitem_response = Screen(name="CreateItem_Response", description="", view_elements=set(), route_path="/CreateItem_Response", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text42 = Text(
    name="text42",
    content="Create Item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container3_1 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton1_1, text42},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
text11 = Text(
    name="text11",
    content="Details for created item revision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container2 = ViewContainer(
    name="container2",
    description="",
    view_elements={text11, textarea1, textbox2, textbox3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text12 = Text(
    name="text12",
    content="Details for created item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea2_1 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox4_1 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
textbox5_1 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container1_1 = ViewContainer(
    name="container1",
    description="",
    view_elements={text12, textarea2_1, textbox4_1, textbox5_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={container1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container2, dataview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
createitem_response.view_elements = {container3_1, dataview1}
createitem_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
createitem_response.layout = createitem_response_layout


# Screen: Home
home = Screen(name="Home", description="", view_elements=set(), route_path="/Home", screen_size="Small")
text40_1 = Text(
    name="text40",
    content="Teamcenter Extension Sample App",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_2 = ViewContainer(
    name="container1",
    description="",
    view_elements={text40_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton17 = Button(
    name="actionButton17",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
actionbutton9 = Button(
    name="actionButton9",
    description="",
    label="Configure Teamcenter",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container2_1 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton17, actionbutton9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton10 = Button(
    name="actionButton10",
    description="",
    label="Search ItemRevision",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton18 = Button(
    name="actionButton18",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container3_2 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton10, actionbutton18},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton11 = Button(
    name="actionButton11",
    description="",
    label="Create Item",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton19 = Button(
    name="actionButton19",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container4 = ViewContainer(
    name="container4",
    description="",
    view_elements={actionbutton11, actionbutton19},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton12 = Button(
    name="actionButton12",
    description="",
    label="Search WorkspaceObject",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton20 = Button(
    name="actionButton20",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container5 = ViewContainer(
    name="container5",
    description="",
    view_elements={actionbutton12, actionbutton20},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton13 = Button(
    name="actionButton13",
    description="",
    label="Teamcenter login",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton21 = Button(
    name="actionButton21",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container6 = ViewContainer(
    name="container6",
    description="",
    view_elements={actionbutton13, actionbutton21},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
home.view_elements = {container1_2, container2_1, container3_2, container4, container5, container6}
home_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
home.layout = home_layout


# Screen: ReviseItemRevision_Request
reviseitemrevision_request = Screen(name="ReviseItemRevision_Request", description="", view_elements=set(), route_path="/ReviseItemRevision_Request", screen_size="Small")
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Revise",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textbox1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
textarea1_1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox2_1 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox3_1 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
dataview6_form = Form(name="dataView6_form", description="", inputFields={textbox1, textarea1_1, textbox2_1, textbox3_1})
dataview6 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton2, actionbutton3_1, dataview6_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
reviseitemrevision_request.view_elements = {dataview6}
reviseitemrevision_request_layout = Layout()
reviseitemrevision_request.layout = reviseitemrevision_request_layout


# Screen: SearchItemRevision_Request
searchitemrevision_request = Screen(name="SearchItemRevision_Request", description="", view_elements=set(), route_path="/SearchItemRevision_Request", screen_size="Small")
actionbutton3_2 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40_2 = Text(
    name="text40",
    content="Search ItemRevision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_3 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_2, text40_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1_2 = Button(
    name="actionButton1",
    description="",
    label="Search",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textbox1_1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox2_2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ItemID"}
)
textbox3_2 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision type",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "_Type"}
)
container2_2 = ViewContainer(
    name="container2",
    description="",
    view_elements={textbox1_1, textbox2_2, textbox3_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview6_1 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_2, container2_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
searchitemrevision_request.view_elements = {container1_3, dataview6_1}
searchitemrevision_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchitemrevision_request.layout = searchitemrevision_request_layout


# Screen: SearchItemRevision_Response
searchitemrevision_response = Screen(name="SearchItemRevision_Response", description="", view_elements=set(), route_path="/SearchItemRevision_Response", screen_size="Small")
searchitemrevision_response.view_elements = set()
searchitemrevision_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchitemrevision_response.layout = searchitemrevision_response_layout


# Screen: SearchWorkspaceObject_Request
searchworkspaceobject_request = Screen(name="SearchWorkspaceObject_Request", description="", view_elements=set(), route_path="/SearchWorkspaceObject_Request", screen_size="Small")
actionbutton3_3 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40_3 = Text(
    name="text40",
    content="Search Workspace Object",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_4 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_3, text40_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1_3 = Button(
    name="actionButton1",
    description="",
    label="Search",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
text12_1 = Text(
    name="text12",
    content="Pagination",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox2_3 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Start index",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "startIndex"}
)
textbox3_3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Max to load",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "maxToLoad"}
)
textbox5_2 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Max to return",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "maxToReturn"}
)
container2_3 = ViewContainer(
    name="container2",
    description="",
    view_elements={text12_1, textbox2_3, textbox3_3, textbox5_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Created after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CreatedAfter"}
)
datepicker2 = InputField(
    name="datePicker2",
    description="",
    field_type=InputFieldType.Date,
    label="Created before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CreatedBefore"}
)
datepicker3 = InputField(
    name="datePicker3",
    description="",
    field_type=InputFieldType.Date,
    label="Modified after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ModifiedAfter"}
)
datepicker4 = InputField(
    name="datePicker4",
    description="",
    field_type=InputFieldType.Date,
    label="Modified before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ModifiedBefore"}
)
datepicker5 = InputField(
    name="datePicker5",
    description="",
    field_type=InputFieldType.Date,
    label="Released after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ReleasedAfter"}
)
datepicker6 = InputField(
    name="datePicker6",
    description="",
    field_type=InputFieldType.Date,
    label="Released before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ReleasedBefore"}
)
text13 = Text(
    name="text13",
    content="Query parameters",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox10 = InputField(
    name="textBox10",
    description="",
    field_type=InputFieldType.Text,
    label="Owning user",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "OwningUser"}
)
textbox11 = InputField(
    name="textBox11",
    description="",
    field_type=InputFieldType.Text,
    label="Owning group",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "OwningGroup"}
)
textbox7 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox8 = InputField(
    name="textBox8",
    description="",
    field_type=InputFieldType.Text,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox9 = InputField(
    name="textBox9",
    description="",
    field_type=InputFieldType.Text,
    label="Type",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "_Type"}
)
container3_3 = ViewContainer(
    name="container3",
    description="",
    view_elements={datepicker1, datepicker2, datepicker3, datepicker4, datepicker5, datepicker6, text13, textbox10, textbox11, textbox7, textbox8, textbox9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview7_1 = ViewContainer(
    name="dataView7",
    description="",
    view_elements={container3_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_2 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_3, container2_3, dataview7_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
searchworkspaceobject_request.view_elements = {container1_4, dataview6_2}
searchworkspaceobject_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchworkspaceobject_request.layout = searchworkspaceobject_request_layout


# Screen: SearchWorkspaceObject_Response
searchworkspaceobject_response = Screen(name="SearchWorkspaceObject_Response", description="", view_elements=set(), route_path="/SearchWorkspaceObject_Response", screen_size="Small")
searchworkspaceobject_response.view_elements = set()
searchworkspaceobject_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchworkspaceobject_response.layout = searchworkspaceobject_response_layout


# Screen: Structure_Request
structure_request = Screen(name="Structure_Request", description="", view_elements=set(), route_path="/Structure_Request", screen_size="Small")
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Structure",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton3_4 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text42_1 = Text(
    name="text42",
    content="Configure structure for {1}/{2} - {3}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
dataview5 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={text42_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container1_5 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_4, dataview5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text2_1 = Text(
    name="text2",
    content="Revision rule",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container3_4 = ViewContainer(
    name="container3",
    description="",
    view_elements={listview1, text2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_4 = ViewContainer(
    name="container2",
    description="",
    view_elements={listview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3 = Text(
    name="text3",
    content="Variant rule",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container2_4, text3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container4_1 = ViewContainer(
    name="container4",
    description="",
    view_elements={dataview1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2_1 = ViewContainer(
    name="dataView2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5 = Text(
    name="text5",
    content="BOM window properties",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container5_1 = ViewContainer(
    name="container5",
    description="",
    view_elements={dataview2_1, text5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
structure_request.view_elements = {actionbutton4, container1_5, container3_4, container4_1, container5_1}
structure_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
structure_request.layout = structure_request_layout


# Screen: Structure_Response
structure_response = Screen(name="Structure_Response", description="", view_elements=set(), route_path="/Structure_Response", screen_size="Small")
structure_response.view_elements = set()
structure_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
structure_response.layout = structure_response_layout


# Screen: UpdateItemRevision_Request
updateitemrevision_request = Screen(name="UpdateItemRevision_Request", description="", view_elements=set(), route_path="/UpdateItemRevision_Request", screen_size="Small")
actionbutton2_1 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_5 = Button(
    name="actionButton3",
    description="",
    label="Update",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textarea1_2 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox3_4 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
textbox2_4 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox1_2 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
dataview6_form_1 = Form(name="dataView6_form", description="", inputFields={textarea1_2, textbox3_4, textbox2_4, textbox1_2})
dataview6_3 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton2_1, actionbutton3_5, dataview6_form_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
updateitemrevision_request.view_elements = {dataview6_3}
updateitemrevision_request_layout = Layout()
updateitemrevision_request.layout = updateitemrevision_request_layout

sampleapp = Module(
    name="SampleApp",
    screens={createitem_request, createitem_response, home, reviseitemrevision_request, searchitemrevision_request, searchitemrevision_response, searchworkspaceobject_request, searchworkspaceobject_response, structure_request, structure_response, updateitemrevision_request}
)

# GUI Model
gui_model = GUIModel(
    name="SampleApp",
    package="",
    versionCode="",
    versionName="",
    modules={sampleapp},
    description=""
)

# Bound-entity data bindings resolved by the Mendix parser
dataview6_form.data_binding = DataBinding(domain_concept=DemoItemRevision)
dataview6_form_1.data_binding = DataBinding(domain_concept=DemoItemRevision)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="B-UML project generated by BESSER Migration Hub.")
project = Project(
    name="SampleApp",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
