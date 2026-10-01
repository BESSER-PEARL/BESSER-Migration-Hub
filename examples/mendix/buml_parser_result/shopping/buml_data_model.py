####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType, DateType,
)

# ------------------------------------------------------------------
# Enumerations
# ------------------------------------------------------------------

UserState = Enumeration(
    name="UserState",
    literals={
        EnumerationLiteral(name="Active"),
        EnumerationLiteral(name="Banned"),
        EnumerationLiteral(name="Blocked"),
        EnumerationLiteral(name="New"),
    },
)

OrderStatus = Enumeration(
    name="OrderStatus",
    literals={
        EnumerationLiteral(name="Closed"),
        EnumerationLiteral(name="Delivered"),
        EnumerationLiteral(name="Hold"),
        EnumerationLiteral(name="New"),
        EnumerationLiteral(name="Shipped"),
    },
)

# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------

WebUser = Class(name="WebUser")
Customer = Class(name="Customer")
Account = Class(name="Account")
ShoppingCart = Class(name="ShoppingCart")
Product = Class(name="Product")
Order = Class(name="Order")
LineItem = Class(name="LineItem")
Payment = Class(name="Payment")

# WebUser attributes
WebUser_loginId: Property = Property(name="loginId",   type=StringType)
WebUser_password: Property = Property(name="password", type=StringType)
WebUser_state: Property = Property(name="state",       type=UserState)
WebUser.attributes = {WebUser_loginId, WebUser_password, WebUser_state}

# Customer attributes
Customer_customerId: Property = Property(name="customerId", type=StringType)
Customer_email: Property = Property(name="email",           type=StringType)
Customer_phone: Property = Property(name="phone",           type=StringType)
Customer_address: Property = Property(name="address",       type=StringType)
Customer.attributes = {Customer_customerId, Customer_email, Customer_phone, Customer_address}

# Account attributes
Account_accountId: Property = Property(name="accountId",         type=StringType)
Account_billingAddress: Property = Property(name="billingAddress", type=StringType)
Account_isClosed: Property = Property(name="isClosed",           type=BooleanType)
Account_openDate: Property = Property(name="openDate",           type=DateType)
Account_closedDate: Property = Property(name="closedDate",       type=DateType)
Account.attributes = {
    Account_accountId, Account_billingAddress,
    Account_isClosed, Account_openDate, Account_closedDate,
}

# ShoppingCart attributes
ShoppingCart_created: Property = Property(name="created", type=DateType)
ShoppingCart.attributes = {ShoppingCart_created}

# Product attributes
Product_identifier: Property = Property(name="identifier", type=StringType)
Product_name: Property = Property(name="name",             type=StringType)
Product.attributes = {Product_identifier, Product_name}

# Order attributes
Order_orderNumber: Property = Property(name="orderNumber",   type=StringType)
Order_orderedDate: Property = Property(name="orderedDate",   type=DateType)
Order_shippedDate: Property = Property(name="shippedDate",   type=DateType)
Order_ship_to: Property = Property(name="ship_to",           type=StringType)
Order_status: Property = Property(name="status",             type=OrderStatus)
Order_total: Property = Property(name="total",               type=FloatType)
Order.attributes = {
    Order_orderNumber, Order_orderedDate, Order_shippedDate,
    Order_ship_to, Order_status, Order_total,
}

# LineItem attributes
LineItem_quantity: Property = Property(name="quantity", type=IntegerType)
LineItem_price: Property = Property(name="price",       type=FloatType)
LineItem.attributes = {LineItem_quantity, LineItem_price}

# Payment attributes
Payment_paymentId: Property = Property(name="paymentId", type=StringType)
Payment_paidDate: Property = Property(name="paidDate",   type=DateType)
Payment_total: Property = Property(name="total",         type=FloatType)
Payment_details: Property = Property(name="details",     type=StringType)
Payment.attributes = {Payment_paymentId, Payment_paidDate, Payment_total, Payment_details}

# ------------------------------------------------------------------
# Associations
# ------------------------------------------------------------------

# WebUser ↔ Customer  (1:1  –  Reference+Both)
WebUser_Customer: BinaryAssociation = BinaryAssociation(
    name="WebUser_Customer",
    ends={
        Property(name="webuser",  type=WebUser,  multiplicity=Multiplicity(1, 1)),
        Property(name="customer", type=Customer, multiplicity=Multiplicity(1, 1)),
    },
)

# Customer ↔ Account  (1:1  –  Reference+Both)
Customer_Account: BinaryAssociation = BinaryAssociation(
    name="Customer_Account",
    ends={
        Property(name="customer", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="account",  type=Account,  multiplicity=Multiplicity(1, 1)),
    },
)

# WebUser ↔ ShoppingCart  (1:1  –  Reference+Both)
WebUser_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="WebUser_ShoppingCart",
    ends={
        Property(name="webuser",      type=WebUser,      multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingcart", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
    },
)

# Account ↔ ShoppingCart  (1:1  –  Reference+Both)
Account_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="Account_ShoppingCart",
    ends={
        Property(name="account",      type=Account,      multiplicity=Multiplicity(1, 1)),
        Property(name="shoppingcart", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
    },
)

# Payment ↔ Account  (N:1  –  Reference)
Payment_Account: BinaryAssociation = BinaryAssociation(
    name="Payment_Account",
    ends={
        Property(name="payment", type=Payment, multiplicity=Multiplicity(0, "*")),
        Property(name="account", type=Account, multiplicity=Multiplicity(1, 1)),
    },
)

# Order ↔ Account  (N:1  –  Reference)
Order_Account: BinaryAssociation = BinaryAssociation(
    name="Order_Account",
    ends={
        Property(name="order",   type=Order,   multiplicity=Multiplicity(0, "*")),
        Property(name="account", type=Account, multiplicity=Multiplicity(1, 1)),
    },
)

# LineItem ↔ ShoppingCart  (N:1  –  Reference)
LineItem_ShoppingCart: BinaryAssociation = BinaryAssociation(
    name="LineItem_ShoppingCart",
    ends={
        Property(name="lineitem",     type=LineItem,     multiplicity=Multiplicity(0, "*")),
        Property(name="shoppingcart", type=ShoppingCart, multiplicity=Multiplicity(1, 1)),
    },
)

# LineItem ↔ Order  (N:1  –  Reference)
LineItem_Order: BinaryAssociation = BinaryAssociation(
    name="LineItem_Order",
    ends={
        Property(name="lineitem", type=LineItem, multiplicity=Multiplicity(0, "*")),
        Property(name="order",    type=Order,    multiplicity=Multiplicity(1, 1)),
    },
)

# Payment ↔ Order  (N:1  –  Reference)
Payment_Order: BinaryAssociation = BinaryAssociation(
    name="Payment_Order",
    ends={
        Property(name="payment", type=Payment, multiplicity=Multiplicity(0, "*")),
        Property(name="order",   type=Order,   multiplicity=Multiplicity(1, 1)),
    },
)

# LineItem ↔ Product  (N:1  –  Reference)
LineItem_Product: BinaryAssociation = BinaryAssociation(
    name="LineItem_Product",
    ends={
        Property(name="lineitem", type=LineItem, multiplicity=Multiplicity(0, "*")),
        Property(name="product",  type=Product,  multiplicity=Multiplicity(1, 1)),
    },
)

# ------------------------------------------------------------------
# Domain Model
# ------------------------------------------------------------------

shopping_domain_model = DomainModel(
    name="MyFirstModule",
    types={
        WebUser, Customer, Account, ShoppingCart,
        Product, Order, LineItem, Payment,
        UserState, OrderStatus,
    },
    associations={
        WebUser_Customer, Customer_Account,
        WebUser_ShoppingCart, Account_ShoppingCart,
        Payment_Account, Order_Account,
        LineItem_ShoppingCart, LineItem_Order, Payment_Order, LineItem_Product,
    },
    generalizations=set(),
)
