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
Inventory = Class(name="Inventory")

# Inventory class attributes and methods
Inventory_id: Property = Property(name="id", type=IntegerType, is_id=True)
Inventory_sku: Property = Property(name="sku", type=StringType)
Inventory_description: Property = Property(name="description", type=StringType)
Inventory_quantity: Property = Property(name="quantity", type=IntegerType)
Inventory_replenish: Property = Property(name="replenish", type=IntegerType)
Inventory_location: Property = Property(name="location", type=StringType)
Inventory_latitude: Property = Property(name="latitude", type=FloatType)
Inventory_longitude: Property = Property(name="longitude", type=FloatType)
Inventory_image_url: Property = Property(name="image_url", type=StringType)
Inventory.attributes={Inventory_description, Inventory_id, Inventory_image_url, Inventory_latitude, Inventory_location, Inventory_longitude, Inventory_quantity, Inventory_replenish, Inventory_sku}

# Domain Model
domain_model = DomainModel(
    name="example2",
    types={Inventory},
    associations={},
    generalizations={},
    metadata=None
)

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
Inventory = Class(name="Inventory")

# Inventory class attributes and methods
Inventory_id: Property = Property(name="id", type=IntegerType, is_id=True)
Inventory_sku: Property = Property(name="sku", type=StringType)
Inventory_description: Property = Property(name="description", type=StringType)
Inventory_quantity: Property = Property(name="quantity", type=IntegerType)
Inventory_replenish: Property = Property(name="replenish", type=IntegerType)
Inventory_location: Property = Property(name="location", type=StringType)
Inventory_latitude: Property = Property(name="latitude", type=FloatType)
Inventory_longitude: Property = Property(name="longitude", type=FloatType)
Inventory_image_url: Property = Property(name="image_url", type=StringType)
Inventory.attributes={Inventory_description, Inventory_id, Inventory_image_url, Inventory_latitude, Inventory_location, Inventory_longitude, Inventory_quantity, Inventory_replenish, Inventory_sku}

# Domain Model
domain_model = DomainModel(
    name="example2",
    types={Inventory},
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

# Module: example2

# Screen: addInventory
addinventory = Screen(name="addInventory", description="", view_elements=set(), is_main_page=True, route_path="/addInventory", screen_size="Medium")
containertitle1 = Text(name="containerTitle1", content="#### Add inventory", description="")
sku = InputField(
    name="sku",
    description="",
    field_type=InputFieldType.TextArea,
    label="SKU",
    placeholder="Enter value",
    required=True
)
image_url = InputField(
    name="image_url",
    description="",
    field_type=InputFieldType.Text,
    label="Image URL",
    placeholder="retool.com",
    required=True
)
description = InputField(
    name="description",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    placeholder="Enter value",
    required=True
)
location = InputField(
    name="location",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Location",
    placeholder="Select an option",
    required=True
)
quantity = InputField(
    name="quantity",
    description="",
    field_type=InputFieldType.Number,
    label="Quantity",
    placeholder="Enter value",
    required=True
)
replenish = InputField(
    name="replenish",
    description="",
    field_type=InputFieldType.Number,
    label="Replenish",
    placeholder="Enter value",
    required=True
)
form1 = Form(name="form1", description="form1SubmitToInventory", inputFields={sku, image_url, description, location, quantity, replenish})
formtitle1 = Text(name="formTitle1", content="#### Inventory item", description="")
addinventory.view_elements = {containertitle1, form1, formtitle1}


# Screen: inventory
inventory = Screen(name="inventory", description="", view_elements=set(), is_main_page=True, route_path="/inventory", screen_size="Medium")
inventory.view_elements = set()


# Screen: inventory_local
inventory_local = Screen(name="inventory_local", description="", view_elements=set(), is_main_page=True, route_path="/inventory_local", screen_size="Medium")
inventorytable_list_source_0 = DataSourceElement(name="inventory")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
inventorytable_list_source_0_domain = None
if domain_model_ref is not None:
    inventorytable_list_source_0_domain = domain_model_ref.get_class_by_name("Inventory")
if inventorytable_list_source_0_domain:
    inventorytable_list_source_0.dataSourceClass = inventorytable_list_source_0_domain
    inventorytable_list_source_0.field_names = ['replenish', 'description', 'latitude', 'sku', 'quantity', 'id', 'location', 'longitude', 'image_url']
    inventorytable_list_source_0.fields = set(attr for attr in inventorytable_list_source_0_domain.attributes if attr.name in ['replenish', 'description', 'latitude', 'sku', 'quantity', 'id', 'location', 'longitude', 'image_url'])
else:
    # Domain class 'Inventory' not resolved for data source 'inventory'.
    inventorytable_list_source_0.field_names = ['replenish', 'description', 'latitude', 'sku', 'quantity', 'id', 'location', 'longitude', 'image_url']
inventorytable_list = DataList(name="inventoryTable_List", description="", list_sources={inventorytable_list_source_0})
inventory_local.view_elements = {inventorytable_list}


# Screen: inventory_vendor
inventory_vendor = Screen(name="inventory_vendor", description="", view_elements=set(), is_main_page=True, route_path="/inventory_vendor", screen_size="Medium")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
localinventorychart_series_0_binding_domain = None
if domain_model_ref is not None:
    localinventorychart_series_0_binding_domain = domain_model_ref.get_class_by_name("Inventory")
if localinventorychart_series_0_binding_domain:
    localinventorychart_series_0_binding = DataBinding(domain_concept=localinventorychart_series_0_binding_domain, name="InventoryDataBinding")
    localinventorychart_series_0_binding.label_field = next((attr for attr in localinventorychart_series_0_binding_domain.attributes if attr.name == "sku"), None)
    localinventorychart_series_0_binding.data_field = next((attr for attr in localinventorychart_series_0_binding_domain.attributes if attr.name == "quantity"), None)
else:
    # Domain class 'Inventory' not resolved; data binding skipped.
    localinventorychart_series_0_binding = None
localinventorychart_series_0 = Series(name="Local_Inventory_Data", label="Local Inventory Data", data_binding=localinventorychart_series_0_binding, styling=None)
localinventorychart = BarChart(
    name="localInventoryChart",
    series=[localinventorychart_series_0],
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
vendorinventorychart_series_0_binding_domain = None
if domain_model_ref is not None:
    vendorinventorychart_series_0_binding_domain = domain_model_ref.get_class_by_name("Inventory")
if vendorinventorychart_series_0_binding_domain:
    vendorinventorychart_series_0_binding = DataBinding(domain_concept=vendorinventorychart_series_0_binding_domain, name="InventoryDataBinding")
    vendorinventorychart_series_0_binding.label_field = next((attr for attr in vendorinventorychart_series_0_binding_domain.attributes if attr.name == "sku"), None)
else:
    # Domain class 'Inventory' not resolved; data binding skipped.
    vendorinventorychart_series_0_binding = None
vendorinventorychart_series_0 = Series(name="Vendor_Inventory_Data", label="Vendor Inventory Data", data_binding=vendorinventorychart_series_0_binding, styling=None)
vendorinventorychart = BarChart(
    name="vendorInventoryChart",
    series=[vendorinventorychart_series_0],
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
inventory_vendor.view_elements = {localinventorychart, vendorinventorychart}

example2 = Module(
    name="example2",
    screens={addinventory, inventory, inventory_local, inventory_vendor}
)

# GUI Model
gui_model = GUIModel(
    name="example2",
    package="",
    versionCode="",
    versionName="",
    modules={example2},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition

# Restore fields omitted by the installed BESSER code builder.
form1.title = '#### Inventory item'
form1.submit_label = 'Submit'
form1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('Inventory'))
inventorytable_list.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('Inventory'))
next(s for s in inventorytable_list.list_sources if s.name == 'inventory').field_names = ['id', 'sku', 'description', 'quantity', 'replenish', 'location', 'latitude', 'longitude', 'image_url']
