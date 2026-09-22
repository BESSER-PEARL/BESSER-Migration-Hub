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

# Screen: Add_Edit_Collection_Member_Form
add_edit_collection_member_form = Screen(name="Add_Edit_Collection_Member_Form", description="", view_elements=set(), route_path="/Add_Edit_Collection_Member_Form", screen_size="Medium")
add_member = Button(
    name="Add_Member",
    description="",
    label="Add_Member",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
cancel = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_member = Button(
    name="Delete_Member",
    description="",
    label="Delete_Member",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
update_member = Button(
    name="Update_Member",
    description="",
    label="Update_Member",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
add_edit_collection_member_form.view_elements = {add_member, cancel, delete_member, update_member}


# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration.view_elements = set()


# Screen: Application_Theme_Style
application_theme_style = Screen(name="Application_Theme_Style", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style", screen_size="Medium")
cancel_1 = Button(
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
application_theme_style.view_elements = {cancel_1, save}


# Screen: Create_Collection_Form
create_collection_form = Screen(name="Create_Collection_Form", description="", view_elements=set(), route_path="/Create_Collection_Form", screen_size="Medium")
cancel_2 = Button(
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
create_replace = Button(
    name="Create_Replace",
    description="",
    label="Create_Replace",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_collection_form.view_elements = {cancel_2, create, create_replace}


# Screen: Data_Synchronization
data_synchronization = Screen(name="Data_Synchronization", description="", view_elements=set(), is_main_page=True, route_path="/Data_Synchronization", screen_size="Medium")
add_member_1 = Button(
    name="Add_Member",
    description="",
    label="Add_Member",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
apply_collection = Button(
    name="Apply_Collection",
    description="",
    label="Apply_Collection",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
populate = Button(
    name="Populate",
    description="",
    label="Populate",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
data_synchronization.view_elements = {add_member_1, apply_collection, populate}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Login_Page
login_page = Screen(name="Login_Page", description="", view_elements=set(), is_main_page=True, route_path="/Login_Page", screen_size="Medium")
login = Button(
    name="Login",
    description="",
    label="Login",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
login_page.view_elements = {login}


# Screen: Modify_Collection
modify_collection = Screen(name="Modify_Collection", description="", view_elements=set(), is_main_page=True, route_path="/Modify_Collection", screen_size="Medium")
add_member_2 = Button(
    name="Add_Member",
    description="",
    label="Add_Member",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
add_member_add_another = Button(
    name="Add_Member_Add_Another",
    description="",
    label="Add_Member_Add_Another",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_collection = Button(
    name="Delete_Collection",
    description="",
    label="Delete_Collection",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
resequence = Button(
    name="Resequence",
    description="",
    label="Resequence",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
truncate_collection = Button(
    name="Truncate_Collection",
    description="",
    label="Truncate_Collection",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
modify_collection.view_elements = {add_member_2, add_member_add_another, cancel_3, delete_collection, resequence, truncate_collection}


# Screen: Modify_Collection_Member_Form
modify_collection_member_form = Screen(name="Modify_Collection_Member_Form", description="", view_elements=set(), route_path="/Modify_Collection_Member_Form", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_member_1 = Button(
    name="Delete_Member",
    description="",
    label="Delete_Member",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
update_member_1 = Button(
    name="Update_Member",
    description="",
    label="Update_Member",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
modify_collection_member_form.view_elements = {cancel_4, delete_member_1, update_member_1}


# Screen: Remove_Collections
remove_collections = Screen(name="Remove_Collections", description="", view_elements=set(), is_main_page=True, route_path="/Remove_Collections", screen_size="Medium")
cancel_5 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
remove_collections_1 = Button(
    name="Remove_Collections",
    description="",
    label="Remove_Collections",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
remove_collections.view_elements = {cancel_5, remove_collections_1}


# Screen: Reset_Data
reset_data = Screen(name="Reset_Data", description="", view_elements=set(), is_main_page=True, route_path="/Reset_Data", screen_size="Medium")
cancel_6 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_data_1 = Button(
    name="Reset_Data",
    description="",
    label="Reset_Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
reset_data.view_elements = {cancel_6, reset_data_1}


# Screen: Sample_Collections___API_Examples
sample_collections_api_examples = Screen(name="Sample_Collections___API_Examples", description="", view_elements=set(), is_main_page=True, route_path="/Sample_Collections___API_Examples", screen_size="Medium")
sample_collections_api_examples.view_elements = set()

oracleapexgui = Module(
    name="OracleApexGUI",
    screens={add_edit_collection_member_form, administration, application_theme_style, create_collection_form, data_synchronization, help, login_page, modify_collection, modify_collection_member_form, remove_collections, reset_data, sample_collections_api_examples}
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
