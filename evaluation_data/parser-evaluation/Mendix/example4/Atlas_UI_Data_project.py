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

# Enumerations
SimpleEnum: Enumeration = Enumeration(
    name="SimpleEnum",
    literals={
            EnumerationLiteral(name="Option_2"),
			EnumerationLiteral(name="Option_1")
    }
)

Departments: Enumeration = Enumeration(
    name="Departments",
    literals={
            EnumerationLiteral(name="Marketing"),
			EnumerationLiteral(name="Sales"),
			EnumerationLiteral(name="RnD"),
			EnumerationLiteral(name="Finance")
    }
)

Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="Primary"),
			EnumerationLiteral(name="Success"),
			EnumerationLiteral(name="Warning"),
			EnumerationLiteral(name="Danger")
    }
)

PeopleAttending: Enumeration = Enumeration(
    name="PeopleAttending",
    literals={
            EnumerationLiteral(name="_1_Person"),
			EnumerationLiteral(name="_2_People"),
			EnumerationLiteral(name="_3_People"),
			EnumerationLiteral(name="_4_People"),
			EnumerationLiteral(name="_5_People")
    }
)

DefaultEnumeration: Enumeration = Enumeration(
    name="DefaultEnumeration",
    literals={
            EnumerationLiteral(name="Option_1"),
			EnumerationLiteral(name="Option_2"),
			EnumerationLiteral(name="Option_3"),
			EnumerationLiteral(name="Option_4"),
			EnumerationLiteral(name="Option_5"),
			EnumerationLiteral(name="Option_6")
    }
)

# Classes
AtlasPeople = Class(name="AtlasPeople")
AtlasGenericObject = Class(name="AtlasGenericObject")
AtlasLocationDate = Class(name="AtlasLocationDate")
AtlasStatistics = Class(name="AtlasStatistics")
AtlasChartData = Class(name="AtlasChartData")
AtlasChartSeriesInfo = Class(name="AtlasChartSeriesInfo")
AtlasContinent = Class(name="AtlasContinent")
AtlasCountry = Class(name="AtlasCountry")
AtlasContext = Class(name="AtlasContext")
MapWithImages = Class(name="MapWithImages")
WhitePaper = Class(name="WhitePaper")
Gallery = Class(name="Gallery")

# AtlasPeople class attributes and methods
AtlasPeople_FirstName: Property = Property(name="FirstName", type=StringType)
AtlasPeople_LastName: Property = Property(name="LastName", type=StringType)
AtlasPeople_Phonenumber: Property = Property(name="Phonenumber", type=StringType)
AtlasPeople_Email: Property = Property(name="Email", type=StringType)
AtlasPeople_Birthday: Property = Property(name="Birthday", type=DateType)
AtlasPeople_Bio: Property = Property(name="Bio", type=StringType)
AtlasPeople_Task: Property = Property(name="Task", type=BooleanType)
AtlasPeople_JobTitle: Property = Property(name="JobTitle", type=StringType)
AtlasPeople_Department: Property = Property(name="Department", type=Departments)
AtlasPeople_CardNumber: Property = Property(name="CardNumber", type=StringType)
AtlasPeople_CardExpiryMonth: Property = Property(name="CardExpiryMonth", type=StringType)
AtlasPeople_CardExpiryYear: Property = Property(name="CardExpiryYear", type=StringType)
AtlasPeople_CCV: Property = Property(name="CCV", type=StringType)
AtlasPeople_Country: Property = Property(name="Country", type=StringType)
AtlasPeople_City: Property = Property(name="City", type=StringType)
AtlasPeople_Address: Property = Property(name="Address", type=StringType)
AtlasPeople_Zipcode: Property = Property(name="Zipcode", type=StringType)
AtlasPeople_Status: Property = Property(name="Status", type=Status)
AtlasPeople.attributes={AtlasPeople_Address, AtlasPeople_Bio, AtlasPeople_Birthday, AtlasPeople_CCV, AtlasPeople_CardExpiryMonth, AtlasPeople_CardExpiryYear, AtlasPeople_CardNumber, AtlasPeople_City, AtlasPeople_Country, AtlasPeople_Department, AtlasPeople_Email, AtlasPeople_FirstName, AtlasPeople_JobTitle, AtlasPeople_LastName, AtlasPeople_Phonenumber, AtlasPeople_Status, AtlasPeople_Task, AtlasPeople_Zipcode}

# AtlasGenericObject class attributes and methods
AtlasGenericObject_AtlasAutonumber: Property = Property(name="AtlasAutonumber", type=IntegerType)
AtlasGenericObject_AtlasBinary: Property = Property(name="AtlasBinary", type=StringType)
AtlasGenericObject_AtlasString: Property = Property(name="AtlasString", type=StringType)
AtlasGenericObject_AtlasBoolean: Property = Property(name="AtlasBoolean", type=BooleanType)
AtlasGenericObject_AtlasDateTime: Property = Property(name="AtlasDateTime", type=DateType)
AtlasGenericObject_AtlasDecimal: Property = Property(name="AtlasDecimal", type=FloatType)
AtlasGenericObject_AtlasEnumeration: Property = Property(name="AtlasEnumeration", type=DefaultEnumeration)
AtlasGenericObject_AtlasHashedString: Property = Property(name="AtlasHashedString", type=StringType)
AtlasGenericObject_AtlasInteger: Property = Property(name="AtlasInteger", type=IntegerType)
AtlasGenericObject_AtlasFloat: Property = Property(name="AtlasFloat", type=FloatType)
AtlasGenericObject_AtlasLong: Property = Property(name="AtlasLong", type=IntegerType)
AtlasGenericObject_AtlasCurrency: Property = Property(name="AtlasCurrency", type=FloatType)
AtlasGenericObject_AtlasChecked: Property = Property(name="AtlasChecked", type=BooleanType)
AtlasGenericObject_AtlasSimpleEnum: Property = Property(name="AtlasSimpleEnum", type=SimpleEnum)
AtlasGenericObject.attributes={AtlasGenericObject_AtlasAutonumber, AtlasGenericObject_AtlasBinary, AtlasGenericObject_AtlasBoolean, AtlasGenericObject_AtlasChecked, AtlasGenericObject_AtlasCurrency, AtlasGenericObject_AtlasDateTime, AtlasGenericObject_AtlasDecimal, AtlasGenericObject_AtlasEnumeration, AtlasGenericObject_AtlasFloat, AtlasGenericObject_AtlasHashedString, AtlasGenericObject_AtlasInteger, AtlasGenericObject_AtlasLong, AtlasGenericObject_AtlasSimpleEnum, AtlasGenericObject_AtlasString}

# AtlasLocationDate class attributes and methods
AtlasLocationDate_Title: Property = Property(name="Title", type=StringType)
AtlasLocationDate_Description: Property = Property(name="Description", type=StringType)
AtlasLocationDate_Location: Property = Property(name="Location", type=StringType)
AtlasLocationDate_Address: Property = Property(name="Address", type=StringType)
AtlasLocationDate_Price: Property = Property(name="Price", type=FloatType)
AtlasLocationDate_Date: Property = Property(name="Date", type=DateType)
AtlasLocationDate_Rating: Property = Property(name="Rating", type=IntegerType)
AtlasLocationDate_Longitude: Property = Property(name="Longitude", type=FloatType)
AtlasLocationDate_Latitude: Property = Property(name="Latitude", type=FloatType)
AtlasLocationDate_NoAttending: Property = Property(name="NoAttending", type=PeopleAttending)
AtlasLocationDate.attributes={AtlasLocationDate_Address, AtlasLocationDate_Date, AtlasLocationDate_Description, AtlasLocationDate_Latitude, AtlasLocationDate_Location, AtlasLocationDate_Longitude, AtlasLocationDate_NoAttending, AtlasLocationDate_Price, AtlasLocationDate_Rating, AtlasLocationDate_Title}

# AtlasStatistics class attributes and methods
AtlasStatistics_Title: Property = Property(name="Title", type=StringType)
AtlasStatistics_Description: Property = Property(name="Description", type=StringType)
AtlasStatistics_Date: Property = Property(name="Date", type=DateType)
AtlasStatistics_FirstDecimal: Property = Property(name="FirstDecimal", type=FloatType)
AtlasStatistics_SecondDecimal: Property = Property(name="SecondDecimal", type=FloatType)
AtlasStatistics_TotalDecimal: Property = Property(name="TotalDecimal", type=FloatType)
AtlasStatistics_Rating: Property = Property(name="Rating", type=IntegerType)
AtlasStatistics_Longitude: Property = Property(name="Longitude", type=FloatType)
AtlasStatistics_Latitude: Property = Property(name="Latitude", type=FloatType)
AtlasStatistics.attributes={AtlasStatistics_Date, AtlasStatistics_Description, AtlasStatistics_FirstDecimal, AtlasStatistics_Latitude, AtlasStatistics_Longitude, AtlasStatistics_Rating, AtlasStatistics_SecondDecimal, AtlasStatistics_Title, AtlasStatistics_TotalDecimal}

# AtlasChartData class attributes and methods
AtlasChartData_DayOfWeek: Property = Property(name="DayOfWeek", type=StringType)
AtlasChartData_Productivity: Property = Property(name="Productivity", type=IntegerType)
AtlasChartData_bubbleSize: Property = Property(name="bubbleSize", type=IntegerType)
AtlasChartData.attributes={AtlasChartData_DayOfWeek, AtlasChartData_Productivity, AtlasChartData_bubbleSize}

# AtlasChartSeriesInfo class attributes and methods
AtlasChartSeriesInfo_Name: Property = Property(name="Name", type=StringType)
AtlasChartSeriesInfo_Color: Property = Property(name="Color", type=StringType)
AtlasChartSeriesInfo.attributes={AtlasChartSeriesInfo_Color, AtlasChartSeriesInfo_Name}

# AtlasContinent class attributes and methods
AtlasContinent_Name: Property = Property(name="Name", type=StringType)
AtlasContinent.attributes={AtlasContinent_Name}

# AtlasCountry class attributes and methods
AtlasCountry_Name: Property = Property(name="Name", type=StringType)
AtlasCountry_FlagBase64Img: Property = Property(name="FlagBase64Img", type=StringType)
AtlasCountry.attributes={AtlasCountry_FlagBase64Img, AtlasCountry_Name}

# AtlasContext class attributes and methods
AtlasContext_String1: Property = Property(name="String1", type=StringType)
AtlasContext_String2: Property = Property(name="String2", type=StringType)
AtlasContext_String3: Property = Property(name="String3", type=StringType)
AtlasContext_String4: Property = Property(name="String4", type=StringType)
AtlasContext.attributes={AtlasContext_String1, AtlasContext_String2, AtlasContext_String3, AtlasContext_String4}

# MapWithImages class attributes and methods
MapWithImages_Title: Property = Property(name="Title", type=StringType)
MapWithImages_Subtitle: Property = Property(name="Subtitle", type=StringType)
MapWithImages.attributes={MapWithImages_Subtitle, MapWithImages_Title}

# WhitePaper class attributes and methods

# Gallery class attributes and methods
Gallery_Title: Property = Property(name="Title", type=StringType)
Gallery_Subtitle: Property = Property(name="Subtitle", type=StringType)
Gallery.attributes={Gallery_Subtitle, Gallery_Title}

# Relationships
AtlasChartData_AtlasChartSeriesInfo: BinaryAssociation = BinaryAssociation(
    name="AtlasChartData_AtlasChartSeriesInfo",
    ends={
        Property(name="atlaschartdata", type=AtlasChartData, multiplicity=Multiplicity(0, 9999)),
        Property(name="atlaschartseriesinfo", type=AtlasChartSeriesInfo, multiplicity=Multiplicity(1, 1))
    }
)
AtlasCountry_AtlasContinent: BinaryAssociation = BinaryAssociation(
    name="AtlasCountry_AtlasContinent",
    ends={
        Property(name="atlascountry", type=AtlasCountry, multiplicity=Multiplicity(0, 9999)),
        Property(name="atlascontinent", type=AtlasContinent, multiplicity=Multiplicity(1, 1))
    }
)
Trading_Partners: BinaryAssociation = BinaryAssociation(
    name="Trading_Partners",
    ends={
        Property(name="atlascountry_parent", type=AtlasCountry, multiplicity=Multiplicity(0, 9999)),
        Property(name="atlascountry_child", type=AtlasCountry, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Atlas_UI_Data",
    types={AtlasPeople, AtlasGenericObject, AtlasLocationDate, AtlasStatistics, AtlasChartData, AtlasChartSeriesInfo, AtlasContinent, AtlasCountry, AtlasContext, MapWithImages, WhitePaper, Gallery, SimpleEnum, Departments, Status, PeopleAttending, DefaultEnumeration},
    associations={AtlasChartData_AtlasChartSeriesInfo, AtlasCountry_AtlasContinent, Trading_Partners},
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

# Module: Atlas_UI_Data

# Screen: AtlasPeople_Objects_Overview
atlaspeople_objects_overview = Screen(name="AtlasPeople_Objects_Overview", description="", view_elements=set(), route_path="/AtlasPeople_Objects_Overview", screen_size="Small")
atlaspeople_objects_overview.view_elements = set()
atlaspeople_objects_overview_layout = Layout()
atlaspeople_objects_overview.layout = atlaspeople_objects_overview_layout


# Screen: AtlasStatistics_Objects_Overview
atlasstatistics_objects_overview = Screen(name="AtlasStatistics_Objects_Overview", description="", view_elements=set(), route_path="/AtlasStatistics_Objects_Overview", screen_size="Small")
atlasstatistics_objects_overview.view_elements = set()
atlasstatistics_objects_overview_layout = Layout()
atlasstatistics_objects_overview.layout = atlasstatistics_objects_overview_layout


# Screen: Create_Edit_AtlasStatistics_Object
create_edit_atlasstatistics_object = Screen(name="Create_Edit_AtlasStatistics_Object", description="", view_elements=set(), route_path="/Create_Edit_AtlasStatistics_Object", screen_size="Small")
actionbutton1 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox7 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Rating",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Rating"}
)
textbox5 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Second decimal",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "SecondDecimal"}
)
textbox8 = InputField(
    name="textBox8",
    description="",
    field_type=InputFieldType.Text,
    label="Longitude",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Longitude"}
)
datepicker1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Date"}
)
textbox6 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="Total decimal",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "TotalDecimal"}
)
textbox2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
textbox1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Latitude",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Latitude"}
)
textbox4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="First decimal",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "FirstDecimal"}
)
dataview5_form = Form(name="dataView5_form", description="", inputFields={textbox3, textbox7, textbox5, textbox8, datepicker1, textbox6, textbox2, textbox1, textbox4})
dataview5 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={actionbutton1, actionbutton2, dataview5_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
create_edit_atlasstatistics_object.view_elements = {dataview5}
create_edit_atlasstatistics_object_layout = Layout()
create_edit_atlasstatistics_object.layout = create_edit_atlasstatistics_object_layout


# Screen: Create_Edit_Generic_Object
create_edit_generic_object = Screen(name="Create_Edit_Generic_Object", description="", view_elements=set(), route_path="/Create_Edit_Generic_Object", screen_size="Small")
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_1 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox7_1 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Default long",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasLong"}
)
textbox2_1 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Default autonumber",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasAutonumber"}
)
textbox5_1 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Default integer",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasInteger"}
)
textbox3_1 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Default string",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasString"}
)
datepicker1_1 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Default date time",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasDateTime"}
)
textbox1_1 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Default currency",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasCurrency"}
)
textbox6_1 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="Default float",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasFloat"}
)
textbox4_1 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Default decimal",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "AtlasDecimal"}
)
dataview6_form = Form(name="dataView6_form", description="", inputFields={textbox7_1, textbox2_1, textbox5_1, textbox3_1, datepicker1_1, textbox1_1, textbox6_1, textbox4_1})
dataview6 = ViewContainer(
    name="dataView6",
    description="",
    view_elements={actionbutton1_1, actionbutton2_1, dataview6_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
create_edit_generic_object.view_elements = {dataview6}
create_edit_generic_object_layout = Layout()
create_edit_generic_object.layout = create_edit_generic_object_layout


# Screen: Create_Edit_LocationDate_Object
create_edit_locationdate_object = Screen(name="Create_Edit_LocationDate_Object", description="", view_elements=set(), route_path="/Create_Edit_LocationDate_Object", screen_size="Small")
actionbutton1_2 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_2 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox3_2 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Description",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Description"}
)
textbox5_2 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Address"}
)
datepicker1_2 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Date",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Date"}
)
textbox8_1 = InputField(
    name="textBox8",
    description="",
    field_type=InputFieldType.Text,
    label="Longitude",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Longitude"}
)
textbox4_2 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Location",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Location"}
)
textbox2_2 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
textbox6_2 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="Price",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Price"}
)
textbox1_2 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Latitude",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Latitude"}
)
textbox7_2 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Rating",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Rating"}
)
dataview5_form_1 = Form(name="dataView5_form", description="", inputFields={textbox3_2, textbox5_2, datepicker1_2, textbox8_1, textbox4_2, textbox2_2, textbox6_2, textbox1_2, textbox7_2})
dataview5_1 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={actionbutton1_2, actionbutton2_2, dataview5_form_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
create_edit_locationdate_object.view_elements = {dataview5_1}
create_edit_locationdate_object_layout = Layout()
create_edit_locationdate_object.layout = create_edit_locationdate_object_layout


# Screen: Create_Edit_People_Object
create_edit_people_object = Screen(name="Create_Edit_People_Object", description="", view_elements=set(), route_path="/Create_Edit_People_Object", screen_size="Small")
actionbutton1_3 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_3 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox12 = InputField(
    name="textBox12",
    description="",
    field_type=InputFieldType.Text,
    label="Address",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Address"}
)
textbox1_3 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Size",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Size"}
)
textbox4_3 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Phonenumber",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Phonenumber"}
)
datepicker1_3 = InputField(
    name="datePicker1",
    description="",
    field_type=InputFieldType.Date,
    label="Birthday",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Birthday"}
)
textbox2_3 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="First name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "FirstName"}
)
textbox7_3 = InputField(
    name="textBox7",
    description="",
    field_type=InputFieldType.Text,
    label="Job title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "JobTitle"}
)
textbox9 = InputField(
    name="textBox9",
    description="",
    field_type=InputFieldType.Text,
    label="Card expiry month",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CardExpiryMonth"}
)
textbox11 = InputField(
    name="textBox11",
    description="",
    field_type=InputFieldType.Text,
    label="CCV",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CCV"}
)
textbox13 = InputField(
    name="textBox13",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox8_2 = InputField(
    name="textBox8",
    description="",
    field_type=InputFieldType.Text,
    label="Card number",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CardNumber"}
)
textbox10 = InputField(
    name="textBox10",
    description="",
    field_type=InputFieldType.Text,
    label="Card expiry year",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "CardExpiryYear"}
)
textbox3_3 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Last name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "LastName"}
)
textbox5_3 = InputField(
    name="textBox5",
    description="",
    field_type=InputFieldType.Text,
    label="Email",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Email"}
)
textbox6_3 = InputField(
    name="textBox6",
    description="",
    field_type=InputFieldType.Text,
    label="Bio",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Bio"}
)
dataview5_form_2 = Form(name="dataView5_form", description="", inputFields={textbox12, textbox1_3, textbox4_3, datepicker1_3, textbox2_3, textbox7_3, textbox9, textbox11, textbox13, textbox8_2, textbox10, textbox3_3, textbox5_3, textbox6_3})
dataview5_2 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={actionbutton1_3, actionbutton2_3, dataview5_form_2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
create_edit_people_object.view_elements = {dataview5_2}
create_edit_people_object_layout = Layout()
create_edit_people_object.layout = create_edit_people_object_layout


# Screen: Generic_Objects_Overview
generic_objects_overview = Screen(name="Generic_Objects_Overview", description="", view_elements=set(), route_path="/Generic_Objects_Overview", screen_size="Small")
generic_objects_overview.view_elements = set()
generic_objects_overview_layout = Layout()
generic_objects_overview.layout = generic_objects_overview_layout


# Screen: Image_NewEdit
image_newedit = Screen(name="Image_NewEdit", description="", view_elements=set(), route_path="/Image_NewEdit", screen_size="Small")
actionbutton1_4 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_4 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox4_4 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Size",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Size"}
)
textbox3_4 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox2_4 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Subtitle",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Subtitle"}
)
textbox1_4 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview1_form = Form(name="dataView1_form", description="", inputFields={textbox4_4, textbox3_4, textbox2_4, textbox1_4})
dataview1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1_4, actionbutton2_4, dataview1_form},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image_newedit.view_elements = {dataview1}
image_newedit_layout = Layout()
image_newedit.layout = image_newedit_layout


# Screen: Image_Overview
image_overview = Screen(name="Image_Overview", description="", view_elements=set(), route_path="/Image_Overview", screen_size="Small")
text1 = Text(
    name="text1",
    content="Gallery",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
text2 = Text(
    name="text2",
    content="Map with Images",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
tabcontainer1 = ViewContainer(
    name="tabContainer1",
    description="",
    view_elements={text1, text2},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
image_overview.view_elements = {tabcontainer1}
image_overview_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
image_overview.layout = image_overview_layout


# Screen: LocationDate_Objects_Overview
locationdate_objects_overview = Screen(name="LocationDate_Objects_Overview", description="", view_elements=set(), route_path="/LocationDate_Objects_Overview", screen_size="Small")
locationdate_objects_overview.view_elements = set()
locationdate_objects_overview_layout = Layout()
locationdate_objects_overview.layout = locationdate_objects_overview_layout


# Screen: MapWithImages_NewEdit
mapwithimages_newedit = Screen(name="MapWithImages_NewEdit", description="", view_elements=set(), route_path="/MapWithImages_NewEdit", screen_size="Small")
actionbutton1_5 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_5 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox3_5 = InputField(
    name="textBox3",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
textbox4_5 = InputField(
    name="textBox4",
    description="",
    field_type=InputFieldType.Text,
    label="Size",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Size"}
)
textbox2_5 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Subtitle",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Subtitle"}
)
textbox1_5 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Title",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Title"}
)
dataview5_form_3 = Form(name="dataView5_form", description="", inputFields={textbox3_5, textbox4_5, textbox2_5, textbox1_5})
dataview5_3 = ViewContainer(
    name="dataView5",
    description="",
    view_elements={actionbutton1_5, actionbutton2_5, dataview5_form_3},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
mapwithimages_newedit.view_elements = {dataview5_3}
mapwithimages_newedit_layout = Layout()
mapwithimages_newedit.layout = mapwithimages_newedit_layout


# Screen: WhitePaper_NewEdit
whitepaper_newedit = Screen(name="WhitePaper_NewEdit", description="", view_elements=set(), route_path="/WhitePaper_NewEdit", screen_size="Small")
actionbutton1_6 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_6 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
textbox1_6 = InputField(
    name="textBox1",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Name"}
)
filemanager1 = InputField(
    name="fileManager1",
    description="",
    field_type=InputFieldType.File,
    label="File",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
textbox2_6 = InputField(
    name="textBox2",
    description="",
    field_type=InputFieldType.Text,
    label="Size",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    custom_attributes={"data-mendix-attribute": "Size"}
)
dataview1_form_1 = Form(name="dataView1_form", description="", inputFields={textbox1_6, filemanager1, textbox2_6})
dataview1_1 = ViewContainer(
    name="dataView1",
    description="",
    view_elements={actionbutton1_6, actionbutton2_6, dataview1_form_1},
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
whitepaper_newedit.view_elements = {dataview1_1}
whitepaper_newedit_layout = Layout()
whitepaper_newedit.layout = whitepaper_newedit_layout


# Screen: WhitePaper_Overview
whitepaper_overview = Screen(name="WhitePaper_Overview", description="", view_elements=set(), route_path="/WhitePaper_Overview", screen_size="Small")
text1_1 = Text(
    name="text1",
    content="White Paper",
    description="",
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default"))
)
whitepaper_overview.view_elements = {text1_1}
whitepaper_overview_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
whitepaper_overview.layout = whitepaper_overview_layout

atlas_ui_data = Module(
    name="Atlas_UI_Data",
    screens={atlaspeople_objects_overview, atlasstatistics_objects_overview, create_edit_atlasstatistics_object, create_edit_generic_object, create_edit_locationdate_object, create_edit_people_object, generic_objects_overview, image_newedit, image_overview, locationdate_objects_overview, mapwithimages_newedit, whitepaper_newedit, whitepaper_overview}
)

# GUI Model
gui_model = GUIModel(
    name="Atlas_UI_Data",
    package="",
    versionCode="",
    versionName="",
    modules={atlas_ui_data},
    description=""
)

# Bound-entity data bindings resolved by the Mendix parser
dataview5_form.data_binding = DataBinding(domain_concept=AtlasStatistics)
dataview6_form.data_binding = DataBinding(domain_concept=AtlasGenericObject)
dataview5_form_1.data_binding = DataBinding(domain_concept=AtlasLocationDate)
dataview5_form_2.data_binding = DataBinding(domain_concept=AtlasPeople)
dataview1_form.data_binding = DataBinding(domain_concept=Gallery)
dataview5_form_3.data_binding = DataBinding(domain_concept=MapWithImages)
dataview1_form_1.data_binding = DataBinding(domain_concept=WhitePaper)


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="B-UML project generated by BESSER Migration Hub.")
project = Project(
    name="Atlas_UI_Data",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
