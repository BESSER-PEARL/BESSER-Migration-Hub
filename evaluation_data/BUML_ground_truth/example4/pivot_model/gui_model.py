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

# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration.view_elements = set()


# Screen: Application_Theme_Style
application_theme_style = Screen(name="Application_Theme_Style", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style", screen_size="Medium")
cancel = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
application_theme_style.view_elements = {cancel, save}


# Screen: Create_Edit_Project_Form
create_edit_project_form = Screen(name="Create_Edit_Project_Form", description="", view_elements=set(), route_path="/Create_Edit_Project_Form", screen_size="Medium")
cancel_1 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
create = Button(
    name="Create",
    description="",
    label="Create",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
delete = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
save_1 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_edit_project_form.view_elements = {cancel_1, create, delete, save_1}


# Screen: Create_Edit_Tasks
create_edit_tasks = Screen(name="Create_Edit_Tasks", description="", view_elements=set(), is_main_page=True, route_path="/Create_Edit_Tasks", screen_size="Medium")
cancel_2 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
create_1 = Button(
    name="Create",
    description="",
    label="Create",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
create_subtask = Button(
    name="Create_Subtask",
    description="",
    label="Create_Subtask",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_1 = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
get_next_task_id = Button(
    name="Get_Next_Task_Id",
    description="",
    label="Get_Next_Task_Id",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
get_previous_task_id = Button(
    name="Get_Previous_Task_Id",
    description="",
    label="Get_Previous_Task_Id",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_2 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_edit_tasks.view_elements = {cancel_2, create_1, create_subtask, delete_1, get_next_task_id, get_previous_task_id, save_2}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Manage_Sample_Data
manage_sample_data = Screen(name="Manage_Sample_Data", description="", view_elements=set(), is_main_page=True, route_path="/Manage_Sample_Data", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_data = Button(
    name="Reset_Data",
    description="",
    label="Reset_Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
manage_sample_data.view_elements = {cancel_3, reset_data}


# Screen: Modify_Subtask_Information_Form
modify_subtask_information_form = Screen(name="Modify_Subtask_Information_Form", description="", view_elements=set(), route_path="/Modify_Subtask_Information_Form", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
create_2 = Button(
    name="Create",
    description="",
    label="Create",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
delete_2 = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
save_3 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
modify_subtask_information_form.view_elements = {cancel_4, create_2, delete_2, save_3}


# Screen: Project_Dashboard
project_dashboard = Screen(name="Project_Dashboard", description="", view_elements=set(), is_main_page=True, route_path="/Project_Dashboard", screen_size="Medium")
create_3 = Button(
    name="Create",
    description="",
    label="Create",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
project_dashboard.view_elements = {create_3}


# Screen: Project_Tracking
project_tracking = Screen(name="Project_Tracking", description="", view_elements=set(), is_main_page=True, route_path="/Project_Tracking", screen_size="Medium")
contract_all = Button(
    name="Contract_All",
    description="",
    label="Contract_All",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
expand_all = Button(
    name="Expand_All",
    description="",
    label="Expand_All",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_tree = Button(
    name="Reset_Tree",
    description="",
    label="Reset_Tree",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
project_tracking.view_elements = {contract_all, expand_all, reset_tree}

oracleapexgui = Module(
    name="OracleApexGUI",
    screens={administration, application_theme_style, create_edit_project_form, create_edit_tasks, help, manage_sample_data, modify_subtask_information_form, project_dashboard, project_tracking}
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
