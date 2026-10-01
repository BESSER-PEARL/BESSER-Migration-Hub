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
TeamMembers = Class(name="TeamMembers")

# TeamMembers class attributes and methods
TeamMembers_id: Property = Property(name="id", type=IntegerType, is_id=True)
TeamMembers_name: Property = Property(name="name", type=StringType)
TeamMembers_email: Property = Property(name="email", type=StringType)
TeamMembers_department: Property = Property(name="department", type=StringType)
TeamMembers_status: Property = Property(name="status", type=StringType)
TeamMembers_role: Property = Property(name="role", type=StringType)
TeamMembers_joined_date: Property = Property(name="joined_date", type=DateType)
TeamMembers_notes: Property = Property(name="notes", type=StringType)
TeamMembers.attributes={TeamMembers_department, TeamMembers_email, TeamMembers_id, TeamMembers_joined_date, TeamMembers_name, TeamMembers_notes, TeamMembers_role, TeamMembers_status}

# Domain Model
domain_model = DomainModel(
    name="example5",
    types={TeamMembers},
    associations={},
    generalizations={},
    metadata=None
)
