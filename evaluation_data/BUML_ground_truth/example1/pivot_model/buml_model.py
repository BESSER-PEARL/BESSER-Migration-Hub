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
EbaDemoCsEmp = Class(name="EbaDemoCsEmp")

# EbaDemoCsEmp class attributes and methods
EbaDemoCsEmp_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoCsEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoCsEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoCsEmp_job: Property = Property(name="job", type=StringType)
EbaDemoCsEmp_mgr: Property = Property(name="mgr", type=IntegerType)
EbaDemoCsEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoCsEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoCsEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoCsEmp.attributes={EbaDemoCsEmp_comm, EbaDemoCsEmp_deptno, EbaDemoCsEmp_empno, EbaDemoCsEmp_ename, EbaDemoCsEmp_hiredate, EbaDemoCsEmp_job, EbaDemoCsEmp_mgr, EbaDemoCsEmp_sal}

# Domain Model
domain_model = DomainModel(
    name="create_eba_demo_cs_emp_table",
    types={EbaDemoCsEmp},
    associations={},
    generalizations={},
    metadata=None
)
