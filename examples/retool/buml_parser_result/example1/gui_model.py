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
Books = Class(name="Books")
DiscountCodes = Class(name="DiscountCodes")
Orders = Class(name="Orders")

# Books class attributes and methods
Books_id: Property = Property(name="id", type=IntegerType, is_id=True)
Books_isbn: Property = Property(name="isbn", type=IntegerType)
Books_title: Property = Property(name="title", type=StringType)
Books_author: Property = Property(name="author", type=StringType)
Books_category: Property = Property(name="category", type=StringType)
Books_price: Property = Property(name="price", type=FloatType)
Books_cover_image: Property = Property(name="cover_image", type=StringType)
Books_bookshelf: Property = Property(name="bookshelf", type=StringType)
Books_quantity_in_stock: Property = Property(name="quantity_in_stock", type=IntegerType)
Books.attributes={Books_author, Books_bookshelf, Books_category, Books_cover_image, Books_id, Books_isbn, Books_price, Books_quantity_in_stock, Books_title}

# DiscountCodes class attributes and methods
DiscountCodes_id: Property = Property(name="id", type=IntegerType, is_id=True)
DiscountCodes_discount_code: Property = Property(name="discount_code", type=StringType)
DiscountCodes_discount_percent: Property = Property(name="discount_percent", type=IntegerType)
DiscountCodes.attributes={DiscountCodes_discount_code, DiscountCodes_discount_percent, DiscountCodes_id}

# Orders class attributes and methods
Orders_id: Property = Property(name="id", type=IntegerType, is_id=True)
Orders_total_amount: Property = Property(name="total_amount", type=FloatType)
Orders.attributes={Orders_id, Orders_total_amount}

# Relationships
Orders_Books: BinaryAssociation = BinaryAssociation(
    name="Orders_Books",
    ends={
        Property(name="orders", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="book", type=Books, multiplicity=Multiplicity(0, 1))
    }
)
Orders_DiscountCodes: BinaryAssociation = BinaryAssociation(
    name="Orders_DiscountCodes",
    ends={
        Property(name="orders", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="discount_code", type=DiscountCodes, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example1",
    types={Books, DiscountCodes, Orders},
    associations={Orders_Books, Orders_DiscountCodes},
    generalizations={},
    metadata=None
)


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

# Module: example1

# Screen: Books
books = Screen(name="Books", description="", view_elements=set(), is_main_page=True, route_path="/Books", screen_size="Medium")
books.view_elements = set()


# Screen: Books_Add_Books
books_add_books = Screen(name="Books_Add_Books", description="", view_elements=set(), is_main_page=True, route_path="/Books_Add_Books", screen_size="Medium")
button9 = Button(
    name="button9",
    description="",
    label="Search Internet",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod
)
onlinebooksearchresultstable_add_to_inventory = Button(
    name="onlineBookSearchResultsTable_Add_to_Inventory",
    description="",
    label="Add to Inventory",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
onlinebooksearchresultstable_list_source_0 = DataSourceElement(name="onlineBookSearchResults")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
onlinebooksearchresultstable_list_source_0_domain = None
onlinebooksearchresultstable_list_source_0.field_names = ['score', 'title', 'author_name', 'edition_count', 'first_publish_year', 'isbn', 'cover_i', 'ia', 'subject', 'edition_key']
onlinebooksearchresultstable_list = DataList(name="onlineBookSearchResultsTable_List", description="", list_sources={onlinebooksearchresultstable_list_source_0})
searchbookonlinetextinput = InputField(
    name="searchBookOnlineTextInput",
    description="",
    field_type=InputFieldType.Text,
    label="Search by title, author, category, ISBN",
    placeholder="Search inventory"
)
books_add_books.view_elements = {button9, onlinebooksearchresultstable_add_to_inventory, onlinebooksearchresultstable_list, searchbookonlinetextinput}


# Screen: Books_Search_Store_Inventory
books_search_store_inventory = Screen(name="Books_Search_Store_Inventory", description="", view_elements=set(), is_main_page=True, route_path="/Books_Search_Store_Inventory", screen_size="Medium")
booksinventorytable_checkout = Button(
    name="booksInventoryTable_Checkout",
    description="",
    label="Checkout",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
booksinventorytable_list_source_0 = DataSourceElement(name="books")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
booksinventorytable_list_source_0_domain = None
if domain_model_ref is not None:
    booksinventorytable_list_source_0_domain = domain_model_ref.get_class_by_name("Books")
if booksinventorytable_list_source_0_domain:
    booksinventorytable_list_source_0.dataSourceClass = booksinventorytable_list_source_0_domain
    booksinventorytable_list_source_0.field_names = ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'book_id', 'created_at', 'last_updated_at']
    booksinventorytable_list_source_0.fields = set(attr for attr in booksinventorytable_list_source_0_domain.attributes if attr.name in ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'book_id', 'created_at', 'last_updated_at'])
else:
    # Domain class 'Books' not resolved for data source 'books'.
    booksinventorytable_list_source_0.field_names = ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'book_id', 'created_at', 'last_updated_at']
booksinventorytable_list = DataList(name="booksInventoryTable_List", description="", list_sources={booksinventorytable_list_source_0})
button10 = Button(
    name="button10",
    description="",
    label="Refresh Table ({{booksInventoryTable.data.title.length}} Records)",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod
)
button8 = Button(
    name="button8",
    description="",
    label="Delete Book",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
containertitle1 = Text(name="containerTitle1", content="#### Store Inventory", description="")
author = InputField(
    name="author",
    description="",
    field_type=InputFieldType.Text,
    label="Author",
    placeholder="Enter value",
    required=True
)
book_id = InputField(
    name="book_id",
    description="",
    field_type=InputFieldType.Text,
    label="Book ID",
    placeholder="Enter value",
    required=True
)
quantity_in_stock = InputField(
    name="quantity_in_stock",
    description="",
    field_type=InputFieldType.Number,
    label="Quantity in stock",
    placeholder="Enter value",
    required=True
)
bookshelf = InputField(
    name="bookshelf",
    description="",
    field_type=InputFieldType.Text,
    label="Bookshelf",
    placeholder="Enter value",
    required=True
)
title = InputField(
    name="title",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    placeholder="Enter value",
    required=True
)
isbn = InputField(
    name="isbn",
    description="",
    field_type=InputFieldType.Text,
    label="Isbn",
    placeholder="Enter value",
    required=True
)
price = InputField(
    name="price",
    description="",
    field_type=InputFieldType.Number,
    label="Price",
    placeholder="Enter value",
    required=True
)
category = InputField(
    name="category",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Category",
    placeholder="Select an option",
    required=True
)
cover_image = InputField(
    name="cover_image",
    description="",
    field_type=InputFieldType.Text,
    label="Cover image",
    placeholder="Enter value",
    required=True
)
form5 = Form(name="form5", description="updateBook", inputFields={author, book_id, quantity_in_stock, bookshelf, title, isbn, price, category, cover_image})
formtitle6 = Text(name="formTitle6", content="#### {{booksInventoryTable.selectedRow.data.title}}", description="")
image3 = Image(name="image3", description="", source="{{booksInventoryTable.selectedRow.data.cover_image}}")
searchinventorytextinput = InputField(
    name="searchInventoryTextInput",
    description="",
    field_type=InputFieldType.Text,
    label="Search by title, author, category, ISBN",
    placeholder="Search by title, author, category, ISBN"
)
books_search_store_inventory.view_elements = {booksinventorytable_checkout, booksinventorytable_list, button10, button8, containertitle1, form5, formtitle6, image3, searchinventorytextinput}


# Screen: Discount_Codes
discount_codes = Screen(name="Discount_Codes", description="", view_elements=set(), is_main_page=True, route_path="/Discount_Codes", screen_size="Medium")
discountcodestable_delete = Button(
    name="discountCodesTable_Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
discountcodestable_list_source_0 = DataSourceElement(name="discount_codes")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
discountcodestable_list_source_0_domain = None
if domain_model_ref is not None:
    discountcodestable_list_source_0_domain = domain_model_ref.get_class_by_name("DiscountCodes")
if discountcodestable_list_source_0_domain:
    discountcodestable_list_source_0.dataSourceClass = discountcodestable_list_source_0_domain
    discountcodestable_list_source_0.field_names = ['discount_percent', 'discount_code', 'id']
    discountcodestable_list_source_0.fields = set(attr for attr in discountcodestable_list_source_0_domain.attributes if attr.name in ['discount_percent', 'discount_code', 'id'])
else:
    # Domain class 'DiscountCodes' not resolved for data source 'discount_codes'.
    discountcodestable_list_source_0.field_names = ['discount_percent', 'discount_code', 'id']
discountcodestable_list = DataList(name="discountCodesTable_List", description="", list_sources={discountcodestable_list_source_0})
discount_code = InputField(
    name="discount_code",
    description="",
    field_type=InputFieldType.Text,
    label="Discount code",
    placeholder="Enter value",
    required=True
)
is_active = InputField(
    name="is_active",
    description="",
    field_type=InputFieldType.Checkbox,
    label="Is active"
)
expiration_date = InputField(
    name="expiration_date",
    description="",
    field_type=InputFieldType.Date,
    label="Expiration date",
    required=True,
    default_value="{{ new Date() }}"
)
discount_percent = InputField(
    name="discount_percent",
    description="",
    field_type=InputFieldType.Number,
    label="Discount percent",
    placeholder="Enter value",
    required=True
)
form3 = Form(name="form3", description="addDiscountCode", inputFields={discount_code, is_active, expiration_date, discount_percent})
formtitle4 = Text(name="formTitle4", content="#### Form title", description="")
discount_codes.view_elements = {discountcodestable_delete, discountcodestable_list, form3, formtitle4}


# Screen: Inventory_Report
inventory_report = Screen(name="Inventory_Report", description="", view_elements=set(), is_main_page=True, route_path="/Inventory_Report", screen_size="Medium")
table2_list_source_0 = DataSourceElement(name="books")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table2_list_source_0_domain = None
if domain_model_ref is not None:
    table2_list_source_0_domain = domain_model_ref.get_class_by_name("Books")
if table2_list_source_0_domain:
    table2_list_source_0.dataSourceClass = table2_list_source_0_domain
    table2_list_source_0.field_names = ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf']
    table2_list_source_0.fields = set(attr for attr in table2_list_source_0_domain.attributes if attr.name in ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf'])
else:
    # Domain class 'Books' not resolved for data source 'books'.
    table2_list_source_0.field_names = ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf']
table2_list = DataList(name="table2_List", description="", list_sources={table2_list_source_0})
table3_list_source_0 = DataSourceElement(name="books")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table3_list_source_0_domain = None
if domain_model_ref is not None:
    table3_list_source_0_domain = domain_model_ref.get_class_by_name("Books")
if table3_list_source_0_domain:
    table3_list_source_0.dataSourceClass = table3_list_source_0_domain
    table3_list_source_0.field_names = ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf']
    table3_list_source_0.fields = set(attr for attr in table3_list_source_0_domain.attributes if attr.name in ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf'])
else:
    # Domain class 'Books' not resolved for data source 'books'.
    table3_list_source_0.field_names = ['id', 'author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf']
table3_list = DataList(name="table3_List", description="", list_sources={table3_list_source_0})
text7 = Text(name="text7", content="## In Stock", description="")
text8 = Text(name="text8", content="## Out Of Stock", description="")
inventory_report.view_elements = {table2_list, table3_list, text7, text8}


# Screen: Orders
orders = Screen(name="Orders", description="", view_elements=set(), is_main_page=True, route_path="/Orders", screen_size="Medium")
orderstable_delete = Button(
    name="ordersTable_Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
orderstable_list_source_0 = DataSourceElement(name="books")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
orderstable_list_source_0_domain = None
if domain_model_ref is not None:
    orderstable_list_source_0_domain = domain_model_ref.get_class_by_name("Books")
if orderstable_list_source_0_domain:
    orderstable_list_source_0.dataSourceClass = orderstable_list_source_0_domain
    orderstable_list_source_0.field_names = ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'order_id', 'book_id', 'created_at', 'last_updated_at', 'total_amount', 'discount_code_id', 'discount_code', 'discount_percent', 'order_date', 'expiration_date', 'is_active']
    orderstable_list_source_0.fields = set(attr for attr in orderstable_list_source_0_domain.attributes if attr.name in ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'order_id', 'book_id', 'created_at', 'last_updated_at', 'total_amount', 'discount_code_id', 'discount_code', 'discount_percent', 'order_date', 'expiration_date', 'is_active'])
else:
    # Domain class 'Books' not resolved for data source 'books'.
    orderstable_list_source_0.field_names = ['author', 'isbn', 'category', 'cover_image', 'price', 'quantity_in_stock', 'title', 'bookshelf', 'order_id', 'book_id', 'created_at', 'last_updated_at', 'total_amount', 'discount_code_id', 'discount_code', 'discount_percent', 'order_date', 'expiration_date', 'is_active']
orderstable_list = DataList(name="ordersTable_List", description="", list_sources={orderstable_list_source_0})
orders.view_elements = {orderstable_delete, orderstable_list}


# Screen: Sales_Reports
sales_reports = Screen(name="Sales_Reports", description="", view_elements=set(), is_main_page=True, route_path="/Sales_Reports", screen_size="Medium")
popularbookstable_list_source_0 = DataSourceElement(name="books")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
popularbookstable_list_source_0_domain = None
if domain_model_ref is not None:
    popularbookstable_list_source_0_domain = domain_model_ref.get_class_by_name("Books")
if popularbookstable_list_source_0_domain:
    popularbookstable_list_source_0.dataSourceClass = popularbookstable_list_source_0_domain
    popularbookstable_list_source_0.field_names = ['author', 'title', 'total_sales', 'discount_code', 'discount_percent', 'total_books_sold']
    popularbookstable_list_source_0.fields = set(attr for attr in popularbookstable_list_source_0_domain.attributes if attr.name in ['author', 'title', 'total_sales', 'discount_code', 'discount_percent', 'total_books_sold'])
else:
    # Domain class 'Books' not resolved for data source 'books'.
    popularbookstable_list_source_0.field_names = ['author', 'title', 'total_sales', 'discount_code', 'discount_percent', 'total_books_sold']
popularbookstable_list = DataList(name="PopularBooksTable_List", description="", list_sources={popularbookstable_list_source_0})
chart1 = BarChart(
    name="chart1",
    bar_width=30,
    orientation="vertical",
    show_grid=True,
    show_legend=True,
    show_tooltip=True,
    stacked=False,
    animate=True,
    legend_position="top",
    grid_color="#e0e0e0",
    bar_gap=4
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
chart1_binding_domain = None
if domain_model_ref is not None:
    chart1_binding_domain = domain_model_ref.get_class_by_name("Orders")
if chart1_binding_domain:
    chart1_binding = DataBinding(domain_concept=chart1_binding_domain, name="OrdersDataBinding")
else:
    # Domain class 'Orders' not resolved; data binding skipped.
    chart1_binding = None
if chart1_binding:
    chart1.data_binding = chart1_binding
chart2 = PieChart(
    name="chart2",
    show_legend=True,
    legend_position=Alignment.LEFT,
    show_labels=True,
    label_position=Alignment.INSIDE,
    padding_angle=0,
    inner_radius=0,
    outer_radius=80,
    start_angle=0,
    end_angle=360
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
chart2_binding_domain = None
if domain_model_ref is not None:
    chart2_binding_domain = domain_model_ref.get_class_by_name("Books")
if chart2_binding_domain:
    chart2_binding = DataBinding(domain_concept=chart2_binding_domain, name="BooksDataBinding")
    chart2_binding.label_field = next((attr for attr in chart2_binding_domain.attributes if attr.name == "title"), None)
else:
    # Domain class 'Books' not resolved; data binding skipped.
    chart2_binding = None
if chart2_binding:
    chart2.data_binding = chart2_binding
chart3 = BarChart(
    name="chart3",
    bar_width=30,
    orientation="vertical",
    show_grid=True,
    show_legend=True,
    show_tooltip=True,
    stacked=False,
    animate=True,
    legend_position="top",
    grid_color="#e0e0e0",
    bar_gap=4
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
chart3_binding_domain = None
if domain_model_ref is not None:
    chart3_binding_domain = domain_model_ref.get_class_by_name("Orders")
if chart3_binding_domain:
    chart3_binding = DataBinding(domain_concept=chart3_binding_domain, name="OrdersDataBinding")
else:
    # Domain class 'Orders' not resolved; data binding skipped.
    chart3_binding = None
if chart3_binding:
    chart3.data_binding = chart3_binding
chart4 = BarChart(
    name="chart4",
    bar_width=30,
    orientation="vertical",
    show_grid=True,
    show_legend=True,
    show_tooltip=True,
    stacked=False,
    animate=True,
    legend_position="top",
    grid_color="#e0e0e0",
    bar_gap=4
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
chart4_binding_domain = None
if domain_model_ref is not None:
    chart4_binding_domain = domain_model_ref.get_class_by_name("Books")
if chart4_binding_domain:
    chart4_binding = DataBinding(domain_concept=chart4_binding_domain, name="BooksDataBinding")
    chart4_binding.label_field = next((attr for attr in chart4_binding_domain.attributes if attr.name == "category"), None)
else:
    # Domain class 'Books' not resolved; data binding skipped.
    chart4_binding = None
if chart4_binding:
    chart4.data_binding = chart4_binding
reportdaterange = InputField(
    name="reportDateRange",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Data Date Range",
    placeholder="Select an option",
    default_value="24 hours",
    options=[SelectOption(value="24 hours", label="24 hours"), SelectOption(value="7 days", label="7 days"), SelectOption(value="30 days", label="30 days")]
)
table1_list_source_0 = DataSourceElement(name="orders")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
table1_list_source_0_domain = None
if domain_model_ref is not None:
    table1_list_source_0_domain = domain_model_ref.get_class_by_name("Orders")
if table1_list_source_0_domain:
    table1_list_source_0.dataSourceClass = table1_list_source_0_domain
    table1_list_source_0.field_names = ['total_amount', 'id']
    table1_list_source_0.fields = set(attr for attr in table1_list_source_0_domain.attributes if attr.name in ['total_amount', 'id'])
else:
    # Domain class 'Orders' not resolved for data source 'orders'.
    table1_list_source_0.field_names = ['total_amount', 'id']
table1_list = DataList(name="table1_List", description="", list_sources={table1_list_source_0})
text4 = Text(name="text4", content="## Overview Sales Report", description="")
text5 = Text(name="text5", content="## Top Selling Books", description="")
text6 = Text(name="text6", content="## Discount Code Report", description="")
sales_reports.view_elements = {popularbookstable_list, chart1, chart2, chart3, chart4, reportdaterange, table1_list, text4, text5, text6}


# Screen: checkoutModal
checkoutmodal = Screen(name="checkoutModal", description="", view_elements=set(), route_path="/checkoutModal", screen_size="Medium")
button11 = Button(
    name="button11",
    description="",
    label="Checkout",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
image4 = Image(name="image4", description="", source="{{booksInventoryTable.selectedRow.data.cover_image}}")
select10 = InputField(
    name="select10",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Discount Code",
    placeholder="Select an option"
)
text2 = Text(name="text2", content="#### {{booksInventoryTable.selectedRow.data.title}}", description="")
text3 = Text(name="text3", content="###### by {{booksInventoryTable.selectedRow.data.author}}", description="")
textinput30 = InputField(
    name="textInput30",
    description="",
    field_type=InputFieldType.Text,
    label="Price",
    placeholder="Enter value",
    default_value="{{booksInventoryTable.selectedRow.data.price}}"
)
textinput31 = InputField(
    name="textInput31",
    description="",
    field_type=InputFieldType.Text,
    label="Discount Percent",
    placeholder="Enter value",
    default_value="{{getDiscountPercent.data.discount_percent[\'0\']*100}}"
)
textinput32 = InputField(
    name="textInput32",
    description="",
    field_type=InputFieldType.Text,
    label="Total",
    placeholder="Enter value",
    default_value="{{calculateCheckoutTotal.value}}"
)
textinput33 = InputField(
    name="textInput33",
    description="",
    field_type=InputFieldType.Text,
    label="Discount Code ID",
    placeholder="Enter value",
    default_value="{{getDiscountPercent.data.discount_code_id[\'0\']}}"
)
checkoutmodal.view_elements = {button11, image4, select10, text2, text3, textinput30, textinput31, textinput32, textinput33}


# Screen: example1_Main
example1_main = Screen(name="example1_Main", description="", view_elements=set(), is_main_page=True, route_path="/example1_Main", screen_size="Medium")
text1 = Text(name="text1", content="## New York\'s Best Small Bookstore", description="")
example1_main.view_elements = {text1}


# Screen: modal1
modal1 = Screen(name="modal1", description="", view_elements=set(), route_path="/modal1", screen_size="Medium")
quantity_in_stock_1 = InputField(
    name="quantity_in_stock",
    description="",
    field_type=InputFieldType.Number,
    label="Quantity in stock",
    placeholder="Enter value",
    required=True
)
price_1 = InputField(
    name="price",
    description="",
    field_type=InputFieldType.Number,
    label="Price",
    placeholder="Enter value",
    required=True,
    default_value=""
)
isbn_1 = InputField(
    name="isbn",
    description="",
    field_type=InputFieldType.Dropdown,
    label="ISBN",
    placeholder="Choose an ISBN"
)
author_1 = InputField(
    name="author",
    description="",
    field_type=InputFieldType.Text,
    label="Author",
    placeholder="Enter value",
    required=True,
    default_value="{{onlineBookSearchResultsTable.selectedRow.data.author_name[\'0\']}}"
)
cover_image_1 = InputField(
    name="cover_image",
    description="",
    field_type=InputFieldType.Text,
    label="Cover image",
    placeholder="Enter value",
    default_value="https://covers.openlibrary.org/b/id/{{onlineBookSearchResultsTable.selectedRow.data.cover_i}}.jpg"
)
created_at = InputField(
    name="created_at",
    description="",
    field_type=InputFieldType.DateTime,
    label="Created at",
    required=True,
    default_value="{{ new Date() }}"
)
category_1 = InputField(
    name="category",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Category",
    placeholder="Select a Category",
    required=True
)
last_updated_at = InputField(
    name="last_updated_at",
    description="",
    field_type=InputFieldType.DateTime,
    label="Last updated at",
    required=True,
    default_value="{{ new Date() }}"
)
book_id_1 = InputField(
    name="book_id",
    description="",
    field_type=InputFieldType.Text,
    label="Book ID",
    placeholder="Enter value",
    required=True,
    default_value="{{formatDataAsArray(getBooksDataForModal.data).length + 1}} "
)
bookshelf_1 = InputField(
    name="bookshelf",
    description="",
    field_type=InputFieldType.Text,
    label="Bookshelf",
    placeholder="Bookshelf Name"
)
title_1 = InputField(
    name="title",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    placeholder="Enter value",
    required=True,
    default_value="{{onlineBookSearchResultsTable.selectedRow.data.title}}"
)
form4 = Form(name="form4", description="addBookFromModal", inputFields={quantity_in_stock_1, price_1, isbn_1, author_1, cover_image_1, created_at, category_1, last_updated_at, book_id_1, bookshelf_1, title_1})
formtitle5 = Text(name="formTitle5", content="#### {{onlineBookSearchResultsTable.selectedRow.data.title}} by {{onlineBookSearchResultsTable.selectedRow.data.author_name}}", description="")
image2 = Image(name="image2", description="", source="https://covers.openlibrary.org/b/id/{{onlineBookSearchResultsTable.selectedRow.data.cover_i}}.jpg")
modal1.view_elements = {form4, formtitle5, image2}

example1 = Module(
    name="example1",
    screens={books, books_add_books, books_search_store_inventory, discount_codes, inventory_report, orders, sales_reports, checkoutmodal, example1_main, modal1}
)

# GUI Model
gui_model = GUIModel(
    name="example1",
    package="",
    versionCode="",
    versionName="",
    modules={example1},
    description=""
)
