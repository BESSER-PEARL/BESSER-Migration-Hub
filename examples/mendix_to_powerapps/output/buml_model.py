# Generated B-UML Model
from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType
)

# Enumerations
MemberType: Enumeration = Enumeration(
    name="MemberType",
    literals={
            EnumerationLiteral(name="SENIOR"),
			EnumerationLiteral(name="CHILD"),
			EnumerationLiteral(name="STUDENT"),
			EnumerationLiteral(name="ADULT")
    }
)

# Classes
Author = Class(name="Author")
Library = Class(name="Library")
Book = Class(name="Book")

# Author class attributes and methods
Author_memberType: Property = Property(name="memberType", type=MemberType)
Author_name: Property = Property(name="name", type=StringType)
Author.attributes={Author_memberType, Author_name}

# Library class attributes and methods
Library_address: Property = Property(name="address", type=StringType)
Library_name: Property = Property(name="name", type=StringType)
Library.attributes={Library_address, Library_name}

# Book class attributes and methods
Book_release: Property = Property(name="release", type=DateType)
Book_pages: Property = Property(name="pages", type=IntegerType)
Book_title: Property = Property(name="title", type=StringType)
Book.attributes={Book_release, Book_pages, Book_title}

# Relationships
Book_Library: BinaryAssociation = BinaryAssociation(
    name="Book_Library",
    ends={
        Property(name="library", type=Library, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=Book, multiplicity=Multiplicity(0, 9999))
    }
)
Book_Author: BinaryAssociation = BinaryAssociation(
    name="Book_Author",
    ends={
        Property(name="book", type=Book, multiplicity=Multiplicity(0, 9999)),
        Property(name="author", type=Author, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="MyFirstModule",
    types={Author, Library, Book, MemberType},
    associations={Book_Library, Book_Author},
    generalizations={}
)
