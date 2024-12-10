# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType
)

# Enumerations
# Classes
cr2a7_book = Class(name="cr2a7_book")
cr2a7_library = Class(name="cr2a7_library")
cr2a7_author = Class(name="cr2a7_author")

# cr2a7_book class attributes and methods
cr2a7_book_creation_date: Property = Property(name="creation_date", type=DateTimeType)
cr2a7_book_release: Property = Property(name="release", type=StringType)
cr2a7_book_title: Property = Property(name="title", type=StringType)
cr2a7_book_modification_date: Property = Property(name="modification_date", type=DateTimeType)
cr2a7_book_pages: Property = Property(name="pages", type=IntegerType)
cr2a7_book_createdby: Property = Property(name="createdby", type=StringType)
cr2a7_book.attributes={cr2a7_book_creation_date, cr2a7_book_release, cr2a7_book_title, cr2a7_book_modification_date, cr2a7_book_pages, cr2a7_book_createdby}

# cr2a7_library class attributes and methods
cr2a7_library_address: Property = Property(name="address", type=StringType)
cr2a7_library_Autor_delegado: Property = Property(name="Autor_delegado", type=StringType)
cr2a7_library_Estado: Property = Property(name="Estado", type=StringType)
cr2a7_library.attributes={cr2a7_library_address, cr2a7_library_Autor_delegado, cr2a7_library_Estado}

# cr2a7_author class attributes and methods
cr2a7_author_modification_date: Property = Property(name="modification_date", type=DateTimeType)
cr2a7_author_name: Property = Property(name="name", type=StringType)
cr2a7_author_createdby: Property = Property(name="createdby", type=StringType)
cr2a7_author_creation_date: Property = Property(name="creation_date", type=DateTimeType)
cr2a7_author_memberType: Property = Property(name="memberType", type=StringType)
cr2a7_author.attributes={cr2a7_author_modification_date, cr2a7_author_name, cr2a7_author_createdby, cr2a7_author_creation_date, cr2a7_author_memberType}

# Relationships
has: BinaryAssociation = BinaryAssociation(
    name="has",
    ends={
        Property(name="cr2a7_book", type=cr2a7_book, multiplicity=Multiplicity(1, 1)),
        Property(name="cr2a7_author", type=cr2a7_author, multiplicity=Multiplicity(0, 9999))
    }
)
contains: BinaryAssociation = BinaryAssociation(
    name="contains",
    ends={
        Property(name="cr2a7_book", type=cr2a7_book, multiplicity=Multiplicity(0, 9999)),
        Property(name="cr2a7_library", type=cr2a7_library, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Domain Model",
    types={cr2a7_book, cr2a7_library, cr2a7_author},
    associations={has, contains},
    generalizations={}
)
