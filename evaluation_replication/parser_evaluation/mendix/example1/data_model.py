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

