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

# Module: MyFirstModule

# Screen: AdministrativeStaff_form_page
administrativestaff_form_page = Screen(name="AdministrativeStaff_form_page", description="", view_elements=set(), route_path="/AdministrativeStaff_form_page", screen_size="Small")
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
actionbutton3 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
administrativestaff_form_page.view_elements = {actionbutton1, actionbutton2, actionbutton3}
administrativestaff_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
administrativestaff_form_page.layout = administrativestaff_form_page_layout


# Screen: AdministrativeStaff_page
administrativestaff_page = Screen(name="AdministrativeStaff_page", description="", view_elements=set(), route_path="/AdministrativeStaff_page", screen_size="Small")
administrativestaff_source_0 = DataSourceElement(name="AdministrativeStaff")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
administrativestaff_source_0_domain = None
administrativestaff_source_0.field_names = ['Person.familyName', 'Person.givenName', 'Person.phone']
administrativestaff = DataList(
    name="AdministrativeStaff",
    description="",
    list_sources={administrativestaff_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_1 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_1 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_1 = Button(
    name="actionButton3",
    description="",
    label="Add Administrative Staff",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
administrativestaff_page.view_elements = {administrativestaff, actionbutton1_1, actionbutton2_1, actionbutton3_1, actionbutton4, actionbutton5}
administrativestaff_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
administrativestaff_page.layout = administrativestaff_page_layout


# Screen: Department_form_page
department_form_page = Screen(name="Department_form_page", description="", view_elements=set(), route_path="/Department_form_page", screen_size="Small")
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
actionbutton3_2 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
department_form_page.view_elements = {actionbutton1_2, actionbutton2_2, actionbutton3_2}
department_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
department_form_page.layout = department_form_page_layout


# Screen: Department_page
department_page = Screen(name="Department_page", description="", view_elements=set(), route_path="/Department_page", screen_size="Small")
department_source_0 = DataSourceElement(name="Department")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
department_source_0_domain = None
department_source_0.field_names = ['Hospital.address']
department = DataList(
    name="Department",
    description="",
    list_sources={department_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_3 = Button(
    name="actionButton1",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton2_3 = Button(
    name="actionButton2",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton3_3 = Button(
    name="actionButton3",
    description="",
    label="Add Department",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_1 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_1 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
department_page.view_elements = {department, actionbutton1_3, actionbutton2_3, actionbutton3_3, actionbutton4_1, actionbutton5_1}
department_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
department_page.layout = department_page_layout


# Screen: Doctor_form_page
doctor_form_page = Screen(name="Doctor_form_page", description="", view_elements=set(), route_path="/Doctor_form_page", screen_size="Small")
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
actionbutton3_4 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
doctor_form_page.view_elements = {actionbutton1_4, actionbutton2_4, actionbutton3_4}
doctor_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
doctor_form_page.layout = doctor_form_page_layout


# Screen: Doctor_page
doctor_page = Screen(name="Doctor_page", description="", view_elements=set(), route_path="/Doctor_page", screen_size="Small")
doctor_source_0 = DataSourceElement(name="Doctor")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
doctor_source_0_domain = None
doctor_source_0.field_names = ['Doctor.speciality', 'Person.familyName', 'Person.givenName', 'Doctor.location']
doctor = DataList(
    name="Doctor",
    description="",
    list_sources={doctor_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_5 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_5 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_5 = Button(
    name="actionButton3",
    description="",
    label="Add Doctor",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_2 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_2 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
doctor_page.view_elements = {doctor, actionbutton1_5, actionbutton2_5, actionbutton3_5, actionbutton4_2, actionbutton5_2}
doctor_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
doctor_page.layout = doctor_page_layout


# Screen: Home_Web
home_web = Screen(name="Home_Web", description="", view_elements=set(), is_main_page=True, route_path="/Home_Web", screen_size="Small")
actionbutton1_6 = Button(
    name="actionButton1",
    description="",
    label="Nurse Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton10 = Button(
    name="actionButton10",
    description="",
    label="Surgeon Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton11 = Button(
    name="actionButton11",
    description="",
    label="Hospital Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton2_6 = Button(
    name="actionButton2",
    description="",
    label="Doctor Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton3_6 = Button(
    name="actionButton3",
    description="",
    label="Technical Staff Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton4_3 = Button(
    name="actionButton4",
    description="",
    label="Operational Staff Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton5_3 = Button(
    name="actionButton5",
    description="",
    label="Administrative Staff Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton6 = Button(
    name="actionButton6",
    description="",
    label="Staff Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton7 = Button(
    name="actionButton7",
    description="",
    label="Patient Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton8 = Button(
    name="actionButton8",
    description="",
    label="Department Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
actionbutton9 = Button(
    name="actionButton9",
    description="",
    label="Person Page",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#17A2B8", text_color="#FFFFFF", border_color="#117A8B", color_palette="default")),
    css_classes=["btn-info"]
)
home_web.view_elements = {actionbutton1_6, actionbutton10, actionbutton11, actionbutton2_6, actionbutton3_6, actionbutton4_3, actionbutton5_3, actionbutton6, actionbutton7, actionbutton8, actionbutton9}
home_web_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
home_web.layout = home_web_layout


# Screen: Hospital_form_page
hospital_form_page = Screen(name="Hospital_form_page", description="", view_elements=set(), route_path="/Hospital_form_page", screen_size="Small")
actionbutton1_7 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_7 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_7 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
hospital_form_page.view_elements = {actionbutton1_7, actionbutton2_7, actionbutton3_7}
hospital_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
hospital_form_page.layout = hospital_form_page_layout


# Screen: Hospital_page
hospital_page = Screen(name="Hospital_page", description="", view_elements=set(), route_path="/Hospital_page", screen_size="Small")
hospital_source_0 = DataSourceElement(name="Hospital")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
hospital_source_0_domain = None
hospital_source_0.field_names = ['Hospital.address', 'Hospital.name']
hospital = DataList(
    name="Hospital",
    description="",
    list_sources={hospital_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_8 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton3_8 = Button(
    name="actionButton3",
    description="",
    label="Add Hospital",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_4 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_4 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
actionbutton6_1 = Button(
    name="actionButton6",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
hospital_page.view_elements = {hospital, actionbutton1_8, actionbutton3_8, actionbutton4_4, actionbutton5_4, actionbutton6_1}
hospital_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
hospital_page.layout = hospital_page_layout


# Screen: Nurse_form_page
nurse_form_page = Screen(name="Nurse_form_page", description="", view_elements=set(), route_path="/Nurse_form_page", screen_size="Small")
actionbutton1_9 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_8 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_9 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
nurse_form_page.view_elements = {actionbutton1_9, actionbutton2_8, actionbutton3_9}
nurse_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
nurse_form_page.layout = nurse_form_page_layout


# Screen: Nurse_page
nurse_page = Screen(name="Nurse_page", description="", view_elements=set(), route_path="/Nurse_page", screen_size="Small")
nurse_source_0 = DataSourceElement(name="Nurse")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
nurse_source_0_domain = None
nurse_source_0.field_names = ['Person.givenName', 'Person.phone', 'Person.familyName']
nurse = DataList(
    name="Nurse",
    description="",
    list_sources={nurse_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_10 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_9 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_10 = Button(
    name="actionButton3",
    description="",
    label="Add Nurse",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_5 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_5 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
nurse_page.view_elements = {nurse, actionbutton1_10, actionbutton2_9, actionbutton3_10, actionbutton4_5, actionbutton5_5}
nurse_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
nurse_page.layout = nurse_page_layout


# Screen: OperationalStaff_form_page
operationalstaff_form_page = Screen(name="OperationalStaff_form_page", description="", view_elements=set(), route_path="/OperationalStaff_form_page", screen_size="Small")
actionbutton1_11 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_10 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_11 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
operationalstaff_form_page.view_elements = {actionbutton1_11, actionbutton2_10, actionbutton3_11}
operationalstaff_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
operationalstaff_form_page.layout = operationalstaff_form_page_layout


# Screen: OperationalStaff_page
operationalstaff_page = Screen(name="OperationalStaff_page", description="", view_elements=set(), route_path="/OperationalStaff_page", screen_size="Small")
operationsstaff_source_0 = DataSourceElement(name="OperationsStaff")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
operationsstaff_source_0_domain = None
operationsstaff_source_0.field_names = ['Person.familyName', 'Person.givenName', 'Person.phone']
operationsstaff = DataList(
    name="OperationsStaff",
    description="",
    list_sources={operationsstaff_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_12 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_11 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_12 = Button(
    name="actionButton3",
    description="",
    label="Add Operational Staff",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_6 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_6 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
operationalstaff_page.view_elements = {operationsstaff, actionbutton1_12, actionbutton2_11, actionbutton3_12, actionbutton4_6, actionbutton5_6}
operationalstaff_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
operationalstaff_page.layout = operationalstaff_page_layout


# Screen: Patient_form_page
patient_form_page = Screen(name="Patient_form_page", description="", view_elements=set(), route_path="/Patient_form_page", screen_size="Small")
actionbutton1_13 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_12 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_13 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
patient_form_page.view_elements = {actionbutton1_13, actionbutton2_12, actionbutton3_13}
patient_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
patient_form_page.layout = patient_form_page_layout


# Screen: Patient_page
patient_page = Screen(name="Patient_page", description="", view_elements=set(), route_path="/Patient_page", screen_size="Small")
patient_source_0 = DataSourceElement(name="Patient")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
patient_source_0_domain = None
patient_source_0.field_names = ['Person.familyName', 'Person.givenName', 'Person.gender', 'Patient.sickness']
patient = DataList(
    name="Patient",
    description="",
    list_sources={patient_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_14 = Button(
    name="actionButton1",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton2_13 = Button(
    name="actionButton2",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton3_14 = Button(
    name="actionButton3",
    description="",
    label="Add Patient",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_7 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_7 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
patient_page.view_elements = {patient, actionbutton1_14, actionbutton2_13, actionbutton3_14, actionbutton4_7, actionbutton5_7}
patient_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
patient_page.layout = patient_page_layout


# Screen: Person_Page
person_page = Screen(name="Person_Page", description="", view_elements=set(), route_path="/Person_Page", screen_size="Small")
person_source_0 = DataSourceElement(name="Person")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
person_source_0_domain = None
person_source_0.field_names = ['Person.familyName', 'Person.givenName']
person = DataList(
    name="Person",
    description="",
    list_sources={person_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_15 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_14 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_15 = Button(
    name="actionButton3",
    description="",
    label="Add Person",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_8 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_8 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
person_page.view_elements = {person, actionbutton1_15, actionbutton2_14, actionbutton3_15, actionbutton4_8, actionbutton5_8}
person_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
person_page.layout = person_page_layout


# Screen: Person_form_page
person_form_page = Screen(name="Person_form_page", description="", view_elements=set(), route_path="/Person_form_page", screen_size="Small")
actionbutton1_16 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_15 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_16 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
person_form_page.view_elements = {actionbutton1_16, actionbutton2_15, actionbutton3_16}
person_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
person_form_page.layout = person_form_page_layout


# Screen: Staff_form_page
staff_form_page = Screen(name="Staff_form_page", description="", view_elements=set(), route_path="/Staff_form_page", screen_size="Small")
actionbutton1_17 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_16 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_17 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
staff_form_page.view_elements = {actionbutton1_17, actionbutton2_16, actionbutton3_17}
staff_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
staff_form_page.layout = staff_form_page_layout


# Screen: Staff_page
staff_page = Screen(name="Staff_page", description="", view_elements=set(), route_path="/Staff_page", screen_size="Small")
staff_source_0 = DataSourceElement(name="Staff")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
staff_source_0_domain = None
staff_source_0.field_names = ['Person.familyName', 'Person.givenName']
staff = DataList(
    name="Staff",
    description="",
    list_sources={staff_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_18 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_17 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_18 = Button(
    name="actionButton3",
    description="",
    label="Add Staff",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_9 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_9 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
staff_page.view_elements = {staff, actionbutton1_18, actionbutton2_17, actionbutton3_18, actionbutton4_9, actionbutton5_9}
staff_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
staff_page.layout = staff_page_layout


# Screen: Surgeon_from_page
surgeon_from_page = Screen(name="Surgeon_from_page", description="", view_elements=set(), route_path="/Surgeon_from_page", screen_size="Small")
actionbutton1_19 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_18 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_19 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
surgeon_from_page.view_elements = {actionbutton1_19, actionbutton2_18, actionbutton3_19}
surgeon_from_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
surgeon_from_page.layout = surgeon_from_page_layout


# Screen: Surgeon_page
surgeon_page = Screen(name="Surgeon_page", description="", view_elements=set(), route_path="/Surgeon_page", screen_size="Small")
surgeon_source_0 = DataSourceElement(name="Surgeon")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
surgeon_source_0_domain = None
surgeon_source_0.field_names = ['Person.familyName', 'Person.givenName']
surgeon = DataList(
    name="Surgeon",
    description="",
    list_sources={surgeon_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_20 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_19 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_20 = Button(
    name="actionButton3",
    description="",
    label="Add Surgeon",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_10 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_10 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
surgeon_page.view_elements = {surgeon, actionbutton1_20, actionbutton2_19, actionbutton3_20, actionbutton4_10, actionbutton5_10}
surgeon_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
surgeon_page.layout = surgeon_page_layout


# Screen: TechnicalStaff_form_page
technicalstaff_form_page = Screen(name="TechnicalStaff_form_page", description="", view_elements=set(), route_path="/TechnicalStaff_form_page", screen_size="Small")
actionbutton1_21 = Button(
    name="actionButton1",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#0C4B33", text_color="#FFFFFF", border_color="#0056b3", color_palette="default")),
    css_classes=["btn-success"]
)
actionbutton2_20 = Button(
    name="actionButton2",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton3_21 = Button(
    name="actionButton3",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
technicalstaff_form_page.view_elements = {actionbutton1_21, actionbutton2_20, actionbutton3_21}
technicalstaff_form_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
technicalstaff_form_page.layout = technicalstaff_form_page_layout


# Screen: TechnicalStaff_page
technicalstaff_page = Screen(name="TechnicalStaff_page", description="", view_elements=set(), route_path="/TechnicalStaff_page", screen_size="Small")
technicalstaff_source_0 = DataSourceElement(name="TechnicalStaff")
try:
    domain_model_ref = domain_model
except NameError:
    domain_model_ref = None
technicalstaff_source_0_domain = None
technicalstaff_source_0.field_names = ['Person.phone', 'Person.familyName', 'Person.givenName']
technicalstaff = DataList(
    name="TechnicalStaff",
    description="",
    list_sources={technicalstaff_source_0},
    css_classes=["lv-col-md-4"]
)
actionbutton1_22 = Button(
    name="actionButton1",
    description="",
    label="Edit",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Navigate,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#FFC107", text_color="#000000", border_color="#FFA000", color_palette="default")),
    css_classes=["btn-warning"]
)
actionbutton2_21 = Button(
    name="actionButton2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#EF4444", text_color="#FFFFFF", border_color="#DC2626", color_palette="default")),
    css_classes=["btn-danger"]
)
actionbutton3_22 = Button(
    name="actionButton3",
    description="",
    label="Add Technical Staff ",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton4_11 = Button(
    name="actionButton4",
    description="",
    label="Unnamed Button",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["btn-default"]
)
actionbutton5_11 = Button(
    name="actionButton5",
    description="",
    label="Back",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Back,
    styling=Styling(position=Position(p_type=PositionType.RELATIVE), color=Color(background_color="#E0E0E0", text_color="#000000", border_color="#B0B0B0", color_palette="default")),
    css_classes=["link-back", "btn-default"]
)
technicalstaff_page.view_elements = {technicalstaff, actionbutton1_22, actionbutton2_21, actionbutton3_22, actionbutton4_11, actionbutton5_11}
technicalstaff_page_layout = Layout(layout_type=LayoutType.FLEX, gap="15px")
technicalstaff_page.layout = technicalstaff_page_layout

# Button events and transitions (written after all screens defined to avoid forward references)
actionbutton1_1.targetScreen = administrativestaff_form_page
actionbutton3_1.targetScreen = administrativestaff_form_page
actionbutton2_3.targetScreen = department_form_page
actionbutton3_3.targetScreen = department_form_page
actionbutton1_5.targetScreen = doctor_form_page
actionbutton3_5.targetScreen = doctor_form_page
actionbutton1_6.targetScreen = nurse_page
actionbutton10.targetScreen = surgeon_page
actionbutton11.targetScreen = hospital_page
actionbutton2_6.targetScreen = doctor_page
actionbutton3_6.targetScreen = technicalstaff_page
actionbutton4_3.targetScreen = operationalstaff_page
actionbutton5_3.targetScreen = administrativestaff_page
actionbutton6.targetScreen = staff_page
actionbutton7.targetScreen = patient_page
actionbutton8.targetScreen = department_page
actionbutton9.targetScreen = person_page
actionbutton1_8.targetScreen = hospital_form_page
actionbutton3_8.targetScreen = hospital_form_page
actionbutton1_10.targetScreen = nurse_form_page
actionbutton3_10.targetScreen = nurse_form_page
actionbutton1_12.targetScreen = operationalstaff_form_page
actionbutton3_12.targetScreen = operationalstaff_form_page
actionbutton2_13.targetScreen = patient_form_page
actionbutton3_14.targetScreen = patient_form_page
actionbutton1_15.targetScreen = person_form_page
actionbutton3_15.targetScreen = person_form_page
actionbutton1_18.targetScreen = staff_form_page
actionbutton3_18.targetScreen = staff_form_page
actionbutton1_20.targetScreen = surgeon_from_page
actionbutton3_20.targetScreen = surgeon_from_page
actionbutton1_22.targetScreen = technicalstaff_form_page
actionbutton3_22.targetScreen = technicalstaff_form_page

myfirstmodule = Module(
    name="MyFirstModule",
    screens={administrativestaff_form_page, administrativestaff_page, department_form_page, department_page, doctor_form_page, doctor_page, home_web, hospital_form_page, hospital_page, nurse_form_page, nurse_page, operationalstaff_form_page, operationalstaff_page, patient_form_page, patient_page, person_page, person_form_page, staff_form_page, staff_page, surgeon_from_page, surgeon_page, technicalstaff_form_page, technicalstaff_page}
)

# GUI Model
gui_model = GUIModel(
    name="MyFirstModule",
    package="",
    versionCode="",
    versionName="",
    modules={myfirstmodule},
    description=""
)
