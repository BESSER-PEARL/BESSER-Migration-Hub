from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement, GUIModel, Module, Screen,
)

# B-UML GUI Model — Brookstrut

_100_Transactions_Generated = Screen(
    name="100_Transactions_Generated", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

About = Screen(
    name="About", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

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

Configuration_Options_List = Screen(
    name="Configuration_Options_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Event_Log_List = Screen(
    name="Event_Log_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Generate_Transaction = Screen(
    name="Generate_Transaction", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Generate_Transactions = Screen(
    name="Generate_Transactions", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Load_Data = Screen(
    name="Load_Data", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Page_Views_List = Screen(
    name="Page_Views_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Product_Availability_List = Screen(
    name="Product_Availability_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Product_Form = Screen(
    name="Product_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Products_List = Screen(
    name="Products_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Recent_Sales_List = Screen(
    name="Recent_Sales_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Region_Form = Screen(
    name="Region_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Region_Stores_List = Screen(
    name="Region_Stores_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Remove_Transaction_History = Screen(
    name="Remove_Transaction_History", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Reports = Screen(
    name="Reports", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Reset_Sample_Data = Screen(
    name="Reset_Sample_Data", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales = Screen(
    name="Sales", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Calendar = Screen(
    name="Sales_History_Calendar", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Cards = Screen(
    name="Sales_History_Cards", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Classic = Screen(
    name="Sales_History_Classic", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Classic_page_00050 = Screen(
    name="Sales_History_Classic_page_00050", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Content_Row = Screen(
    name="Sales_History_Content_Row", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Content_Row_with_Menu = Screen(
    name="Sales_History_Content_Row_with_Menu", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Generation_Log_List = Screen(
    name="Sales_History_Generation_Log_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Interactive_Grid = Screen(
    name="Sales_History_Interactive_Grid", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Interactive_Report_List = Screen(
    name="Sales_History_Interactive_Report_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_History_Smart_Search_w_Menu_Actions = Screen(
    name="Sales_History_Smart_Search_w_Menu_Actions", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_by_Product = Screen(
    name="Sales_by_Product", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_by_Product_and_Store_by_Week_List = Screen(
    name="Sales_by_Product_and_Store_by_Week_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_by_Store_by_Day = Screen(
    name="Sales_by_Store_by_Day", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Sales_by_Store_by_Week_List = Screen(
    name="Sales_by_Store_by_Week_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Store = Screen(
    name="Store", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Store_Regions_List = Screen(
    name="Store_Regions_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Store_page_00007 = Screen(
    name="Store_page_00007", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Stores_Report_Content_Row = Screen(
    name="Stores_Report_Content_Row", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Table_Counts = Screen(
    name="Table_Counts", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Theme_Style_Selection_Form = Screen(
    name="Theme_Style_Selection_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Top_Users_List = Screen(
    name="Top_Users_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Transaction = Screen(
    name="Transaction", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Transaction_Detail_Form = Screen(
    name="Transaction_Detail_Form", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=False, view_elements=set(),
)

Transaction_Log_List = Screen(
    name="Transaction_Log_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Transaction_Summary_by_Hour_List = Screen(
    name="Transaction_Summary_by_Hour_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Transaction_Summary_by_Minute_List = Screen(
    name="Transaction_Summary_by_Minute_List", description='',
    x_dpi="", y_dpi="", screen_size="Small",
    is_main_page=True, view_elements=set(),
)

Refresh_Page = Button(
    name="Refresh_Page", label='Refresh_Page',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_100_Transactions_Generated.view_elements = {Refresh_Page, Up}

Up_2 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

About.view_elements = {Up_2}

Refresh = Button(
    name="Refresh", label='Refresh',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_3 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Activity_Calendar.view_elements = {Refresh, Up_3}

Up_4 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Administration.view_elements = {Up_4}

Apply_Changes = Button(
    name="Apply_Changes", label='Apply_Changes',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

_ds_Configuration_Options_List = DataSourceElement(name="Configuration_Options")
Configuration_Options_List = DataList(name="Configuration_Options_List", description='', list_sources={_ds_Configuration_Options_List})

Reset_Report = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Configuration_Options_List.view_elements = {Apply_Changes, Configuration_Options_List, Reset_Report}

_ds_Event_Log_List = DataSourceElement(name="Event_Log")
Event_Log_List = DataList(name="Event_Log_List", description='', list_sources={_ds_Event_Log_List})

Up_5 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Event_Log_List.view_elements = {Event_Log_List, Up_5}

Generate_Transaction = Button(
    name="Generate_Transaction", label='Generate_Transaction',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Reset = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_6 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Generate_Transaction.view_elements = {Generate_Transaction, Reset, Up_6}

Up_7 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Generate_Transactions.view_elements = {Up_7}

Reload = Button(
    name="Reload", label='Reload',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_8 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Load_Data.view_elements = {Reload, Up_8}

Page_Performance = Button(
    name="Page_Performance", label='Page_Performance',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Page_Views_List = DataSourceElement(name="Page_Views")
Page_Views_List = DataList(name="Page_Views_List", description='', list_sources={_ds_Page_Views_List})

Up_9 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Page_Views_List.view_elements = {Page_Performance, Page_Views_List, Up_9}

_ds_Product_Availability_List = DataSourceElement(name="Product_Availability")
Product_Availability_List = DataList(name="Product_Availability_List", description='', list_sources={_ds_Product_Availability_List})

Up_10 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Product_Availability_List.view_elements = {Product_Availability_List, Up_10}

Cancel = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Product_Form.view_elements = {Cancel, Create, Delete, Save}

Create_2 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

_ds_Products_List = DataSourceElement(name="Products")
Products_List = DataList(name="Products_List", description='', list_sources={_ds_Products_List})

Reset_Report_2 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_11 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Products_List.view_elements = {Create_2, Products_List, Reset_Report_2, Up_11}

_ds_Recent_Sales_List = DataSourceElement(name="Recent_Sales")
Recent_Sales_List = DataList(name="Recent_Sales_List", description='', list_sources={_ds_Recent_Sales_List})

Recent_Sales_List.view_elements = {Recent_Sales_List}

Cancel_2 = Button(
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

Save_2 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Region_Form.view_elements = {Cancel_2, Create_3, Delete_2, Save_2}

Edit = Button(
    name="Edit", label='Edit',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Region_Stores_List = DataSourceElement(name="Region_Stores")
Region_Stores_List = DataList(name="Region_Stores_List", description='', list_sources={_ds_Region_Stores_List})

Reset_Report_3 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_12 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Region_Stores_List.view_elements = {Edit, Region_Stores_List, Reset_Report_3, Up_12}

Cancel_3 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Remove_Transactions = Button(
    name="Remove_Transactions", label='Remove_Transactions',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_13 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Remove_Transaction_History.view_elements = {Cancel_3, Remove_Transactions, Up_13}

Up_14 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Reports.view_elements = {Up_14}

Up_15 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Reset_Sample_Data.view_elements = {Up_15}

Generate_Transaction_2 = Button(
    name="Generate_Transaction", label='Generate_Transaction',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Refresh_2 = Button(
    name="Refresh", label='Refresh',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_16 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales.view_elements = {Generate_Transaction_2, Refresh_2, Up_16}

Reset_2 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_17 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Calendar.view_elements = {Reset_2, Up_17}

Reset_3 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_18 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Cards.view_elements = {Reset_3, Up_18}

Reset_4 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_19 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Classic.view_elements = {Reset_4, Up_19}

Reset_5 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_20 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Classic_page_00050.view_elements = {Reset_5, Up_20}

Reset_6 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_21 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Content_Row.view_elements = {Reset_6, Up_21}

Reset_7 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_22 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Content_Row_with_Menu.view_elements = {Reset_7, Up_22}

_ds_Sales_History_Generation_Log_List = DataSourceElement(name="Sales_History_Generation_Log")
Sales_History_Generation_Log_List = DataList(name="Sales_History_Generation_Log_List", description='', list_sources={_ds_Sales_History_Generation_Log_List})

Sales_History_Generation_Log_List.view_elements = {Sales_History_Generation_Log_List}

Reset_8 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_23 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Interactive_Grid.view_elements = {Reset_8, Up_23}

Reset_9 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Sales_History_Interactive_Report_List = DataSourceElement(name="Sales_History_Interactive_Report")
Sales_History_Interactive_Report_List = DataList(name="Sales_History_Interactive_Report_List", description='', list_sources={_ds_Sales_History_Interactive_Report_List})

Up_24 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Interactive_Report_List.view_elements = {Reset_9, Sales_History_Interactive_Report_List, Up_24}

Reset_10 = Button(
    name="Reset", label='Reset',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_25 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_History_Smart_Search_w_Menu_Actions.view_elements = {Reset_10, Up_25}

Up_26 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_by_Product.view_elements = {Up_26}

Reset_Report_4 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Sales_by_Product_and_Store_by_Week_List = DataSourceElement(name="Sales_by_Product_and_Store_by_Week")
Sales_by_Product_and_Store_by_Week_List = DataList(name="Sales_by_Product_and_Store_by_Week_List", description='', list_sources={_ds_Sales_by_Product_and_Store_by_Week_List})

Up_27 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_by_Product_and_Store_by_Week_List.view_elements = {Reset_Report_4, Sales_by_Product_and_Store_by_Week_List, Up_27}

Up_28 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_by_Store_by_Day.view_elements = {Up_28}

Reset_Report_5 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Sales_by_Store_by_Week_List = DataSourceElement(name="Sales_by_Store_by_Week")
Sales_by_Store_by_Week_List = DataList(name="Sales_by_Store_by_Week_List", description='', list_sources={_ds_Sales_by_Store_by_Week_List})

Up_29 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Sales_by_Store_by_Week_List.view_elements = {Reset_Report_5, Sales_by_Store_by_Week_List, Up_29}

Edit_Store = Button(
    name="Edit_Store", label='Edit_Store',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_30 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Store.view_elements = {Edit_Store, Up_30}

Create_4 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Reset_Report_6 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Store_Regions_List = DataSourceElement(name="Store_Regions")
Store_Regions_List = DataList(name="Store_Regions_List", description='', list_sources={_ds_Store_Regions_List})

Up_31 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Store_Regions_List.view_elements = {Create_4, Reset_Report_6, Store_Regions_List, Up_31}

Cancel_4 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Create_5 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Delete_3 = Button(
    name="Delete", label='Delete',
    description="", visibility="",
    buttonType=ButtonType.OutlinedButton, actionType=ButtonActionType.Delete)

Save_3 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Store_page_00007.view_elements = {Cancel_4, Create_5, Delete_3, Save_3}

Create_6 = Button(
    name="Create", label='Create',
    description="", visibility="",
    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add)

Reset_Report_7 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_32 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Stores_Report_Content_Row.view_elements = {Create_6, Reset_Report_7, Up_32}

Up_33 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Table_Counts.view_elements = {Up_33}

Cancel_5 = Button(
    name="Cancel", label='Cancel',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Save_4 = Button(
    name="Save", label='Save',
    description="", visibility="",
    buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Save)

Theme_Style_Selection_Form.view_elements = {Cancel_5, Save_4}

Reset_Report_8 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Top_Users_List = DataSourceElement(name="Top_Users")
Top_Users_List = DataList(name="Top_Users_List", description='', list_sources={_ds_Top_Users_List})

Up_34 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Top_Users_List.view_elements = {Reset_Report_8, Top_Users_List, Up_34}

Refresh_Page_2 = Button(
    name="Refresh_Page", label='Refresh_Page',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Up_35 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Transaction.view_elements = {Refresh_Page_2, Up_35}

Reset_Report_9 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Transaction_Log_List = DataSourceElement(name="Transaction_Log")
Transaction_Log_List = DataList(name="Transaction_Log_List", description='', list_sources={_ds_Transaction_Log_List})

Up_36 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Transaction_Log_List.view_elements = {Reset_Report_9, Transaction_Log_List, Up_36}

Reset_Report_10 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Transaction_Summary_by_Hour_List = DataSourceElement(name="Transaction_Summary_by_Hour")
Transaction_Summary_by_Hour_List = DataList(name="Transaction_Summary_by_Hour_List", description='', list_sources={_ds_Transaction_Summary_by_Hour_List})

Up_37 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Transaction_Summary_by_Hour_List.view_elements = {Reset_Report_10, Transaction_Summary_by_Hour_List, Up_37}

Reset_Report_11 = Button(
    name="Reset_Report", label='Reset_Report',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

_ds_Transaction_Summary_by_Minute_List = DataSourceElement(name="Transaction_Summary_by_Minute")
Transaction_Summary_by_Minute_List = DataList(name="Transaction_Summary_by_Minute_List", description='', list_sources={_ds_Transaction_Summary_by_Minute_List})

Up_38 = Button(
    name="Up", label='Up',
    description="", visibility="",
    buttonType=ButtonType.TextButton, actionType=ButtonActionType.Cancel)

Transaction_Summary_by_Minute_List.view_elements = {Reset_Report_11, Transaction_Summary_by_Minute_List, Up_38}

Brookstrut_module = Module(
    name="Brookstrut",
    screens={_100_Transactions_Generated, About, Activity_Calendar, Administration, Configuration_Options_List, Event_Log_List, Generate_Transaction, Generate_Transactions, Load_Data, Page_Views_List, Product_Availability_List, Product_Form, Products_List, Recent_Sales_List, Region_Form, Region_Stores_List, Remove_Transaction_History, Reports, Reset_Sample_Data, Sales, Sales_History_Calendar, Sales_History_Cards, Sales_History_Classic, Sales_History_Classic_page_00050, Sales_History_Content_Row, Sales_History_Content_Row_with_Menu, Sales_History_Generation_Log_List, Sales_History_Interactive_Grid, Sales_History_Interactive_Report_List, Sales_History_Smart_Search_w_Menu_Actions, Sales_by_Product, Sales_by_Product_and_Store_by_Week_List, Sales_by_Store_by_Day, Sales_by_Store_by_Week_List, Store, Store_Regions_List, Store_page_00007, Stores_Report_Content_Row, Table_Counts, Theme_Style_Selection_Form, Top_Users_List, Transaction, Transaction_Detail_Form, Transaction_Log_List, Transaction_Summary_by_Hour_List, Transaction_Summary_by_Minute_List},
)

gui_model = GUIModel(
    name="Brookstrut",
    package='',
    versionCode='',
    versionName='',
    modules={Brookstrut_module},
    description='',
)
