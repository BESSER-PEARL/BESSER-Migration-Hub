##############
# GUI MODEL  #
##############

from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement, GUIModel, Module, Screen,
)

from buml_data_model import (
    Hospital, Hospital_name, Hospital_address, Hospital_phone,
    Person, Person_givenName, Person_middleName, Person_familyName,
    Person_birthDate, Person_gender, Person_phone,
    Department,
    Patient, Patient_patientId, Patient_acceptedDate, Patient_sickness,
    Patient_allergies, Patient_specialReqs,
    Staff, Staff_joined, Staff_education, Staff_certification, Staff_Language,
)

# ------------------------------------------------------------------
# List screens  (one per entity — matches generated APEX pages)
# ------------------------------------------------------------------

HospitalScreen = Screen(
    name="Hospital", description="List of hospitals",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
DepartmentScreen = Screen(
    name="Department", description="List of departments",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
PersonScreen = Screen(
    name="Person_Page", description="List of persons",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
PatientScreen = Screen(
    name="Patient", description="List of patients",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
StaffScreen = Screen(
    name="Staff", description="List of staff members",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)

# ------------------------------------------------------------------
# Home screen with navigation buttons
# ------------------------------------------------------------------

btn_nav_hospital   = Button(name="Nav_Hospital",   label="Hospital",   buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=HospitalScreen)
btn_nav_department = Button(name="Nav_Department", label="Department", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=DepartmentScreen)
btn_nav_person     = Button(name="Nav_Person",     label="Person",     buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=PersonScreen)
btn_nav_patient    = Button(name="Nav_Patient",    label="Patient",    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=PatientScreen)
btn_nav_staff      = Button(name="Nav_Staff",      label="Staff",      buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=StaffScreen)

HomeScreen = Screen(
    name="Home_Web", description="Hospital Management – Home",
    x_dpi="", y_dpi="", screen_size="Small", is_main_page=True,
    view_elements={
        btn_nav_hospital, btn_nav_department, btn_nav_person,
        btn_nav_patient, btn_nav_staff,
    },
)

# ------------------------------------------------------------------
# Data sources
# ------------------------------------------------------------------

ds_hospital = DataSourceElement(
    name="Hospital", dataSourceClass=Hospital,
    fields={Hospital_address, Hospital_name, Hospital_phone},
)
ds_department = DataSourceElement(
    name="Department", dataSourceClass=Department,
    fields=set(),
)
ds_person = DataSourceElement(
    name="Person", dataSourceClass=Person,
    fields={
        Person_givenName, Person_middleName, Person_familyName,
        Person_birthDate, Person_gender, Person_phone,
    },
)
ds_patient = DataSourceElement(
    name="Patient", dataSourceClass=Patient,
    fields={
        Patient_patientId, Patient_acceptedDate, Patient_sickness,
        Patient_allergies, Patient_specialReqs,
    },
)
ds_staff = DataSourceElement(
    name="Staff", dataSourceClass=Staff,
    fields={Staff_joined, Staff_education, Staff_certification, Staff_Language},
)

# ------------------------------------------------------------------
# Data lists
# ------------------------------------------------------------------

list_hospital   = DataList(name="HospitalList",   description="", list_sources={ds_hospital})
list_department = DataList(name="DepartmentList", description="", list_sources={ds_department})
list_person     = DataList(name="PersonList",     description="", list_sources={ds_person})
list_patient    = DataList(name="PatientList",    description="", list_sources={ds_patient})
list_staff      = DataList(name="StaffList",      description="", list_sources={ds_staff})

# ------------------------------------------------------------------
# Add buttons per entity screen
# ------------------------------------------------------------------

btn_add_hospital   = Button(name="Add_Hospital",   label="Add Hospital",   buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_department = Button(name="Add_Department", label="Add Department", buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_person     = Button(name="Add_Person",     label="Add Person",     buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_patient    = Button(name="Add_Patient",    label="Add Patient",    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_staff      = Button(name="Add_Staff",      label="Add Staff",      buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")

# Wire view elements
HospitalScreen.view_elements   = {list_hospital,   btn_add_hospital}
DepartmentScreen.view_elements = {list_department, btn_add_department}
PersonScreen.view_elements     = {list_person,     btn_add_person}
PatientScreen.view_elements    = {list_patient,    btn_add_patient}
StaffScreen.view_elements      = {list_staff,      btn_add_staff}

# ------------------------------------------------------------------
# Module & GUIModel
# ------------------------------------------------------------------

HospitalModule = Module(
    name="MyFirstModule",
    screens={
        HomeScreen, HospitalScreen, DepartmentScreen,
        PersonScreen, PatientScreen, StaffScreen,
    },
)

hospital_gui_model = GUIModel(
    name="HospitalManagement",
    package="com.example.hospital",
    versionCode="1",
    versionName="1.0",
    modules={HospitalModule},
    description="Hospital management application migrated from Mendix to Oracle APEX via B-UML.",
)
