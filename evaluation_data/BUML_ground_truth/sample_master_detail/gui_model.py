from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement, GUIModel, Module, Screen,
)

# B-UML GUI Model — SampleMasterDetail

Activity_Calendar = Screen(
    name="Activity_Calendar", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Administration = Screen(
    name="Administration", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Application_Theme_Style = Screen(
    name="Application_Theme_Style", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Comments_Form = Screen(
    name="Comments_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Drill_Down_List = Screen(
    name="Drill_Down_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Eba_demo_md_comments_Form = Screen(
    name="Eba_demo_md_comments_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_comments_Form_page_00019 = Screen(
    name="Eba_demo_md_comments_Form_page_00019", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_milestones_Form = Screen(
    name="Eba_demo_md_milestones_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_milestones_Form_page_00016 = Screen(
    name="Eba_demo_md_milestones_Form_page_00016", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_projects_Form = Screen(
    name="Eba_demo_md_projects_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_projects_Form_page_00010 = Screen(
    name="Eba_demo_md_projects_Form_page_00010", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_projects_Form_page_00049 = Screen(
    name="Eba_demo_md_projects_Form_page_00049", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Eba_demo_md_task_links_Form = Screen(
    name="Eba_demo_md_task_links_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_task_todos_Form = Screen(
    name="Eba_demo_md_task_todos_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_tasks_Form = Screen(
    name="Eba_demo_md_tasks_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Eba_demo_md_tasks_Form_page_00018 = Screen(
    name="Eba_demo_md_tasks_Form_page_00018", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Feedback_Form = Screen(
    name="Feedback_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Links_Form = Screen(
    name="Links_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Login_Page = Screen(
    name="Login_Page", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Manage_Sample_Data = Screen(
    name="Manage_Sample_Data", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Milestones_Form = Screen(
    name="Milestones_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Page_Views_List = Screen(
    name="Page_Views_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Preferences = Screen(
    name="Preferences", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Report_and_Marquee_Marquee = Screen(
    name="Report_and_Marquee_Marquee", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Report_and_Marquee_Report = Screen(
    name="Report_and_Marquee_Report", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Side_by_Side = Screen(
    name="Side_by_Side", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Stacked = Screen(
    name="Stacked", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Stacked_with_Sub_Detail = Screen(
    name="Stacked_with_Sub_Detail", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Task_Details = Screen(
    name="Task_Details", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Tasks_Form = Screen(
    name="Tasks_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

ToDos_Form = Screen(
    name="ToDos_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Top_Users_List = Screen(
    name="Top_Users_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Cancel = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Application_Theme_Style.view_elements = {Cancel, Save}

Create = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

_ds_Drill_Down_List = DataSourceElement(name="Drill_Down")
Drill_Down_List = DataList(name="Drill_Down_List", description='', list_sources={_ds_Drill_Down_List})

Drill_Down_List.view_elements = {Create, Drill_Down_List}

Cancel_2 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_2 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_2 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_comments_Form.view_elements = {Cancel_2, Create_2, Delete, Save_2}

Cancel_3 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_3 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_2 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_3 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_comments_Form_page_00019.view_elements = {Cancel_3, Create_3, Delete_2, Save_3}

Cancel_4 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_4 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_3 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_4 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_milestones_Form.view_elements = {Cancel_4, Create_4, Delete_3, Save_4}

Cancel_5 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_5 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_4 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_5 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_milestones_Form_page_00016.view_elements = {Cancel_5, Create_5, Delete_4, Save_5}

Cancel_6 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_6 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_5 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_6 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_projects_Form.view_elements = {Cancel_6, Create_6, Delete_5, Save_6}

Cancel_7 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_7 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_6 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_7 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_projects_Form_page_00010.view_elements = {Cancel_7, Create_7, Delete_6, Save_7}

Add_Comment = Button(
    name="Add_Comment", label='Add_Comment',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Cancel_8 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_8 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_7 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Get_Next_Rowid = Button(
    name="Get_Next_Rowid", label='Get_Next_Rowid',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Get_Previous_Rowid = Button(
    name="Get_Previous_Rowid", label='Get_Previous_Rowid',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save_8 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_projects_Form_page_00049.view_elements = {Add_Comment, Cancel_8, Create_8, Delete_7, Get_Next_Rowid, Get_Previous_Rowid, Save_8}

Add = Button(
    name="Add", label='Add',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Cancel_9 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Delete_8 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_9 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_task_links_Form.view_elements = {Add, Cancel_9, Delete_8, Save_9}

Cancel_10 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_9 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_9 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_10 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_task_todos_Form.view_elements = {Cancel_10, Create_9, Delete_9, Save_10}

Cancel_11 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_10 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_10 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_11 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_tasks_Form.view_elements = {Cancel_11, Create_10, Delete_10, Save_11}

Cancel_12 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_11 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_11 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_12 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Eba_demo_md_tasks_Form_page_00018.view_elements = {Cancel_12, Create_11, Delete_11, Save_12}

Cancel_13 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Submit = Button(
    name="Submit", label='Submit',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Feedback_Form.view_elements = {Cancel_13, Submit}

Cancel_14 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save_13 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Links_Form.view_elements = {Cancel_14, Save_13}

Login = Button(
    name="Login", label='Login',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Login_Page.view_elements = {Login}

Cancel_15 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Load_Sample_Data = Button(
    name="Load_Sample_Data", label='Load_Sample_Data',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Remove_Sample_Data = Button(
    name="Remove_Sample_Data", label='Remove_Sample_Data',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Reset_Data = Button(
    name="Reset_Data", label='Reset_Data',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Manage_Sample_Data.view_elements = {Cancel_15, Load_Sample_Data, Remove_Sample_Data, Reset_Data}

_ds_Page_Views_List = DataSourceElement(name="Page_Views")
Page_Views_List = DataList(name="Page_Views_List", description='', list_sources={_ds_Page_Views_List})

Reset_Report = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Page_Views_List.view_elements = {Page_Views_List, Reset_Report}

Apply_Changes = Button(
    name="Apply_Changes", label='Apply_Changes',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Cancel_16 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Preferences.view_elements = {Apply_Changes, Cancel_16}

Add_Comment_2 = Button(
    name="Add_Comment", label='Add_Comment',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Add_Milestone = Button(
    name="Add_Milestone", label='Add_Milestone',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Add_Task = Button(
    name="Add_Task", label='Add_Task',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Cancel_17 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Edit_Project = Button(
    name="Edit_Project", label='Edit_Project',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Report_and_Marquee_Marquee.view_elements = {Add_Comment_2, Add_Milestone, Add_Task, Cancel_17, Edit_Project}

Create_12 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Report_and_Marquee_Report.view_elements = {Create_12}

Create_13 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Edit = Button(
    name="Edit", label='Edit',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Pop_Eba_Demo_Md_Comments = Button(
    name="Pop_Eba_Demo_Md_Comments", label='Pop_Eba_Demo_Md_Comments',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Pop_Eba_Demo_Md_Milestones = Button(
    name="Pop_Eba_Demo_Md_Milestones", label='Pop_Eba_Demo_Md_Milestones',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Pop_Eba_Demo_Md_Tasks = Button(
    name="Pop_Eba_Demo_Md_Tasks", label='Pop_Eba_Demo_Md_Tasks',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Reset = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Side_by_Side.view_elements = {Create_13, Edit, Pop_Eba_Demo_Md_Comments, Pop_Eba_Demo_Md_Milestones, Pop_Eba_Demo_Md_Tasks, Reset}

Calendar = Button(
    name="Calendar", label='Calendar',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save_14 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Stacked.view_elements = {Calendar, Save_14}

Save_15 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Stacked_with_Sub_Detail.view_elements = {Save_15}

Add_Link = Button(
    name="Add_Link", label='Add_Link',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Add_Todo = Button(
    name="Add_Todo", label='Add_Todo',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Cancel_18 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Edit_Task = Button(
    name="Edit_Task", label='Edit_Task',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Task_Details.view_elements = {Add_Link, Add_Todo, Cancel_18, Edit_Task}

Cancel_19 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save_16 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

ToDos_Form.view_elements = {Cancel_19, Save_16}

Reset_Report_2 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Top_Users_List = DataSourceElement(name="Top_Users")
Top_Users_List = DataList(name="Top_Users_List", description='', list_sources={_ds_Top_Users_List})

Top_Users_List.view_elements = {Reset_Report_2, Top_Users_List}

SampleMasterDetail_module = Module(
    name="SampleMasterDetail",
    screens={Activity_Calendar, Administration, Application_Theme_Style, Comments_Form, Drill_Down_List, Eba_demo_md_comments_Form, Eba_demo_md_comments_Form_page_00019, Eba_demo_md_milestones_Form, Eba_demo_md_milestones_Form_page_00016, Eba_demo_md_projects_Form, Eba_demo_md_projects_Form_page_00010, Eba_demo_md_projects_Form_page_00049, Eba_demo_md_task_links_Form, Eba_demo_md_task_todos_Form, Eba_demo_md_tasks_Form, Eba_demo_md_tasks_Form_page_00018, Feedback_Form, Links_Form, Login_Page, Manage_Sample_Data, Milestones_Form, Page_Views_List, Preferences, Report_and_Marquee_Marquee, Report_and_Marquee_Report, Side_by_Side, Stacked, Stacked_with_Sub_Detail, Task_Details, Tasks_Form, ToDos_Form, Top_Users_List},
)

gui_model = GUIModel(
    name="SampleMasterDetail",
    package='',
    versionCode='',
    versionName='',
    modules={SampleMasterDetail_module},
    description='',
)
