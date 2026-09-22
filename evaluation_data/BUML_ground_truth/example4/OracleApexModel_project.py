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
EbaDemoTreeProjects = Class(name="EbaDemoTreeProjects")
EbaDemoTreeTask = Class(name="EbaDemoTreeTask")
EbaDemoTreeSubtask = Class(name="EbaDemoTreeSubtask")
EbaDemoTreeStocks = Class(name="EbaDemoTreeStocks")
EbaDemoTreePopulation = Class(name="EbaDemoTreePopulation")
EbaDemoTreeDept = Class(name="EbaDemoTreeDept")
EbaDemoTreeEmp = Class(name="EbaDemoTreeEmp")
EbaDemoTreeProjFiles = Class(name="EbaDemoTreeProjFiles")

# EbaDemoTreeProjects class attributes and methods
EbaDemoTreeProjects_completion_date: Property = Property(name="completion_date", type=DateType)
EbaDemoTreeProjects_status: Property = Property(name="status", type=IntegerType)
EbaDemoTreeProjects_description: Property = Property(name="description", type=StringType)
EbaDemoTreeProjects_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjects_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjects_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjects_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjects_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjects_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeProjects_project_name: Property = Property(name="project_name", type=StringType)
EbaDemoTreeProjects_start_date: Property = Property(name="start_date", type=DateType)
EbaDemoTreeProjects_estimated_completion: Property = Property(name="estimated_completion", type=DateType)
EbaDemoTreeProjects.attributes={EbaDemoTreeProjects_completion_date, EbaDemoTreeProjects_created, EbaDemoTreeProjects_created_by, EbaDemoTreeProjects_description, EbaDemoTreeProjects_estimated_completion, EbaDemoTreeProjects_proj_id, EbaDemoTreeProjects_project_name, EbaDemoTreeProjects_row_version_number, EbaDemoTreeProjects_start_date, EbaDemoTreeProjects_status, EbaDemoTreeProjects_updated, EbaDemoTreeProjects_updated_by}

# EbaDemoTreeTask class attributes and methods
EbaDemoTreeTask_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeTask_task_name: Property = Property(name="task_name", type=StringType)
EbaDemoTreeTask_task_start: Property = Property(name="task_start", type=DateType)
EbaDemoTreeTask_task_est_comp: Property = Property(name="task_est_comp", type=DateType)
EbaDemoTreeTask_task_comp: Property = Property(name="task_comp", type=DateType)
EbaDemoTreeTask_task_priority: Property = Property(name="task_priority", type=IntegerType)
EbaDemoTreeTask_task_status: Property = Property(name="task_status", type=IntegerType)
EbaDemoTreeTask_task_assign: Property = Property(name="task_assign", type=IntegerType)
EbaDemoTreeTask_task_desc: Property = Property(name="task_desc", type=StringType)
EbaDemoTreeTask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeTask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeTask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeTask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeTask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeTask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeTask.attributes={EbaDemoTreeTask_created, EbaDemoTreeTask_created_by, EbaDemoTreeTask_proj_id, EbaDemoTreeTask_row_version_number, EbaDemoTreeTask_task_assign, EbaDemoTreeTask_task_comp, EbaDemoTreeTask_task_desc, EbaDemoTreeTask_task_est_comp, EbaDemoTreeTask_task_id, EbaDemoTreeTask_task_name, EbaDemoTreeTask_task_priority, EbaDemoTreeTask_task_start, EbaDemoTreeTask_task_status, EbaDemoTreeTask_updated, EbaDemoTreeTask_updated_by}

# EbaDemoTreeSubtask class attributes and methods
EbaDemoTreeSubtask_sub_id: Property = Property(name="sub_id", type=IntegerType)
EbaDemoTreeSubtask_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeSubtask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeSubtask_sub_name: Property = Property(name="sub_name", type=StringType)
EbaDemoTreeSubtask_sub_start: Property = Property(name="sub_start", type=DateType)
EbaDemoTreeSubtask_sub_est_comp: Property = Property(name="sub_est_comp", type=DateType)
EbaDemoTreeSubtask_sub_comp: Property = Property(name="sub_comp", type=DateType)
EbaDemoTreeSubtask_sub_priority: Property = Property(name="sub_priority", type=StringType)
EbaDemoTreeSubtask_sub_status: Property = Property(name="sub_status", type=StringType)
EbaDemoTreeSubtask_sub_assign: Property = Property(name="sub_assign", type=StringType)
EbaDemoTreeSubtask_sub_desc: Property = Property(name="sub_desc", type=StringType)
EbaDemoTreeSubtask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeSubtask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeSubtask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeSubtask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeSubtask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeSubtask.attributes={EbaDemoTreeSubtask_created, EbaDemoTreeSubtask_created_by, EbaDemoTreeSubtask_proj_id, EbaDemoTreeSubtask_row_version_number, EbaDemoTreeSubtask_sub_assign, EbaDemoTreeSubtask_sub_comp, EbaDemoTreeSubtask_sub_desc, EbaDemoTreeSubtask_sub_est_comp, EbaDemoTreeSubtask_sub_id, EbaDemoTreeSubtask_sub_name, EbaDemoTreeSubtask_sub_priority, EbaDemoTreeSubtask_sub_start, EbaDemoTreeSubtask_sub_status, EbaDemoTreeSubtask_task_id, EbaDemoTreeSubtask_updated, EbaDemoTreeSubtask_updated_by}

# EbaDemoTreeStocks class attributes and methods
EbaDemoTreeStocks_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeStocks_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeStocks_stock_code: Property = Property(name="stock_code", type=StringType)
EbaDemoTreeStocks_stock_name: Property = Property(name="stock_name", type=StringType)
EbaDemoTreeStocks_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeStocks_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeStocks_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeStocks_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeStocks_pricing_date: Property = Property(name="pricing_date", type=DateType)
EbaDemoTreeStocks_opening_val: Property = Property(name="opening_val", type=IntegerType)
EbaDemoTreeStocks_high: Property = Property(name="high", type=IntegerType)
EbaDemoTreeStocks_low: Property = Property(name="low", type=IntegerType)
EbaDemoTreeStocks_closing_val: Property = Property(name="closing_val", type=IntegerType)
EbaDemoTreeStocks.attributes={EbaDemoTreeStocks_closing_val, EbaDemoTreeStocks_created, EbaDemoTreeStocks_created_by, EbaDemoTreeStocks_high, EbaDemoTreeStocks_id, EbaDemoTreeStocks_low, EbaDemoTreeStocks_opening_val, EbaDemoTreeStocks_pricing_date, EbaDemoTreeStocks_row_version_number, EbaDemoTreeStocks_stock_code, EbaDemoTreeStocks_stock_name, EbaDemoTreeStocks_updated, EbaDemoTreeStocks_updated_by}

# EbaDemoTreePopulation class attributes and methods
EbaDemoTreePopulation_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreePopulation_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreePopulation_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreePopulation_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreePopulation_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreePopulation_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreePopulation_state_name: Property = Property(name="state_name", type=StringType)
EbaDemoTreePopulation_state_code: Property = Property(name="state_code", type=StringType)
EbaDemoTreePopulation_population: Property = Property(name="population", type=IntegerType)
EbaDemoTreePopulation_region: Property = Property(name="region", type=IntegerType)
EbaDemoTreePopulation.attributes={EbaDemoTreePopulation_created, EbaDemoTreePopulation_created_by, EbaDemoTreePopulation_id, EbaDemoTreePopulation_population, EbaDemoTreePopulation_region, EbaDemoTreePopulation_row_version_number, EbaDemoTreePopulation_state_code, EbaDemoTreePopulation_state_name, EbaDemoTreePopulation_updated, EbaDemoTreePopulation_updated_by}

# EbaDemoTreeDept class attributes and methods
EbaDemoTreeDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoTreeDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoTreeDept.attributes={EbaDemoTreeDept_deptno, EbaDemoTreeDept_dname, EbaDemoTreeDept_loc}

# EbaDemoTreeEmp class attributes and methods
EbaDemoTreeEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoTreeEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoTreeEmp_job: Property = Property(name="job", type=StringType)
EbaDemoTreeEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoTreeEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoTreeEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoTreeEmp_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeEmp.attributes={EbaDemoTreeEmp_comm, EbaDemoTreeEmp_deptno, EbaDemoTreeEmp_empno, EbaDemoTreeEmp_ename, EbaDemoTreeEmp_hiredate, EbaDemoTreeEmp_job, EbaDemoTreeEmp_sal}

# EbaDemoTreeProjFiles class attributes and methods
EbaDemoTreeProjFiles_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeProjFiles_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjFiles_file_name: Property = Property(name="file_name", type=StringType)
EbaDemoTreeProjFiles_file_mimetype: Property = Property(name="file_mimetype", type=StringType)
EbaDemoTreeProjFiles_file_charset: Property = Property(name="file_charset", type=StringType)
EbaDemoTreeProjFiles_file_lastupd: Property = Property(name="file_lastupd", type=DateType)
EbaDemoTreeProjFiles_file_comments: Property = Property(name="file_comments", type=StringType)
EbaDemoTreeProjFiles_tags: Property = Property(name="tags", type=StringType)
EbaDemoTreeProjFiles_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjFiles_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjFiles_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjFiles_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjFiles.attributes={EbaDemoTreeProjFiles_created, EbaDemoTreeProjFiles_created_by, EbaDemoTreeProjFiles_file_charset, EbaDemoTreeProjFiles_file_comments, EbaDemoTreeProjFiles_file_lastupd, EbaDemoTreeProjFiles_file_mimetype, EbaDemoTreeProjFiles_file_name, EbaDemoTreeProjFiles_id, EbaDemoTreeProjFiles_row_version_number, EbaDemoTreeProjFiles_tags, EbaDemoTreeProjFiles_updated, EbaDemoTreeProjFiles_updated_by}

# Relationships
EbaDemoTreeEmp_EbaDemoTreeEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeEmp_EbaDemoTreeEmp",
    ends={
        Property(name="ebademotreeemp", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeemp_mgr", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoTreeProjFiles_EbaDemoTreeProjects: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeProjFiles_EbaDemoTreeProjects",
    ends={
        Property(name="ebademotreeprojfiles", type=EbaDemoTreeProjFiles, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeprojects", type=EbaDemoTreeProjects, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="OracleApexModel",
    types={EbaDemoTreeProjects, EbaDemoTreeTask, EbaDemoTreeSubtask, EbaDemoTreeStocks, EbaDemoTreePopulation, EbaDemoTreeDept, EbaDemoTreeEmp, EbaDemoTreeProjFiles},
    associations={EbaDemoTreeEmp_EbaDemoTreeEmp, EbaDemoTreeProjFiles_EbaDemoTreeProjects},
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


######################
# PROJECT DEFINITION #
######################

from besser.BUML.metamodel.project import Project
from besser.BUML.metamodel.structural.structural import Metadata

metadata = Metadata(description="B-UML project generated by BESSER Migration Hub.")
project = Project(
    name="OracleApexModel",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
