##############
# GUI MODEL  #
##############

from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement, GUIModel, Module, Screen,
)

from buml_data_model import (
    Product, Product_identifier, Product_name,
    WebUser, WebUser_loginId, WebUser_password, WebUser_state,
    Customer, Customer_customerId, Customer_email, Customer_phone, Customer_address,
    ShoppingCart, ShoppingCart_created,
    Account, Account_accountId, Account_billingAddress,
    Account_isClosed, Account_openDate, Account_closedDate,
    Order, Order_orderNumber, Order_orderedDate, Order_shippedDate,
    Order_ship_to, Order_status, Order_total,
    LineItem, LineItem_quantity, LineItem_price,
    Payment, Payment_paymentId, Payment_paidDate, Payment_total, Payment_details,
)

# ------------------------------------------------------------------
# List screens  (one per entity — matches generated APEX pages)
# ------------------------------------------------------------------

ProductScreen = Screen(
    name="Product", description="List of products",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
WebUserScreen = Screen(
    name="WebUser", description="List of web users",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
CustomerScreen = Screen(
    name="Customer", description="List of customers",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
ShoppingCartScreen = Screen(
    name="ShoppingCart", description="List of shopping carts",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
AccountScreen = Screen(
    name="Account", description="List of accounts",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
OrderScreen = Screen(
    name="Order", description="List of orders",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
LineItemScreen = Screen(
    name="LineItem", description="List of line items",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
PaymentScreen = Screen(
    name="Payment", description="List of payments",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)

# ------------------------------------------------------------------
# Home screen with navigation buttons
# ------------------------------------------------------------------

btn_nav_product      = Button(name="Nav_Product",      label="Product",      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=ProductScreen)
btn_nav_webuser      = Button(name="Nav_WebUser",      label="WebUser",      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=WebUserScreen)
btn_nav_customer     = Button(name="Nav_Customer",     label="Customer",     buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=CustomerScreen)
btn_nav_shoppingcart = Button(name="Nav_ShoppingCart", label="ShoppingCart", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=ShoppingCartScreen)
btn_nav_account      = Button(name="Nav_Account",      label="Account",      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=AccountScreen)
btn_nav_order        = Button(name="Nav_Order",        label="Order",        buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=OrderScreen)
btn_nav_lineitem     = Button(name="Nav_LineItem",     label="LineItem",     buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=LineItemScreen)
btn_nav_payment      = Button(name="Nav_Payment",      label="Payment",      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=PaymentScreen)

HomeScreen = Screen(
    name="Home_Web", description="Shopping Management – Home",
    x_dpi="", y_dpi="", screen_size="Small", is_main_page=True,
    view_elements={
        btn_nav_product, btn_nav_webuser, btn_nav_customer,
        btn_nav_shoppingcart, btn_nav_account, btn_nav_order,
        btn_nav_lineitem, btn_nav_payment,
    },
)

# ------------------------------------------------------------------
# Data sources
# ------------------------------------------------------------------

ds_product = DataSourceElement(
    name="Product", dataSourceClass=Product,
    fields={Product_identifier, Product_name},
)
ds_webuser = DataSourceElement(
    name="WebUser", dataSourceClass=WebUser,
    fields={WebUser_loginId, WebUser_password, WebUser_state},
)
ds_customer = DataSourceElement(
    name="Customer", dataSourceClass=Customer,
    fields={Customer_customerId, Customer_email, Customer_phone, Customer_address},
)
ds_shoppingcart = DataSourceElement(
    name="ShoppingCart", dataSourceClass=ShoppingCart,
    fields={ShoppingCart_created},
)
ds_account = DataSourceElement(
    name="Account", dataSourceClass=Account,
    fields={
        Account_accountId, Account_billingAddress,
        Account_isClosed, Account_openDate, Account_closedDate,
    },
)
ds_order = DataSourceElement(
    name="Order", dataSourceClass=Order,
    fields={
        Order_orderNumber, Order_orderedDate, Order_shippedDate,
        Order_ship_to, Order_status, Order_total,
    },
)
ds_lineitem = DataSourceElement(
    name="LineItem", dataSourceClass=LineItem,
    fields={LineItem_quantity, LineItem_price},
)
ds_payment = DataSourceElement(
    name="Payment", dataSourceClass=Payment,
    fields={Payment_paymentId, Payment_paidDate, Payment_total, Payment_details},
)

# ------------------------------------------------------------------
# Data lists
# ------------------------------------------------------------------

list_product      = DataList(name="ProductList",      description="", list_sources={ds_product})
list_webuser      = DataList(name="WebUserList",      description="", list_sources={ds_webuser})
list_customer     = DataList(name="CustomerList",     description="", list_sources={ds_customer})
list_shoppingcart = DataList(name="ShoppingCartList", description="", list_sources={ds_shoppingcart})
list_account      = DataList(name="AccountList",      description="", list_sources={ds_account})
list_order        = DataList(name="OrderList",        description="", list_sources={ds_order})
list_lineitem     = DataList(name="LineItemList",     description="", list_sources={ds_lineitem})
list_payment      = DataList(name="PaymentList",      description="", list_sources={ds_payment})

# ------------------------------------------------------------------
# Add buttons per entity screen
# ------------------------------------------------------------------

btn_add_product      = Button(name="Add_Product",      label="Add Product",      buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_webuser      = Button(name="Add_WebUser",      label="Add WebUser",      buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_customer     = Button(name="Add_Customer",     label="Add Customer",     buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_shoppingcart = Button(name="Add_ShoppingCart", label="Add ShoppingCart", buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_account      = Button(name="Add_Account",      label="Add Account",      buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_order        = Button(name="Add_Order",        label="Add Order",        buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_lineitem     = Button(name="Add_LineItem",     label="Add LineItem",     buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_payment      = Button(name="Add_Payment",      label="Add Payment",      buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")

# Wire view elements
ProductScreen.view_elements      = {list_product,      btn_add_product}
WebUserScreen.view_elements      = {list_webuser,      btn_add_webuser}
CustomerScreen.view_elements     = {list_customer,     btn_add_customer}
ShoppingCartScreen.view_elements = {list_shoppingcart, btn_add_shoppingcart}
AccountScreen.view_elements      = {list_account,      btn_add_account}
OrderScreen.view_elements        = {list_order,        btn_add_order}
LineItemScreen.view_elements     = {list_lineitem,     btn_add_lineitem}
PaymentScreen.view_elements      = {list_payment,      btn_add_payment}

# ------------------------------------------------------------------
# Module & GUIModel
# ------------------------------------------------------------------

ShoppingModule = Module(
    name="MyFirstModule",
    screens={
        HomeScreen, ProductScreen, WebUserScreen, CustomerScreen,
        ShoppingCartScreen, AccountScreen, OrderScreen, LineItemScreen, PaymentScreen,
    },
)

shopping_gui_model = GUIModel(
    name="ShoppingManagement",
    package="com.example.shopping",
    versionCode="1",
    versionName="1.0",
    modules={ShoppingModule},
    description="Shopping management application migrated from Mendix to Oracle APEX via B-UML.",
)
