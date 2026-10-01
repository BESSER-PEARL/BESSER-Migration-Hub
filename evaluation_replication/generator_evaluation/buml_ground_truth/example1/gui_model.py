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
EbaDemoCsEmp = Class(name="EbaDemoCsEmp")

# EbaDemoCsEmp class attributes and methods
EbaDemoCsEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoCsEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoCsEmp_job: Property = Property(name="job", type=StringType)
EbaDemoCsEmp_mgr: Property = Property(name="mgr", type=IntegerType)
EbaDemoCsEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoCsEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoCsEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoCsEmp_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoCsEmp.attributes={EbaDemoCsEmp_comm, EbaDemoCsEmp_deptno, EbaDemoCsEmp_empno, EbaDemoCsEmp_ename, EbaDemoCsEmp_hiredate, EbaDemoCsEmp_job, EbaDemoCsEmp_mgr, EbaDemoCsEmp_sal}

# Domain Model
domain_model = DomainModel(
    name="example1",
    types={EbaDemoCsEmp},
    associations={},
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

# Module: example1

# Screen: Add_Edit_Collection_Member_Form
add_edit_collection_member_form = Screen(name="Add_Edit_Collection_Member_Form", description="", view_elements=set(), route_path="/Add_Edit_Collection_Member_Form", screen_size="Medium")
p7_deptno = InputField(
    name="P7_DEPTNO",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Dept&nbsp;No"
)
p7_comm = InputField(
    name="P7_COMM",
    description="",
    field_type=InputFieldType.Number,
    label="Commission"
)
p7_sal = InputField(
    name="P7_SAL",
    description="",
    field_type=InputFieldType.Number,
    label="Salary"
)
p7_hiredate = InputField(
    name="P7_HIREDATE",
    description="",
    field_type=InputFieldType.Date,
    label="Hire&nbsp;Date"
)
p7_xmltype = InputField(
    name="P7_XMLTYPE",
    description="",
    field_type=InputFieldType.TextArea,
    label="XMLType"
)
p7_ename = InputField(
    name="P7_ENAME",
    description="",
    field_type=InputFieldType.Text,
    label="Employee&nbsp;Name"
)
p7_seq = InputField(name="P7_SEQ", description="", field_type=InputFieldType.Hidden)
p7_job = InputField(
    name="P7_JOB",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Job"
)
p7_empno = InputField(
    name="P7_EMPNO",
    description="",
    field_type=InputFieldType.Number,
    label="Emp&nbsp;No"
)
p7_status = InputField(
    name="P7_STATUS",
    description="",
    field_type=InputFieldType.Text,
    label="Status"
)
p7_mgr = InputField(
    name="P7_MGR",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Manager"
)
add_edit_collection_member_fields_1 = Form(name="Add_Edit_Collection_Member_fields_1", description="", inputFields={p7_deptno, p7_comm, p7_sal, p7_hiredate, p7_xmltype, p7_ename, p7_seq, p7_job, p7_empno, p7_status, p7_mgr})
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
    label="Delete Member",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
update_member = Button(
    name="Update_Member",
    description="",
    label="Update Member",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
add_edit_collection_member_form.view_elements = {add_edit_collection_member_fields_1, cancel, delete_member, update_member}


# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration.view_elements = set()


# Screen: Application_Theme_Style_Form
application_theme_style_form = Screen(name="Application_Theme_Style_Form", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style_Form", screen_size="Medium")
p5_desktop_theme_style_id = InputField(
    name="P5_DESKTOP_THEME_STYLE_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Desktop Theme Style",
    required=True
)
application_theme_style_fields_1 = Form(name="Application_Theme_Style_fields_1", description="", inputFields={p5_desktop_theme_style_id})
cancel_1 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
application_theme_style_form.view_elements = {application_theme_style_fields_1, cancel_1}


# Screen: Create_Collection_Form
create_collection_form = Screen(name="Create_Collection_Form", description="", view_elements=set(), route_path="/Create_Collection_Form", screen_size="Medium")
cancel_2 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p2_name = InputField(
    name="P2_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Collection Name",
    required=True
)
create_collection_fields_1 = Form(name="Create_Collection_fields_1", description="", inputFields={p2_name})
create_replace = Button(
    name="Create_Replace",
    description="",
    label="Create/Replace Collection",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_collection_form.view_elements = {cancel_2, create_collection_fields_1, create_replace}


# Screen: Data_Synchronization
data_synchronization = Screen(name="Data_Synchronization", description="", view_elements=set(), is_main_page=True, route_path="/Data_Synchronization", screen_size="Medium")
add_member = Button(
    name="Add_Member",
    description="",
    label="Add Member",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
apply_collection = Button(
    name="Apply_Collection",
    description="",
    label="Apply Collection",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
populate = Button(
    name="Populate",
    description="",
    label="Populate Collection from EBA_DEMO_CS_EMP ",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
data_synchronization.view_elements = {add_member, apply_collection, populate}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Login_Page_Form
login_page_form = Screen(name="Login_Page_Form", description="", view_elements=set(), is_main_page=True, route_path="/Login_Page_Form", screen_size="Medium")
p101_username = InputField(
    name="P101_USERNAME",
    description="",
    field_type=InputFieldType.Text,
    label="Username",
    placeholder="username",
    required=True
)
p101_password = InputField(
    name="P101_PASSWORD",
    description="",
    field_type=InputFieldType.Password,
    label="Password",
    placeholder="password",
    required=True
)
login_page_fields_1 = Form(name="Login_Page_fields_1", description="", inputFields={p101_username, p101_password})
login_page_form.view_elements = {login_page_fields_1}


# Screen: Modify_Collection_Form
modify_collection_form = Screen(name="Modify_Collection_Form", description="", view_elements=set(), is_main_page=True, route_path="/Modify_Collection_Form", screen_size="Medium")
add_member_add_another = Button(
    name="Add_Member_Add_Another",
    description="",
    label="Add Member & Add Another",
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
    label="Delete Collection",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
p3_attr4 = InputField(
    name="P3_ATTR4",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 4"
)
p3_attr3 = InputField(
    name="P3_ATTR3",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 3"
)
p3_date_attr1 = InputField(
    name="P3_DATE_ATTR1",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 1"
)
p3_attr1 = InputField(
    name="P3_ATTR1",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 1"
)
p3_attr2 = InputField(
    name="P3_ATTR2",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 2"
)
p3_num_attr1 = InputField(
    name="P3_NUM_ATTR1",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 1"
)
p3_num_attr2 = InputField(
    name="P3_NUM_ATTR2",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 2"
)
p3_attr5 = InputField(
    name="P3_ATTR5",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 5"
)
p3_name = InputField(
    name="P3_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Collection Name"
)
p3_date_attr3 = InputField(
    name="P3_DATE_ATTR3",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 3"
)
p3_date_attr2 = InputField(
    name="P3_DATE_ATTR2",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 2"
)
p3_num_attr3 = InputField(
    name="P3_NUM_ATTR3",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 3"
)
modify_collection_fields_1 = Form(name="Modify_Collection_fields_1", description="", inputFields={p3_attr4, p3_attr3, p3_date_attr1, p3_attr1, p3_attr2, p3_num_attr1, p3_num_attr2, p3_attr5, p3_name, p3_date_attr3, p3_date_attr2, p3_num_attr3})
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
    label="Truncate Collection",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
modify_collection_form.view_elements = {add_member_add_another, cancel_3, delete_collection, modify_collection_fields_1, resequence, truncate_collection}


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
    label="Delete Member",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
p4_attr2 = InputField(
    name="P4_ATTR2",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 2"
)
p4_num_attr3 = InputField(
    name="P4_NUM_ATTR3",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 3"
)
p4_date_attr3 = InputField(
    name="P4_DATE_ATTR3",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 3"
)
p4_num_attr2 = InputField(
    name="P4_NUM_ATTR2",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 2"
)
p4_attr1 = InputField(
    name="P4_ATTR1",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 1"
)
p4_xmltype = InputField(
    name="P4_XMLTYPE",
    description="",
    field_type=InputFieldType.TextArea,
    label="XMLType"
)
p4_date_attr1 = InputField(
    name="P4_DATE_ATTR1",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 1"
)
p4_attr4 = InputField(
    name="P4_ATTR4",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 4"
)
p4_seq = InputField(
    name="P4_SEQ",
    description="",
    field_type=InputFieldType.Text,
    label="Sequence"
)
p4_num_attr1 = InputField(
    name="P4_NUM_ATTR1",
    description="",
    field_type=InputFieldType.Number,
    label="Numeric Attribute 1"
)
p4_name = InputField(
    name="P4_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name"
)
p4_attr5 = InputField(
    name="P4_ATTR5",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 5"
)
p4_attr3 = InputField(
    name="P4_ATTR3",
    description="",
    field_type=InputFieldType.Text,
    label="Character Attribute 3"
)
p4_date_attr2 = InputField(
    name="P4_DATE_ATTR2",
    description="",
    field_type=InputFieldType.Date,
    label="Date Attribute 2"
)
modify_collection_member_fields_1 = Form(name="Modify_Collection_Member_fields_1", description="", inputFields={p4_attr2, p4_num_attr3, p4_date_attr3, p4_num_attr2, p4_attr1, p4_xmltype, p4_date_attr1, p4_attr4, p4_seq, p4_num_attr1, p4_name, p4_attr5, p4_attr3, p4_date_attr2})
modify_collection_member_form.view_elements = {cancel_4, delete_member_1, modify_collection_member_fields_1}


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
    label="Remove Collections",
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
    label="Reset Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
reset_data.view_elements = {cancel_6, reset_data_1}


# Screen: Sample_Collections___API_Examples
sample_collections_api_examples = Screen(name="Sample_Collections___API_Examples", description="", view_elements=set(), is_main_page=True, route_path="/Sample_Collections___API_Examples", screen_size="Medium")
sample_collections_api_examples.view_elements = set()

example1 = Module(
    name="example1",
    screens={add_edit_collection_member_form, administration, application_theme_style_form, create_collection_form, data_synchronization, help, login_page_form, modify_collection_form, modify_collection_member_form, remove_collections, reset_data, sample_collections_api_examples}
)

# GUI Model
gui_model = GUIModel(
    name="example1",
    package="",
    versionCode="",
    versionName="",
    modules={example1},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition
add_edit_collection_member_fields_1.title = 'Add/Edit Collection Member'
add_edit_collection_member_fields_1.submit_label = 'Add Member'
application_theme_style_fields_1.title = 'Application Theme Style'
application_theme_style_fields_1.submit_label = 'Apply Changes'
create_collection_fields_1.title = 'Create Collection'
create_collection_fields_1.submit_label = 'Create Collection'
login_page_fields_1.title = 'Login Page'
login_page_fields_1.submit_label = 'Sign In'
modify_collection_fields_1.title = 'Modify Collection'
modify_collection_fields_1.submit_label = 'Add Member'
modify_collection_member_fields_1.title = 'Modify Collection Member'
modify_collection_member_fields_1.submit_label = 'Update Member'
