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
EbaDemoDaDept = Class(name="EbaDemoDaDept")
EbaDemoDaEmp = Class(name="EbaDemoDaEmp")

# EbaDemoDaDept class attributes and methods
EbaDemoDaDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDaDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDaDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDaDept.attributes={EbaDemoDaDept_deptno, EbaDemoDaDept_dname, EbaDemoDaDept_loc}

# EbaDemoDaEmp class attributes and methods
EbaDemoDaEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDaEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDaEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDaEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDaEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDaEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDaEmp.attributes={EbaDemoDaEmp_comm, EbaDemoDaEmp_empno, EbaDemoDaEmp_ename, EbaDemoDaEmp_hiredate, EbaDemoDaEmp_job, EbaDemoDaEmp_sal}

# Relationships
EbaDemoDaEmp_EbaDemoDaEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaEmp",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodaemp_mgr", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDaEmp_EbaDemoDaDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDaEmp_EbaDemoDaDept",
    ends={
        Property(name="ebademodaemp", type=EbaDemoDaEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodadept", type=EbaDemoDaDept, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="create_tables",
    types={EbaDemoDaDept, EbaDemoDaEmp},
    associations={EbaDemoDaEmp_EbaDemoDaEmp, EbaDemoDaEmp_EbaDemoDaDept},
    generalizations={},
    metadata=None
)
