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

# Screen: Add_Remove_Class__Error__List
add_remove_class_error_list = Screen(name="Add_Remove_Class__Error__List", description="", view_elements=set(), is_main_page=True, route_path="/Add_Remove_Class__Error__List", screen_size="Medium")
add_remove_class_error_list_1_source_0 = DataSourceElement(name="Add/Remove_Class_(Error)")
add_remove_class_error_list_1 = DataList(name="Add/Remove_Class_(Error)_List", description="", list_sources={add_remove_class_error_list_1_source_0})
reset = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
add_remove_class_error_list.view_elements = {add_remove_class_error_list_1, reset}


# Screen: Add_Remove_Class__Focus__List
add_remove_class_focus_list = Screen(name="Add_Remove_Class__Focus__List", description="", view_elements=set(), is_main_page=True, route_path="/Add_Remove_Class__Focus__List", screen_size="Medium")
add_remove_class_focus_list_1_source_0 = DataSourceElement(name="Add/Remove_Class_(Focus)")
add_remove_class_focus_list_1 = DataList(name="Add/Remove_Class_(Focus)_List", description="", list_sources={add_remove_class_focus_list_1_source_0})
reset_1 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
add_remove_class_focus_list.view_elements = {add_remove_class_focus_list_1, reset_1}


# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
cancel = Button(
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
administration.view_elements = {cancel, reset_data}


# Screen: Administration_p26
administration_p26 = Screen(name="Administration_p26", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration_p26.view_elements = set()


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


# Screen: Debounce_and_Throttle
debounce_and_throttle = Screen(name="Debounce_and_Throttle", description="", view_elements=set(), is_main_page=True, route_path="/Debounce_and_Throttle", screen_size="Medium")
debounce_and_throttle.view_elements = set()


# Screen: Delete_and_Refresh_List
delete_and_refresh_list = Screen(name="Delete_and_Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Delete_and_Refresh_List", screen_size="Medium")
delete_and_refresh_list_1_source_0 = DataSourceElement(name="Delete_and_Refresh")
delete_and_refresh_list_1 = DataList(name="Delete_and_Refresh_List", description="", list_sources={delete_and_refresh_list_1_source_0})
reset_2 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_and_refresh_list.view_elements = {delete_and_refresh_list_1, reset_2}


# Screen: Disable_Enable_List
disable_enable_list = Screen(name="Disable_Enable_List", description="", view_elements=set(), is_main_page=True, route_path="/Disable_Enable_List", screen_size="Medium")
disable_enable_list_1_source_0 = DataSourceElement(name="Disable/Enable")
disable_enable_list_1 = DataList(name="Disable/Enable_List", description="", list_sources={disable_enable_list_1_source_0})
reset_3 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
disable_enable_list.view_elements = {disable_enable_list_1, reset_3}


# Screen: Edit
edit = Screen(name="Edit", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_2 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_1 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit.view_elements = {cancel_2, save_1}


# Screen: Edit_p13
edit_p13 = Screen(name="Edit_p13", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
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
edit_p13.view_elements = {cancel_3, save_2}


# Screen: Edit_p15
edit_p15 = Screen(name="Edit_p15", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_3 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit_p15.view_elements = {cancel_4, save_3}


# Screen: Edit_p22
edit_p22 = Screen(name="Edit_p22", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_5 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_4 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit_p22.view_elements = {cancel_5, save_4}


# Screen: Edit_p5
edit_p5 = Screen(name="Edit_p5", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_6 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_5 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit_p5.view_elements = {cancel_6, save_5}


# Screen: Edit_p7
edit_p7 = Screen(name="Edit_p7", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_7 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_6 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit_p7.view_elements = {cancel_7, save_6}


# Screen: Edit_p9
edit_p9 = Screen(name="Edit_p9", description="", view_elements=set(), is_main_page=True, route_path="/Edit", screen_size="Medium")
cancel_8 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_7 = Button(
    name="Save",
    description="",
    label="Save",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
edit_p9.view_elements = {cancel_8, save_7}


# Screen: Execute_PL_SQL_Code_List
execute_pl_sql_code_list = Screen(name="Execute_PL_SQL_Code_List", description="", view_elements=set(), is_main_page=True, route_path="/Execute_PL_SQL_Code_List", screen_size="Medium")
execute_pl_sql_code_list_1_source_0 = DataSourceElement(name="Execute_PL/SQL_Code")
execute_pl_sql_code_list_1 = DataList(name="Execute_PL/SQL_Code_List", description="", list_sources={execute_pl_sql_code_list_1_source_0})
reset_4 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
update_salary = Button(
    name="Update_Salary",
    description="",
    label="Update_Salary",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
execute_pl_sql_code_list.view_elements = {execute_pl_sql_code_list_1, reset_4, update_salary}


# Screen: Filter_and_Refresh_List
filter_and_refresh_list = Screen(name="Filter_and_Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Filter_and_Refresh_List", screen_size="Medium")
filter_and_refresh_list_1_source_0 = DataSourceElement(name="Filter_and_Refresh")
filter_and_refresh_list_1 = DataList(name="Filter_and_Refresh_List", description="", list_sources={filter_and_refresh_list_1_source_0})
p19_reset = Button(
    name="P19_Reset",
    description="",
    label="P19_Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
filter_and_refresh_list.view_elements = {filter_and_refresh_list_1, p19_reset}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Hide_Show_List
hide_show_list = Screen(name="Hide_Show_List", description="", view_elements=set(), is_main_page=True, route_path="/Hide_Show_List", screen_size="Medium")
hide_show_list_1_source_0 = DataSourceElement(name="Hide/Show")
hide_show_list_1 = DataList(name="Hide/Show_List", description="", list_sources={hide_show_list_1_source_0})
reset_5 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
hide_show_list.view_elements = {hide_show_list_1, reset_5}


# Screen: Refresh_List
refresh_list = Screen(name="Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Refresh_List", screen_size="Medium")
refresh_list_1_source_0 = DataSourceElement(name="Refresh")
refresh_list_1 = DataList(name="Refresh_List", description="", list_sources={refresh_list_1_source_0})
reset_6 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
refresh_list.view_elements = {refresh_list_1, reset_6}


# Screen: Set_Values__PL_SQL__List
set_values_pl_sql_list = Screen(name="Set_Values__PL_SQL__List", description="", view_elements=set(), is_main_page=True, route_path="/Set_Values__PL_SQL__List", screen_size="Medium")
reset_7 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
set_values_pl_sql_list_1_source_0 = DataSourceElement(name="Set_Values_(PL/SQL)")
set_values_pl_sql_list_1 = DataList(name="Set_Values_(PL/SQL)_List", description="", list_sources={set_values_pl_sql_list_1_source_0})
set_values_pl_sql_list.view_elements = {reset_7, set_values_pl_sql_list_1}


# Screen: Set_Values__SQL__List
set_values_sql_list = Screen(name="Set_Values__SQL__List", description="", view_elements=set(), is_main_page=True, route_path="/Set_Values__SQL__List", screen_size="Medium")
reset_8 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
set_values_sql_list_1_source_0 = DataSourceElement(name="Set_Values_(SQL)")
set_values_sql_list_1 = DataList(name="Set_Values_(SQL)_List", description="", list_sources={set_values_sql_list_1_source_0})
set_values_sql_list.view_elements = {reset_8, set_values_sql_list_1}


# Screen: Shuttle_Refresh_List
shuttle_refresh_list = Screen(name="Shuttle_Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Shuttle_Refresh_List", screen_size="Medium")
reset_9 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
shuttle_refresh_list_1_source_0 = DataSourceElement(name="Shuttle_Refresh")
shuttle_refresh_list_1 = DataList(name="Shuttle_Refresh_List", description="", list_sources={shuttle_refresh_list_1_source_0})
shuttle_refresh_list.view_elements = {reset_9, shuttle_refresh_list_1}


# Screen: Stripe_Report_List
stripe_report_list = Screen(name="Stripe_Report_List", description="", view_elements=set(), is_main_page=True, route_path="/Stripe_Report_List", screen_size="Medium")
reset_10 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
stripe_report_list_1_source_0 = DataSourceElement(name="Stripe_Report")
stripe_report_list_1 = DataList(name="Stripe_Report_List", description="", list_sources={stripe_report_list_1_source_0})
stripe_report_list.view_elements = {reset_10, stripe_report_list_1}


# Screen: Timer_List
timer_list = Screen(name="Timer_List", description="", view_elements=set(), is_main_page=True, route_path="/Timer_List", screen_size="Medium")
reset_11 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
timer_list_1_source_0 = DataSourceElement(name="Timer")
timer_list_1 = DataList(name="Timer_List", description="", list_sources={timer_list_1_source_0})
timer_list.view_elements = {reset_11, timer_list_1}

oracleapexgui = Module(
    name="OracleApexGUI",
    screens={add_remove_class_error_list, add_remove_class_focus_list, administration, administration_p26, application_theme_style, debounce_and_throttle, delete_and_refresh_list, disable_enable_list, edit, edit_p13, edit_p15, edit_p22, edit_p5, edit_p7, edit_p9, execute_pl_sql_code_list, filter_and_refresh_list, help, hide_show_list, refresh_list, set_values_pl_sql_list, set_values_sql_list, shuttle_refresh_list, stripe_report_list, timer_list}
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
