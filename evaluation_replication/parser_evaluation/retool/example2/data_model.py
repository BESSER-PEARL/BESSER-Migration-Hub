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
Inventory = Class(name="Inventory")

# Inventory class attributes and methods
Inventory_id: Property = Property(name="id", type=IntegerType, is_id=True)
Inventory_sku: Property = Property(name="sku", type=StringType)
Inventory_description: Property = Property(name="description", type=StringType)
Inventory_quantity: Property = Property(name="quantity", type=IntegerType)
Inventory_replenish: Property = Property(name="replenish", type=IntegerType)
Inventory_location: Property = Property(name="location", type=StringType)
Inventory_latitude: Property = Property(name="latitude", type=FloatType)
Inventory_longitude: Property = Property(name="longitude", type=FloatType)
Inventory_image_url: Property = Property(name="image_url", type=StringType)
Inventory.attributes={Inventory_description, Inventory_id, Inventory_image_url, Inventory_latitude, Inventory_location, Inventory_longitude, Inventory_quantity, Inventory_replenish, Inventory_sku}

# Domain Model
domain_model = DomainModel(
    name="example2",
    types={Inventory},
    associations={},
    generalizations={},
    metadata=None
)
