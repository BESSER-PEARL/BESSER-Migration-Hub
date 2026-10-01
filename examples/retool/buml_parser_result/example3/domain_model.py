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
Products = Class(name="Products")

# Products class attributes and methods
Products_id: Property = Property(name="id", type=IntegerType, is_id=True)
Products_name: Property = Property(name="name", type=StringType)
Products_description: Property = Property(name="description", type=StringType)
Products_category: Property = Property(name="category", type=StringType)
Products_price: Property = Property(name="price", type=FloatType)
Products_created_at: Property = Property(name="created_at", type=DateTimeType)
Products.attributes={Products_category, Products_created_at, Products_description, Products_id, Products_name, Products_price}

# Domain Model
domain_model = DomainModel(
    name="example3",
    types={Products},
    associations={},
    generalizations={},
    metadata=None
)
