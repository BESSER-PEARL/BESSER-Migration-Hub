from pathlib import Path
import runpy
globals().update({key: value for key, value in runpy.run_path(str(Path(__file__).with_name("data_model.py"))).items() if not key.startswith("__")})

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

# Module: SampleApp

# Screen: CreateItem_Request
createitem_request = Screen(name="CreateItem_Request", description="", view_elements=set(), route_path="/CreateItem_Request", screen_size="Small")
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40 = Text(
    name="text40",
    content="Create Item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3, text40},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Create",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
text2 = Text(
    name="text2",
    content="Data for initial revision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea2 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox5 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container3 = ViewContainer(
    name="container3",
    description="",
    view_elements={text2, textarea2, textbox4, textbox5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview7 = ViewContainer(
    name="dataView7",
    description="",
    view_elements={actionbutton1, container3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
createitem_request.view_elements = {container1, dataview7}
createitem_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
createitem_request.layout = createitem_request_layout


# Screen: CreateItem_Response
createitem_response = Screen(name="CreateItem_Response", description="", view_elements=set(), route_path="/CreateItem_Response", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text42 = Text(
    name="text42",
    content="Create Item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container3_1 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton1_1, text42},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
text11 = Text(
    name="text11",
    content="Details for created item revision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container2 = ViewContainer(
    name="container2",
    description="",
    view_elements={text11, textarea1, textbox2, textbox3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
text12 = Text(
    name="text12",
    content="Details for created item",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textarea2_1 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox4_1 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
textbox5_1 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
container1_1 = ViewContainer(
    name="container1",
    description="",
    view_elements={text12, textarea2_1, textbox4_1, textbox5_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={container1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container2, dataview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
createitem_response.view_elements = {container3_1, dataview1}
createitem_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
createitem_response.layout = createitem_response_layout


# Screen: Home
home = Screen(name="Home", description="", view_elements=set(), route_path="/Home", screen_size="Small")
text40_1 = Text(
    name="text40",
    content="Teamcenter Extension Sample App",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_2 = ViewContainer(
    name="container1",
    description="",
    view_elements={text40_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
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
    label="Configure Teamcenter",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container2_1 = ViewContainer(
    name="container2",
    description="",
    view_elements={actionbutton17, actionbutton9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton10 = Button(
    name="actionButton10",
    description="",
    label="Search ItemRevision",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton18 = Button(
    name="actionButton18",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container3_2 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton10, actionbutton18},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton11 = Button(
    name="actionButton11",
    description="",
    label="Create Item",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton19 = Button(
    name="actionButton19",
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
    view_elements={actionbutton11, actionbutton19},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton12 = Button(
    name="actionButton12",
    description="",
    label="Search WorkspaceObject",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton20 = Button(
    name="actionButton20",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container5 = ViewContainer(
    name="container5",
    description="",
    view_elements={actionbutton12, actionbutton20},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
actionbutton13 = Button(
    name="actionButton13",
    description="",
    label="Teamcenter login",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton21 = Button(
    name="actionButton21",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card-icon", "btn-default"]
)
container6 = ViewContainer(
    name="container6",
    description="",
    view_elements={actionbutton13, actionbutton21},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
home.view_elements = {container1_2, container2_1, container3_2, container4, container5, container6}
home_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
home.layout = home_layout


# Screen: ReviseItemRevision_Request
reviseitemrevision_request = Screen(name="ReviseItemRevision_Request", description="", view_elements=set(), route_path="/ReviseItemRevision_Request", screen_size="Small")
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Revise",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textbox1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
textarea1_1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox2_1 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox3_1 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
dataview6_form = Form(name="dataView6_form", description="", inputFields={textbox1, textarea1_1, textbox2_1, textbox3_1})
dataview6 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton2, actionbutton3_1, dataview6_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
reviseitemrevision_request.view_elements = {dataview6}
reviseitemrevision_request_layout = Layout()
reviseitemrevision_request.layout = reviseitemrevision_request_layout


# Screen: SearchItemRevision_Request
searchitemrevision_request = Screen(name="SearchItemRevision_Request", description="", view_elements=set(), route_path="/SearchItemRevision_Request", screen_size="Small")
actionbutton3_2 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40_2 = Text(
    name="text40",
    content="Search ItemRevision",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_3 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_2, text40_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1_2 = Button(
    name="actionButton1",
    description="",
    label="Search",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textbox1_1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox2_2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ItemID"}
)
textbox3_2 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision type",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "_Type"}
)
container2_2 = ViewContainer(
    name="container2",
    description="",
    view_elements={textbox1_1, textbox2_2, textbox3_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview6_1 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_2, container2_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
searchitemrevision_request.view_elements = {container1_3, dataview6_1}
searchitemrevision_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchitemrevision_request.layout = searchitemrevision_request_layout


# Screen: SearchItemRevision_Response
searchitemrevision_response = Screen(name="SearchItemRevision_Response", description="", view_elements=set(), route_path="/SearchItemRevision_Response", screen_size="Small")
searchitemrevision_response.view_elements = set()
searchitemrevision_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchitemrevision_response.layout = searchitemrevision_response_layout


# Screen: SearchWorkspaceObject_Request
searchworkspaceobject_request = Screen(name="SearchWorkspaceObject_Request", description="", view_elements=set(), route_path="/SearchWorkspaceObject_Request", screen_size="Small")
actionbutton3_3 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text40_3 = Text(
    name="text40",
    content="Search Workspace Object",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1_4 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_3, text40_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
actionbutton1_3 = Button(
    name="actionButton1",
    description="",
    label="Search",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
text12_1 = Text(
    name="text12",
    content="Pagination",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox2_3 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Start index",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "startIndex"}
)
textbox3_3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Max to load",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "maxToLoad"}
)
textbox5_2 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Max to return",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "maxToReturn"}
)
container2_3 = ViewContainer(
    name="container2",
    description="",
    view_elements={text12_1, textbox2_3, textbox3_3, textbox5_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Created after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CreatedAfter"}
)
datepicker2 = InputField(
    name="datePicker2",
    description="",
    field_type=InputFieldType.Date,
    label="Created before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CreatedBefore"}
)
datepicker3 = InputField(
    name="datePicker3",
    description="",
    field_type=InputFieldType.Date,
    label="Modified after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ModifiedAfter"}
)
datepicker4 = InputField(
    name="datePicker4",
    description="",
    field_type=InputFieldType.Date,
    label="Modified before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ModifiedBefore"}
)
datepicker5 = InputField(
    name="datePicker5",
    description="",
    field_type=InputFieldType.Date,
    label="Released after",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ReleasedAfter"}
)
datepicker6 = InputField(
    name="datePicker6",
    description="",
    field_type=InputFieldType.Date,
    label="Released before",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "ReleasedBefore"}
)
text13 = Text(
    name="text13",
    content="Query parameters",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox10 = InputField(
    name="textBox10",
    description="",
    field_type=InputFieldType.Text,
    label="Owning user",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "OwningUser"}
)
textbox11 = InputField(
    name="textBox11",
    description="",
    field_type=InputFieldType.Text,
    label="Owning group",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "OwningGroup"}
)
textbox7 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox8 = InputField(
    name="textBox8",
    description="",
    field_type=InputFieldType.Text,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox9 = InputField(
    name="textBox9",
    description="",
    field_type=InputFieldType.Text,
    label="Type",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "_Type"}
)
container3_3 = ViewContainer(
    name="container3",
    description="",
    view_elements={datepicker1, datepicker2, datepicker3, datepicker4, datepicker5, datepicker6, text13, textbox10, textbox11, textbox7, textbox8, textbox9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview7_1 = ViewContainer(
    name="dataView7",
    description="",
    view_elements={container3_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview6_2 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_3, container2_3, dataview7_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
searchworkspaceobject_request.view_elements = {container1_4, dataview6_2}
searchworkspaceobject_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchworkspaceobject_request.layout = searchworkspaceobject_request_layout


# Screen: SearchWorkspaceObject_Response
searchworkspaceobject_response = Screen(name="SearchWorkspaceObject_Response", description="", view_elements=set(), route_path="/SearchWorkspaceObject_Response", screen_size="Small")
searchworkspaceobject_response.view_elements = set()
searchworkspaceobject_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
searchworkspaceobject_response.layout = searchworkspaceobject_response_layout


# Screen: Structure_Request
structure_request = Screen(name="Structure_Request", description="", view_elements=set(), route_path="/Structure_Request", screen_size="Small")
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Structure",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton3_4 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
text42_1 = Text(
    name="text42",
    content="Configure structure for {1}/{2} - {3}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
dataview5 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={text42_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container1_5 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton3_4, dataview5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader"]
)
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text2_1 = Text(
    name="text2",
    content="Revision rule",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container3_4 = ViewContainer(
    name="container3",
    description="",
    view_elements={listview1, text2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2_4 = ViewContainer(
    name="container2",
    description="",
    view_elements={listview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3 = Text(
    name="text3",
    content="Variant rule",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container2_4, text3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container4_1 = ViewContainer(
    name="container4",
    description="",
    view_elements={dataview1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
dataview2_1 = ViewContainer(
    name="dataView2",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5 = Text(
    name="text5",
    content="BOM window properties",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container5_1 = ViewContainer(
    name="container5",
    description="",
    view_elements={dataview2_1, text5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["card"]
)
structure_request.view_elements = {actionbutton4, container1_5, container3_4, container4_1, container5_1}
structure_request_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
structure_request.layout = structure_request_layout


# Screen: Structure_Response
structure_response = Screen(name="Structure_Response", description="", view_elements=set(), route_path="/Structure_Response", screen_size="Small")
structure_response.view_elements = set()
structure_response_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
structure_response.layout = structure_response_layout


# Screen: UpdateItemRevision_Request
updateitemrevision_request = Screen(name="UpdateItemRevision_Request", description="", view_elements=set(), route_path="/UpdateItemRevision_Request", screen_size="Small")
actionbutton2_1 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_5 = Button(
    name="actionButton3",
    description="",
    label="Update",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textarea1_2 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_desc"}
)
textbox3_4 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "object_name"}
)
textbox2_4 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Item revision ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_revision_id"}
)
textbox1_2 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Item ID",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "item_id"}
)
dataview6_form_1 = Form(name="dataView6_form", description="", inputFields={textarea1_2, textbox3_4, textbox2_4, textbox1_2})
dataview6_3 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton2_1, actionbutton3_5, dataview6_form_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
updateitemrevision_request.view_elements = {dataview6_3}
updateitemrevision_request_layout = Layout()
updateitemrevision_request.layout = updateitemrevision_request_layout

sampleapp = Module(
    name="SampleApp",
    screens={createitem_request, createitem_response, home, reviseitemrevision_request, searchitemrevision_request, searchitemrevision_response, searchworkspaceobject_request, searchworkspaceobject_response, structure_request, structure_response, updateitemrevision_request}
)

# GUI Model
gui_model = GUIModel(
    name="SampleApp",
    package="",
    versionCode="",
    versionName="",
    modules={sampleapp},
    description=""
)

# Bound-entity data bindings resolved by the Mendix parser
dataview6_form.data_binding = DataBinding(domain_concept=DemoItemRevision)
dataview6_form_1.data_binding = DataBinding(domain_concept=DemoItemRevision)


######################
# PROJECT DEFINITION #
######################

