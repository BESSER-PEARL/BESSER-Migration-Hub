import builtins as _evaluation_builtins
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
EbaDemoLoadSales_order_priority: Property = Property(name="order_priority", type=StringType)
EbaDemoLoadSales_order_date: Property = Property(name="order_date", type=DateType)
EbaDemoLoadSales_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoLoadSales_ship_date: Property = Property(name="ship_date", type=DateType)
EbaDemoLoadSales_units_sold: Property = Property(name="units_sold", type=IntegerType)
EbaDemoLoadSales_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoLoadSales_unit_cost: Property = Property(name="unit_cost", type=IntegerType)
EbaDemoLoadSales_total_revenue: Property = Property(name="total_revenue", type=IntegerType)
EbaDemoLoadSales_total_cost: Property = Property(name="total_cost", type=IntegerType)
EbaDemoLoadSales_total_profit: Property = Property(name="total_profit", type=IntegerType)
EbaDemoLoadSales_created: Property = Property(name="created", type=DateType)
EbaDemoLoadSales_last_updated: Property = Property(name="last_updated", type=DateType)
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
    name="example2",
    types={EbaDemoLoadDept, EbaDemoLoadEmp, EbaDemoLoadSales},
    associations={EbaDemoLoadEmp_EbaDemoLoadEmp, EbaDemoLoadEmp_EbaDemoLoadDept},
    generalizations={},
    metadata=None
)


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

# Module: example2

# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration.view_elements = set()


# Screen: Application_Theme_Style_Form
application_theme_style_form = Screen(name="Application_Theme_Style_Form", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style_Form", screen_size="Medium")
p7_desktop_theme_style_id = InputField(
    name="P7_DESKTOP_THEME_STYLE_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Desktop Theme Style",
    required=True
)
application_theme_style_fields_1 = Form(name="Application_Theme_Style_fields_1", description="", inputFields={p7_desktop_theme_style_id})
cancel = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
application_theme_style_form.view_elements = {application_theme_style_fields_1, cancel}


# Screen: Background_Load_Form
background_load_form = Screen(name="Background_Load_Form", description="", view_elements=set(), is_main_page=True, route_path="/Background_Load_Form", screen_size="Medium")
p17_file = InputField(
    name="P17_FILE",
    description="",
    field_type=InputFieldType.File,
    label="Upload a File"
)
p17_processed_rows = InputField(name="P17_PROCESSED_ROWS", description="", field_type=InputFieldType.Hidden)
p17_file_name = InputField(
    name="P17_FILE_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Loaded File"
)
p17_load_exec_id = InputField(name="P17_LOAD_EXEC_ID", description="", field_type=InputFieldType.Hidden)
p17_error_rows = InputField(name="P17_ERROR_ROWS", description="", field_type=InputFieldType.Hidden)
background_load_fields_1 = Form(name="Background_Load_fields_1", description="", inputFields={p17_file, p17_processed_rows, p17_file_name, p17_load_exec_id, p17_error_rows})
clear = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
background_load_form.view_elements = {background_load_fields_1, clear}


# Screen: CSV_Load_Form
csv_load_form = Screen(name="CSV_Load_Form", description="", view_elements=set(), is_main_page=True, route_path="/CSV_Load_Form", screen_size="Medium")
p11_copy_paste_error_row_count = InputField(name="P11_COPY_PASTE_ERROR_ROW_COUNT", description="", field_type=InputFieldType.Hidden)
p11_file = InputField(
    name="P11_FILE",
    description="",
    field_type=InputFieldType.File,
    label="Upload a File"
)
p11_data = InputField(
    name="P11_DATA",
    description="",
    field_type=InputFieldType.TextArea,
    label="Copy and Paste Delimited Data"
)
p11_pasted_data = InputField(
    name="P11_PASTED_DATA",
    description="",
    field_type=InputFieldType.Text,
    label="Pasted Data"
)
p11_file_error_row_count = InputField(name="P11_FILE_ERROR_ROW_COUNT", description="", field_type=InputFieldType.Hidden)
p11_file_name = InputField(
    name="P11_FILE_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Loaded File"
)
csv_load_fields_1 = Form(name="CSV_Load_fields_1", description="", inputFields={p11_copy_paste_error_row_count, p11_file, p11_data, p11_pasted_data, p11_file_error_row_count, p11_file_name})
clear_data = Button(
    name="Clear_Data",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
clear_file = Button(
    name="Clear_File",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
load_file = Button(
    name="Load_File",
    description="",
    label="Load Data",
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
csv_load_form.view_elements = {csv_load_fields_1, clear_data, clear_file, load_file, next}


# Screen: Data_Load_Results
data_load_results = Screen(name="Data_Load_Results", description="", view_elements=set(), is_main_page=True, route_path="/Data_Load_Results", screen_size="Medium")
cancel_1 = Button(
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
data_load_results.view_elements = {cancel_1, finish}


# Screen: Data_Load_Source
data_load_source = Screen(name="Data_Load_Source", description="", view_elements=set(), is_main_page=True, route_path="/Data_Load_Source", screen_size="Medium")
cancel_2 = Button(
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
data_load_source.view_elements = {cancel_2, next_1}


# Screen: Data_Loading
data_loading = Screen(name="Data_Loading", description="", view_elements=set(), is_main_page=True, route_path="/Data_Loading", screen_size="Medium")
data_loading.view_elements = set()


# Screen: Data_Validation
data_validation = Screen(name="Data_Validation", description="", view_elements=set(), is_main_page=True, route_path="/Data_Validation", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
next_2 = Button(
    name="Next",
    description="",
    label="Load Data",
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
data_validation.view_elements = {cancel_3, next_2, previous}


# Screen: Eba_demo_load_sales_List
eba_demo_load_sales_list = Screen(name="Eba_demo_load_sales_List", description="", view_elements=set(), is_main_page=True, route_path="/Eba_demo_load_sales_List", screen_size="Medium")
eba_demo_load_sales_list_1_source_0 = DataSourceElement(name="EbaDemoLoadSales")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
eba_demo_load_sales_list_1_source_0_domain = None
if domain_model_ref is not None:
    eba_demo_load_sales_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoLoadSales")
if eba_demo_load_sales_list_1_source_0_domain:
    eba_demo_load_sales_list_1_source_0.dataSourceClass = eba_demo_load_sales_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoLoadSales' not resolved for data source 'EbaDemoLoadSales'.
eba_demo_load_sales_list_1 = DataList(name="Eba_demo_load_sales_List", description="", list_sources={eba_demo_load_sales_list_1_source_0})
eba_demo_load_sales_list.view_elements = {eba_demo_load_sales_list_1}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Load_Data_using_PL_SQL_API_Form
load_data_using_pl_sql_api_form = Screen(name="Load_Data_using_PL_SQL_API_Form", description="", view_elements=set(), is_main_page=True, route_path="/Load_Data_using_PL_SQL_API_Form", screen_size="Medium")
p32_sample_data = InputField(name="P32_SAMPLE_DATA", description="", field_type=InputFieldType.Hidden)
p32_rows_loaded = InputField(name="P32_ROWS_LOADED", description="", field_type=InputFieldType.Hidden)
p32_rows_failed = InputField(name="P32_ROWS_FAILED", description="", field_type=InputFieldType.Hidden)
p32_data = InputField(
    name="P32_DATA",
    description="",
    field_type=InputFieldType.TextArea,
    label="Copy and Paste Delimited Data"
)
load_data_using_pl_sql_api_fields_1 = Form(name="Load_Data_using_PL_SQL_API_fields_1", description="", inputFields={p32_sample_data, p32_rows_loaded, p32_rows_failed, p32_data})
load_data_using_pl_sql_api_form.view_elements = {load_data_using_pl_sql_api_fields_1}


# Screen: Manual_Data_Loading
manual_data_loading = Screen(name="Manual_Data_Loading", description="", view_elements=set(), is_main_page=True, route_path="/Manual_Data_Loading", screen_size="Medium")
manual_data_loading.view_elements = set()


# Screen: Multiple_File_Types_Load_Form
multiple_file_types_load_form = Screen(name="Multiple_File_Types_Load_Form", description="", view_elements=set(), is_main_page=True, route_path="/Multiple_File_Types_Load_Form", screen_size="Medium")
clear_1 = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p16_file_name = InputField(
    name="P16_FILE_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Loaded File"
)
p16_xlsx_worksheet = InputField(
    name="P16_XLSX_WORKSHEET",
    description="",
    field_type=InputFieldType.Dropdown,
    label="XLSX Worksheet"
)
p16_processed_row_count = InputField(name="P16_PROCESSED_ROW_COUNT", description="", field_type=InputFieldType.Hidden)
p16_error_row_count = InputField(name="P16_ERROR_ROW_COUNT", description="", field_type=InputFieldType.Hidden)
p16_file_type = InputField(name="P16_FILE_TYPE", description="", field_type=InputFieldType.Hidden)
p16_file = InputField(
    name="P16_FILE",
    description="",
    field_type=InputFieldType.File,
    label="Upload a File"
)
multiple_file_types_load_fields_1 = Form(name="Multiple_File_Types_Load_fields_1", description="", inputFields={p16_file_name, p16_xlsx_worksheet, p16_processed_row_count, p16_error_row_count, p16_file_type, p16_file})
multiple_file_types_load_form.view_elements = {clear_1, multiple_file_types_load_fields_1}


# Screen: PL_SQL_Parser_Form
pl_sql_parser_form = Screen(name="PL_SQL_Parser_Form", description="", view_elements=set(), is_main_page=True, route_path="/PL_SQL_Parser_Form", screen_size="Medium")
p31_xlsx_worksheet = InputField(
    name="P31_XLSX_WORKSHEET",
    description="",
    field_type=InputFieldType.Dropdown,
    label="XLSX Worksheet"
)
p31_file = InputField(
    name="P31_FILE",
    description="",
    field_type=InputFieldType.File,
    label="Upload a File"
)
pl_sql_parser_fields_1 = Form(name="PL_SQL_Parser_fields_1", description="", inputFields={p31_xlsx_worksheet, p31_file})
pl_sql_parser_form.view_elements = {pl_sql_parser_fields_1}


# Screen: Reset_Data
reset_data = Screen(name="Reset_Data", description="", view_elements=set(), is_main_page=True, route_path="/Reset_Data", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_data_1 = Button(
    name="Reset_Data",
    description="",
    label="Reset Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
reset_data.view_elements = {cancel_4, reset_data_1}


# Screen: Transform_and_Lookup_Form
transform_and_lookup_form = Screen(name="Transform_and_Lookup_Form", description="", view_elements=set(), is_main_page=True, route_path="/Transform_and_Lookup_Form", screen_size="Medium")
clear_2 = Button(
    name="Clear",
    description="",
    label="Clear",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p15_error_row_count = InputField(name="P15_ERROR_ROW_COUNT", description="", field_type=InputFieldType.Hidden)
p15_file_name = InputField(
    name="P15_FILE_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Loaded File"
)
p15_file = InputField(
    name="P15_FILE",
    description="",
    field_type=InputFieldType.File,
    label="Upload a File"
)
transform_and_lookup_fields_1 = Form(name="Transform_and_Lookup_fields_1", description="", inputFields={p15_error_row_count, p15_file_name, p15_file})
transform_and_lookup_form.view_elements = {clear_2, transform_and_lookup_fields_1}

example2 = Module(
    name="example2",
    screens={administration, application_theme_style_form, background_load_form, csv_load_form, data_load_results, data_load_source, data_loading, data_validation, eba_demo_load_sales_list, help, load_data_using_pl_sql_api_form, manual_data_loading, multiple_file_types_load_form, pl_sql_parser_form, reset_data, transform_and_lookup_form}
)

# GUI Model
gui_model = GUIModel(
    name="example2",
    package="",
    versionCode="",
    versionName="",
    modules={example2},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition
application_theme_style_fields_1.title = 'Application Theme Style'
application_theme_style_fields_1.submit_label = 'Apply Changes'
background_load_fields_1.title = 'Background Load'
background_load_fields_1.submit_label = 'Load Data'
csv_load_fields_1.title = 'CSV Load'
csv_load_fields_1.submit_label = 'Load Data'
eba_demo_load_sales_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoLoadSales'))
_evaluation_builtins.next(s for s in eba_demo_load_sales_list_1.list_sources if s.name == 'EbaDemoLoadSales').field_names = []
load_data_using_pl_sql_api_fields_1.title = 'Load Data using PL/SQL API'
load_data_using_pl_sql_api_fields_1.submit_label = 'Load Data'
multiple_file_types_load_fields_1.title = 'Multiple File Types Load'
multiple_file_types_load_fields_1.submit_label = 'Load Data'
pl_sql_parser_fields_1.title = 'PL/SQL Parser'
pl_sql_parser_fields_1.submit_label = 'Upload File'
transform_and_lookup_fields_1.title = 'Transform and Lookup'
transform_and_lookup_fields_1.submit_label = 'Load Data'
