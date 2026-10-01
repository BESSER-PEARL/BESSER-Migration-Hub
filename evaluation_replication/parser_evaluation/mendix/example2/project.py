####################
# STRUCTURAL MODEL #
####################

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
Content = Class(name="Content")
Feedback = Class(name="Feedback")
ContentAttachment = Class(name="ContentAttachment")
MendixSSOUser = Class(name="MendixSSOUser")

# Content class attributes and methods
Content_Title: Property = Property(name="Title", type=StringType)
Content_FreeText: Property = Property(name="FreeText", type=StringType)
Content_AverageRating: Property = Property(name="AverageRating", type=FloatType)
Content_URL: Property = Property(name="URL", type=StringType)
Content_PublishedOn: Property = Property(name="PublishedOn", type=DateType)
Content_Keyword1: Property = Property(name="Keyword1", type=StringType)
Content_Keyword2: Property = Property(name="Keyword2", type=StringType)
Content_Keyword3: Property = Property(name="Keyword3", type=StringType)
Content_Featured: Property = Property(name="Featured", type=BooleanType)
Content_Read: Property = Property(name="Read", type=BooleanType)
Content_Announcement: Property = Property(name="Announcement", type=BooleanType)
Content.attributes={Content_Announcement, Content_AverageRating, Content_Featured, Content_FreeText, Content_Keyword1, Content_Keyword2, Content_Keyword3, Content_PublishedOn, Content_Read, Content_Title, Content_URL}

# Feedback class attributes and methods
Feedback_Comment: Property = Property(name="Comment", type=StringType)
Feedback_Rating: Property = Property(name="Rating", type=FloatType)
Feedback_CommentDate: Property = Property(name="CommentDate", type=DateType)
Feedback.attributes={Feedback_Comment, Feedback_CommentDate, Feedback_Rating}

# ContentAttachment class attributes and methods

# MendixSSOUser class attributes and methods
MendixSSOUser_DisplayName: Property = Property(name="DisplayName", type=StringType)
MendixSSOUser_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
MendixSSOUser_AvatarURL: Property = Property(name="AvatarURL", type=StringType)
MendixSSOUser_AvatarThumbURL: Property = Property(name="AvatarThumbURL", type=StringType)
MendixSSOUser.attributes={MendixSSOUser_AvatarThumbURL, MendixSSOUser_AvatarURL, MendixSSOUser_DisplayName, MendixSSOUser_EmailAddress}

# Relationships
Feedback_Content: BinaryAssociation = BinaryAssociation(
    name="Feedback_Content",
    ends={
        Property(name="content", type=Content, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="feedback", type=Feedback, multiplicity=Multiplicity(0, 9999))
    }
)
ContentAttachment_Content: BinaryAssociation = BinaryAssociation(
    name="ContentAttachment_Content",
    ends={
        Property(name="content", type=Content, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="contentattachment", type=ContentAttachment, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ContentPortal",
    types={Content, Feedback, ContentAttachment, MendixSSOUser},
    associations={Feedback_Content, ContentAttachment_Content},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

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

# Module: ContentPortal

# Screen: Bookmarks
bookmarks = Screen(name="Bookmarks", description="", view_elements=set(), route_path="/Bookmarks", screen_size="Small")
listview1_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_source_0_domain = None
listview1_source_0.field_names = ['MendixSSOUser.DisplayName', 'Content.Title']
listview1 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-stories"]
)
container12 = ViewContainer(
    name="container12",
    description="",
    view_elements={listview1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listcards"]
)
text37 = Text(
    name="text37",
    content="Bookmarks",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container10 = ViewContainer(
    name="container10",
    description="",
    view_elements={text37},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container11 = ViewContainer(
    name="container11",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container9 = ViewContainer(
    name="container9",
    description="",
    view_elements={container10, container11},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center", "flex-wrap"]
)
container25 = ViewContainer(
    name="container25",
    description="",
    view_elements={container9},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sectionheader-search", "container"]
)
bookmarks.view_elements = {container12, container25}
bookmarks_layout = Layout()
bookmarks.layout = bookmarks_layout


# Screen: Discover
discover = Screen(name="Discover", description="", view_elements=set(), route_path="/Discover", screen_size="Small")
listview1_1_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_1_source_0_domain = None
listview1_1_source_0.field_names = ['MendixSSOUser.DisplayName', 'Content.Title']
listview1_1 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-stories"]
)
container12_1 = ViewContainer(
    name="container12",
    description="",
    view_elements={listview1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listcards"]
)
text37_1 = Text(
    name="text37",
    content="Discover",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container10_1 = ViewContainer(
    name="container10",
    description="",
    view_elements={text37_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container11_1 = ViewContainer(
    name="container11",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container9_1 = ViewContainer(
    name="container9",
    description="",
    view_elements={container10_1, container11_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center", "flex-wrap"]
)
container25_1 = ViewContainer(
    name="container25",
    description="",
    view_elements={container9_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["container", "sectionheader-search"]
)
discover.view_elements = {container12_1, container25_1}
discover_layout = Layout()
discover.layout = discover_layout


# Screen: Home
home = Screen(name="Home", description="", view_elements=set(), is_main_page=True, route_path="/Home", screen_size="Small")
text38 = Text(
    name="text38",
    content="Latest",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sectionheader-title"]
)
container14 = ViewContainer(
    name="container14",
    description="",
    view_elements={text38},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="View all",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container15 = ViewContainer(
    name="container15",
    description="",
    view_elements={actionbutton1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container13 = ViewContainer(
    name="container13",
    description="",
    view_elements={container14, container15},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
container25_2 = ViewContainer(
    name="container25",
    description="",
    view_elements={container13},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sectionheader-sub"]
)
text39 = Text(
    name="text39",
    content="Announcements",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sectionheader-title"]
)
container21 = ViewContainer(
    name="container21",
    description="",
    view_elements={text39},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="View all",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
container22 = ViewContainer(
    name="container22",
    description="",
    view_elements={actionbutton3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container18 = ViewContainer(
    name="container18",
    description="",
    view_elements={container21, container22},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
container26 = ViewContainer(
    name="container26",
    description="",
    view_elements={container18},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["sectionheader-sub"]
)
actionbutton5 = Button(
    name="actionButton5",
    description="",
    label="Start reading",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
text19 = Text(
    name="text19",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheaderfeatured-title", "text-white", "text-2-lines"]
)
text20 = Text(
    name="text20",
    content="Featured",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["text-white"]
)
container4 = ViewContainer(
    name="container4",
    description="",
    view_elements={actionbutton5, text19, text20},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheaderfeatured-overlay"]
)
container7 = ViewContainer(
    name="container7",
    description="",
    view_elements={container4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheaderfeatured-centered"]
)
container6 = ViewContainer(
    name="container6",
    description="",
    view_elements={container7},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader", "heroheaderfeatured"]
)
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={container6},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Your bookmarks",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
actionbutton6 = Button(
    name="actionButton6",
    description="",
    label="Add content",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#343A40", text_color="#FFFFFF", border_color="#1D2124", color_palette="default")),
    css_classes=["btn-inverse"]
)
text2 = Text(
    name="text2",
    content="Here is the latest news in the Mendix network.",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text36 = Text(
    name="text36",
    content="Hello, {1}. ",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container1 = ViewContainer(
    name="container1",
    description="",
    view_elements={actionbutton4, actionbutton6, text2, text36},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["alert", "alert-info", "container"]
)
dataview2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={container1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview1_2_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_2_source_0_domain = None
listview1_2_source_0.field_names = ['Content.Title', 'Content.PublishedOn', 'MendixSSOUser.DisplayName']
listview1_2 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-limited"]
)
listview2_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview2_source_0_domain = None
listview2_source_0.field_names = ['Content.PublishedOn', 'Content.Title']
listview2 = DataList(
    name="listView2",
    description="",
    list_sources={listview2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-limited", "listview-announcement"]
)
home.view_elements = {container25_2, container26, dataview1, dataview2, listview1_2, listview2}
home_layout = Layout()
home.layout = home_layout


# Screen: Manage
manage = Screen(name="Manage", description="", view_elements=set(), route_path="/Manage", screen_size="Small")
text38_1 = Text(
    name="text38",
    content="Manage",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["pageheader-title"]
)
container15_1 = ViewContainer(
    name="container15",
    description="",
    view_elements={text38_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
actionbutton5_1 = Button(
    name="actionButton5",
    description="",
    label="Add content",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
container16 = ViewContainer(
    name="container16",
    description="",
    view_elements={actionbutton5_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container14_1 = ViewContainer(
    name="container14",
    description="",
    view_elements={container15_1, container16},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center", "flex-wrap"]
)
container26_1 = ViewContainer(
    name="container26",
    description="",
    view_elements={container14_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["container", "sectionheader-search"]
)
listview1_3_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview1_3_source_0_domain = None
listview1_3_source_0.field_names = ['MendixSSOUser.DisplayName', 'Content.Title', 'Content.PublishedOn']
listview1_3 = DataList(
    name="listView1",
    description="",
    list_sources={listview1_3_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
listview2_1_source_0 = DataSourceElement(name="Content")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview2_1_source_0_domain = None
listview2_1_source_0.field_names = ['Content.Title', 'Content.PublishedOn', 'MendixSSOUser.DisplayName']
listview2_1 = DataList(
    name="listView2",
    description="",
    list_sources={listview2_1_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={listview1_3, listview2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["tab-lined"]
)
manage.view_elements = {container26_1, tabcontainer1}
manage_layout = Layout()
manage.layout = manage_layout


# Screen: Publish
publish = Screen(name="Publish", description="", view_elements=set(), route_path="/Publish", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Publish",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
label4 = Text(
    name="label4",
    content="",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["control-label"]
)
text4 = Text(
    name="text4",
    content="Is your content an announcement or a story?",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container13_1 = ViewContainer(
    name="container13",
    description="",
    view_elements={label4, text4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container14_2 = ViewContainer(
    name="container14",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container12_2 = ViewContainer(
    name="container12",
    description="",
    view_elements={container13_1, container14_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
label1 = Text(
    name="label1",
    content="",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["control-label"]
)
text1 = Text(
    name="text1",
    content="Set this article as a featured article. ",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container3 = ViewContainer(
    name="container3",
    description="",
    view_elements={label1, text1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container5 = ViewContainer(
    name="container5",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container4_1 = ViewContainer(
    name="container4",
    description="",
    view_elements={container3, container5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
label2 = Text(
    name="label2",
    content="",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["control-label"]
)
text2_1 = Text(
    name="text2",
    content="Set an image as the stories featured image.",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container7_1 = ViewContainer(
    name="container7",
    description="",
    view_elements={label2, text2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container8 = ViewContainer(
    name="container8",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container6_1 = ViewContainer(
    name="container6",
    description="",
    view_elements={container7_1, container8},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
label3 = Text(
    name="label3",
    content="",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["control-label"]
)
text3 = Text(
    name="text3",
    content="Preview your content before you publish it. ",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container10_2 = ViewContainer(
    name="container10",
    description="",
    view_elements={label3, text3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Preview",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#3B82F6", text_color="#FFFFFF", border_color="#2563EB", color_palette="default")),
    css_classes=["btn-primary"]
)
container11_2 = ViewContainer(
    name="container11",
    description="",
    view_elements={actionbutton3_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container9_2 = ViewContainer(
    name="container9",
    description="",
    view_elements={container10_2, container11_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
container1_1 = ViewContainer(
    name="container1",
    description="",
    view_elements={container12_2, container4_1, container6_1, container9_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["form-section"]
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Published on",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "PublishedOn"}
)
textbox2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Full name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "DisplayName"}
)
textbox4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Keyword 1",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Keyword1"}
)
textbox5 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Keyword 2",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Keyword2"}
)
textbox6 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="Keyword 3",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Keyword3"}
)
container2 = ViewContainer(
    name="container2",
    description="",
    view_elements={datepicker1, textbox2, textbox4, textbox5, textbox6},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["form-section"]
)
textarea1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    placeholder="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["formcontrol-lg", "border", "card"],
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview2_form = Form(name="dataView2_form", description="", inputFields={textarea1})
dataview2_1 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={actionbutton1_1, actionbutton2, container1_1, container2, dataview2_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
publish.view_elements = {dataview2_1}
publish_layout = Layout()
publish.layout = publish_layout


# Screen: Read
read = Screen(name="Read", description="", view_elements=set(), route_path="/Read", screen_size="Small")
container3_1 = ViewContainer(
    name="container3",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main", "heroheaderstory-image"]
)
text2_2 = Text(
    name="text2",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-inline", "text-inline"]
)
container9_3 = ViewContainer(
    name="container9",
    description="",
    view_elements={text2_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["d-block"]
)
text1_1 = Text(
    name="text1",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["author-title", "d-block"]
)
container7_2 = ViewContainer(
    name="container7",
    description="",
    view_elements={container9_3, text1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container8_1 = ViewContainer(
    name="container8",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container6_2 = ViewContainer(
    name="container6",
    description="",
    view_elements={container7_2, container8_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer", "flex-center"]
)
container4_2 = ViewContainer(
    name="container4",
    description="",
    view_elements={container6_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["section-author"]
)
text19_1 = Text(
    name="text19",
    content="{1}",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container5_1 = ViewContainer(
    name="container5",
    description="",
    view_elements={container4_2, text19_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main", "heroheaderstory-details"]
)
container2_1 = ViewContainer(
    name="container2",
    description="",
    view_elements={container3_1, container5_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheaderstory-content", "flexcontainer", "flex-center"]
)
container1_2 = ViewContainer(
    name="container1",
    description="",
    view_elements={container2_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["heroheader", "heroheaderstory"]
)
container14_3 = ViewContainer(
    name="container14",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["keywords-section"]
)
container15_2 = ViewContainer(
    name="container15",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["rating-section"]
)
container10_3 = ViewContainer(
    name="container10",
    description="",
    view_elements={container14_3, container15_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["centered", "spacing-inner-top-large"]
)
actionbutton1_2 = Button(
    name="actionButton1",
    description="",
    label="Publish",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
textarea1_1 = InputField(
    name="textArea1",
    description="",
    field_type=InputFieldType.TextArea,
    placeholder="Write a response...",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["formcontrol-comment"],
    custom_attributes={"data-mendix-attribute": "Comment"}
)
container18_1 = ViewContainer(
    name="container18",
    description="",
    view_elements={textarea1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem", "flexitem-main"]
)
container19 = ViewContainer(
    name="container19",
    description="",
    view_elements=set(),
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexitem"]
)
container17 = ViewContainer(
    name="container17",
    description="",
    view_elements={container18_1, container19},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["flexcontainer"]
)
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1_2, container17},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container20 = ViewContainer(
    name="container20",
    description="",
    view_elements={dataview1_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["feedback-form"]
)
listview2_2_source_0 = DataSourceElement(name="Feedback")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
listview2_2_source_0_domain = None
listview2_2_source_0.field_names = ['MendixSSOUser.DisplayName', 'Feedback.Comment', 'Feedback.CommentDate']
listview2_2 = DataList(
    name="listView2",
    description="",
    list_sources={listview2_2_source_0},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-comments"]
)
text5 = Text(
    name="text5",
    content="Responses",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
container16_1 = ViewContainer(
    name="container16",
    description="",
    view_elements={container20, listview2_2, text5},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["spacing-inner-top-large", "spacing-inner-bottom-large"]
)
listview1_4 = DataList(
    name="listView1",
    description="",
    list_sources={},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["listview-attachments"]
)
container13_2 = ViewContainer(
    name="container13",
    description="",
    view_elements={container16_1, listview1_4},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["centered"]
)
container11_3 = ViewContainer(
    name="container11",
    description="",
    view_elements={container13_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
dataview2_2 = ViewContainer(
    name="dataView2",
    description="",
    view_elements={container1_2, container10_3, container11_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
read.view_elements = {dataview2_2}
read_layout = Layout()
read.layout = read_layout

# Button events and transitions (written after all screens defined to avoid forward references)
actionbutton1.targetScreen = discover
actionbutton3.targetScreen = discover
actionbutton5.targetScreen = read
actionbutton4.targetScreen = bookmarks
actionbutton5_1.targetScreen = publish
actionbutton3_1.targetScreen = read

contentportal = Module(
    name="ContentPortal",
    screens={bookmarks, discover, home, manage, publish, read}
)

# GUI Model
gui_model = GUIModel(
    name="ContentPortal",
    package="",
    versionCode="",
    versionName="",
    modules={contentportal},
    description=""
)

# Bound-entity data bindings resolved by the Mendix parser
listview1.data_binding = DataBinding(domain_concept=Content)
listview1_1.data_binding = DataBinding(domain_concept=Content)
listview1_2.data_binding = DataBinding(domain_concept=Content)
listview2.data_binding = DataBinding(domain_concept=Content)
listview1_3.data_binding = DataBinding(domain_concept=Content)
listview2_1.data_binding = DataBinding(domain_concept=Content)
dataview2_form.data_binding = DataBinding(domain_concept=Content)
listview2_2.data_binding = DataBinding(domain_concept=Feedback)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="B-UML project generated by BESSER Migration Hub.")
project = Project(
    name="ContentPortal",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
