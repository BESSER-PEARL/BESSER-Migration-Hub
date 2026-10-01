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

# Module: TaskTracker

# Screen: MyAccountViewEdit
myaccountviewedit = Screen(name="MyAccountViewEdit", description="", view_elements=set(), route_path="/MyAccountViewEdit", screen_size="Small")
cancelbutton2 = Button(
    name="cancelButton2",
    description="",
    label="Close",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
myaccountviewedit.view_elements = {cancelbutton2}
myaccountviewedit_layout = Layout()
myaccountviewedit.layout = myaccountviewedit_layout


# Screen: TaskEdit
taskedit = Screen(name="TaskEdit", description="", view_elements=set(), route_path="/TaskEdit", screen_size="Small")
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Opslaan",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Annuleren",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Opslaan",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Opslaan",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5 = Button(
    name="actionButton5",
    description="",
    label="Koppeling",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-block", "btn-default"]
)
actionbutton6 = Button(
    name="actionButton6",
    description="",
    label="Verwijderen",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["text-small", "text-danger", "btn-default"]
)
actionbutton7 = Button(
    name="actionButton7",
    description="",
    label="Verwijderen",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["text-small", "text-danger", "btn-default"]
)
actionbutton8 = Button(
    name="actionButton8",
    description="",
    label="Knop",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={},
    css_classes=["listview-empty"]
)
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    css_classes=["listview-empty"]
)
microflowtrigger1 = Button(
    name="microflowTrigger1",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
taskedit.view_elements = {actionbutton1, actionbutton2, actionbutton3, actionbutton4, actionbutton5, actionbutton6, actionbutton7, actionbutton8, listview1, listview2, microflowtrigger1}
taskedit_layout = Layout()
taskedit.layout = taskedit_layout


# Screen: TaskOverview
taskoverview = Screen(name="TaskOverview", description="", view_elements=set(), is_main_page=True, route_path="/TaskOverview", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Nieuw",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Nieuw",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
taskoverview.view_elements = {actionbutton1_1, actionbutton3_1}
taskoverview_layout = Layout()
taskoverview.layout = taskoverview_layout


# Screen: TeamOverview
teamoverview = Screen(name="TeamOverview", description="", view_elements=set(), route_path="/TeamOverview", screen_size="Small")
teamoverview.view_elements = set()
teamoverview_layout = Layout()
teamoverview.layout = teamoverview_layout

# Button events and transitions (written after all screens defined to avoid forward references)
actionbutton3_1.targetScreen = taskedit

tasktracker = Module(
    name="TaskTracker",
    screens={myaccountviewedit, taskedit, taskoverview, teamoverview}
)

# GUI Model
gui_model = GUIModel(
    name="TaskTracker",
    package="",
    versionCode="",
    versionName="",
    modules={tasktracker},
    description=""
)
