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
pagetitle1 = Text(name="pageTitle1", content="{PageTitle}", description="Dynamic page title placeholder")
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={cancelbutton2, pagetitle1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
myaccountviewedit.view_elements = {dataview1}
myaccountviewedit_layout = Layout()
myaccountviewedit.layout = myaccountviewedit_layout


# Screen: TaskEdit
taskedit = Screen(name="TaskEdit", description="", view_elements=set(), route_path="/TaskEdit", screen_size="Small")
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Save changes",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Cancel changes",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container24 = ViewContainer(
    name="container24",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image1 = Image(
    name="image1",
    description="",
    source="TaskTracker.Images.Low",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container25 = ViewContainer(
    name="container25",
    description="",
    view_elements={image1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container23 = ViewContainer(
    name="container23",
    description="",
    view_elements={container24, container25},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option", "brand-info"]
)
container27 = ViewContainer(
    name="container27",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image2 = Image(
    name="image2",
    description="",
    source="TaskTracker.Images.Medium",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container28 = ViewContainer(
    name="container28",
    description="",
    view_elements={image2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container26 = ViewContainer(
    name="container26",
    description="",
    view_elements={container27, container28},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option", "brand-warning"]
)
container30 = ViewContainer(
    name="container30",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image3 = Image(
    name="image3",
    description="",
    source="TaskTracker.Images.High",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container31 = ViewContainer(
    name="container31",
    description="",
    view_elements={image3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container29 = ViewContainer(
    name="container29",
    description="",
    view_elements={container30, container31},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option", "brand-danger"]
)
text1 = Text(
    name="text1",
    content="Low",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text11 = Text(
    name="text11",
    content="Priority",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text8 = Text(
    name="text8",
    content="Medium",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text9 = Text(
    name="text9",
    content="High",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container2 = ViewContainer(
    name="container2",
    description="",
    view_elements={container23, container26, container29, text1, text11, text8, text9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton8 = Button(
    name="actionButton8",
    description="",
    label="Assign to Me",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
referenceselector1 = InputField(
    name="referenceSelector1",
    description="",
    field_type=InputFieldType.Dropdown,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
text3 = Text(
    name="text3",
    content="Assign to",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container47 = ViewContainer(
    name="container47",
    description="",
    view_elements={actionbutton8, referenceselector1, text3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container12 = ViewContainer(
    name="container12",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image4 = Image(
    name="image4",
    description="",
    source="TaskTracker.Images.ToDo",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container20 = ViewContainer(
    name="container20",
    description="",
    view_elements={image4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container11 = ViewContainer(
    name="container11",
    description="",
    view_elements={container12, container20},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option"]
)
container14 = ViewContainer(
    name="container14",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image5 = Image(
    name="image5",
    description="",
    source="TaskTracker.Images.Running",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container19 = ViewContainer(
    name="container19",
    description="",
    view_elements={image5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container13 = ViewContainer(
    name="container13",
    description="",
    view_elements={container14, container19},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option"]
)
container16 = ViewContainer(
    name="container16",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image6 = Image(
    name="image6",
    description="",
    source="TaskTracker.Images.Review",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container21 = ViewContainer(
    name="container21",
    description="",
    view_elements={image6},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container15 = ViewContainer(
    name="container15",
    description="",
    view_elements={container16, container21},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option"]
)
container18 = ViewContainer(
    name="container18",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-select"]
)
image7 = Image(
    name="image7",
    description="",
    source="TaskTracker.Images.Done",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-icon"]
)
container22 = ViewContainer(
    name="container22",
    description="",
    view_elements={image7},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option-wrapper"]
)
container17 = ViewContainer(
    name="container17",
    description="",
    view_elements={container18, container22},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["option"]
)
text12 = Text(
    name="text12",
    content="Status\r\n",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text4 = Text(
    name="text4",
    content="To Do",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text5 = Text(
    name="text5",
    content="In Progress",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text6 = Text(
    name="text6",
    content="Review",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text7 = Text(
    name="text7",
    content="Done",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container9 = ViewContainer(
    name="container9",
    description="",
    view_elements={container11, container13, container15, container17, text12, text4, text5, text6, text7},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Due date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DueDate"}
)
textarea1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description",
    placeholder="Task description...",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    placeholder="Task title...",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview1_form = Form(name="dataView1_form", description="", inputFields={datepicker1, textarea1, textbox1})
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Post comment",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textarea2 = InputField(
    name="textArea2",
    description="",
    field_type=InputFieldType.TextArea,
    placeholder="Add a comment...",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Content"}
)
dataview2_form = Form(name="dataView2_form", description="", inputFields={textarea2})
dataview2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={actionbutton3, dataview2_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image11 = Image(
    name="image11",
    description="",
    source="{1}",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview4 = ViewContainer(
    name="dataView4",
    description="",
    view_elements={image11},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
groupbox1_title = Text(name="groupBox1_title", content="Comments", description="")
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-empty"]
)
groupbox1 = ViewContainer(
    name="groupBox1",
    description="",
    view_elements={dataview2, dataview4, groupbox1_title, listview2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Upload file",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
filemanager1 = InputField(
    name="fileManager1",
    description="",
    field_type=InputFieldType.File,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["file-uploader"]
)
container1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton4, filemanager1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview3 = ViewContainer(
    name="dataView3",
    description="",
    view_elements={container1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
groupbox2_title = Text(name="groupBox2_title", content="Files", description="")
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-empty"]
)
groupbox2 = ViewContainer(
    name="groupBox2",
    description="",
    view_elements={dataview3, groupbox2_title, listview1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
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
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1, actionbutton2, container2, container47, container9, dataview1_form, groupbox1, groupbox2, microflowtrigger1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
taskedit.view_elements = {dataview1_1}
taskedit_layout = Layout()
taskedit.layout = taskedit_layout


# Screen: TaskOverview
taskoverview = Screen(name="TaskOverview", description="", view_elements=set(), is_main_page=True, route_path="/TaskOverview", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="+",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
gallery2_source_0 = DataSourceElement(name="Task")
gallery2 = DataList(
    name="gallery2",
    description="",
    list_sources={gallery2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery3_source_0 = DataSourceElement(name="Task")
gallery3 = DataList(
    name="gallery3",
    description="",
    list_sources={gallery3_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery4_source_0 = DataSourceElement(name="Task")
gallery4 = DataList(
    name="gallery4",
    description="",
    list_sources={gallery4_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery5_source_0 = DataSourceElement(name="Task")
gallery5 = DataList(
    name="gallery5",
    description="",
    list_sources={gallery5_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text10 = Text(
    name="text10",
    content="In Progress",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text19 = Text(
    name="text19",
    content="To Review",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text21 = Text(
    name="text21",
    content="Done",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3_1 = Text(
    name="text3",
    content="To Do",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container3 = ViewContainer(
    name="container3",
    description="",
    view_elements={actionbutton1_1, gallery2, gallery3, gallery4, gallery5, text10, text19, text21, text3_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="+",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
gallery6_source_0 = DataSourceElement(name="Task")
gallery6 = DataList(
    name="gallery6",
    description="",
    list_sources={gallery6_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery7_source_0 = DataSourceElement(name="Task")
gallery7 = DataList(
    name="gallery7",
    description="",
    list_sources={gallery7_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery8_source_0 = DataSourceElement(name="Task")
gallery8 = DataList(
    name="gallery8",
    description="",
    list_sources={gallery8_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
gallery9_source_0 = DataSourceElement(name="Task")
gallery9 = DataList(
    name="gallery9",
    description="",
    list_sources={gallery9_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text11_1 = Text(
    name="text11",
    content="In Progress",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flex1"]
)
text23 = Text(
    name="text23",
    content="To Review",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flex1"]
)
text24 = Text(
    name="text24",
    content="Done",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flex1"]
)
text8_1 = Text(
    name="text8",
    content="To Do",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container6 = ViewContainer(
    name="container6",
    description="",
    view_elements={actionbutton3_1, gallery6, gallery7, gallery8, gallery9, text11_1, text23, text24, text8_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
taskoverview.view_elements = {container3, container6}
taskoverview_layout = Layout()
taskoverview.layout = taskoverview_layout


# Screen: TeamOverview
teamoverview = Screen(name="TeamOverview", description="", view_elements=set(), route_path="/TeamOverview", screen_size="Small")
gallery2_1_source_0 = DataSourceElement(name="MendixSSOUser")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
gallery2_1_source_0_domain = None
gallery2_1_source_0.field_names = ['PageHelper.AssignedTasks', 'MendixSSOUser.AvatarURL', 'MendixSSOUser.EmailAddress', 'MendixSSOUser.DisplayName']
gallery2_1 = DataList(
    name="gallery2",
    description="",
    list_sources={gallery2_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text3_2 = Text(
    name="text3",
    content="The Team",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container9_1 = ViewContainer(
    name="container9",
    description="",
    view_elements={gallery2_1, text3_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
teamoverview.view_elements = {container9_1}
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

# Bound-entity data bindings resolved by the Mendix parser
dataview1_form.data_binding = DataBinding(domain_concept=Task)
gallery2.data_binding = DataBinding(domain_concept=Task)
gallery3.data_binding = DataBinding(domain_concept=Task)
gallery4.data_binding = DataBinding(domain_concept=Task)
gallery5.data_binding = DataBinding(domain_concept=Task)
gallery6.data_binding = DataBinding(domain_concept=Task)
gallery7.data_binding = DataBinding(domain_concept=Task)
gallery8.data_binding = DataBinding(domain_concept=Task)
gallery9.data_binding = DataBinding(domain_concept=Task)
gallery2_1.data_binding = DataBinding(domain_concept=MendixSSOUser)


######################
# PROJECT DEFINITION #
######################

