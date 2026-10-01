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
EbaDemoDaDept = Class(name="EbaDemoDaDept")
EbaDemoDaEmp = Class(name="EbaDemoDaEmp")

# EbaDemoDaDept class attributes and methods
EbaDemoDaDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDaDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDaDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDaDept.attributes={EbaDemoDaDept_deptno, EbaDemoDaDept_dname, EbaDemoDaDept_loc}

# EbaDemoDaEmp class attributes and methods
EbaDemoDaEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDaEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDaEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDaEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDaEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDaEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDaEmp.attributes={EbaDemoDaEmp_comm, EbaDemoDaEmp_empno, EbaDemoDaEmp_ename, EbaDemoDaEmp_hiredate, EbaDemoDaEmp_job, EbaDemoDaEmp_sal}

# Relationships
EbaDemoDaEmp_EbaDemoDaEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaEmp",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodaemp_mgr", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDaEmp_EbaDemoDaDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaDept",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodadept", type=EbaDemoDaDept, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example5",
    types={EbaDemoDaDept, EbaDemoDaEmp},
    associations={EbaDemoDaEmp_EbaDemoDaEmp, EbaDemoDaEmp_EbaDemoDaDept},
    generalizations={},
    metadata=None
)

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
EbaDemoDaDept = Class(name="EbaDemoDaDept")
EbaDemoDaEmp = Class(name="EbaDemoDaEmp")

# EbaDemoDaDept class attributes and methods
EbaDemoDaDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDaDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDaDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDaDept.attributes={EbaDemoDaDept_deptno, EbaDemoDaDept_dname, EbaDemoDaDept_loc}

# EbaDemoDaEmp class attributes and methods
EbaDemoDaEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDaEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDaEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDaEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDaEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDaEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDaEmp.attributes={EbaDemoDaEmp_comm, EbaDemoDaEmp_empno, EbaDemoDaEmp_ename, EbaDemoDaEmp_hiredate, EbaDemoDaEmp_job, EbaDemoDaEmp_sal}

# Relationships
EbaDemoDaEmp_EbaDemoDaEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaEmp",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodaemp_mgr", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDaEmp_EbaDemoDaDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaDept",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodadept", type=EbaDemoDaDept, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example5",
    types={EbaDemoDaDept, EbaDemoDaEmp},
    associations={EbaDemoDaEmp_EbaDemoDaEmp, EbaDemoDaEmp_EbaDemoDaDept},
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

# Module: example5

# Screen: Add_Remove_Class__Error__List
add_remove_class_error_list = Screen(name="Add_Remove_Class__Error__List", description="", view_elements=set(), is_main_page=True, route_path="/Add_Remove_Class__Error__List", screen_size="Medium")
add_remove_class_error_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
add_remove_class_error_list_1_source_0_domain = None
if domain_model_ref is not None:
    add_remove_class_error_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if add_remove_class_error_list_1_source_0_domain:
    add_remove_class_error_list_1_source_0.dataSourceClass = add_remove_class_error_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
add_remove_class_error_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
add_remove_class_error_list_1_source_1_domain = None
if domain_model_ref is not None:
    add_remove_class_error_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if add_remove_class_error_list_1_source_1_domain:
    add_remove_class_error_list_1_source_1.dataSourceClass = add_remove_class_error_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
add_remove_class_error_list_1 = DataList(name="Add/Remove_Class_(Error)_List", description="", list_sources={add_remove_class_error_list_1_source_0, add_remove_class_error_list_1_source_1})
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
add_remove_class_focus_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
add_remove_class_focus_list_1_source_0_domain = None
if domain_model_ref is not None:
    add_remove_class_focus_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if add_remove_class_focus_list_1_source_0_domain:
    add_remove_class_focus_list_1_source_0.dataSourceClass = add_remove_class_focus_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
add_remove_class_focus_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
add_remove_class_focus_list_1_source_1_domain = None
if domain_model_ref is not None:
    add_remove_class_focus_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if add_remove_class_focus_list_1_source_1_domain:
    add_remove_class_focus_list_1_source_1.dataSourceClass = add_remove_class_focus_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
add_remove_class_focus_list_1 = DataList(name="Add/Remove_Class_(Focus)_List", description="", list_sources={add_remove_class_focus_list_1_source_0, add_remove_class_focus_list_1_source_1})
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
    label="Reset Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
administration.view_elements = {cancel, reset_data}


# Screen: Administration_p26
administration_p26 = Screen(name="Administration_p26", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration_p26.view_elements = set()


# Screen: Application_Theme_Style_Form
application_theme_style_form = Screen(name="Application_Theme_Style_Form", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style_Form", screen_size="Medium")
p24_desktop_theme_style_id = InputField(
    name="P24_DESKTOP_THEME_STYLE_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Desktop Theme Style",
    required=True
)
application_theme_style_fields_1 = Form(name="Application_Theme_Style_fields_1", description="", inputFields={p24_desktop_theme_style_id})
cancel_1 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
application_theme_style_form.view_elements = {application_theme_style_fields_1, cancel_1}


# Screen: Debounce_and_Throttle
debounce_and_throttle = Screen(name="Debounce_and_Throttle", description="", view_elements=set(), is_main_page=True, route_path="/Debounce_and_Throttle", screen_size="Medium")
debounce_and_throttle.view_elements = set()


# Screen: Delete_and_Refresh_List
delete_and_refresh_list = Screen(name="Delete_and_Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Delete_and_Refresh_List", screen_size="Medium")
delete_and_refresh_list_1_source_0 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
delete_and_refresh_list_1_source_0_domain = None
if domain_model_ref is not None:
    delete_and_refresh_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if delete_and_refresh_list_1_source_0_domain:
    delete_and_refresh_list_1_source_0.dataSourceClass = delete_and_refresh_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
delete_and_refresh_list_1_source_1 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
delete_and_refresh_list_1_source_1_domain = None
if domain_model_ref is not None:
    delete_and_refresh_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if delete_and_refresh_list_1_source_1_domain:
    delete_and_refresh_list_1_source_1.dataSourceClass = delete_and_refresh_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
delete_and_refresh_list_1 = DataList(name="Delete_and_Refresh_List", description="", list_sources={delete_and_refresh_list_1_source_0, delete_and_refresh_list_1_source_1})
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
disable_enable_list_1_source_0 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
disable_enable_list_1_source_0_domain = None
if domain_model_ref is not None:
    disable_enable_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if disable_enable_list_1_source_0_domain:
    disable_enable_list_1_source_0.dataSourceClass = disable_enable_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
disable_enable_list_1_source_1 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
disable_enable_list_1_source_1_domain = None
if domain_model_ref is not None:
    disable_enable_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if disable_enable_list_1_source_1_domain:
    disable_enable_list_1_source_1.dataSourceClass = disable_enable_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
disable_enable_list_1 = DataList(name="Disable/Enable_List", description="", list_sources={disable_enable_list_1_source_0, disable_enable_list_1_source_1})
reset_3 = Button(
    name="Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
disable_enable_list.view_elements = {disable_enable_list_1, reset_3}


# Screen: Edit_Form
edit_form = Screen(name="Edit_Form", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_2 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p3_comm = InputField(
    name="P3_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p3_rowid = InputField(name="P3_ROWID", description="", field_type=InputFieldType.Hidden)
p3_sal = InputField(
    name="P3_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p3_deptno = InputField(
    name="P3_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p3_job = InputField(
    name="P3_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p3_empno = InputField(
    name="P3_EMPNO",
    description="",
    field_type=InputFieldType.Number,
    label="Employee Number",
    required=True
)
p3_ename = InputField(
    name="P3_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
p3_hiredate = InputField(
    name="P3_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p3_mgr = InputField(
    name="P3_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
edit_fields_1 = Form(name="Edit_fields_1", description="", inputFields={p3_comm, p3_rowid, p3_sal, p3_deptno, p3_job, p3_empno, p3_ename, p3_hiredate, p3_mgr})
edit_form.view_elements = {cancel_2, edit_fields_1}


# Screen: Edit_Form_p13
edit_form_p13 = Screen(name="Edit_Form_p13", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p13_empno = InputField(
    name="P13_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
p13_rowid = InputField(name="P13_ROWID", description="", field_type=InputFieldType.Hidden)
p13_mgr = InputField(
    name="P13_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p13_hiredate = InputField(
    name="P13_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p13_job = InputField(
    name="P13_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p13_deptno = InputField(
    name="P13_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p13_comm = InputField(
    name="P13_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p13_ename = InputField(
    name="P13_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
p13_location = InputField(
    name="P13_LOCATION",
    description="",
    field_type=InputFieldType.Text,
    label="Location"
)
p13_sal = InputField(
    name="P13_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p13_no_of_employees = InputField(
    name="P13_NO_OF_EMPLOYEES",
    description="",
    field_type=InputFieldType.Text,
    label="Number of Employees"
)
edit_fields_1_1 = Form(name="Edit_fields_1", description="", inputFields={p13_empno, p13_rowid, p13_mgr, p13_hiredate, p13_job, p13_deptno, p13_comm, p13_ename, p13_location, p13_sal, p13_no_of_employees})
edit_form_p13.view_elements = {cancel_3, edit_fields_1_1}


# Screen: Edit_Form_p15
edit_form_p15 = Screen(name="Edit_Form_p15", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p15_hiredate = InputField(
    name="P15_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p15_deptno = InputField(
    name="P15_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p15_job = InputField(
    name="P15_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p15_mgr = InputField(
    name="P15_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p15_rowid = InputField(name="P15_ROWID", description="", field_type=InputFieldType.Hidden)
p15_comm = InputField(
    name="P15_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p15_sal = InputField(
    name="P15_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p15_empno = InputField(
    name="P15_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
p15_ename = InputField(
    name="P15_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
edit_fields_1_2 = Form(name="Edit_fields_1", description="", inputFields={p15_hiredate, p15_deptno, p15_job, p15_mgr, p15_rowid, p15_comm, p15_sal, p15_empno, p15_ename})
edit_form_p15.view_elements = {cancel_4, edit_fields_1_2}


# Screen: Edit_Form_p22
edit_form_p22 = Screen(name="Edit_Form_p22", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_5 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p22_empno = InputField(
    name="P22_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
p22_deptno = InputField(
    name="P22_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p22_job = InputField(
    name="P22_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p22_hiredate = InputField(
    name="P22_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p22_sal = InputField(
    name="P22_SAL",
    description="",
    field_type=InputFieldType.Text,
    label="Salary"
)
p22_comm = InputField(
    name="P22_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p22_mgr = InputField(
    name="P22_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p22_rowid = InputField(name="P22_ROWID", description="", field_type=InputFieldType.Hidden)
p22_ename = InputField(
    name="P22_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
edit_fields_1_3 = Form(name="Edit_fields_1", description="", inputFields={p22_empno, p22_deptno, p22_job, p22_hiredate, p22_sal, p22_comm, p22_mgr, p22_rowid, p22_ename})
edit_form_p22.view_elements = {cancel_5, edit_fields_1_3}


# Screen: Edit_Form_p5
edit_form_p5 = Screen(name="Edit_Form_p5", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_6 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p5_hiredate = InputField(
    name="P5_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p5_ename = InputField(
    name="P5_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
p5_comm = InputField(
    name="P5_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p5_rowid = InputField(name="P5_ROWID", description="", field_type=InputFieldType.Hidden)
p5_mgr = InputField(
    name="P5_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p5_empno = InputField(
    name="P5_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
p5_job = InputField(
    name="P5_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p5_deptno = InputField(
    name="P5_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p5_sal = InputField(
    name="P5_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
edit_fields_1_4 = Form(name="Edit_fields_1", description="", inputFields={p5_hiredate, p5_ename, p5_comm, p5_rowid, p5_mgr, p5_empno, p5_job, p5_deptno, p5_sal})
edit_form_p5.view_elements = {cancel_6, edit_fields_1_4}


# Screen: Edit_Form_p7
edit_form_p7 = Screen(name="Edit_Form_p7", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_7 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p7_comm = InputField(
    name="P7_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p7_ename = InputField(
    name="P7_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    required=True
)
p7_hiredate = InputField(
    name="P7_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
p7_deptno = InputField(
    name="P7_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p7_mgr = InputField(
    name="P7_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p7_job = InputField(
    name="P7_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p7_sal = InputField(
    name="P7_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p7_rowid = InputField(name="P7_ROWID", description="", field_type=InputFieldType.Hidden)
p7_empno = InputField(
    name="P7_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
edit_fields_1_5 = Form(name="Edit_fields_1", description="", inputFields={p7_comm, p7_ename, p7_hiredate, p7_deptno, p7_mgr, p7_job, p7_sal, p7_rowid, p7_empno})
edit_form_p7.view_elements = {cancel_7, edit_fields_1_5}


# Screen: Edit_Form_p9
edit_form_p9 = Screen(name="Edit_Form_p9", description="", view_elements=set(), is_main_page=True, route_path="/Edit_Form", screen_size="Medium")
cancel_8 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p9_mgr = InputField(
    name="P9_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
p9_rowid = InputField(name="P9_ROWID", description="", field_type=InputFieldType.Hidden)
p9_sal = InputField(
    name="P9_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p9_job = InputField(
    name="P9_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p9_comm = InputField(
    name="P9_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p9_deptno = InputField(
    name="P9_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
p9_empno = InputField(
    name="P9_EMPNO",
    description="",
    field_type=InputFieldType.Text,
    label="Employee Number",
    required=True
)
p9_ename = InputField(
    name="P9_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
p9_hiredate = InputField(
    name="P9_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire date"
)
edit_fields_1_6 = Form(name="Edit_fields_1", description="", inputFields={p9_mgr, p9_rowid, p9_sal, p9_job, p9_comm, p9_deptno, p9_empno, p9_ename, p9_hiredate})
edit_form_p9.view_elements = {cancel_8, edit_fields_1_6}


# Screen: Execute_PL_SQL_Code_List
execute_pl_sql_code_list = Screen(name="Execute_PL_SQL_Code_List", description="", view_elements=set(), is_main_page=True, route_path="/Execute_PL_SQL_Code_List", screen_size="Medium")
execute_pl_sql_code_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
execute_pl_sql_code_list_1_source_0_domain = None
if domain_model_ref is not None:
    execute_pl_sql_code_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if execute_pl_sql_code_list_1_source_0_domain:
    execute_pl_sql_code_list_1_source_0.dataSourceClass = execute_pl_sql_code_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
execute_pl_sql_code_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
execute_pl_sql_code_list_1_source_1_domain = None
if domain_model_ref is not None:
    execute_pl_sql_code_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if execute_pl_sql_code_list_1_source_1_domain:
    execute_pl_sql_code_list_1_source_1.dataSourceClass = execute_pl_sql_code_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
execute_pl_sql_code_list_1 = DataList(name="Execute_PL/SQL_Code_List", description="", list_sources={execute_pl_sql_code_list_1_source_0, execute_pl_sql_code_list_1_source_1})
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
    label="Update Salary by 10%",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
execute_pl_sql_code_list.view_elements = {execute_pl_sql_code_list_1, reset_4, update_salary}


# Screen: Filter_and_Refresh_List
filter_and_refresh_list = Screen(name="Filter_and_Refresh_List", description="", view_elements=set(), is_main_page=True, route_path="/Filter_and_Refresh_List", screen_size="Medium")
filter_and_refresh_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
filter_and_refresh_list_1_source_0_domain = None
if domain_model_ref is not None:
    filter_and_refresh_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if filter_and_refresh_list_1_source_0_domain:
    filter_and_refresh_list_1_source_0.dataSourceClass = filter_and_refresh_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
filter_and_refresh_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
filter_and_refresh_list_1_source_1_domain = None
if domain_model_ref is not None:
    filter_and_refresh_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if filter_and_refresh_list_1_source_1_domain:
    filter_and_refresh_list_1_source_1.dataSourceClass = filter_and_refresh_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
filter_and_refresh_list_1 = DataList(name="Filter_and_Refresh_List", description="", list_sources={filter_and_refresh_list_1_source_0, filter_and_refresh_list_1_source_1})
p19_reset = Button(
    name="P19_Reset",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
filter_and_refresh_list.view_elements = {filter_and_refresh_list_1, p19_reset}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Hide_Show_List
hide_show_list = Screen(name="Hide_Show_List", description="", view_elements=set(), is_main_page=True, route_path="/Hide_Show_List", screen_size="Medium")
hide_show_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
hide_show_list_1_source_0_domain = None
if domain_model_ref is not None:
    hide_show_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if hide_show_list_1_source_0_domain:
    hide_show_list_1_source_0.dataSourceClass = hide_show_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
hide_show_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
hide_show_list_1_source_1_domain = None
if domain_model_ref is not None:
    hide_show_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if hide_show_list_1_source_1_domain:
    hide_show_list_1_source_1.dataSourceClass = hide_show_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
hide_show_list_1 = DataList(name="Hide/Show_List", description="", list_sources={hide_show_list_1_source_0, hide_show_list_1_source_1})
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
refresh_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
refresh_list_1_source_0_domain = None
if domain_model_ref is not None:
    refresh_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if refresh_list_1_source_0_domain:
    refresh_list_1_source_0.dataSourceClass = refresh_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
refresh_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
refresh_list_1_source_1_domain = None
if domain_model_ref is not None:
    refresh_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if refresh_list_1_source_1_domain:
    refresh_list_1_source_1.dataSourceClass = refresh_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
refresh_list_1 = DataList(name="Refresh_List", description="", list_sources={refresh_list_1_source_0, refresh_list_1_source_1})
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
set_values_pl_sql_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
set_values_pl_sql_list_1_source_0_domain = None
if domain_model_ref is not None:
    set_values_pl_sql_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if set_values_pl_sql_list_1_source_0_domain:
    set_values_pl_sql_list_1_source_0.dataSourceClass = set_values_pl_sql_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
set_values_pl_sql_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
set_values_pl_sql_list_1_source_1_domain = None
if domain_model_ref is not None:
    set_values_pl_sql_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if set_values_pl_sql_list_1_source_1_domain:
    set_values_pl_sql_list_1_source_1.dataSourceClass = set_values_pl_sql_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
set_values_pl_sql_list_1 = DataList(name="Set_Values_(PL/SQL)_List", description="", list_sources={set_values_pl_sql_list_1_source_0, set_values_pl_sql_list_1_source_1})
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
set_values_sql_list_1_source_0 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
set_values_sql_list_1_source_0_domain = None
if domain_model_ref is not None:
    set_values_sql_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if set_values_sql_list_1_source_0_domain:
    set_values_sql_list_1_source_0.dataSourceClass = set_values_sql_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
set_values_sql_list_1_source_1 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
set_values_sql_list_1_source_1_domain = None
if domain_model_ref is not None:
    set_values_sql_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if set_values_sql_list_1_source_1_domain:
    set_values_sql_list_1_source_1.dataSourceClass = set_values_sql_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
set_values_sql_list_1 = DataList(name="Set_Values_(SQL)_List", description="", list_sources={set_values_sql_list_1_source_0, set_values_sql_list_1_source_1})
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
shuttle_refresh_list_1_source_0 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
shuttle_refresh_list_1_source_0_domain = None
if domain_model_ref is not None:
    shuttle_refresh_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if shuttle_refresh_list_1_source_0_domain:
    shuttle_refresh_list_1_source_0.dataSourceClass = shuttle_refresh_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
shuttle_refresh_list_1_source_1 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
shuttle_refresh_list_1_source_1_domain = None
if domain_model_ref is not None:
    shuttle_refresh_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if shuttle_refresh_list_1_source_1_domain:
    shuttle_refresh_list_1_source_1.dataSourceClass = shuttle_refresh_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
shuttle_refresh_list_1 = DataList(name="Shuttle_Refresh_List", description="", list_sources={shuttle_refresh_list_1_source_0, shuttle_refresh_list_1_source_1})
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
stripe_report_list_1_source_0 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
stripe_report_list_1_source_0_domain = None
if domain_model_ref is not None:
    stripe_report_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if stripe_report_list_1_source_0_domain:
    stripe_report_list_1_source_0.dataSourceClass = stripe_report_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
stripe_report_list_1_source_1 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
stripe_report_list_1_source_1_domain = None
if domain_model_ref is not None:
    stripe_report_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if stripe_report_list_1_source_1_domain:
    stripe_report_list_1_source_1.dataSourceClass = stripe_report_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
stripe_report_list_1 = DataList(name="Stripe_Report_List", description="", list_sources={stripe_report_list_1_source_0, stripe_report_list_1_source_1})
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
timer_list_1_source_0 = DataSourceElement(name="EbaDemoDaDept")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
timer_list_1_source_0_domain = None
if domain_model_ref is not None:
    timer_list_1_source_0_domain = domain_model_ref.get_class_by_name("EbaDemoDaDept")
if timer_list_1_source_0_domain:
    timer_list_1_source_0.dataSourceClass = timer_list_1_source_0_domain
else:
    pass
    # Domain class 'EbaDemoDaDept' not resolved for data source 'EbaDemoDaDept'.
timer_list_1_source_1 = DataSourceElement(name="EbaDemoDaEmp")
domain_model_ref = globals().get('domain_model') or _evaluation_builtins.next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
timer_list_1_source_1_domain = None
if domain_model_ref is not None:
    timer_list_1_source_1_domain = domain_model_ref.get_class_by_name("EbaDemoDaEmp")
if timer_list_1_source_1_domain:
    timer_list_1_source_1.dataSourceClass = timer_list_1_source_1_domain
else:
    pass
    # Domain class 'EbaDemoDaEmp' not resolved for data source 'EbaDemoDaEmp'.
timer_list_1 = DataList(name="Timer_List", description="", list_sources={timer_list_1_source_0, timer_list_1_source_1})
timer_list.view_elements = {reset_11, timer_list_1}

example5 = Module(
    name="example5",
    screens={add_remove_class_error_list, add_remove_class_focus_list, administration, administration_p26, application_theme_style_form, debounce_and_throttle, delete_and_refresh_list, disable_enable_list, edit_form, edit_form_p13, edit_form_p15, edit_form_p22, edit_form_p5, edit_form_p7, edit_form_p9, execute_pl_sql_code_list, filter_and_refresh_list, help, hide_show_list, refresh_list, set_values_pl_sql_list, set_values_sql_list, shuttle_refresh_list, stripe_report_list, timer_list}
)

# GUI Model
gui_model = GUIModel(
    name="example5",
    package="",
    versionCode="",
    versionName="",
    modules={example5},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition

# Restore fields omitted by the installed BESSER code builder.
add_remove_class_error_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in add_remove_class_error_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in add_remove_class_error_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
add_remove_class_focus_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in add_remove_class_focus_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in add_remove_class_focus_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
application_theme_style_fields_1.title = 'Application Theme Style'
application_theme_style_fields_1.submit_label = 'Apply Changes'
delete_and_refresh_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in delete_and_refresh_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
_evaluation_builtins.next(s for s in delete_and_refresh_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
disable_enable_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in disable_enable_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
_evaluation_builtins.next(s for s in disable_enable_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
edit_fields_1.title = 'Edit'
edit_fields_1.submit_label = 'Apply Changes'
edit_fields_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_1.title = 'Edit'
edit_fields_1_1.submit_label = 'Apply Changes'
edit_fields_1_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_2.title = 'Edit'
edit_fields_1_2.submit_label = 'Apply Changes'
edit_fields_1_2.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_3.title = 'Edit'
edit_fields_1_3.submit_label = 'Apply Changes'
edit_fields_1_3.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_4.title = 'Edit'
edit_fields_1_4.submit_label = 'Apply Changes'
edit_fields_1_4.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_5.title = 'Edit'
edit_fields_1_5.submit_label = 'Apply Changes'
edit_fields_1_5.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
edit_fields_1_6.title = 'Edit'
edit_fields_1_6.submit_label = 'Apply Changes'
edit_fields_1_6.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
execute_pl_sql_code_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in execute_pl_sql_code_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in execute_pl_sql_code_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
filter_and_refresh_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in filter_and_refresh_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in filter_and_refresh_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
hide_show_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in hide_show_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in hide_show_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
refresh_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in refresh_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in refresh_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
set_values_pl_sql_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in set_values_pl_sql_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in set_values_pl_sql_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
set_values_sql_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in set_values_sql_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
_evaluation_builtins.next(s for s in set_values_sql_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
shuttle_refresh_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in shuttle_refresh_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
_evaluation_builtins.next(s for s in shuttle_refresh_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
stripe_report_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in stripe_report_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
_evaluation_builtins.next(s for s in stripe_report_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []
timer_list_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoDaEmp'))
_evaluation_builtins.next(s for s in timer_list_1.list_sources if s.name == 'EbaDemoDaDept').field_names = []
_evaluation_builtins.next(s for s in timer_list_1.list_sources if s.name == 'EbaDemoDaEmp').field_names = []

from besser.BUML.metamodel.project import Project
project = Project(name='example5', models=[domain_model, gui_model])
