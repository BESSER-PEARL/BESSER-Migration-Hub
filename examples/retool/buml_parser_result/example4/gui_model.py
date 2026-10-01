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
MonthlySales = Class(name="MonthlySales")
CategorySales = Class(name="CategorySales")

# MonthlySales class attributes and methods
MonthlySales_revenue: Property = Property(name="revenue", type=IntegerType)
MonthlySales_month_number: Property = Property(name="month_number", type=IntegerType)
MonthlySales_month: Property = Property(name="month", type=StringType)
MonthlySales.attributes={MonthlySales_month, MonthlySales_month_number, MonthlySales_revenue}

# CategorySales class attributes and methods
CategorySales_category: Property = Property(name="category", type=StringType)
CategorySales_revenue: Property = Property(name="revenue", type=IntegerType)
CategorySales_orders: Property = Property(name="orders", type=IntegerType)
CategorySales.attributes={CategorySales_category, CategorySales_orders, CategorySales_revenue}

# Domain Model
domain_model = DomainModel(
    name="example4",
    types={MonthlySales, CategorySales},
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

# Module: example4

# Screen: example4_Main
example4_main = Screen(name="example4_Main", description="", view_elements=set(), is_main_page=True, route_path="/example4_Main", screen_size="Medium")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
categorychart_series_0_binding_domain = None
if domain_model_ref is not None:
    categorychart_series_0_binding_domain = domain_model_ref.get_class_by_name("CategorySales")
if categorychart_series_0_binding_domain:
    categorychart_series_0_binding = DataBinding(domain_concept=categorychart_series_0_binding_domain, name="CategorySalesDataBinding")
    categorychart_series_0_binding.label_field = next((attr for attr in categorychart_series_0_binding_domain.attributes if attr.name == "category"), None)
    categorychart_series_0_binding.data_field = next((attr for attr in categorychart_series_0_binding_domain.attributes if attr.name == "revenue"), None)
else:
    # Domain class 'CategorySales' not resolved; data binding skipped.
    categorychart_series_0_binding = None
categorychart_series_0 = Series(name="revenue", label="revenue", data_binding=categorychart_series_0_binding, styling=None)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
categorychart_series_1_binding_domain = None
if domain_model_ref is not None:
    categorychart_series_1_binding_domain = domain_model_ref.get_class_by_name("CategorySales")
if categorychart_series_1_binding_domain:
    categorychart_series_1_binding = DataBinding(domain_concept=categorychart_series_1_binding_domain, name="CategorySalesDataBinding")
    categorychart_series_1_binding.label_field = next((attr for attr in categorychart_series_1_binding_domain.attributes if attr.name == "category"), None)
    categorychart_series_1_binding.data_field = next((attr for attr in categorychart_series_1_binding_domain.attributes if attr.name == "orders"), None)
else:
    # Domain class 'CategorySales' not resolved; data binding skipped.
    categorychart_series_1_binding = None
categorychart_series_1 = Series(name="orders", label="orders", data_binding=categorychart_series_1_binding, styling=None)
categorychart = BarChart(
    name="categoryChart",
    series=[categorychart_series_0, categorychart_series_1],
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
categorychart_binding_domain = None
if domain_model_ref is not None:
    categorychart_binding_domain = domain_model_ref.get_class_by_name("CategorySales")
if categorychart_binding_domain:
    categorychart_binding = DataBinding(domain_concept=categorychart_binding_domain, name="CategorySalesDataBinding")
    categorychart_binding.label_field = next((attr for attr in categorychart_binding_domain.attributes if attr.name == "category"), None)
else:
    # Domain class 'CategorySales' not resolved; data binding skipped.
    categorychart_binding = None
if categorychart_binding:
    categorychart.data_binding = categorychart_binding
categorycharttitle = Text(name="categoryChartTitle", content="#### Revenue by Category", description="")
datatabletitle = Text(name="dataTableTitle", content="#### Raw Data", description="")
pagetitle = Text(name="pageTitle", content="### Sales Dashboard", description="")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
revenuechart_series_0_binding_domain = None
if domain_model_ref is not None:
    revenuechart_series_0_binding_domain = domain_model_ref.get_class_by_name("MonthlySales")
if revenuechart_series_0_binding_domain:
    revenuechart_series_0_binding = DataBinding(domain_concept=revenuechart_series_0_binding_domain, name="MonthlySalesDataBinding")
    revenuechart_series_0_binding.label_field = next((attr for attr in revenuechart_series_0_binding_domain.attributes if attr.name == "month"), None)
    revenuechart_series_0_binding.data_field = next((attr for attr in revenuechart_series_0_binding_domain.attributes if attr.name == "revenue"), None)
else:
    # Domain class 'MonthlySales' not resolved; data binding skipped.
    revenuechart_series_0_binding = None
revenuechart_series_0 = Series(name="revenue", label="revenue", data_binding=revenuechart_series_0_binding, styling=None)
revenuechart = LineChart(
    name="revenueChart",
    series=[revenuechart_series_0],
    line_width=2,
    show_grid=True,
    show_legend=True,
    show_tooltip=True,
    curve_type="monotone",
    animate=True,
    legend_position="top",
    grid_color="#e0e0e0",
    dot_size=5
)
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
revenuechart_binding_domain = None
if domain_model_ref is not None:
    revenuechart_binding_domain = domain_model_ref.get_class_by_name("MonthlySales")
if revenuechart_binding_domain:
    revenuechart_binding = DataBinding(domain_concept=revenuechart_binding_domain, name="MonthlySalesDataBinding")
    revenuechart_binding.label_field = next((attr for attr in revenuechart_binding_domain.attributes if attr.name == "month"), None)
else:
    # Domain class 'MonthlySales' not resolved; data binding skipped.
    revenuechart_binding = None
if revenuechart_binding:
    revenuechart.data_binding = revenuechart_binding
revenuecharttitle = Text(name="revenueChartTitle", content="#### Monthly Revenue", description="")
salestable_list_source_0 = DataSourceElement(name="monthly_sales")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
salestable_list_source_0_domain = None
if domain_model_ref is not None:
    salestable_list_source_0_domain = domain_model_ref.get_class_by_name("MonthlySales")
if salestable_list_source_0_domain:
    salestable_list_source_0.dataSourceClass = salestable_list_source_0_domain
    salestable_list_source_0.field_names = ['month', 'revenue', 'orders', 'conversion']
    salestable_list_source_0.fields = set(attr for attr in salestable_list_source_0_domain.attributes if attr.name in ['month', 'revenue', 'orders', 'conversion'])
else:
    # Domain class 'MonthlySales' not resolved for data source 'monthly_sales'.
    salestable_list_source_0.field_names = ['month', 'revenue', 'orders', 'conversion']
salestable_list = DataList(name="salesTable_List", description="", list_sources={salestable_list_source_0})
setupguidebtn = Button(
    name="setupGuideBtn",
    description="",
    label="Setup Guide",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate
)
statconversion = Text(name="statConversion", content="{{ Array.isArray(fetchSalesData.data) ? (fetchSalesData.data.reduce((sum, r) => sum + r.conversion, 0) / fetchSalesData.data.length).toFixed(1) : \'3.2\' }}%", description="Avg Conversion")
statorders = Text(name="statOrders", content="{{ Array.isArray(fetchSalesData.data) ? fetchSalesData.data.reduce((sum, r) => sum + r.orders, 0).toLocaleString() : \'1,847\' }}", description="Total Orders")
statrevenue = Text(name="statRevenue", content="${{ Array.isArray(fetchSalesData.data) ? fetchSalesData.data.reduce((sum, r) => sum + r.revenue, 0).toLocaleString() : \'124,500\' }}", description="Total Revenue")
example4_main.view_elements = {categorychart, categorycharttitle, datatabletitle, pagetitle, revenuechart, revenuecharttitle, salestable_list, setupguidebtn, statconversion, statorders, statrevenue}


# Screen: setupGuideModal
setupguidemodal = Screen(name="setupGuideModal", description="", view_elements=set(), route_path="/setupGuideModal", screen_size="Medium")
setupguidetext = Text(name="setupGuideText", content="{{ \'Welcome! This app demonstrates **PlotlyChart** with Statistic KPIs and a data table.\\n\\nTo connect your real data source:\\n\\n1. Open the **fetchSalesData** and **fetchCategoryData** queries in the bottom panel and update the API URL — or replace them with a database query\\n2. Select each **PlotlyChart** component and update the **Data** and **Layout** JSON to map your fields\\n3. Update the **Statistic** component values to reference your query data\\n4. Remove the mock data fallback from the **salesTable** data property\\n5. Delete this Setup Guide modal and the Setup Guide button\\n\\nCharts use Plotly.js — see plotly.com/javascript for layout and trace options.\' }}", description="")
setupguidetitle = Text(name="setupGuideTitle", content="## Setup Guide", description="")
setupguidemodal.view_elements = {setupguidetext, setupguidetitle}

# Button events and transitions (written after all screens defined to avoid forward references)
setupguidebtn_event_0_action_0 = Transition(name="setupGuideBtn_open_0", description="", target_screen=setupguidemodal)
setupguidebtn_event_0 = Event(name="setupGuideBtn_click_0", event_type=EventType.OnClick, actions={setupguidebtn_event_0_action_0})
setupguidebtn_event_0_action_0.triggered_by = setupguidebtn
setupguidebtn.events = {setupguidebtn_event_0}

example4 = Module(
    name="example4",
    screens={example4_main, setupguidemodal}
)

# GUI Model
gui_model = GUIModel(
    name="example4",
    package="",
    versionCode="",
    versionName="",
    modules={example4},
    description=""
)
