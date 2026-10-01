####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType, DateType,
)

# ------------------------------------------------------------------
# Enumerations
# ------------------------------------------------------------------

Language = Enumeration(
    name="Language",
    literals={
        EnumerationLiteral(name="English"),
        EnumerationLiteral(name="French"),
        EnumerationLiteral(name="German"),
        EnumerationLiteral(name="Italian"),
        EnumerationLiteral(name="Spanish"),
    },
)

AccountState = Enumeration(
    name="AccountState",
    literals={
        EnumerationLiteral(name="Active"),
        EnumerationLiteral(name="Closed"),
        EnumerationLiteral(name="Frozen"),
    },
)

Format = Enumeration(
    name="Format",
    literals={
        EnumerationLiteral(name="AudioCD"),
        EnumerationLiteral(name="Audiobook"),
        EnumerationLiteral(name="Hardcover"),
        EnumerationLiteral(name="MP3CD"),
        EnumerationLiteral(name="PDF"),
        EnumerationLiteral(name="PaperBack"),
    },
)

# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------

Author = Class(name="Author")
Book = Class(name="Book")
BookItem = Class(name="BookItem")   # generalizes Book
Account = Class(name="Account")
Patron = Class(name="Patron")
Library = Class(name="Library")
Librarian = Class(name="Librarian")
Catalog = Class(name="Catalog")

# Author attributes
Author_biography: Property = Property(name="biography", type=StringType)
Author_birthDate: Property = Property(name="birthDate",  type=DateType)
Author_name: Property = Property(name="name",      type=StringType)
Author.attributes = {Author_biography, Author_birthDate, Author_name}

# Book attributes
Book_ISBN: Property = Property(name="ISBN",          type=StringType)
Book_language: Property = Property(name="language",  type=Language)
Book_name: Property = Property(name="name",          type=StringType)
Book_overview: Property = Property(name="overview",  type=StringType)
Book_publisher: Property = Property(name="publisher", type=StringType)
Book_publisherDate: Property = Property(name="publisherDate", type=DateType)
Book_subject: Property = Property(name="subject",    type=StringType)
Book.attributes = {
    Book_ISBN, Book_language, Book_name, Book_overview,
    Book_publisher, Book_publisherDate, Book_subject,
}

# BookItem own attributes  (inherits Book attrs via generalization)
BookItem_barcode: Property = Property(name="barcode",       type=StringType)
BookItem_tag: Property = Property(name="tag",               type=StringType)
BookItem_title: Property = Property(name="title",           type=StringType)
BookItem_isRefernceOnly: Property = Property(name="isRefernceOnly", type=BooleanType)
BookItem_format: Property = Property(name="format",         type=Format)
BookItem_pages: Property = Property(name="pages",           type=IntegerType)
BookItem_borrowed: Property = Property(name="borrowed",     type=DateType)
BookItem_loanPeriod: Property = Property(name="loanPeriod", type=IntegerType)
BookItem_dueDate: Property = Property(name="dueDate",       type=DateType)
BookItem_isOverdue: Property = Property(name="isOverdue",   type=BooleanType)
BookItem.attributes = {
    BookItem_barcode, BookItem_tag, BookItem_title, BookItem_isRefernceOnly,
    BookItem_format, BookItem_pages, BookItem_borrowed, BookItem_loanPeriod,
    BookItem_dueDate, BookItem_isOverdue,
}

# Account attributes
Account_number: Property = Property(name="number", type=IntegerType)
Account_opened: Property = Property(name="opened", type=DateType)
Account_state: Property = Property(name="state",   type=AccountState)
Account.attributes = {Account_number, Account_opened, Account_state}

# Patron attributes
Patron_name: Property = Property(name="name",       type=StringType)
Patron_address: Property = Property(name="address", type=StringType)
Patron.attributes = {Patron_name, Patron_address}

# Library attributes
Library_name: Property = Property(name="name",       type=StringType)
Library_address: Property = Property(name="address", type=StringType)
Library.attributes = {Library_name, Library_address}

# Librarian attributes
Librarian_name: Property = Property(name="name",         type=StringType)
Librarian_address: Property = Property(name="address",   type=StringType)
Librarian_position: Property = Property(name="position", type=StringType)
Librarian.attributes = {Librarian_name, Librarian_address, Librarian_position}

# Catalog – no own attributes
Catalog.attributes = set()

# ------------------------------------------------------------------
# Generalization
# ------------------------------------------------------------------

# BookItem IS-A Book
gen_bookitem_book = Generalization(general=Book, specific=BookItem)

# ------------------------------------------------------------------
# Associations
# ------------------------------------------------------------------

# Author ↔ Book  (N:M  –  ReferenceSet)
Author_Book: BinaryAssociation = BinaryAssociation(
    name="Author_Book",
    ends={
        Property(name="author", type=Author, multiplicity=Multiplicity(0, "*")),
        Property(name="book",   type=Book,   multiplicity=Multiplicity(0, "*")),
    },
)

# Account ↔ Patron  (1:1  –  Reference+Both)
Account_Patron: BinaryAssociation = BinaryAssociation(
    name="Account_Patron",
    ends={
        Property(name="account", type=Account, multiplicity=Multiplicity(1, 1)),
        Property(name="patron",  type=Patron,  multiplicity=Multiplicity(1, 1)),
    },
)

# Account ↔ Library  (N:1  –  Reference)
Account_Library: BinaryAssociation = BinaryAssociation(
    name="Account_Library",
    ends={
        Property(name="account", type=Account, multiplicity=Multiplicity(0, "*")),
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 1)),
    },
)

# BookItem ↔ Library  (N:1  –  Reference)
BookItem_Library: BinaryAssociation = BinaryAssociation(
    name="BookItem_Library",
    ends={
        Property(name="bookitem", type=BookItem, multiplicity=Multiplicity(0, "*")),
        Property(name="library",  type=Library,  multiplicity=Multiplicity(1, 1)),
    },
)

# BookItem ↔ Catalog  (N:1  –  Reference)
BookItem_Catalog: BinaryAssociation = BinaryAssociation(
    name="BookItem_Catalog",
    ends={
        Property(name="bookitem", type=BookItem, multiplicity=Multiplicity(0, "*")),
        Property(name="catalog",  type=Catalog,  multiplicity=Multiplicity(1, 1)),
    },
)

# BookItem ↔ Account  (N:1  –  Reference)
BookItem_Account: BinaryAssociation = BinaryAssociation(
    name="BookItem_Account",
    ends={
        Property(name="bookitem", type=BookItem, multiplicity=Multiplicity(0, "*")),
        Property(name="account",  type=Account,  multiplicity=Multiplicity(1, 1)),
    },
)

# Catalog ↔ Library  (1:1  –  Reference+Both)
Catalog_Library: BinaryAssociation = BinaryAssociation(
    name="Catalog_Library",
    ends={
        Property(name="catalog", type=Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 1)),
    },
)

# Librarian ↔ Library  (N:1  –  Reference)
Librarian_Library: BinaryAssociation = BinaryAssociation(
    name="Librarian_Library",
    ends={
        Property(name="librarian", type=Librarian, multiplicity=Multiplicity(0, "*")),
        Property(name="library",   type=Library,   multiplicity=Multiplicity(1, 1)),
    },
)

# ------------------------------------------------------------------
# Domain Model
# ------------------------------------------------------------------

library_domain_model = DomainModel(
    name="MyFirstModule",
    types={
        Author, Book, BookItem, Account, Patron, Library, Librarian, Catalog,
        Language, AccountState, Format,
    },
    associations={
        Author_Book, Account_Patron, Account_Library,
        BookItem_Library, BookItem_Catalog, BookItem_Account,
        Catalog_Library, Librarian_Library,
    },
    generalizations={gen_bookitem_book},
)
