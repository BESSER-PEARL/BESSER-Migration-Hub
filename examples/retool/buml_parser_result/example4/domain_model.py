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
MonthlySales = Class(name="MonthlySales")
CategorySales = Class(name="CategorySales")

# MonthlySales class attributes and methods
MonthlySales_revenue: Property = Property(name="revenue", type=IntegerType)
MonthlySales_month_number: Property = Property(name="month_number", type=IntegerType)
MonthlySales_month: Property = Property(name="month", type=StringType)
MonthlySales.attributes={MonthlySales_month, MonthlySales_month_number, MonthlySales_revenue}

# CategorySales class attributes and methods
CategorySales_category: Property = Property(name="category", type=StringType)
CategorySales_revenue: Property = Property(name="revenue", type=IntegerType)
CategorySales_orders: Property = Property(name="orders", type=IntegerType)
CategorySales.attributes={CategorySales_category, CategorySales_orders, CategorySales_revenue}

# Domain Model
domain_model = DomainModel(
    name="example4",
    types={MonthlySales, CategorySales},
    associations={},
    generalizations={},
    metadata=None
)
