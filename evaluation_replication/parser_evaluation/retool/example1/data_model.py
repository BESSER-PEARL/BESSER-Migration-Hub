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
Books = Class(name="Books")
DiscountCodes = Class(name="DiscountCodes")
Orders = Class(name="Orders")

# Books class attributes and methods
Books_id: Property = Property(name="id", type=IntegerType, is_id=True)
Books_isbn: Property = Property(name="isbn", type=IntegerType)
Books_title: Property = Property(name="title", type=StringType)
Books_author: Property = Property(name="author", type=StringType)
Books_category: Property = Property(name="category", type=StringType)
Books_price: Property = Property(name="price", type=FloatType)
Books_cover_image: Property = Property(name="cover_image", type=StringType)
Books_bookshelf: Property = Property(name="bookshelf", type=StringType)
Books_quantity_in_stock: Property = Property(name="quantity_in_stock", type=IntegerType)
Books.attributes={Books_author, Books_bookshelf, Books_category, Books_cover_image, Books_id, Books_isbn, Books_price, Books_quantity_in_stock, Books_title}

# DiscountCodes class attributes and methods
DiscountCodes_id: Property = Property(name="id", type=IntegerType, is_id=True)
DiscountCodes_discount_code: Property = Property(name="discount_code", type=StringType)
DiscountCodes_discount_percent: Property = Property(name="discount_percent", type=IntegerType)
DiscountCodes.attributes={DiscountCodes_discount_code, DiscountCodes_discount_percent, DiscountCodes_id}

# Orders class attributes and methods
Orders_id: Property = Property(name="id", type=IntegerType, is_id=True)
Orders_total_amount: Property = Property(name="total_amount", type=FloatType)
Orders.attributes={Orders_id, Orders_total_amount}

# Relationships
Orders_Books: BinaryAssociation = BinaryAssociation(
    name="Orders_Books",
    ends={
        Property(name="orders", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="book", type=Books, multiplicity=Multiplicity(0, 1))
    }
)
Orders_DiscountCodes: BinaryAssociation = BinaryAssociation(
    name="Orders_DiscountCodes",
    ends={
        Property(name="orders", type=Orders, multiplicity=Multiplicity(0, 9999)),
        Property(name="discount_code", type=DiscountCodes, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example1",
    types={Books, DiscountCodes, Orders},
    associations={Orders_Books, Orders_DiscountCodes},
    generalizations={},
    metadata=None
)
