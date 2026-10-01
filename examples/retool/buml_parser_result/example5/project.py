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
TeamMembers = Class(name="TeamMembers")

# TeamMembers class attributes and methods
TeamMembers_id: Property = Property(name="id", type=IntegerType, is_id=True)
TeamMembers_name: Property = Property(name="name", type=StringType)
TeamMembers_email: Property = Property(name="email", type=StringType)
TeamMembers_department: Property = Property(name="department", type=StringType)
TeamMembers_status: Property = Property(name="status", type=StringType)
TeamMembers_role: Property = Property(name="role", type=StringType)
TeamMembers_joined_date: Property = Property(name="joined_date", type=DateType)
TeamMembers_notes: Property = Property(name="notes", type=StringType)
TeamMembers.attributes={TeamMembers_department, TeamMembers_email, TeamMembers_id, TeamMembers_joined_date, TeamMembers_name, TeamMembers_notes, TeamMembers_role, TeamMembers_status}

# Domain Model
domain_model = DomainModel(
    name="example5",
    types={TeamMembers},
    associations={},
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
TeamMembers = Class(name="TeamMembers")

# TeamMembers class attributes and methods
TeamMembers_id: Property = Property(name="id", type=IntegerType, is_id=True)
TeamMembers_name: Property = Property(name="name", type=StringType)
TeamMembers_email: Property = Property(name="email", type=StringType)
TeamMembers_department: Property = Property(name="department", type=StringType)
TeamMembers_status: Property = Property(name="status", type=StringType)
TeamMembers_role: Property = Property(name="role", type=StringType)
TeamMembers_joined_date: Property = Property(name="joined_date", type=DateType)
TeamMembers_notes: Property = Property(name="notes", type=StringType)
TeamMembers.attributes={TeamMembers_department, TeamMembers_email, TeamMembers_id, TeamMembers_joined_date, TeamMembers_name, TeamMembers_notes, TeamMembers_role, TeamMembers_status}

# Domain Model
domain_model = DomainModel(
    name="example5",
    types={TeamMembers},
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

# Module: example5

# Screen: activity
activity = Screen(name="activity", description="", view_elements=set(), is_main_page=True, route_path="/activity", screen_size="Medium")
activityplaceholder = Text(name="activityPlaceholder", content="Activity log for **{{ membersTable.selectedRow.name }}** will appear here.\\n\\nThis view demonstrates the tabbed detail pane pattern with dynamic width — the Activity tab expands the panel to 550px to accommodate richer content.", description="")
activity.view_elements = {activityplaceholder}


# Screen: confirmBulkUpdate
confirmbulkupdate = Screen(name="confirmBulkUpdate", description="", view_elements=set(), route_path="/confirmBulkUpdate", screen_size="Medium")
bulkcancelbtn = Button(
    name="bulkCancelBtn",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
bulkclosebtn = Button(
    name="bulkCloseBtn",
    description="",
    label="bulkCloseBtn",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
bulkconfirmbtn = Button(
    name="bulkConfirmBtn",
    description="",
    label="Confirm update ({{ bulkUpdateData.value.length }})",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
bulkfieldsummary = Text(name="bulkFieldSummary", content="{{ \'**Fields that will be updated:** status, role\\n\\n_Only editable columns from the table will be included in the update._\' }}", description="")
bulkmembertags = InputField(
    name="bulkMemberTags",
    description="",
    field_type=InputFieldType.Tags,
    default_value="{{ bulkUpdateData.value.map(r => r.name) }}"
)
bulktitle = Text(name="bulkTitle", content="#### Bulk Update Confirmation", description="")
bulkwarning = Text(name="bulkWarning", content="You are about to update **{{ bulkUpdateData.value.length }}** team member(s). Please review the affected members below before confirming.", description="")
confirmbulkupdate.view_elements = {bulkcancelbtn, bulkclosebtn, bulkconfirmbtn, bulkfieldsummary, bulkmembertags, bulktitle, bulkwarning}


# Screen: details
details = Screen(name="details", description="", view_elements=set(), is_main_page=True, route_path="/details", screen_size="Medium")
role = InputField(
    name="role",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Role",
    options=[SelectOption(value="Engineer", label="Engineer"), SelectOption(value="Designer", label="Designer"), SelectOption(value="Manager", label="Manager"), SelectOption(value="Analyst", label="Analyst"), SelectOption(value="Lead", label="Lead")]
)
notes = InputField(
    name="notes",
    description="",
    field_type=InputFieldType.TextArea,
    label="Notes"
)
name = InputField(
    name="name",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    required=True
)
status = InputField(
    name="status",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Status",
    options=[SelectOption(value="active", label="Active"), SelectOption(value="on_leave", label="On Leave"), SelectOption(value="offboarded", label="Offboarded")]
)
department = InputField(
    name="department",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department"
)
joined_date = InputField(
    name="joined_date",
    description="",
    field_type=InputFieldType.Date,
    label="Joined"
)
email = InputField(
    name="email",
    description="",
    field_type=InputFieldType.Text,
    label="Email",
    required=True
)
detailform = Form(name="DetailForm", description="updateMember", inputFields={role, notes, name, status, department, joined_date, email})
details.view_elements = {detailform}


# Screen: example5_Main
example5_main = Screen(name="example5_Main", description="", view_elements=set(), is_main_page=True, route_path="/example5_Main", screen_size="Medium")
a01a1 = Button(
    name="a01a1",
    description="",
    label="Edit",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate
)
a02b2 = Button(
    name="a02b2",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
daterangefilter = InputField(
    name="dateRangeFilter",
    description="",
    field_type=InputFieldType.DateRange,
    label="Joined"
)
departmentfilter = InputField(
    name="departmentFilter",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Department",
    placeholder="All departments"
)
detailclosebtn = Button(
    name="detailCloseBtn",
    description="",
    label="detailCloseBtn",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
detailtitle = Text(name="detailTitle", content="#### {{ membersTable.selectedRow.name }}", description="")
memberstable_list_source_0 = DataSourceElement(name="team_members")
domain_model_ref = globals().get('domain_model') or next((v for k, v in globals().items() if k.startswith('domain_model') and hasattr(v, 'get_class_by_name')), None)
memberstable_list_source_0_domain = None
if domain_model_ref is not None:
    memberstable_list_source_0_domain = domain_model_ref.get_class_by_name("TeamMembers")
if memberstable_list_source_0_domain:
    memberstable_list_source_0.dataSourceClass = memberstable_list_source_0_domain
    memberstable_list_source_0.field_names = ['status', 'email', 'name', 'department', 'id', 'joined_date', 'role']
    memberstable_list_source_0.fields = set(attr for attr in memberstable_list_source_0_domain.attributes if attr.name in ['status', 'email', 'name', 'department', 'id', 'joined_date', 'role'])
else:
    # Domain class 'TeamMembers' not resolved for data source 'team_members'.
    memberstable_list_source_0.field_names = ['status', 'email', 'name', 'department', 'id', 'joined_date', 'role']
memberstable_list = DataList(name="membersTable_List", description="", list_sources={memberstable_list_source_0})
pagetitle = Text(name="pageTitle", content="### Team Members", description="")
resetbtn = Button(
    name="resetBtn",
    description="",
    label="Reset",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.RunMethod
)
searchinput = InputField(
    name="searchInput",
    description="",
    field_type=InputFieldType.Text,
    placeholder="Search by name or email..."
)
setupguidebtn = Button(
    name="setupGuideBtn",
    description="",
    label="Setup Guide",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Navigate
)
statusfilter = InputField(
    name="statusFilter",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Status",
    placeholder="All statuses",
    options=[SelectOption(value="active", label="Active"), SelectOption(value="on_leave", label="On Leave"), SelectOption(value="offboarded", label="Offboarded")]
)
example5_main.view_elements = {a01a1, a02b2, daterangefilter, departmentfilter, detailclosebtn, detailtitle, memberstable_list, pagetitle, resetbtn, searchinput, setupguidebtn, statusfilter}


# Screen: setupGuideModal
setupguidemodal = Screen(name="setupGuideModal", description="", view_elements=set(), route_path="/setupGuideModal", screen_size="Medium")
setupguidetext = Text(name="setupGuideText", content="{{ \'Welcome! This app is loaded with **sample data** so you can click around and explore right away.\\n\\nWhen you are ready to wire up your real database, follow these steps:\\n\\n1. 🔌 **Connect your database** — Go to *Resources* in Retool and add your DB\\n2. 🔄 **Update queries** — Open each query in the bottom panel and switch the Resource\\n3. 📝 **Update table/column names** — Edit the SQL in each query to match your schema\\n4. 🧹 **Remove mock data** — In each Table/Select, remove the mock array fallback from the data attribute\\n5. 🗑️ **Delete this modal** — Remove this Setup Guide and the setupGuideBtn button\\n\\n✅ You are all set — happy building!\' }}", description="")
setupguidetitle = Text(name="setupGuideTitle", content="## 🚀 Setup Guide", description="")
setupguidemodal.view_elements = {setupguidetext, setupguidetitle}

# Button events and transitions (written after all screens defined to avoid forward references)
setupguidebtn_event_0_action_0 = Transition(name="setupGuideBtn_open_0", description="", target_screen=setupguidemodal)
setupguidebtn_event_0 = Event(name="setupGuideBtn_click_0", event_type=EventType.OnClick, actions={setupguidebtn_event_0_action_0})
setupguidebtn_event_0_action_0.triggered_by = setupguidebtn
setupguidebtn.events = {setupguidebtn_event_0}

example5 = Module(
    name="example5",
    screens={activity, confirmbulkupdate, details, example5_main, setupguidemodal}
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
bulkclosebtn._synthetic_label = True
detailform.title = None
detailform.submit_label = 'Save changes'
detailform.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('TeamMembers'))
detailclosebtn._synthetic_label = True
memberstable_list.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('TeamMembers'))
next(s for s in memberstable_list.list_sources if s.name == 'team_members').field_names = ['id', 'name', 'email', 'department', 'status', 'joined_date', 'role']
setupguidebtn.events = set()
setupguidebtn.events.add(Event(name='setupGuideBtn_click_0', event_type=EventType.OnClick, actions={Transition(name='setupGuideBtn_open_0', target_screen=next(s for m in gui_model.modules for s in m.screens if s.name == 'setupGuideModal'), triggered_by=setupguidebtn)}))
