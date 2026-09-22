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
EbaDemoDgDept = Class(name="EbaDemoDgDept")
EbaDemoDgCustomers = Class(name="EbaDemoDgCustomers")
EbaDemoDgEmp = Class(name="EbaDemoDgEmp")
EbaDemoDgProducts = Class(name="EbaDemoDgProducts")
EbaDemoDgOrderItems = Class(name="EbaDemoDgOrderItems")
EbaDemoDgOrders = Class(name="EbaDemoDgOrders")

# EbaDemoDgDept class attributes and methods
EbaDemoDgDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDgDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDgDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDgDept.attributes={EbaDemoDgDept_deptno, EbaDemoDgDept_dname, EbaDemoDgDept_loc}

# EbaDemoDgCustomers class attributes and methods
EbaDemoDgCustomers_customer_id: Property = Property(name="customer_id", type=IntegerType)
EbaDemoDgCustomers_full_name: Property = Property(name="full_name", type=StringType)
EbaDemoDgCustomers_email_address: Property = Property(name="email_address", type=StringType)
EbaDemoDgCustomers.attributes={EbaDemoDgCustomers_customer_id, EbaDemoDgCustomers_email_address, EbaDemoDgCustomers_full_name}

# EbaDemoDgEmp class attributes and methods
EbaDemoDgEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDgEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDgEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDgEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDgEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDgEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDgEmp.attributes={EbaDemoDgEmp_comm, EbaDemoDgEmp_empno, EbaDemoDgEmp_ename, EbaDemoDgEmp_hiredate, EbaDemoDgEmp_job, EbaDemoDgEmp_sal}

# EbaDemoDgProducts class attributes and methods
EbaDemoDgProducts_product_id: Property = Property(name="product_id", type=IntegerType)
EbaDemoDgProducts_product_name: Property = Property(name="product_name", type=StringType)
EbaDemoDgProducts_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgProducts_image_mime_type: Property = Property(name="image_mime_type", type=StringType)
EbaDemoDgProducts_image_filename: Property = Property(name="image_filename", type=StringType)
EbaDemoDgProducts_image_charset: Property = Property(name="image_charset", type=StringType)
EbaDemoDgProducts_image_last_updated: Property = Property(name="image_last_updated", type=DateType)
EbaDemoDgProducts.attributes={EbaDemoDgProducts_image_charset, EbaDemoDgProducts_image_filename, EbaDemoDgProducts_image_last_updated, EbaDemoDgProducts_image_mime_type, EbaDemoDgProducts_product_id, EbaDemoDgProducts_product_name, EbaDemoDgProducts_unit_price}

# EbaDemoDgOrderItems class attributes and methods
EbaDemoDgOrderItems_line_item_id: Property = Property(name="line_item_id", type=IntegerType)
EbaDemoDgOrderItems_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgOrderItems_quantity: Property = Property(name="quantity", type=IntegerType)
EbaDemoDgOrderItems.attributes={EbaDemoDgOrderItems_line_item_id, EbaDemoDgOrderItems_quantity, EbaDemoDgOrderItems_unit_price}

# EbaDemoDgOrders class attributes and methods
EbaDemoDgOrders_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoDgOrders_order_datetime: Property = Property(name="order_datetime", type=DateTimeType)
EbaDemoDgOrders_order_status: Property = Property(name="order_status", type=StringType)
EbaDemoDgOrders.attributes={EbaDemoDgOrders_order_datetime, EbaDemoDgOrders_order_id, EbaDemoDgOrders_order_status}

# Relationships
EbaDemoDgEmp_EbaDemoDgDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgDept",
    ends={
        Property(name="ebademodgdept", type=EbaDemoDgDept, multiplicity=Multiplicity(0, 1)),
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999))
    }
)
EbaDemoDgEmp_EbaDemoDgEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgEmp",
    ends={
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgemp_mgr", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDgOrders_EbaDemoDgCustomers: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgOrders_EbaDemoDgCustomers",
    ends={
        Property(name="ebademodgorders", type=EbaDemoDgOrders, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgcustomers", type=EbaDemoDgCustomers, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDgOrderItems_EbaDemoDgOrders: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgOrderItems_EbaDemoDgOrders",
    ends={
        Property(name="ebademodgorderitems", type=EbaDemoDgOrderItems, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgorders", type=EbaDemoDgOrders, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoDgOrderItems_EbaDemoDgProducts: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgOrderItems_EbaDemoDgProducts",
    ends={
        Property(name="ebademodgorderitems", type=EbaDemoDgOrderItems, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgproducts", type=EbaDemoDgProducts, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="OracleApexModel",
    types={EbaDemoDgDept, EbaDemoDgCustomers, EbaDemoDgEmp, EbaDemoDgProducts, EbaDemoDgOrderItems, EbaDemoDgOrders},
    associations={EbaDemoDgEmp_EbaDemoDgDept, EbaDemoDgEmp_EbaDemoDgEmp, EbaDemoDgOrders_EbaDemoDgCustomers, EbaDemoDgOrderItems_EbaDemoDgOrders, EbaDemoDgOrderItems_EbaDemoDgProducts},
    generalizations={},
    metadata=None
)
