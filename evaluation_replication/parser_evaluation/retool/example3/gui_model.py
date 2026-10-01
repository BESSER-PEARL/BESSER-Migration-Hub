import builtins as _evaluation_builtins
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
Products = Class(name="Products")

# Products class attributes and methods
Products_id: Property = Property(name="id", type=IntegerType, is_id=True)
Products_name: Property = Property(name="name", type=StringType)
Products_description: Property = Property(name="description", type=StringType)
Products_category: Property = Property(name="category", type=StringType)
Products_price: Property = Property(name="price", type=FloatType)
Products_created_at: Property = Property(name="created_at", type=DateTimeType)
Products.attributes={Products_category, Products_created_at, Products_description, Products_id, Products_name, Products_price}

# Domain Model
domain_model = DomainModel(
    name="example3",
    types={Products},
    associations={},
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

# Module: example3

# Screen: createModal
createmodal = Screen(name="createModal", description="", view_elements=set(), route_path="/createModal", screen_size="Medium")
description = InputField(
    name="description",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    placeholder="Enter description"
)
category = InputField(
    name="category",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Category",
    placeholder="Select category",
    required=True,
    options=[SelectOption(value="Electronics", label="Electronics"), SelectOption(value="Clothing", label="Clothing"), SelectOption(value="Books", label="Books")]
)
name = InputField(
    name="name",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    placeholder="Enter product name",
    required=True
)
createproductform = Form(name="CreateProductForm", description="insertProduct", inputFields={description, category, name})
createclearbtn = Button(
    name="createClearBtn",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod
)
createformtitle = Text(name="createFormTitle", content="#### New product", description="")
createmodal.view_elements = {createproductform, createclearbtn, createformtitle}


# Screen: editModal
editmodal = Screen(name="editModal", description="", view_elements=set(), route_path="/editModal", screen_size="Medium")
category_1 = InputField(
    name="category",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Category",
    placeholder="Select category",
    required=True,
    options=[SelectOption(value="Electronics", label="Electronics"), SelectOption(value="Clothing", label="Clothing"), SelectOption(value="Books", label="Books")]
)
name_1 = InputField(
    name="name",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    placeholder="Enter product name",
    required=True
)
description_1 = InputField(
    name="description",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    placeholder="Enter description"
)
editproductform = Form(name="EditProductForm", description="updateProduct", inputFields={category_1, name_1, description_1})
editcancelbtn = Button(
    name="editCancelBtn",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
edittitle = Text(name="editTitle", content="#### Edit product", description="")
editmodal.view_elements = {editproductform, editcancelbtn, edittitle}


# Screen: example3_Main
example3_main = Screen(name="example3_Main", description="", view_elements=set(), is_main_page=True, route_path="/example3_Main", screen_size="Medium")
a01a1 = Button(
    name="a01a1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
a02b2 = Button(
    name="a02b2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
pagetitle = Text(name="pageTitle", content="### Products", description="")
productstable_list_source_0 = DataSourceElement(name="products")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
productstable_list_source_0_domain = None
if domain_model_ref is not None:
    productstable_list_source_0_domain = domain_model_ref.get_class_by_name("Products")
if productstable_list_source_0_domain:
    productstable_list_source_0.dataSourceClass = productstable_list_source_0_domain
    productstable_list_source_0.field_names = ['price', 'category', 'name', 'id', 'created_at', 'description']
    productstable_list_source_0.fields = set(attr for attr in productstable_list_source_0_domain.attributes if attr.name in ['price', 'category', 'name', 'id', 'created_at', 'description'])
else:
    # Domain class 'Products' not resolved for data source 'products'.
    productstable_list_source_0.field_names = ['price', 'category', 'name', 'id', 'created_at', 'description']
productstable_list = DataList(name="productsTable_List", description="", list_sources={productstable_list_source_0})
setupguidebtn = Button(
    name="setupGuideBtn",
    description="",
    label="Setup Guide",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate
)
example3_main.view_elements = {a01a1, a02b2, pagetitle, productstable_list, setupguidebtn}


# Screen: setupGuideModal
setupguidemodal = Screen(name="setupGuideModal", description="", view_elements=set(), route_path="/setupGuideModal", screen_size="Medium")
setupguidetext = Text(name="setupGuideText", content="{{ \'Welcome! This app is loaded with **sample data** so you can click around and explore right away.\\n\\nWhen you are ready to wire up your real database, follow these steps:\\n\\n1. 🔌 **Connect your database** — Go to *Resources* in Retool and add your DB\\n2. 🔄 **Update queries** — Open each query in the bottom panel and switch the Resource\\n3. 📝 **Update table/column names** — Edit the SQL in each query to match your schema\\n4. 🧹 **Remove mock data** — In each Table/Select, remove the mock array fallback from the data attribute\\n5. 🗑️ **Delete this modal** — Remove this Setup Guide and the setupGuideBtn button\\n\\n✅ You are all set — happy building!\' }}", description="")
setupguidetitle = Text(name="setupGuideTitle", content="## 🚀 Setup Guide", description="")
setupguidemodal.view_elements = {setupguidetext, setupguidetitle}

# Button events and transitions (written after all screens defined to avoid forward references)
setupguidebtn_event_0_action_0 = Transition(name="setupGuideBtn_open_0", description="", target_screen=setupguidemodal)
setupguidebtn_event_0 = Event(name="setupGuideBtn_click_0", event_type=EventType.OnClick, actions={setupguidebtn_event_0_action_0})
setupguidebtn_event_0_action_0.triggered_by = setupguidebtn
setupguidebtn.events = {setupguidebtn_event_0}

example3 = Module(
    name="example3",
    screens={createmodal, editmodal, example3_main, setupguidemodal}
)

# GUI Model
gui_model = GUIModel(
    name="example3",
    package="",
    versionCode="",
    versionName="",
    modules={example3},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition
createproductform.title = '#### New product'
createproductform.submit_label = 'Create'
createproductform.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('Products'))
editproductform.title = None
editproductform.submit_label = 'Save'
editproductform.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('Products'))
productstable_list.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('Products'))
_evaluation_builtins.next(s for s in productstable_list.list_sources if s.name == 'products').field_names = ['id', 'name', 'description', 'category', 'price', 'created_at']
setupguidebtn.events = set()
setupguidebtn.events.add(Event(name='setupGuideBtn_click_0', event_type=EventType.OnClick, actions={Transition(name='setupGuideBtn_open_0', target_screen=_evaluation_builtins.next(s for m in gui_model.modules for s in m.screens if s.name == 'setupGuideModal'), triggered_by=setupguidebtn)}))
