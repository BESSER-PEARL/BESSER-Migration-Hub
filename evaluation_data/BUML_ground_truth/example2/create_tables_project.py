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
EbaDemoLoadDept = Class(name="EbaDemoLoadDept")
EbaDemoLoadEmp = Class(name="EbaDemoLoadEmp")
EbaDemoLoadSales = Class(name="EbaDemoLoadSales")

# EbaDemoLoadDept class attributes and methods
EbaDemoLoadDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoLoadDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoLoadDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoLoadDept.attributes={EbaDemoLoadDept_deptno, EbaDemoLoadDept_dname, EbaDemoLoadDept_loc}

# EbaDemoLoadEmp class attributes and methods
EbaDemoLoadEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoLoadEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoLoadEmp_job: Property = Property(name="job", type=StringType)
EbaDemoLoadEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoLoadEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoLoadEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoLoadEmp_created: Property = Property(name="created", type=DateType)
EbaDemoLoadEmp_last_updated: Property = Property(name="last_updated", type=DateType)
EbaDemoLoadEmp.attributes={EbaDemoLoadEmp_comm, EbaDemoLoadEmp_created, EbaDemoLoadEmp_empno, EbaDemoLoadEmp_ename, EbaDemoLoadEmp_hiredate, EbaDemoLoadEmp_job, EbaDemoLoadEmp_last_updated, EbaDemoLoadEmp_sal}

# EbaDemoLoadSales class attributes and methods
EbaDemoLoadSales_id: Property = Property(name="id", type=IntegerType)
EbaDemoLoadSales_region: Property = Property(name="region", type=StringType)
EbaDemoLoadSales_country: Property = Property(name="country", type=StringType)
EbaDemoLoadSales_item_type: Property = Property(name="item_type", type=StringType)
EbaDemoLoadSales_sales_channel: Property = Property(name="sales_channel", type=StringType)
EbaDemoLoadSales_total_profit: Property = Property(name="total_profit", type=IntegerType)
EbaDemoLoadSales_created: Property = Property(name="created", type=DateType)
EbaDemoLoadSales_last_updated: Property = Property(name="last_updated", type=DateType)
EbaDemoLoadSales_order_priority: Property = Property(name="order_priority", type=StringType)
EbaDemoLoadSales_order_date: Property = Property(name="order_date", type=DateType)
EbaDemoLoadSales_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoLoadSales_ship_date: Property = Property(name="ship_date", type=DateType)
EbaDemoLoadSales_units_sold: Property = Property(name="units_sold", type=IntegerType)
EbaDemoLoadSales_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoLoadSales_unit_cost: Property = Property(name="unit_cost", type=IntegerType)
EbaDemoLoadSales_total_revenue: Property = Property(name="total_revenue", type=IntegerType)
EbaDemoLoadSales_total_cost: Property = Property(name="total_cost", type=IntegerType)
EbaDemoLoadSales.attributes={EbaDemoLoadSales_country, EbaDemoLoadSales_created, EbaDemoLoadSales_id, EbaDemoLoadSales_item_type, EbaDemoLoadSales_last_updated, EbaDemoLoadSales_order_date, EbaDemoLoadSales_order_id, EbaDemoLoadSales_order_priority, EbaDemoLoadSales_region, EbaDemoLoadSales_sales_channel, EbaDemoLoadSales_ship_date, EbaDemoLoadSales_total_cost, EbaDemoLoadSales_total_profit, EbaDemoLoadSales_total_revenue, EbaDemoLoadSales_unit_cost, EbaDemoLoadSales_unit_price, EbaDemoLoadSales_units_sold}

# Relationships
EbaDemoLoadEmp_EbaDemoLoadEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoLoadEmp_EbaDemoLoadEmp",
    ends={
        Property(name="ebademoloademp", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademoloademp_mgr", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoLoadEmp_EbaDemoLoadDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoLoadEmp_EbaDemoLoadDept",
    ends={
        Property(name="ebademoloademp", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademoloaddept", type=EbaDemoLoadDept, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="create_tables",
    types={EbaDemoLoadDept, EbaDemoLoadEmp, EbaDemoLoadSales},
    associations={EbaDemoLoadEmp_EbaDemoLoadEmp, EbaDemoLoadEmp_EbaDemoLoadDept},
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


# Screen: Administration_p35
administration_p35 = Screen(name="Administration_p35", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration_p35.view_elements = set()


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


# Screen: Application_Theme_Style_p7
application_theme_style_p7 = Screen(name="Application_Theme_Style_p7", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style", screen_size="Medium")
cancel_1 = Button(
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
application_theme_style_p7.view_elements = {cancel_1, save_1}


# Screen: Background_Load
background_load = Screen(name="Background_Load", description="", view_elements=set(), is_main_page=True, route_path="/Background_Load", screen_size="Medium")
clear = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
load = Button(
    name="Load",
    description="",
    label="Load",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
background_load.view_elements = {clear, load}


# Screen: CSV_Load
csv_load = Screen(name="CSV_Load", description="", view_elements=set(), is_main_page=True, route_path="/CSV_Load", screen_size="Medium")
clear_data = Button(
    name="Clear_Data",
    description="",
    label="Clear_Data",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
clear_file = Button(
    name="Clear_File",
    description="",
    label="Clear_File",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
load_data = Button(
    name="Load_Data",
    description="",
    label="Load_Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
load_file = Button(
    name="Load_File",
    description="",
    label="Load_File",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
next = Button(
    name="Next",
    description="",
    label="Next",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
csv_load.view_elements = {clear_data, clear_file, load_data, load_file, next}


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


# Screen: Data_Load_Results
data_load_results = Screen(name="Data_Load_Results", description="", view_elements=set(), is_main_page=True, route_path="/Data_Load_Results", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
finish = Button(
    name="Finish",
    description="",
    label="Finish",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
data_load_results.view_elements = {cancel_3, finish}


# Screen: Data_Load_Source
data_load_source = Screen(name="Data_Load_Source", description="", view_elements=set(), is_main_page=True, route_path="/Data_Load_Source", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
next_1 = Button(
    name="Next",
    description="",
    label="Next",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
data_load_source.view_elements = {cancel_4, next_1}


# Screen: Data_Loading
data_loading = Screen(name="Data_Loading", description="", view_elements=set(), is_main_page=True, route_path="/Data_Loading", screen_size="Medium")
data_loading.view_elements = set()


# Screen: Data_Validation
data_validation = Screen(name="Data_Validation", description="", view_elements=set(), is_main_page=True, route_path="/Data_Validation", screen_size="Medium")
cancel_5 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
next_2 = Button(
    name="Next",
    description="",
    label="Next",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
previous = Button(
    name="Previous",
    description="",
    label="Previous",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
data_validation.view_elements = {cancel_5, next_2, previous}


# Screen: Eba_demo_load_sales_List
eba_demo_load_sales_list = Screen(name="Eba_demo_load_sales_List", description="", view_elements=set(), is_main_page=True, route_path="/Eba_demo_load_sales_List", screen_size="Medium")
eba_demo_load_sales_list_1_source_0 = DataSourceElement(name="Eba_demo_load_sales")
eba_demo_load_sales_list_1 = DataList(name="Eba_demo_load_sales_List", description="", list_sources={eba_demo_load_sales_list_1_source_0})
eba_demo_load_sales_list.view_elements = {eba_demo_load_sales_list_1}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Load_Data_using_PL_SQL_API
load_data_using_pl_sql_api = Screen(name="Load_Data_using_PL_SQL_API", description="", view_elements=set(), is_main_page=True, route_path="/Load_Data_using_PL_SQL_API", screen_size="Medium")
load_data_1 = Button(
    name="Load_Data",
    description="",
    label="Load_Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
load_data_using_pl_sql_api.view_elements = {load_data_1}


# Screen: Manual_Data_Loading
manual_data_loading = Screen(name="Manual_Data_Loading", description="", view_elements=set(), is_main_page=True, route_path="/Manual_Data_Loading", screen_size="Medium")
manual_data_loading.view_elements = set()


# Screen: Modify_Collection
modify_collection = Screen(name="Modify_Collection", description="", view_elements=set(), is_main_page=True, route_path="/Modify_Collection", screen_size="Medium")
add_member = Button(
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
cancel_6 = Button(
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
modify_collection.view_elements = {add_member, add_member_add_another, cancel_6, delete_collection, resequence, truncate_collection}


# Screen: Modify_Collection_Member_Form
modify_collection_member_form = Screen(name="Modify_Collection_Member_Form", description="", view_elements=set(), route_path="/Modify_Collection_Member_Form", screen_size="Medium")
cancel_7 = Button(
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
modify_collection_member_form.view_elements = {cancel_7, delete_member, update_member}


# Screen: Multiple_File_Types_Load
multiple_file_types_load = Screen(name="Multiple_File_Types_Load", description="", view_elements=set(), is_main_page=True, route_path="/Multiple_File_Types_Load", screen_size="Medium")
clear_1 = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
load_1 = Button(
    name="Load",
    description="",
    label="Load",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
multiple_file_types_load.view_elements = {clear_1, load_1}


# Screen: PL_SQL_Parser
pl_sql_parser = Screen(name="PL_SQL_Parser", description="", view_elements=set(), is_main_page=True, route_path="/PL_SQL_Parser", screen_size="Medium")
upload = Button(
    name="Upload",
    description="",
    label="Upload",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
pl_sql_parser.view_elements = {upload}


# Screen: Remove_Collections
remove_collections = Screen(name="Remove_Collections", description="", view_elements=set(), is_main_page=True, route_path="/Remove_Collections", screen_size="Medium")
cancel_8 = Button(
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
remove_collections.view_elements = {cancel_8, remove_collections_1}


# Screen: Reset_Data
reset_data = Screen(name="Reset_Data", description="", view_elements=set(), is_main_page=True, route_path="/Reset_Data", screen_size="Medium")
cancel_9 = Button(
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
reset_data.view_elements = {cancel_9, reset_data_1}


# Screen: Reset_Data_p39
reset_data_p39 = Screen(name="Reset_Data_p39", description="", view_elements=set(), is_main_page=True, route_path="/Reset_Data", screen_size="Medium")
cancel_10 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_data_2 = Button(
    name="Reset_Data",
    description="",
    label="Reset_Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
reset_data_p39.view_elements = {cancel_10, reset_data_2}


# Screen: Sample_Collections___API_Examples
sample_collections_api_examples = Screen(name="Sample_Collections___API_Examples", description="", view_elements=set(), is_main_page=True, route_path="/Sample_Collections___API_Examples", screen_size="Medium")
sample_collections_api_examples.view_elements = set()


# Screen: Transform_and_Lookup
transform_and_lookup = Screen(name="Transform_and_Lookup", description="", view_elements=set(), is_main_page=True, route_path="/Transform_and_Lookup", screen_size="Medium")
clear_2 = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
load_2 = Button(
    name="Load",
    description="",
    label="Load",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
transform_and_lookup.view_elements = {clear_2, load_2}

oracleapexgui = Module(
    name="OracleApexGUI",
    screens={administration, administration_p35, application_theme_style, application_theme_style_p7, background_load, csv_load, create_collection_form, data_load_results, data_load_source, data_loading, data_validation, eba_demo_load_sales_list, help, load_data_using_pl_sql_api, manual_data_loading, modify_collection, modify_collection_member_form, multiple_file_types_load, pl_sql_parser, remove_collections, reset_data, reset_data_p39, sample_collections_api_examples, transform_and_lookup}
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
    name="create_tables",
    models=[domain_model, gui_model],
    owner="BESSER User",
    metadata=metadata
)
