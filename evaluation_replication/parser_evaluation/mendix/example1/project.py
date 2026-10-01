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

# Enumerations
ENUM_Receipt: Enumeration = Enumeration(
    name="ENUM_Receipt",
    literals={
            EnumerationLiteral(name="New"),
			EnumerationLiteral(name="Awaiting_delivery"),
			EnumerationLiteral(name="Completed"),
			EnumerationLiteral(name="Damaged"),
			EnumerationLiteral(name="Missing")
    }
)

ENUM_Status: Enumeration = Enumeration(
    name="ENUM_Status",
    literals={
            EnumerationLiteral(name="Pending_Approval"),
			EnumerationLiteral(name="Rejected"),
			EnumerationLiteral(name="In_Progress"),
			EnumerationLiteral(name="Declined"),
			EnumerationLiteral(name="Finished")
    }
)

ENUM_PO: Enumeration = Enumeration(
    name="ENUM_PO",
    literals={
            EnumerationLiteral(name="Please_assign_vendors"),
			EnumerationLiteral(name="Ready_to_create_PO"),
			EnumerationLiteral(name="Please_fill_out_the_missing_fields"),
			EnumerationLiteral(name="Ready_to_complete_the_task")
    }
)

ENUM_Department: Enumeration = Enumeration(
    name="ENUM_Department",
    literals={
            EnumerationLiteral(name="Marketing"),
			EnumerationLiteral(name="Sales"),
			EnumerationLiteral(name="Finance"),
			EnumerationLiteral(name="Operations"),
			EnumerationLiteral(name="Human_Resources")
    }
)

# Classes
Request = Class(name="Request")
Attachment = Class(name="Attachment")
Vendor = Class(name="Vendor")
Product = Class(name="Product")
ProductLine = Class(name="ProductLine")
TaskInboxBadge = Class(name="TaskInboxBadge")
MyRequestsDashboard = Class(name="MyRequestsDashboard")
PurchaseOrder = Class(name="PurchaseOrder")
MendixSSOUser = Class(name="MendixSSOUser")
TaskCount = Class(name="TaskCount")
WorkflowSummary = Class(name="WorkflowSummary")

# Request class attributes and methods
Request_RequestID: Property = Property(name="RequestID", type=IntegerType)
Request_Title: Property = Property(name="Title", type=StringType)
Request_Status: Property = Property(name="Status", type=ENUM_Status)
Request_RequestReason: Property = Property(name="RequestReason", type=StringType)
Request_RequiredDeliveryDate: Property = Property(name="RequiredDeliveryDate", type=DateType)
Request_Department: Property = Property(name="Department", type=ENUM_Department)
Request_ShippingAddress: Property = Property(name="ShippingAddress", type=StringType)
Request_SumTotalPrice: Property = Property(name="SumTotalPrice", type=FloatType)
Request_POState: Property = Property(name="POState", type=ENUM_PO)
Request.attributes={Request_Department, Request_POState, Request_RequestID, Request_RequestReason, Request_RequiredDeliveryDate, Request_ShippingAddress, Request_Status, Request_SumTotalPrice, Request_Title}

# Attachment class attributes and methods

# Vendor class attributes and methods
Vendor_VendorID: Property = Property(name="VendorID", type=StringType)
Vendor_Name: Property = Property(name="Name", type=StringType)
Vendor_Address: Property = Property(name="Address", type=StringType)
Vendor_BankAccount: Property = Property(name="BankAccount", type=StringType)
Vendor_Phone: Property = Property(name="Phone", type=StringType)
Vendor.attributes={Vendor_Address, Vendor_BankAccount, Vendor_Name, Vendor_Phone, Vendor_VendorID}

# Product class attributes and methods
Product_ProductID: Property = Property(name="ProductID", type=IntegerType)
Product_Name: Property = Property(name="Name", type=StringType)
Product_Description: Property = Property(name="Description", type=StringType)
Product_InputPrice: Property = Property(name="InputPrice", type=FloatType)
Product_VATPercentage: Property = Property(name="VATPercentage", type=FloatType)
Product_VATIncludedInPrice: Property = Property(name="VATIncludedInPrice", type=BooleanType)
Product_UnitPrice: Property = Property(name="UnitPrice", type=FloatType)
Product_VAT: Property = Property(name="VAT", type=FloatType)
Product.attributes={Product_Description, Product_InputPrice, Product_Name, Product_ProductID, Product_UnitPrice, Product_VAT, Product_VATIncludedInPrice, Product_VATPercentage}

# ProductLine class attributes and methods
ProductLine_Quantity: Property = Property(name="Quantity", type=IntegerType)
ProductLine_TotalGrossPrice: Property = Property(name="TotalGrossPrice", type=FloatType)
ProductLine_TotalVAT: Property = Property(name="TotalVAT", type=FloatType)
ProductLine_TotalNetPrice: Property = Property(name="TotalNetPrice", type=FloatType)
ProductLine_Status: Property = Property(name="Status", type=ENUM_Receipt)
ProductLine_DateOfReceipt: Property = Property(name="DateOfReceipt", type=DateType)
ProductLine_InvoiceNumber: Property = Property(name="InvoiceNumber", type=StringType)
ProductLine_InvoiceDate: Property = Property(name="InvoiceDate", type=DateType)
ProductLine_POCreated: Property = Property(name="POCreated", type=BooleanType)
ProductLine.attributes={ProductLine_DateOfReceipt, ProductLine_InvoiceDate, ProductLine_InvoiceNumber, ProductLine_POCreated, ProductLine_Quantity, ProductLine_Status, ProductLine_TotalGrossPrice, ProductLine_TotalNetPrice, ProductLine_TotalVAT}

# TaskInboxBadge class attributes and methods
TaskInboxBadge_OpenTasks: Property = Property(name="OpenTasks", type=IntegerType)
TaskInboxBadge_MyTasks: Property = Property(name="MyTasks", type=IntegerType)
TaskInboxBadge.attributes={TaskInboxBadge_MyTasks, TaskInboxBadge_OpenTasks}

# MyRequestsDashboard class attributes and methods
MyRequestsDashboard_PendingApproval: Property = Property(name="PendingApproval", type=IntegerType)
MyRequestsDashboard_InProgress: Property = Property(name="InProgress", type=IntegerType)
MyRequestsDashboard_Finished: Property = Property(name="Finished", type=IntegerType)
MyRequestsDashboard_Rejected: Property = Property(name="Rejected", type=IntegerType)
MyRequestsDashboard.attributes={MyRequestsDashboard_Finished, MyRequestsDashboard_InProgress, MyRequestsDashboard_PendingApproval, MyRequestsDashboard_Rejected}

# PurchaseOrder class attributes and methods
PurchaseOrder_Number: Property = Property(name="Number", type=IntegerType)
PurchaseOrder_PODate: Property = Property(name="PODate", type=DateType)
PurchaseOrder_PromiseDate: Property = Property(name="PromiseDate", type=DateType)
PurchaseOrder_GeneralLedgerNumber: Property = Property(name="GeneralLedgerNumber", type=IntegerType)
PurchaseOrder_Subtotal: Property = Property(name="Subtotal", type=FloatType)
PurchaseOrder_TotalVAT: Property = Property(name="TotalVAT", type=FloatType)
PurchaseOrder_TotalCost: Property = Property(name="TotalCost", type=FloatType)
PurchaseOrder.attributes={PurchaseOrder_GeneralLedgerNumber, PurchaseOrder_Number, PurchaseOrder_PODate, PurchaseOrder_PromiseDate, PurchaseOrder_Subtotal, PurchaseOrder_TotalCost, PurchaseOrder_TotalVAT}

# MendixSSOUser class attributes and methods
MendixSSOUser_DisplayName: Property = Property(name="DisplayName", type=StringType)
MendixSSOUser_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
MendixSSOUser_AvatarURL: Property = Property(name="AvatarURL", type=StringType)
MendixSSOUser_AvatarThumbURL: Property = Property(name="AvatarThumbURL", type=StringType)
MendixSSOUser.attributes={MendixSSOUser_AvatarThumbURL, MendixSSOUser_AvatarURL, MendixSSOUser_DisplayName, MendixSSOUser_EmailAddress}

# TaskCount class attributes and methods
TaskCount_MyOpenTaskCount: Property = Property(name="MyOpenTaskCount", type=IntegerType)
TaskCount_AllOpenTaskCount: Property = Property(name="AllOpenTaskCount", type=IntegerType)
TaskCount_UnassignedTaskCount: Property = Property(name="UnassignedTaskCount", type=IntegerType)
TaskCount_CompletedTaskCount: Property = Property(name="CompletedTaskCount", type=IntegerType)
TaskCount_AssigneeSearch: Property = Property(name="AssigneeSearch", type=StringType)
TaskCount.attributes={TaskCount_AllOpenTaskCount, TaskCount_AssigneeSearch, TaskCount_CompletedTaskCount, TaskCount_MyOpenTaskCount, TaskCount_UnassignedTaskCount}

# WorkflowSummary class attributes and methods
WorkflowSummary_NumberOfWorkflowsInProgress: Property = Property(name="NumberOfWorkflowsInProgress", type=IntegerType)
WorkflowSummary_NumberOfWorkflowOverdue: Property = Property(name="NumberOfWorkflowOverdue", type=IntegerType)
WorkflowSummary_NumberOfWorkflowsCompleted: Property = Property(name="NumberOfWorkflowsCompleted", type=IntegerType)
WorkflowSummary_IsLocked: Property = Property(name="IsLocked", type=BooleanType)
WorkflowSummary_IsObsolete: Property = Property(name="IsObsolete", type=BooleanType)
WorkflowSummary.attributes={WorkflowSummary_IsLocked, WorkflowSummary_IsObsolete, WorkflowSummary_NumberOfWorkflowOverdue, WorkflowSummary_NumberOfWorkflowsCompleted, WorkflowSummary_NumberOfWorkflowsInProgress}

# Relationships
Attachment_Request: BinaryAssociation = BinaryAssociation(
    name="Attachment_Request",
    ends={
        Property(name="request", type=Request, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="attachment", type=Attachment, multiplicity=Multiplicity(0, 9999))
    }
)
Vendor_Product: BinaryAssociation = BinaryAssociation(
    name="Vendor_Product",
    ends={
        Property(name="vendor", type=Vendor, multiplicity=Multiplicity(0, 9999)),
        Property(name="product", type=Product, multiplicity=Multiplicity(0, 9999))
    }
)
ProductLine_SelectedVendor: BinaryAssociation = BinaryAssociation(
    name="ProductLine_SelectedVendor",
    ends={
        Property(name="vendor", type=Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="productline", type=ProductLine, multiplicity=Multiplicity(0, 9999))
    }
)
ProductLine_PurchaseOrder: BinaryAssociation = BinaryAssociation(
    name="ProductLine_PurchaseOrder",
    ends={
        Property(name="productline", type=ProductLine, multiplicity=Multiplicity(0, 9999)),
        Property(name="purchaseorder", type=PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
PurchaseOrder_Vendor: BinaryAssociation = BinaryAssociation(
    name="PurchaseOrder_Vendor",
    ends={
        Property(name="vendor", type=Vendor, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseorder", type=PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
PurchaseOrder_Request: BinaryAssociation = BinaryAssociation(
    name="PurchaseOrder_Request",
    ends={
        Property(name="request", type=Request, multiplicity=Multiplicity(1, 1)),
        Property(name="purchaseorder", type=PurchaseOrder, multiplicity=Multiplicity(0, 9999))
    }
)
ProductLine_Request: BinaryAssociation = BinaryAssociation(
    name="ProductLine_Request",
    ends={
        Property(name="request", type=Request, multiplicity=Multiplicity(1, 1)),
        Property(name="productline", type=ProductLine, multiplicity=Multiplicity(0, 9999))
    }
)
ProductLine_Product: BinaryAssociation = BinaryAssociation(
    name="ProductLine_Product",
    ends={
        Property(name="product", type=Product, multiplicity=Multiplicity(1, 1)),
        Property(name="productline", type=ProductLine, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PurchaseApprovals",
    types={Request, Attachment, Vendor, Product, ProductLine, TaskInboxBadge, MyRequestsDashboard, PurchaseOrder, MendixSSOUser, TaskCount, WorkflowSummary, ENUM_Receipt, ENUM_Status, ENUM_PO, ENUM_Department},
    associations={Attachment_Request, Vendor_Product, ProductLine_SelectedVendor, ProductLine_PurchaseOrder, PurchaseOrder_Vendor, PurchaseOrder_Request, ProductLine_Request, ProductLine_Product},
    generalizations={},
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

# Module: PurchaseApprovals

# Screen: Admin_Homepage
admin_homepage = Screen(name="Admin_Homepage", description="", view_elements=set(), route_path="/Admin_Homepage", screen_size="Small")
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
    label="Workflow dashboard",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container2 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton17, actionbutton9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton13 = Button(
    name="actionButton13",
    description="",
    label="Workflow management",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton22 = Button(
    name="actionButton22",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container3 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton13, actionbutton22},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton14 = Button(
    name="actionButton14",
    description="",
    label="User management",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton23 = Button(
    name="actionButton23",
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
    view_elements={actionbutton14, actionbutton23},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text3 = Text(
    name="text3",
    content="Purchase Request App",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero-title"]
)
container6 = ViewContainer(
    name="container6",
    description="",
    view_elements={text3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader-overlay"]
)
image2 = Image(
    name="image2",
    description="",
    source="PurchaseApprovals.Images.header_purchase",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero-backgroundimage"]
)
container5 = ViewContainer(
    name="container5",
    description="",
    view_elements={container6, image2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero", "text-center"]
)
actionbutton15 = Button(
    name="actionButton15",
    description="",
    label="Products overview",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton24 = Button(
    name="actionButton24",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container7 = ViewContainer(
    name="container7",
    description="",
    view_elements={actionbutton15, actionbutton24},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton16 = Button(
    name="actionButton16",
    description="",
    label="Vendors overview",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton25 = Button(
    name="actionButton25",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container8 = ViewContainer(
    name="container8",
    description="",
    view_elements={actionbutton16, actionbutton25},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
admin_homepage.view_elements = {container2, container3, container4, container5, container7, container8}
admin_homepage_layout = Layout()
admin_homepage.layout = admin_homepage_layout


# Screen: Admin_Workflow_Dashboard
admin_workflow_dashboard = Screen(name="Admin_Workflow_Dashboard", description="", view_elements=set(), route_path="/Admin_Workflow_Dashboard", screen_size="Small")
tabcontainer2 = ViewContainer(
    name="tabContainer2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined", "cardtabs-tabs"]
)
dataview7 = ViewContainer(
    name="dataView7",
    description="",
    view_elements={tabcontainer2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
admin_workflow_dashboard.view_elements = {dataview7}
admin_workflow_dashboard_layout = Layout()
admin_workflow_dashboard.layout = admin_workflow_dashboard_layout


# Screen: Admin_Workflow_InstanceOverview
admin_workflow_instanceoverview = Screen(name="Admin_Workflow_InstanceOverview", description="", view_elements=set(), route_path="/Admin_Workflow_InstanceOverview", screen_size="Small")
actionbutton7 = Button(
    name="actionButton7",
    description="",
    label="< Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Delete all workflows",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
container1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
datagrid21_col_0 = ExpressionColumn(label="Workflow name", expression="Name")
datagrid21_col_1 = ExpressionColumn(label="State", expression="State")
datagrid21_col_2 = ExpressionColumn(label="Due by", expression="DueDate")
datagrid21_col_3 = ExpressionColumn(label="Started on", expression="StartTime")
datagrid21_col_4 = ExpressionColumn(label=" ", expression="Name")
datagrid21 = Table(
    name="dataGrid21",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=10,
    action_buttons=False,
    columns=[datagrid21_col_0, datagrid21_col_1, datagrid21_col_2, datagrid21_col_3, datagrid21_col_4],
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container32 = ViewContainer(
    name="container32",
    description="",
    view_elements={datagrid21},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-content"]
)
label49 = Text(
    name="label49",
    content="Workflows",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
container39 = ViewContainer(
    name="container39",
    description="",
    view_elements={container32, label49},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text41 = Text(
    name="text41",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7, container1, container39, text41},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
admin_workflow_instanceoverview.view_elements = {dataview1}
admin_workflow_instanceoverview_layout = Layout()
admin_workflow_instanceoverview.layout = admin_workflow_instanceoverview_layout


# Screen: Admin_Workflow_Instance_View
admin_workflow_instance_view = Screen(name="Admin_Workflow_Instance_View", description="", view_elements=set(), route_path="/Admin_Workflow_Instance_View", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Required delivery date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequiredDeliveryDate"}
)
textbox2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
referenceselector4 = InputField(
    name="referenceSelector4",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Invoice Processor",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
referenceselector6 = InputField(
    name="referenceSelector6",
    description="",
    field_type=InputFieldType.Dropdown,
    label="PO Creator",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
referenceselector3 = InputField(
    name="referenceSelector3",
    description="",
    field_type=InputFieldType.Dropdown,
    label="First Approver",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
textarea2 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Shipping address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ShippingAddress"}
)
textbox1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Request ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequestID"}
)
textarea1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Request reason",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequestReason"}
)
referenceselector1 = InputField(
    name="referenceSelector1",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Workflow",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
referenceselector5 = InputField(
    name="referenceSelector5",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Receiver",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
referenceselector7 = InputField(
    name="referenceSelector7",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Second Approver",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
textbox3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Sum total price",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "SumTotalPrice"}
)
referenceselector2 = InputField(
    name="referenceSelector2",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Requester",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
t_innerdataview_form = Form(name="T_InnerDataView_form", description="", inputFields={datepicker1, textbox2, referenceselector4, referenceselector6, referenceselector3, textarea2, textbox1, textarea1, referenceselector1, referenceselector5, referenceselector7, textbox3, referenceselector2})
t_innerdataview = ViewContainer(
    name="T_InnerDataView",
    description="",
    view_elements={t_innerdataview_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container11 = ViewContainer(
    name="container11",
    description="",
    view_elements={t_innerdataview},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-content"]
)
container2_1 = ViewContainer(
    name="container2",
    description="",
    view_elements={container11},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
tabcontainer1 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined"]
)
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1_1, actionbutton2, tabcontainer1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
admin_workflow_instance_view.view_elements = {dataview1_1}
admin_workflow_instance_view_layout = Layout()
admin_workflow_instance_view.layout = admin_workflow_instance_view_layout


# Screen: Admin_Workflow_Overview
admin_workflow_overview = Screen(name="Admin_Workflow_Overview", description="", view_elements=set(), route_path="/Admin_Workflow_Overview", screen_size="Small")
actionbutton7_1 = Button(
    name="actionButton7",
    description="",
    label="< Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
datagrid21_1_col_0 = ExpressionColumn(label="Workflow name", expression="Title")
datagrid21_1_col_1 = ExpressionColumn(label="In Progress", expression="NumberOfWorkflowsInProgress")
datagrid21_1_col_2 = ExpressionColumn(label="Overdue", expression="NumberOfWorkflowOverdue")
datagrid21_1 = Table(
    name="dataGrid21",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=20,
    action_buttons=False,
    columns=[datagrid21_1_col_0, datagrid21_1_col_1, datagrid21_1_col_2],
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text40 = Text(
    name="text40",
    content="Workflow management",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
admin_workflow_overview.view_elements = {actionbutton7_1, datagrid21_1, text40}
admin_workflow_overview_layout = Layout()
admin_workflow_overview.layout = admin_workflow_overview_layout


# Screen: Attachment_NewEdit
attachment_newedit = Screen(name="Attachment_NewEdit", description="", view_elements=set(), route_path="/Attachment_NewEdit", screen_size="Small")
actionbutton1_2 = Button(
    name="actionButton1",
    description="",
    label="Add",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_1 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container1_1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton1_2, actionbutton2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
filemanager1 = InputField(
    name="fileManager1",
    description="",
    field_type=InputFieldType.File,
    label="File",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview5_form = Form(name="dataView5_form", description="", inputFields={filemanager1})
dataview5 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={container1_1, dataview5_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
attachment_newedit.view_elements = {dataview5}
attachment_newedit_layout = Layout()
attachment_newedit.layout = attachment_newedit_layout


# Screen: MendixSSOUserOverview
mendixssouseroverview = Screen(name="MendixSSOUserOverview", description="", view_elements=set(), route_path="/MendixSSOUserOverview", screen_size="Small")
container1_2 = ViewContainer(
    name="container1",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text40_1 = Text(
    name="text40",
    content="Mendix SSO Users Overview",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container2_2 = ViewContainer(
    name="container2",
    description="",
    view_elements={text40_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
mendixssouseroverview.view_elements = {container1_2, container2_2}
mendixssouseroverview_layout = Layout()
mendixssouseroverview.layout = mendixssouseroverview_layout


# Screen: MendixSSOUser_NewEdit
mendixssouser_newedit = Screen(name="MendixSSOUser_NewEdit", description="", view_elements=set(), route_path="/MendixSSOUser_NewEdit", screen_size="Small")
actionbutton1_3 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
referenceselector2_1 = InputField(
    name="referenceSelector2",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Time zone",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Code"}
)
textbox4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Avatar thumb URL",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AvatarThumbURL"}
)
datepicker1_1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Last login",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "LastLogin"}
)
textbox1_1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Display name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
textbox2_1 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Email address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "EmailAddress"}
)
referenceselector1_1 = InputField(
    name="referenceSelector1",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Language",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Code"}
)
textbox3_1 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Avatar URL",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AvatarURL"}
)
datepicker2 = InputField(
    name="datePicker2",
    description="",
    field_type=InputFieldType.Date,
    label="Blocked since",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "BlockedSince"}
)
textbox5 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
dataview6_form = Form(name="dataView6_form", description="", inputFields={referenceselector2_1, textbox4, datepicker1_1, textbox1_1, textbox2_1, referenceselector1_1, textbox3_1, datepicker2, textbox5})
dataview6 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_3, actionbutton2_2, dataview6_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
mendixssouser_newedit.view_elements = {dataview6}
mendixssouser_newedit_layout = Layout()
mendixssouser_newedit.layout = mendixssouser_newedit_layout


# Screen: MyRequests
myrequests = Screen(name="MyRequests", description="", view_elements=set(), is_main_page=True, route_path="/MyRequests", screen_size="Small")
actionbutton10 = Button(
    name="actionButton10",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#343A40", text_color="#FFFFFF", border_color="#1D2124", color_palette="default")),
    css_classes=["text-large", "btn-inverse"]
)
text30 = Text(
    name="text30",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text31 = Text(
    name="text31",
    content="Pending approval",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container11_1 = ViewContainer(
    name="container11",
    description="",
    view_elements={actionbutton10, text30, text31},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton9_1 = Button(
    name="actionButton9",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["text-large", "btn-warning"]
)
text32 = Text(
    name="text32",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text33 = Text(
    name="text33",
    content="In progress",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container12 = ViewContainer(
    name="container12",
    description="",
    view_elements={actionbutton9_1, text32, text33},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton8 = Button(
    name="actionButton8",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["text-large", "btn-success"]
)
text34 = Text(
    name="text34",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text35 = Text(
    name="text35",
    content="Finished",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container13 = ViewContainer(
    name="container13",
    description="",
    view_elements={actionbutton8, text34, text35},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton11 = Button(
    name="actionButton11",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["text-large", "btn-danger"]
)
text36 = Text(
    name="text36",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text37 = Text(
    name="text37",
    content="Rejected",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container14 = ViewContainer(
    name="container14",
    description="",
    view_elements={actionbutton11, text36, text37},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview11 = ViewContainer(
    name="dataView11",
    description="",
    view_elements={container11_1, container12, container13, container14},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader-overlay"]
)
image2_1 = Image(
    name="image2",
    description="",
    source="PurchaseApprovals.Images.header_purchase",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero-backgroundimage"]
)
container2_3 = ViewContainer(
    name="container2",
    description="",
    view_elements={dataview11, image2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero", "text-center"]
)
actionbutton2_3 = Button(
    name="actionButton2",
    description="",
    label="New Request",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["pull-right", "btn-primary"]
)
container10 = ViewContainer(
    name="container10",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image5 = Image(
    name="image5",
    description="",
    source="PurchaseApprovals.Images.icon_user",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["img-circle"]
)
text17 = Text(
    name="text17",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text18 = Text(
    name="text18",
    content="Not assigned yet",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview4 = ViewContainer(
    name="dataView4",
    description="",
    view_elements={container10, image5, text17, text18},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label22 = Text(
    name="label22",
    content="Requested products",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
listview3_source_0 = DataSourceElement(name="listView3")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview3_source_0_domain = None
listview3_source_0.field_names = ['ProductLine.TotalGrossPrice', 'ProductLine.Quantity', 'ProductLine.Status', 'Product.Name']
listview3 = DataList(
    name="listView3",
    description="",
    list_sources={listview3_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container1_3 = ViewContainer(
    name="container1",
    description="",
    view_elements={label22, listview3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image13 = Image(
    name="image13",
    description="",
    source="PurchaseApprovals.Images.icon_attachment",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label21 = Text(
    name="label21",
    content="Attachments",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview6_source_0 = DataSourceElement(name="listView6")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview6_source_0_domain = None
listview6_source_0.field_names = ['FileDocument.Name']
listview6 = DataList(
    name="listView6",
    description="",
    list_sources={listview6_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["lv-col-md-3", "lv-col-sm-6"]
)
text13 = Text(
    name="text13",
    content="Request Reason",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text14 = Text(
    name="text14",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text20 = Text(
    name="text20",
    content="Creation Date",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text22 = Text(
    name="text22",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5 = Text(
    name="text5",
    content="Required Delivery Date\r\n",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text6 = Text(
    name="text6",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text7 = Text(
    name="text7",
    content="Shipping Address",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text8 = Text(
    name="text8",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1_1 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container1_3, image13, label21, listview6, text13, text14, text20, text22, text5, text6, text7, text8},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text15 = Text(
    name="text15",
    content="Last updated: {1}\r\nRequest ID: {2}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text16 = Text(
    name="text16",
    content="Current Assignee",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text27 = Text(
    name="text27",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container5_1 = ViewContainer(
    name="container5",
    description="",
    view_elements={dataview4, tabcontainer1_1, text15, text16, text27},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_1 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={container5_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_source_0 = DataSourceElement(name="listView1")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_source_0_domain = None
listview1_source_0.field_names = ['Request.Status', 'Request.RequestID', 'Request.Title']
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3_1 = Text(
    name="text3",
    content="My Requests",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={actionbutton2_3, dataview6_1, listview1, text3_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
myrequests.view_elements = {container2_3, dataview2}
myrequests_layout = Layout()
myrequests.layout = myrequests_layout


# Screen: NewRequest_Step1
newrequest_step1 = Screen(name="NewRequest_Step1", description="", view_elements=set(), route_path="/NewRequest_Step1", screen_size="Small")
actionbutton1_4 = Button(
    name="actionButton1",
    description="",
    label="Next",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_4 = Button(
    name="actionButton2",
    description="",
    label="Discard",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5 = Button(
    name="actionButton5",
    description="",
    label="New Attachment",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
image11 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_attachment",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label21_1 = Text(
    name="label21",
    content="Attachments",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview6_1_source_0 = DataSourceElement(name="listView6")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview6_1_source_0_domain = None
listview6_1_source_0.field_names = ['FileDocument.Name', 'FileDocument.createdDate']
listview6_1 = DataList(
    name="listView6",
    description="",
    list_sources={listview6_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["lv-col-md-3", "lv-col-sm-6"]
)
container4_1 = ViewContainer(
    name="container4",
    description="",
    view_elements={actionbutton5, image11, label21_1, listview6_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea1_1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Request reason",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequestReason"}
)
textarea2_1 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Shipping address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ShippingAddress"}
)
datepicker1_2 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Required delivery date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequiredDeliveryDate"}
)
textbox1_2 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview6_form_1 = Form(name="dataView6_form", description="", inputFields={textarea1_1, textarea2_1, datepicker1_2, textbox1_2})
text3_2 = Text(
    name="text3",
    content="Request information",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_2 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_4, actionbutton2_4, container4_1, dataview6_form_1, text3_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["container", "background-secondary"]
)
container2_4 = ViewContainer(
    name="container2",
    description="",
    view_elements={dataview6_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
container5_2 = ViewContainer(
    name="container5",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sidebar-progress", "w-75", "h-75"]
)
container1_4 = ViewContainer(
    name="container1",
    description="",
    view_elements={container5_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_2 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container1_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
newrequest_step1.view_elements = {container2_4, dataview1_2}
newrequest_step1_layout = Layout()
newrequest_step1.layout = newrequest_step1_layout


# Screen: NewRequest_Step2
newrequest_step2 = Screen(name="NewRequest_Step2", description="", view_elements=set(), route_path="/NewRequest_Step2", screen_size="Small")
actionbutton2_5 = Button(
    name="actionButton2",
    description="",
    label="Next",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Previous",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Add product",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#343A40", text_color="#FFFFFF", border_color="#1D2124", color_palette="default")),
    css_classes=["btn-inverse"]
)
actionbutton5_1 = Button(
    name="actionButton5",
    description="",
    label="Discard",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1_1_source_0 = DataSourceElement(name="listView1")
listview1_1 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text1 = Text(
    name="text1",
    content="My requested products",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview2_1 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={actionbutton2_5, actionbutton3, actionbutton4, actionbutton5_1, listview1_1, text1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["container"]
)
container4_2 = ViewContainer(
    name="container4",
    description="",
    view_elements={dataview2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
container5_3 = ViewContainer(
    name="container5",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sidebar-progress", "w-75", "h-75"]
)
container3_1 = ViewContainer(
    name="container3",
    description="",
    view_elements={container5_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_3 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container3_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
newrequest_step2.view_elements = {container4_2, dataview1_3}
newrequest_step2_layout = Layout()
newrequest_step2.layout = newrequest_step2_layout


# Screen: NewRequest_Step3
newrequest_step3 = Screen(name="NewRequest_Step3", description="", view_elements=set(), route_path="/NewRequest_Step3", screen_size="Small")
actionbutton1_5 = Button(
    name="actionButton1",
    description="",
    label="Submit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_6 = Button(
    name="actionButton2",
    description="",
    label="Discard",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Previous",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
image11_1 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_attachment",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label21_2 = Text(
    name="label21",
    content="Attachments",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview6_2_source_0 = DataSourceElement(name="listView6")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview6_2_source_0_domain = None
listview6_2_source_0.field_names = ['FileDocument.Size', 'FileDocument.Name']
listview6_2 = DataList(
    name="listView6",
    description="",
    list_sources={listview6_2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["lv-col-md-3", "lv-col-sm-6"]
)
container4_3 = ViewContainer(
    name="container4",
    description="",
    view_elements={image11_1, label21_2, listview6_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea1_2 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Request reason",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequestReason"}
)
textarea2_2 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Shipping address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ShippingAddress"}
)
datepicker1_3 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Required delivery date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "RequiredDeliveryDate"}
)
textbox3_2 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview6_form_2 = Form(name="dataView6_form", description="", inputFields={textarea1_2, textarea2_2, datepicker1_3, textbox3_2})
image12 = Image(
    name="image12",
    description="",
    source="PurchaseApprovals.Images.icon_article",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label22_1 = Text(
    name="label22",
    content="Product",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_2_source_0 = DataSourceElement(name="listView1")
listview1_2 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text1_1 = Text(
    name="text1",
    content="Summary",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_3 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_5, actionbutton2_6, actionbutton3_1, container4_3, dataview6_form_2, image12, label22_1, listview1_2, text1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["container"]
)
container8_1 = ViewContainer(
    name="container8",
    description="",
    view_elements={dataview6_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
container5_4 = ViewContainer(
    name="container5",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sidebar-progress", "w-75", "h-75"]
)
container2_5 = ViewContainer(
    name="container2",
    description="",
    view_elements={container5_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_4 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container2_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
newrequest_step3.view_elements = {container8_1, dataview1_4}
newrequest_step3_layout = Layout()
newrequest_step3.layout = newrequest_step3_layout


# Screen: ProductLine_Edit_POCreator
productline_edit_pocreator = Screen(name="ProductLine_Edit_POCreator", description="", view_elements=set(), route_path="/ProductLine_Edit_POCreator", screen_size="Small")
actionbutton1_6 = Button(
    name="actionButton1",
    description="",
    label="Save changes",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_7 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox1_3 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Requested quantity",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Quantity"}
)
textbox6 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="VAT percentage",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "VATPercentage"}
)
textbox4_1 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox2_2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Product ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ProductID"}
)
textbox5_1 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Price in USD",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "InputPrice"}
)
textbox3_3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
dataview6_form_3 = Form(name="dataView6_form", description="", inputFields={textbox1_3, textbox6, textbox4_1, textbox2_2, textbox5_1, textbox3_3})
dataview6_4 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_6, actionbutton2_7, dataview6_form_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
productline_edit_pocreator.view_elements = {dataview6_4}
productline_edit_pocreator_layout = Layout()
productline_edit_pocreator.layout = productline_edit_pocreator_layout


# Screen: ProductLine_Edit_Receiver
productline_edit_receiver = Screen(name="ProductLine_Edit_Receiver", description="", view_elements=set(), route_path="/ProductLine_Edit_Receiver", screen_size="Small")
actionbutton2_8 = Button(
    name="actionButton2",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton5_2 = Button(
    name="actionButton5",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_2 = Button(
    name="actionButton3",
    description="",
    label="Missing",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container2_6 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton3_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton4_1 = Button(
    name="actionButton4",
    description="",
    label="Damaged",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container3_2 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton4_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton1_7 = Button(
    name="actionButton1",
    description="",
    label="Complete",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container4_4 = ViewContainer(
    name="container4",
    description="",
    view_elements={actionbutton1_7},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
datepicker1_4 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Date of receipt",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DateOfReceipt"}
)
datepicker2_1 = InputField(
    name="datePicker2",
    description="",
    field_type=InputFieldType.Date,
    label="Invoice date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "InvoiceDate"}
)
text1_2 = Text(
    name="text1",
    content="Status of the product",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox5_2 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Invoice number",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "InvoiceNumber"}
)
container1_5 = ViewContainer(
    name="container1",
    description="",
    view_elements={container2_6, container3_2, container4_4, datepicker1_4, datepicker2_1, text1_2, textbox5_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_5 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton2_8, actionbutton5_2, container1_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
productline_edit_receiver.view_elements = {dataview1_5}
productline_edit_receiver_layout = Layout()
productline_edit_receiver.layout = productline_edit_receiver_layout


# Screen: ProductLine_NewEdit
productline_newedit = Screen(name="ProductLine_NewEdit", description="", view_elements=set(), route_path="/ProductLine_NewEdit", screen_size="Small")
actionbutton1_8 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_9 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox1_4 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Quantity",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Quantity"}
)
referenceselector2_2 = InputField(
    name="referenceSelector2",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Product",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
dataview1_form = Form(name="dataView1_form", description="", inputFields={textbox1_4, referenceselector2_2})
dataview1_6 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1_8, actionbutton2_9, dataview1_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
productline_newedit.view_elements = {dataview1_6}
productline_newedit_layout = Layout()
productline_newedit.layout = productline_newedit_layout


# Screen: Product_NewEdit
product_newedit = Screen(name="Product_NewEdit", description="", view_elements=set(), route_path="/Product_NewEdit", screen_size="Small")
actionbutton1_9 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_10 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox4_2 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Price (in USD)",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "InputPrice"}
)
textbox2_3 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox5_3 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="VAT percentage in %",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "VATPercentage"}
)
textbox1_5 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Product ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ProductID"}
)
textarea1_3 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
dataview6_form_4 = Form(name="dataView6_form", description="", inputFields={textbox4_2, textbox2_3, textbox5_3, textbox1_5, textarea1_3})
dataview6_5 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_9, actionbutton2_10, dataview6_form_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
product_newedit.view_elements = {dataview6_5}
product_newedit_layout = Layout()
product_newedit.layout = product_newedit_layout


# Screen: Product_Overview
product_overview = Screen(name="Product_Overview", description="", view_elements=set(), route_path="/Product_Overview", screen_size="Small")
container1_6 = ViewContainer(
    name="container1",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text39 = Text(
    name="text39",
    content="You can manage products for your app",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-subtitle"]
)
text40_2 = Text(
    name="text40",
    content="Products Overview",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container2_7 = ViewContainer(
    name="container2",
    description="",
    view_elements={text39, text40_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
product_overview.view_elements = {container1_6, container2_7}
product_overview_layout = Layout()
product_overview.layout = product_overview_layout


# Screen: Product_Select
product_select = Screen(name="Product_Select", description="", view_elements=set(), route_path="/Product_Select", screen_size="Small")
actionbutton1_10 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_11 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container1_7 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton1_10, actionbutton2_11},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton3_3 = Button(
    name="actionButton3",
    description="",
    label="Try to create a new one.",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text2 = Text(
    name="text2",
    content="Can\'t find the product you are looing for? ",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_8 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton3_3, text2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["alert-info", "alert"]
)
listview1_3_source_0 = DataSourceElement(name="Product")
listview1_3 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_3_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
product_select.view_elements = {container1_7, container2_8, listview1_3}
product_select_layout = Layout()
product_select.layout = product_select_layout


# Screen: Product_SelectVendors
product_selectvendors = Screen(name="Product_SelectVendors", description="", view_elements=set(), route_path="/Product_SelectVendors", screen_size="Small")
actionbutton1_11 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_12 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1_4_source_0 = DataSourceElement(name="Vendor")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_4_source_0_domain = None
listview1_4_source_0.field_names = ['Vendor.VendorID', 'Vendor.Name']
listview1_4 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_4_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
product_selectvendors.view_elements = {actionbutton1_11, actionbutton2_12, listview1_4}
product_selectvendors_layout = Layout()
product_selectvendors.layout = product_selectvendors_layout


# Screen: PurchaseOrder_Edit
purchaseorder_edit = Screen(name="PurchaseOrder_Edit", description="", view_elements=set(), route_path="/PurchaseOrder_Edit", screen_size="Small")
actionbutton1_12 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_13 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1_5_source_0 = DataSourceElement(name="listView1")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_5_source_0_domain = None
listview1_5_source_0.field_names = ['Vendor.Name', 'PurchaseOrder.Number']
listview1_5 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_5_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_6 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_12, actionbutton2_13, listview1_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
purchaseorder_edit.view_elements = {dataview6_6}
purchaseorder_edit_layout = Layout()
purchaseorder_edit.layout = purchaseorder_edit_layout


# Screen: TaskInbox
taskinbox = Screen(name="TaskInbox", description="", view_elements=set(), route_path="/TaskInbox", screen_size="Small")
actionbutton10_1 = Button(
    name="actionButton10",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
text36_1 = Text(
    name="text36",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text37_1 = Text(
    name="text37",
    content="New requests",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container15 = ViewContainer(
    name="container15",
    description="",
    view_elements={actionbutton10_1, text36_1, text37_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton16_1 = Button(
    name="actionButton16",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
text41_1 = Text(
    name="text41",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text45 = Text(
    name="text45",
    content="In progress requests",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container16 = ViewContainer(
    name="container16",
    description="",
    view_elements={actionbutton16_1, text41_1, text45},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton14_1 = Button(
    name="actionButton14",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
text39_1 = Text(
    name="text39",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
text47 = Text(
    name="text47",
    content="My tasks",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container23 = ViewContainer(
    name="container23",
    description="",
    view_elements={actionbutton14_1, text39_1, text47},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3_3 = Text(
    name="text3",
    content="Task Inbox",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero-title"]
)
container3_3 = ViewContainer(
    name="container3",
    description="",
    view_elements={text3_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader-overlay"]
)
dataview11_1 = ViewContainer(
    name="dataView11",
    description="",
    view_elements={container15, container16, container23, container3_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader-overlay"]
)
image2_2 = Image(
    name="image2",
    description="",
    source="PurchaseApprovals.Images.header_purchase",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero-backgroundimage"]
)
container2_9 = ViewContainer(
    name="container2",
    description="",
    view_elements={dataview11_1, image2_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["headerhero", "text-center"]
)
listview4_source_0 = DataSourceElement(name="WorkflowUserTask")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview4_source_0_domain = None
listview4_source_0.field_names = ['Request.Title', 'Request.SumTotalPrice', 'Request.Department', 'Request.RequiredDeliveryDate', 'Request.RequestID', 'MendixSSOUser.DisplayName']
listview4 = DataList(
    name="listView4",
    description="",
    list_sources={listview4_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["lv-col-md-3", "lv-col-sm-6"]
)
container6_1 = ViewContainer(
    name="container6",
    description="",
    view_elements={listview4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview5_source_0 = DataSourceElement(name="WorkflowUserTask")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview5_source_0_domain = None
listview5_source_0.field_names = ['Request.Title', 'Request.SumTotalPrice', 'Request.Department', 'Request.RequiredDeliveryDate', 'Request.RequestID', 'MendixSSOUser.DisplayName']
listview5 = DataList(
    name="listView5",
    description="",
    list_sources={listview5_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["lv-col-md-3", "lv-col-sm-6"]
)
container7_1 = ViewContainer(
    name="container7",
    description="",
    view_elements={listview5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1_2 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container6_1, container7_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["cardtabs-tabs"]
)
dataview1_7 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={tabcontainer1_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5_1 = Text(
    name="text5",
    content="Requests",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
taskinbox.view_elements = {container2_9, dataview1_7, text5_1}
taskinbox_layout = Layout()
taskinbox.layout = taskinbox_layout


# Screen: Task_Approver
task_approver = Screen(name="Task_Approver", description="", view_elements=set(), route_path="/Task_Approver", screen_size="Small")
actionbutton7_2 = Button(
    name="actionButton7",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
image11_2 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_article",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text40_3 = Text(
    name="text40",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container23_1 = ViewContainer(
    name="container23",
    description="",
    view_elements={image11_2, text40_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-row"]
)
actionbutton10_2 = Button(
    name="actionButton10",
    description="",
    label="Reject",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton11_1 = Button(
    name="actionButton11",
    description="",
    label="Approve",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton8_1 = Button(
    name="actionButton8",
    description="",
    label="Reject",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton9_2 = Button(
    name="actionButton9",
    description="",
    label="Approve",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
container11_2 = ViewContainer(
    name="container11",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-remove"]
)
container3_4 = ViewContainer(
    name="container3",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-ok"]
)
text1_3 = Text(
    name="text1",
    content="Approved",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5_2 = Text(
    name="text5",
    content="Rejected",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
t_buttoncontainer3 = ViewContainer(
    name="T_ButtonContainer3",
    description="",
    view_elements={actionbutton10_2, actionbutton11_1, actionbutton8_1, actionbutton9_2, container11_2, container3_4, text1_3, text5_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["controlgroup"]
)
text10 = Text(
    name="text10",
    content="Approver Panel",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["hidden"]
)
container6_2 = ViewContainer(
    name="container6",
    description="",
    view_elements={t_buttoncontainer3, text10},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview3 = ViewContainer(
    name="dataView3",
    description="",
    view_elements={container6_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image15 = Image(
    name="image15",
    description="",
    source="PurchaseApprovals.Images.icon_product",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label22_2 = Text(
    name="label22",
    content="Products",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_6_source_0 = DataSourceElement(name="listView1")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_6_source_0_domain = None
listview1_6_source_0.field_names = ['Product.Description', 'ProductLine.Quantity', 'Product.Name']
listview1_6 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_6_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text23 = Text(
    name="text23",
    content="Name",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text51 = Text(
    name="text51",
    content="Quantity",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text52 = Text(
    name="text52",
    content="Description",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_10 = ViewContainer(
    name="container2",
    description="",
    view_elements={image15, label22_2, listview1_6, text23, text51, text52},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
tabcontainer1_3 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container2_10},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined", "cardtabs-tabs"]
)
text2_1 = Text(
    name="text2",
    content="Requested on: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text39_2 = Text(
    name="text39",
    content="Request ID: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
dataview13 = ViewContainer(
    name="dataView13",
    description="",
    view_elements={container23_1, dataview3, tabcontainer1_3, text2_1, text39_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
container16_1 = ViewContainer(
    name="container16",
    description="",
    view_elements={dataview13},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2_2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["border-bottom", "spacing-inner-bottom", "spacing-outer-bottom"]
)
dataview1_8 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7_2, container16_1, dataview2_2, listview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
task_approver.view_elements = {dataview1_8}
task_approver_layout = Layout()
task_approver.layout = task_approver_layout


# Screen: Task_InvoiceProcessor
task_invoiceprocessor = Screen(name="Task_InvoiceProcessor", description="", view_elements=set(), route_path="/Task_InvoiceProcessor", screen_size="Small")
actionbutton7_3 = Button(
    name="actionButton7",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
image11_3 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_article",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text40_4 = Text(
    name="text40",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container23_2 = ViewContainer(
    name="container23",
    description="",
    view_elements={image11_3, text40_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-row"]
)
actionbutton9_3 = Button(
    name="actionButton9",
    description="",
    label="Complete",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
container3_5 = ViewContainer(
    name="container3",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-ok"]
)
text1_4 = Text(
    name="text1",
    content="The request has been completed",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
t_buttoncontainer3_1 = ViewContainer(
    name="T_ButtonContainer3",
    description="",
    view_elements={actionbutton9_3, container3_5, text1_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["controlgroup"]
)
text10_1 = Text(
    name="text10",
    content="Invoice processor panel",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["hidden"]
)
container6_3 = ViewContainer(
    name="container6",
    description="",
    view_elements={t_buttoncontainer3_1, text10_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview3_1 = ViewContainer(
    name="dataView3",
    description="",
    view_elements={container6_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image16 = Image(
    name="image16",
    description="",
    source="PurchaseApprovals.Images.icon_product",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label23 = Text(
    name="label23",
    content="Requested product details",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_7_source_0 = DataSourceElement(name="listView1")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_7_source_0_domain = None
listview1_7_source_0.field_names = ['ProductLine.Quantity', 'Product.Name', 'Product.ProductID', 'Product.Description']
listview1_7 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_7_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text23_1 = Text(
    name="text23",
    content="Name",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text24 = Text(
    name="text24",
    content="ID",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text51_1 = Text(
    name="text51",
    content="Quantity",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text52_1 = Text(
    name="text52",
    content="Description",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_11 = ViewContainer(
    name="container2",
    description="",
    view_elements={image16, label23, listview1_7, text23_1, text24, text51_1, text52_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
image17 = Image(
    name="image17",
    description="",
    source="PurchaseApprovals.Images.icon_vendor",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label24 = Text(
    name="label24",
    content="Purchase orders for this request",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview2_1_source_0 = DataSourceElement(name="PurchaseOrder")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview2_1_source_0_domain = None
listview2_1_source_0.field_names = ['Vendor.Address', 'ProductLine.Quantity', 'Vendor.Phone', 'Product.UnitPrice', 'Request.ShippingAddress', 'ProductLine.TotalNetPrice', 'Request.RequiredDeliveryDate', 'PurchaseOrder.GeneralLedgerNumber', 'PurchaseOrder.TotalCost', 'MendixSSOUser.DisplayName', 'PurchaseOrder.Number', 'Request.Department', 'PurchaseOrder.PODate', 'PurchaseOrder.PromiseDate', 'PurchaseOrder.Subtotal', 'Vendor.VendorID', 'Product.Name', 'PurchaseOrder.TotalVAT', 'Vendor.Name', 'ProductLine.Status']
listview2_1 = DataList(
    name="listView2",
    description="",
    list_sources={listview2_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1_4 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container2_11, image17, label24, listview2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined", "cardtabs-tabs"]
)
text2_2 = Text(
    name="text2",
    content="Requested on: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text39_3 = Text(
    name="text39",
    content="Request ID: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
dataview13_1 = ViewContainer(
    name="dataView13",
    description="",
    view_elements={container23_2, dataview3_1, tabcontainer1_4, text2_2, text39_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
container16_2 = ViewContainer(
    name="container16",
    description="",
    view_elements={dataview13_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview4_1 = ViewContainer(
    name="dataView4",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview4_1 = DataList(
    name="listView4",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["border-bottom", "spacing-inner-bottom", "spacing-outer-bottom"]
)
dataview1_9 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7_3, container16_2, dataview4_1, listview4_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
task_invoiceprocessor.view_elements = {dataview1_9}
task_invoiceprocessor_layout = Layout()
task_invoiceprocessor.layout = task_invoiceprocessor_layout


# Screen: Task_POCreator
task_pocreator = Screen(name="Task_POCreator", description="", view_elements=set(), route_path="/Task_POCreator", screen_size="Small")
actionbutton7_4 = Button(
    name="actionButton7",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
image11_4 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_article",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text40_5 = Text(
    name="text40",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container23_3 = ViewContainer(
    name="container23",
    description="",
    view_elements={image11_4, text40_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-row"]
)
actionbutton10_3 = Button(
    name="actionButton10",
    description="",
    label="Create PO(s)",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton11_2 = Button(
    name="actionButton11",
    description="",
    label="Decline",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton12 = Button(
    name="actionButton12",
    description="",
    label="Decline",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton13_1 = Button(
    name="actionButton13",
    description="",
    label="Decline",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton14_2 = Button(
    name="actionButton14",
    description="",
    label="Decline",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_3 = Button(
    name="actionButton5",
    description="",
    label="Complete PO(s)",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton9_4 = Button(
    name="actionButton9",
    description="",
    label="Finish",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
text29 = Text(
    name="text29",
    content="Step 2: Please create purchase orders",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container1_8 = ViewContainer(
    name="container1",
    description="",
    view_elements={text29},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container11_3 = ViewContainer(
    name="container11",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-remove"]
)
container3_6 = ViewContainer(
    name="container3",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-ok"]
)
text30_1 = Text(
    name="text30",
    content="Step 3: Please complete missing fields in PO(s)",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container5_5 = ViewContainer(
    name="container5",
    description="",
    view_elements={text30_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text32_1 = Text(
    name="text32",
    content="Step 1: Please assign a vendor for each product",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container7_2 = ViewContainer(
    name="container7",
    description="",
    view_elements={text32_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text37_2 = Text(
    name="text37",
    content="This task is ready to be finished",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container8_2 = ViewContainer(
    name="container8",
    description="",
    view_elements={text37_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text1_5 = Text(
    name="text1",
    content="PO has been created",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5_3 = Text(
    name="text5",
    content="Declined",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
t_buttoncontainer3_2 = ViewContainer(
    name="T_ButtonContainer3",
    description="",
    view_elements={actionbutton10_3, actionbutton11_2, actionbutton12, actionbutton13_1, actionbutton14_2, actionbutton5_3, actionbutton9_4, container1_8, container11_3, container3_6, container5_5, container7_2, container8_2, text1_5, text5_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["controlgroup"]
)
text10_2 = Text(
    name="text10",
    content="PO Creator panel",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["hidden"]
)
container6_4 = ViewContainer(
    name="container6",
    description="",
    view_elements={t_buttoncontainer3_2, text10_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview3_2 = ViewContainer(
    name="dataView3",
    description="",
    view_elements={container6_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image15_1 = Image(
    name="image15",
    description="",
    source="PurchaseApprovals.Images.icon_timeline",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label22_3 = Text(
    name="label22",
    content="Products",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_12 = ViewContainer(
    name="container2",
    description="",
    view_elements={image15_1, label22_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
image16_1 = Image(
    name="image16",
    description="",
    source="PurchaseApprovals.Images.icon_vendor",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label23_1 = Text(
    name="label23",
    content="Purchase order templates for this request",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_8_source_0 = DataSourceElement(name="PurchaseOrder")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_8_source_0_domain = None
listview1_8_source_0.field_names = ['Product.Name', 'PurchaseOrder.TotalVAT', 'Vendor.Name', 'ProductLine.Quantity', 'Vendor.Address', 'Product.UnitPrice', 'Vendor.Phone', 'ProductLine.TotalNetPrice', 'Request.ShippingAddress', 'Request.RequiredDeliveryDate', 'PurchaseOrder.TotalCost', 'PurchaseOrder.GeneralLedgerNumber', 'MendixSSOUser.DisplayName', 'PurchaseOrder.Number', 'Request.Department', 'PurchaseOrder.PODate', 'PurchaseOrder.PromiseDate', 'PurchaseOrder.Subtotal', 'Vendor.VendorID']
listview1_8 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_8_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1_5 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={container2_12, image16_1, label23_1, listview1_8},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined", "cardtabs-tabs"]
)
text2_3 = Text(
    name="text2",
    content="Requested on: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text31_1 = Text(
    name="text31",
    content="Task progress:",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text39_4 = Text(
    name="text39",
    content="Request ID: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
dataview13_2 = ViewContainer(
    name="dataView13",
    description="",
    view_elements={container23_3, dataview3_2, tabcontainer1_5, text2_3, text31_1, text39_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
container16_3 = ViewContainer(
    name="container16",
    description="",
    view_elements={dataview13_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2_3 = ViewContainer(
    name="dataView2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview2_2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["border-bottom", "spacing-inner-bottom", "spacing-outer-bottom"]
)
dataview1_10 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7_4, container16_3, dataview2_3, listview2_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
task_pocreator.view_elements = {dataview1_10}
task_pocreator_layout = Layout()
task_pocreator.layout = task_pocreator_layout


# Screen: Task_Receiver
task_receiver = Screen(name="Task_Receiver", description="", view_elements=set(), route_path="/Task_Receiver", screen_size="Small")
actionbutton7_5 = Button(
    name="actionButton7",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
image11_5 = Image(
    name="image11",
    description="",
    source="PurchaseApprovals.Images.icon_article",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text40_6 = Text(
    name="text40",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container23_4 = ViewContainer(
    name="container23",
    description="",
    view_elements={image11_5, text40_6},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-row"]
)
actionbutton9_5 = Button(
    name="actionButton9",
    description="",
    label="Received",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
container3_7 = ViewContainer(
    name="container3",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["glyphicon", "glyphicon-ok"]
)
text1_6 = Text(
    name="text1",
    content="Received",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
t_buttoncontainer3_3 = ViewContainer(
    name="T_ButtonContainer3",
    description="",
    view_elements={actionbutton9_5, container3_7, text1_6},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["controlgroup"]
)
text10_3 = Text(
    name="text10",
    content="Receiver Panel",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["hidden"]
)
container6_5 = ViewContainer(
    name="container6",
    description="",
    view_elements={t_buttoncontainer3_3, text10_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview3_3 = ViewContainer(
    name="dataView3",
    description="",
    view_elements={container6_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
datagrid21_2_col_0_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "vendor")
datagrid21_2_col_0 = LookupColumn(label="Vendor", path=datagrid21_2_col_0_path, field=Vendor_Name)
datagrid21_2_col_1_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "product")
datagrid21_2_col_1 = LookupColumn(label="Product", path=datagrid21_2_col_1_path, field=Product_Name)
datagrid21_2_col_2 = FieldColumn(label="Quantity", field=ProductLine_Quantity)
datagrid21_2_col_3_path = next(end for assoc in domain_model.associations for end in assoc.ends if end.name == "purchaseorder")
datagrid21_2_col_3 = LookupColumn(label="Promise Date", path=datagrid21_2_col_3_path, field=PurchaseOrder_PromiseDate)
datagrid21_2_col_4 = FieldColumn(label="Status", field=ProductLine_Status)
datagrid21_2_col_5 = FieldColumn(label="Task", field=ProductLine_Status)
datagrid21_2 = Table(
    name="dataGrid21",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=10,
    action_buttons=False,
    columns=[datagrid21_2_col_0, datagrid21_2_col_1, datagrid21_2_col_2, datagrid21_2_col_3, datagrid21_2_col_4, datagrid21_2_col_5],
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
datagrid21_2_binding_domain = None
if domain_model_ref is not None:
    datagrid21_2_binding_domain = domain_model_ref.get_class_by_name("ProductLine")
if datagrid21_2_binding_domain:
    datagrid21_2_binding = DataBinding(domain_concept=datagrid21_2_binding_domain, name="ProductLineDataBinding")
else:
    # Domain class 'ProductLine' not resolved; data binding skipped.
    datagrid21_2_binding = None
if datagrid21_2_binding:
    datagrid21_2.data_binding = datagrid21_2_binding
image16_2 = Image(
    name="image16",
    description="",
    source="PurchaseApprovals.Images.icon_product",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
label23_2 = Text(
    name="label23",
    content="Expected products",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1_6 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={datagrid21_2, image16_2, label23_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined", "cardtabs-tabs"]
)
text2_4 = Text(
    name="text2",
    content="Requested on: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text39_5 = Text(
    name="text39",
    content="Request ID: {1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
dataview13_3 = ViewContainer(
    name="dataView13",
    description="",
    view_elements={container23_4, dataview3_3, tabcontainer1_6, text2_4, text39_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline"]
)
container16_4 = ViewContainer(
    name="container16",
    description="",
    view_elements={dataview13_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2_4 = ViewContainer(
    name="dataView2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview2_3 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["border-bottom", "spacing-inner-bottom", "spacing-outer-bottom"]
)
dataview1_11 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7_5, container16_4, dataview2_4, listview2_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
task_receiver.view_elements = {dataview1_11}
task_receiver_layout = Layout()
task_receiver.layout = task_receiver_layout


# Screen: UserRole_Select
userrole_select = Screen(name="UserRole_Select", description="", view_elements=set(), route_path="/UserRole_Select", screen_size="Small")
actionbutton1_13 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_14 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1_9_source_0 = DataSourceElement(name="UserRole")
listview1_9 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_9_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
userrole_select.view_elements = {actionbutton1_13, actionbutton2_14, listview1_9}
userrole_select_layout = Layout()
userrole_select.layout = userrole_select_layout


# Screen: Vendor_NewEdit
vendor_newedit = Screen(name="Vendor_NewEdit", description="", view_elements=set(), route_path="/Vendor_NewEdit", screen_size="Small")
actionbutton1_14 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_15 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox1_6 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Vendor name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox2_4 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Bank account",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "BankAccount"}
)
textarea1_4 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Vendor ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "VendorID"}
)
textarea2_3 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Address"}
)
textbox3_4 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Phone",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Phone"}
)
dataview6_form_5 = Form(name="dataView6_form", description="", inputFields={textbox1_6, textbox2_4, textarea1_4, textarea2_3, textbox3_4})
dataview6_7 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_14, actionbutton2_15, dataview6_form_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
vendor_newedit.view_elements = {dataview6_7}
vendor_newedit_layout = Layout()
vendor_newedit.layout = vendor_newedit_layout


# Screen: Vendor_Overview
vendor_overview = Screen(name="Vendor_Overview", description="", view_elements=set(), route_path="/Vendor_Overview", screen_size="Small")
container1_9 = ViewContainer(
    name="container1",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text39_6 = Text(
    name="text39",
    content="You can manage vendors for your app",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-subtitle"]
)
text40_7 = Text(
    name="text40",
    content="Vendors Overview",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container2_13 = ViewContainer(
    name="container2",
    description="",
    view_elements={text39_6, text40_7},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
vendor_overview.view_elements = {container1_9, container2_13}
vendor_overview_layout = Layout()
vendor_overview.layout = vendor_overview_layout


# Screen: Vendor_Select
vendor_select = Screen(name="Vendor_Select", description="", view_elements=set(), route_path="/Vendor_Select", screen_size="Small")
actionbutton1_15 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_16 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container1_10 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton1_15, actionbutton2_16},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton3_4 = Button(
    name="actionButton3",
    description="",
    label="Create a new vendor.",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text2_5 = Text(
    name="text2",
    content="Can\'t find the vendor you are looing for this product? ",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_14 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton3_4, text2_5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["alert-info", "alert"]
)
listview1_10_source_0 = DataSourceElement(name="Vendor")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_10_source_0_domain = None
listview1_10_source_0.field_names = ['Vendor.Address', 'Vendor.Name', 'Vendor.VendorID']
listview1_10 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_10_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text10_4 = Text(
    name="text10",
    content="ID",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text12 = Text(
    name="text12",
    content="Name",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text14_1 = Text(
    name="text14",
    content="Address",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_12 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container1_10, container2_14, listview1_10, text10_4, text12, text14_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
vendor_select.view_elements = {dataview1_12}
vendor_select_layout = Layout()
vendor_select.layout = vendor_select_layout


# Screen: Vendor_SelectProduct
vendor_selectproduct = Screen(name="Vendor_SelectProduct", description="", view_elements=set(), route_path="/Vendor_SelectProduct", screen_size="Small")
actionbutton1_16 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2_17 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1_11_source_0 = DataSourceElement(name="Product")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_11_source_0_domain = None
listview1_11_source_0.field_names = ['Product.Description', 'Product.Name', 'Product.ProductID']
listview1_11 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_11_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
vendor_selectproduct.view_elements = {actionbutton1_16, actionbutton2_17, listview1_11}
vendor_selectproduct_layout = Layout()
vendor_selectproduct.layout = vendor_selectproduct_layout


# Screen: WorkflowDefinition_View
workflowdefinition_view = Screen(name="WorkflowDefinition_View", description="", view_elements=set(), route_path="/WorkflowDefinition_View", screen_size="Small")
actionbutton7_6 = Button(
    name="actionButton7",
    description="",
    label="< Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton1_17 = Button(
    name="actionButton1",
    description="",
    label="Delete all workflows",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
container1_11 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton1_17},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
datagrid21_3_col_0 = ExpressionColumn(label="Workflow name", expression="Name")
datagrid21_3_col_1 = ExpressionColumn(label="State", expression="State")
datagrid21_3_col_2 = ExpressionColumn(label="Due by", expression="DueDate")
datagrid21_3_col_3 = ExpressionColumn(label="Started on", expression="StartTime")
datagrid21_3_col_4 = ExpressionColumn(label=" ", expression="Name")
datagrid21_3 = Table(
    name="dataGrid21",
    show_header=True,
    striped_rows=False,
    show_pagination=True,
    rows_per_page=10,
    action_buttons=False,
    columns=[datagrid21_3_col_0, datagrid21_3_col_1, datagrid21_3_col_2, datagrid21_3_col_3, datagrid21_3_col_4],
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container32_1 = ViewContainer(
    name="container32",
    description="",
    view_elements={datagrid21_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-content"]
)
label49_1 = Text(
    name="label49",
    content="Workflows",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-title"]
)
container39_1 = ViewContainer(
    name="container39",
    description="",
    view_elements={container32_1, label49_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text41_2 = Text(
    name="text41",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
dataview1_13 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton7_6, container1_11, container39_1, text41_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
workflowdefinition_view.view_elements = {dataview1_13}
workflowdefinition_view_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
workflowdefinition_view.layout = workflowdefinition_view_layout

# Button events and transitions (written after all screens defined to avoid forward references)
actionbutton1_4.targetScreen = newrequest_step2
actionbutton2_5.targetScreen = newrequest_step3
actionbutton3.targetScreen = newrequest_step1
actionbutton3_1.targetScreen = newrequest_step2
actionbutton3_3.targetScreen = product_newedit
actionbutton5_3.targetScreen = purchaseorder_edit

purchaseapprovals = Module(
    name="PurchaseApprovals",
    screens={admin_homepage, admin_workflow_dashboard, admin_workflow_instanceoverview, admin_workflow_instance_view, admin_workflow_overview, attachment_newedit, mendixssouseroverview, mendixssouser_newedit, myrequests, newrequest_step1, newrequest_step2, newrequest_step3, productline_edit_pocreator, productline_edit_receiver, productline_newedit, product_newedit, product_overview, product_select, product_selectvendors, purchaseorder_edit, taskinbox, task_approver, task_invoiceprocessor, task_pocreator, task_receiver, userrole_select, vendor_newedit, vendor_overview, vendor_select, vendor_selectproduct, workflowdefinition_view}
)

# GUI Model
gui_model = GUIModel(
    name="PurchaseApprovals",
    package="",
    versionCode="",
    versionName="",
    modules={purchaseapprovals},
    description=""
)

# Bound-entity data bindings resolved by the Mendix parser
t_innerdataview_form.data_binding = DataBinding(domain_concept=Request)
dataview5_form.data_binding = DataBinding(domain_concept=Attachment)
dataview6_form.data_binding = DataBinding(domain_concept=MendixSSOUser)
listview3.data_binding = DataBinding(domain_concept=ProductLine)
listview6.data_binding = DataBinding(domain_concept=Attachment)
listview1.data_binding = DataBinding(domain_concept=Request)
listview6_1.data_binding = DataBinding(domain_concept=Attachment)
dataview6_form_1.data_binding = DataBinding(domain_concept=Request)
listview1_1.data_binding = DataBinding(domain_concept=ProductLine)
listview6_2.data_binding = DataBinding(domain_concept=Attachment)
dataview6_form_2.data_binding = DataBinding(domain_concept=Request)
listview1_2.data_binding = DataBinding(domain_concept=ProductLine)
dataview6_form_3.data_binding = DataBinding(domain_concept=ProductLine)
dataview1_form.data_binding = DataBinding(domain_concept=ProductLine)
dataview6_form_4.data_binding = DataBinding(domain_concept=Product)
listview1_3.data_binding = DataBinding(domain_concept=Product)
listview1_4.data_binding = DataBinding(domain_concept=Vendor)
listview1_5.data_binding = DataBinding(domain_concept=PurchaseOrder)
listview1_6.data_binding = DataBinding(domain_concept=ProductLine)
listview1_7.data_binding = DataBinding(domain_concept=ProductLine)
listview2.data_binding = DataBinding(domain_concept=PurchaseOrder)
listview1_8.data_binding = DataBinding(domain_concept=PurchaseOrder)
dataview6_form_5.data_binding = DataBinding(domain_concept=Vendor)
listview1_9.data_binding = DataBinding(domain_concept=Vendor)
listview1_10.data_binding = DataBinding(domain_concept=Product)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="B-UML project generated by BESSER Migration Hub.")
project = Project(
    name="PurchaseApprovals",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
