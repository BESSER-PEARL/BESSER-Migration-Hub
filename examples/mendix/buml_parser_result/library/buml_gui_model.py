##############
# GUI MODEL  #
##############

from besser.BUML.metamodel.gui.graphical_ui import (
    Button, ButtonActionType, ButtonType,
    DataList, DataSourceElement, GUIModel, Module, Screen,
)

from buml_data_model import (
    Author, Author_birthDate, Author_name,
    Book, Book_ISBN, Book_language, Book_name, Book_overview,
    Book_publisher, Book_publisherDate, Book_subject,
    BookItem, BookItem_barcode, BookItem_tag, BookItem_title,
    BookItem_isRefernceOnly, BookItem_format, BookItem_pages,
    BookItem_borrowed, BookItem_loanPeriod, BookItem_dueDate, BookItem_isOverdue,
    Library, Library_name, Library_address,
    Patron, Patron_name, Patron_address,
    Catalog,
    Librarian, Librarian_name, Librarian_address, Librarian_position,
    Account, Account_number, Account_opened, Account_state,
)

# ------------------------------------------------------------------
# List screens  (one per entity — matches generated APEX pages)
# ------------------------------------------------------------------

AuthorScreen = Screen(
    name="Author", description="List of authors",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
BookItemScreen = Screen(
    name="BookItem", description="List of book items",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
LibraryScreen = Screen(
    name="Library", description="List of libraries",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
PatronScreen = Screen(
    name="Patron", description="List of patrons",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
CatalogScreen = Screen(
    name="Catalog", description="List of catalogs",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
LibrarianScreen = Screen(
    name="Librarian", description="List of librarians",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)
AccountScreen = Screen(
    name="Account", description="List of accounts",
    x_dpi="", y_dpi="", screen_size="Small", view_elements=set(),
)

# ------------------------------------------------------------------
# Home screen with navigation buttons
# ------------------------------------------------------------------

btn_nav_author   = Button(name="Nav_Author",   label="Author",   buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=AuthorScreen)
btn_nav_bookitem = Button(name="Nav_BookItem", label="BookItem", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=BookItemScreen)
btn_nav_library  = Button(name="Nav_Library",  label="Library",  buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=LibraryScreen)
btn_nav_patron   = Button(name="Nav_Patron",   label="Patron",   buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=PatronScreen)
btn_nav_catalog  = Button(name="Nav_Catalog",  label="Catalog",  buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=CatalogScreen)
btn_nav_librarian = Button(name="Nav_Librarian", label="Librarian", buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=LibrarianScreen)
btn_nav_account  = Button(name="Nav_Account",  label="Account",  buttonType=ButtonType.RaisedButton, actionType=ButtonActionType.Navigate, description="", visibility="", targetScreen=AccountScreen)

HomeScreen = Screen(
    name="Home_Web", description="Library Management – Home",
    x_dpi="", y_dpi="", screen_size="Small", is_main_page=True,
    view_elements={
        btn_nav_author, btn_nav_bookitem, btn_nav_library,
        btn_nav_patron, btn_nav_catalog, btn_nav_librarian, btn_nav_account,
    },
)

# ------------------------------------------------------------------
# Data sources
# ------------------------------------------------------------------

ds_author = DataSourceElement(
    name="Author", dataSourceClass=Author,
    fields={Author_birthDate, Author_name},
)
ds_bookitem = DataSourceElement(
    name="BookItem", dataSourceClass=BookItem,
    fields={
        BookItem_barcode, BookItem_tag, BookItem_title, BookItem_isRefernceOnly,
        BookItem_format, BookItem_pages, BookItem_borrowed,
        BookItem_loanPeriod, BookItem_dueDate, BookItem_isOverdue,
    },
)
ds_library = DataSourceElement(
    name="Library", dataSourceClass=Library,
    fields={Library_name, Library_address},
)
ds_patron = DataSourceElement(
    name="Patron", dataSourceClass=Patron,
    fields={Patron_name, Patron_address},
)
ds_catalog = DataSourceElement(
    name="Catalog", dataSourceClass=Catalog,
    fields=set(),
)
ds_librarian = DataSourceElement(
    name="Librarian", dataSourceClass=Librarian,
    fields={Librarian_name, Librarian_address, Librarian_position},
)
ds_account = DataSourceElement(
    name="Account", dataSourceClass=Account,
    fields={Account_number, Account_opened, Account_state},
)

# ------------------------------------------------------------------
# Data lists
# ------------------------------------------------------------------

list_author    = DataList(name="AuthorList",    description="", list_sources={ds_author})
list_bookitem  = DataList(name="BookItemList",  description="", list_sources={ds_bookitem})
list_library   = DataList(name="LibraryList",   description="", list_sources={ds_library})
list_patron    = DataList(name="PatronList",    description="", list_sources={ds_patron})
list_catalog   = DataList(name="CatalogList",   description="", list_sources={ds_catalog})
list_librarian = DataList(name="LibrarianList", description="", list_sources={ds_librarian})
list_account   = DataList(name="AccountList",   description="", list_sources={ds_account})

# ------------------------------------------------------------------
# Add buttons per entity screen
# ------------------------------------------------------------------

btn_add_author    = Button(name="Add_Author",    label="Add Author",    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_bookitem  = Button(name="Add_BookItem",  label="Add BookItem",  buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_library   = Button(name="Add_Library",   label="Add Library",   buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_patron    = Button(name="Add_Patron",    label="Add Patron",    buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_catalog   = Button(name="Add_Catalog",   label="Add Catalog",   buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_librarian = Button(name="Add_Librarian", label="Add Librarian", buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")
btn_add_account   = Button(name="Add_Account",   label="Add Account",   buttonType=ButtonType.FloatingActionButton, actionType=ButtonActionType.Add, description="", visibility="")

# Wire view elements
AuthorScreen.view_elements    = {list_author,    btn_add_author}
BookItemScreen.view_elements  = {list_bookitem,  btn_add_bookitem}
LibraryScreen.view_elements   = {list_library,   btn_add_library}
PatronScreen.view_elements    = {list_patron,    btn_add_patron}
CatalogScreen.view_elements   = {list_catalog,   btn_add_catalog}
LibrarianScreen.view_elements = {list_librarian, btn_add_librarian}
AccountScreen.view_elements   = {list_account,   btn_add_account}

# ------------------------------------------------------------------
# Module & GUIModel
# ------------------------------------------------------------------

LibraryModule = Module(
    name="MyFirstModule",
    screens={
        HomeScreen, AuthorScreen, BookItemScreen, LibraryScreen,
        PatronScreen, CatalogScreen, LibrarianScreen, AccountScreen,
    },
)

library_gui_model = GUIModel(
    name="LibraryManagement",
    package="com.example.library",
    versionCode="1",
    versionName="1.0",
    modules={LibraryModule},
    description="Library management application migrated from Mendix to Oracle APEX via B-UML.",
)
