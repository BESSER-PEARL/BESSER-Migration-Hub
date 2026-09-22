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
EbaDemoLoadDept = Class(name="EbaDemoLoadDept")
EbaDemoLoadEmp = Class(name="EbaDemoLoadEmp")
EbaDemoLoadSales = Class(name="EbaDemoLoadSales")

# EbaDemoLoadDept class attributes and methods
EbaDemoLoadDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoLoadDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoLoadDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoLoadDept.attributes={EbaDemoLoadDept_deptno, EbaDemoLoadDept_dname, EbaDemoLoadDept_loc}

# EbaDemoLoadEmp class attributes and methods
EbaDemoLoadEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoLoadEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoLoadEmp_job: Property = Property(name="job", type=StringType)
EbaDemoLoadEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoLoadEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoLoadEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoLoadEmp_created: Property = Property(name="created", type=DateType)
EbaDemoLoadEmp_last_updated: Property = Property(name="last_updated", type=DateType)
EbaDemoLoadEmp.attributes={EbaDemoLoadEmp_comm, EbaDemoLoadEmp_created, EbaDemoLoadEmp_empno, EbaDemoLoadEmp_ename, EbaDemoLoadEmp_hiredate, EbaDemoLoadEmp_job, EbaDemoLoadEmp_last_updated, EbaDemoLoadEmp_sal}

# EbaDemoLoadSales class attributes and methods
EbaDemoLoadSales_id: Property = Property(name="id", type=IntegerType)
EbaDemoLoadSales_region: Property = Property(name="region", type=StringType)
EbaDemoLoadSales_country: Property = Property(name="country", type=StringType)
EbaDemoLoadSales_item_type: Property = Property(name="item_type", type=StringType)
EbaDemoLoadSales_sales_channel: Property = Property(name="sales_channel", type=StringType)
EbaDemoLoadSales_total_profit: Property = Property(name="total_profit", type=IntegerType)
EbaDemoLoadSales_created: Property = Property(name="created", type=DateType)
EbaDemoLoadSales_last_updated: Property = Property(name="last_updated", type=DateType)
EbaDemoLoadSales_order_priority: Property = Property(name="order_priority", type=StringType)
EbaDemoLoadSales_order_date: Property = Property(name="order_date", type=DateType)
EbaDemoLoadSales_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoLoadSales_ship_date: Property = Property(name="ship_date", type=DateType)
EbaDemoLoadSales_units_sold: Property = Property(name="units_sold", type=IntegerType)
EbaDemoLoadSales_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoLoadSales_unit_cost: Property = Property(name="unit_cost", type=IntegerType)
EbaDemoLoadSales_total_revenue: Property = Property(name="total_revenue", type=IntegerType)
EbaDemoLoadSales_total_cost: Property = Property(name="total_cost", type=IntegerType)
EbaDemoLoadSales.attributes={EbaDemoLoadSales_country, EbaDemoLoadSales_created, EbaDemoLoadSales_id, EbaDemoLoadSales_item_type, EbaDemoLoadSales_last_updated, EbaDemoLoadSales_order_date, EbaDemoLoadSales_order_id, EbaDemoLoadSales_order_priority, EbaDemoLoadSales_region, EbaDemoLoadSales_sales_channel, EbaDemoLoadSales_ship_date, EbaDemoLoadSales_total_cost, EbaDemoLoadSales_total_profit, EbaDemoLoadSales_total_revenue, EbaDemoLoadSales_unit_cost, EbaDemoLoadSales_unit_price, EbaDemoLoadSales_units_sold}

# Relationships
EbaDemoLoadEmp_EbaDemoLoadEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoLoadEmp_EbaDemoLoadEmp",
    ends={
        Property(name="ebademoloademp", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademoloademp_mgr", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoLoadEmp_EbaDemoLoadDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoLoadEmp_EbaDemoLoadDept",
    ends={
        Property(name="ebademoloademp", type=EbaDemoLoadEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademoloaddept", type=EbaDemoLoadDept, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="create_tables",
    types={EbaDemoLoadDept, EbaDemoLoadEmp, EbaDemoLoadSales},
    associations={EbaDemoLoadEmp_EbaDemoLoadEmp, EbaDemoLoadEmp_EbaDemoLoadDept},
    generalizations={},
    metadata=None
)
