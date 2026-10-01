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
CategorySales = Class(name="CategorySales")
MonthlySales = Class(name="MonthlySales")

# CategorySales class attributes and methods
CategorySales_category: Property = Property(name="category", type=StringType)
CategorySales_revenue: Property = Property(name="revenue", type=IntegerType)
CategorySales_orders: Property = Property(name="orders", type=IntegerType)
CategorySales.attributes={CategorySales_category, CategorySales_orders, CategorySales_revenue}

# MonthlySales class attributes and methods
MonthlySales_month_number: Property = Property(name="month_number", type=IntegerType)
MonthlySales_month: Property = Property(name="month", type=StringType)
MonthlySales_revenue: Property = Property(name="revenue", type=IntegerType)
MonthlySales.attributes={MonthlySales_month, MonthlySales_month_number, MonthlySales_revenue}

# Domain Model
domain_model = DomainModel(
    name="example4",
    types={CategorySales, MonthlySales},
    associations={},
    generalizations={},
    metadata=None
)
