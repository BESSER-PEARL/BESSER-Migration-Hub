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

# Module: OracleApexGUI

# Screen: About
about = Screen(name="About", description="", view_elements=set(), is_main_page=True, route_path="/About", screen_size="Medium")
about.view_elements = set()

oracleapexgui = Module(
    name="OracleApexGUI",
    screens={about}
)

# GUI Model
gui_model = GUIModel(
    name="OracleApexGUI",
    package="",
    versionCode="",
    versionName="",
    modules={oracleapexgui},
    description=""
)
