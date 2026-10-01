import builtins as _evaluation_builtins
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
EbaDemoDgEmp = Class(name="EbaDemoDgEmp")
EbaDemoDgCustomers = Class(name="EbaDemoDgCustomers")
EbaDemoDgProducts = Class(name="EbaDemoDgProducts")
EbaDemoDgOrders = Class(name="EbaDemoDgOrders")
EbaDemoDgOrderItems = Class(name="EbaDemoDgOrderItems")

# EbaDemoDgDept class attributes and methods
EbaDemoDgDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDgDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDgDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDgDept.attributes={EbaDemoDgDept_deptno, EbaDemoDgDept_dname, EbaDemoDgDept_loc}

# EbaDemoDgEmp class attributes and methods
EbaDemoDgEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDgEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDgEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDgEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDgEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDgEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDgEmp.attributes={EbaDemoDgEmp_comm, EbaDemoDgEmp_empno, EbaDemoDgEmp_ename, EbaDemoDgEmp_hiredate, EbaDemoDgEmp_job, EbaDemoDgEmp_sal}

# EbaDemoDgCustomers class attributes and methods
EbaDemoDgCustomers_customer_id: Property = Property(name="customer_id", type=IntegerType)
EbaDemoDgCustomers_full_name: Property = Property(name="full_name", type=StringType)
EbaDemoDgCustomers_email_address: Property = Property(name="email_address", type=StringType)
EbaDemoDgCustomers.attributes={EbaDemoDgCustomers_customer_id, EbaDemoDgCustomers_email_address, EbaDemoDgCustomers_full_name}

# EbaDemoDgProducts class attributes and methods
EbaDemoDgProducts_product_id: Property = Property(name="product_id", type=IntegerType)
EbaDemoDgProducts_product_name: Property = Property(name="product_name", type=StringType)
EbaDemoDgProducts_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgProducts_image_mime_type: Property = Property(name="image_mime_type", type=StringType)
EbaDemoDgProducts_image_filename: Property = Property(name="image_filename", type=StringType)
EbaDemoDgProducts_image_charset: Property = Property(name="image_charset", type=StringType)
EbaDemoDgProducts_image_last_updated: Property = Property(name="image_last_updated", type=DateType)
EbaDemoDgProducts.attributes={EbaDemoDgProducts_image_charset, EbaDemoDgProducts_image_filename, EbaDemoDgProducts_image_last_updated, EbaDemoDgProducts_image_mime_type, EbaDemoDgProducts_product_id, EbaDemoDgProducts_product_name, EbaDemoDgProducts_unit_price}

# EbaDemoDgOrders class attributes and methods
EbaDemoDgOrders_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoDgOrders_order_datetime: Property = Property(name="order_datetime", type=DateTimeType)
EbaDemoDgOrders_order_status: Property = Property(name="order_status", type=StringType)
EbaDemoDgOrders.attributes={EbaDemoDgOrders_order_datetime, EbaDemoDgOrders_order_id, EbaDemoDgOrders_order_status}

# EbaDemoDgOrderItems class attributes and methods
EbaDemoDgOrderItems_line_item_id: Property = Property(name="line_item_id", type=IntegerType)
EbaDemoDgOrderItems_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgOrderItems_quantity: Property = Property(name="quantity", type=IntegerType)
EbaDemoDgOrderItems.attributes={EbaDemoDgOrderItems_line_item_id, EbaDemoDgOrderItems_quantity, EbaDemoDgOrderItems_unit_price}

# Relationships
EbaDemoDgEmp_EbaDemoDgDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgDept",
    ends={
        Property(name="ebademodgdept", type=EbaDemoDgDept, multiplicity=Multiplicity(0, 1)),
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999))
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
EbaDemoDgEmp_EbaDemoDgEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgEmp",
    ends={
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgemp_mgr", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example3",
    types={EbaDemoDgDept, EbaDemoDgEmp, EbaDemoDgCustomers, EbaDemoDgProducts, EbaDemoDgOrders, EbaDemoDgOrderItems},
    associations={EbaDemoDgEmp_EbaDemoDgDept, EbaDemoDgOrders_EbaDemoDgCustomers, EbaDemoDgOrderItems_EbaDemoDgOrders, EbaDemoDgOrderItems_EbaDemoDgProducts, EbaDemoDgEmp_EbaDemoDgEmp},
    generalizations={},
    metadata=None
)

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
EbaDemoDgEmp = Class(name="EbaDemoDgEmp")
EbaDemoDgCustomers = Class(name="EbaDemoDgCustomers")
EbaDemoDgProducts = Class(name="EbaDemoDgProducts")
EbaDemoDgOrders = Class(name="EbaDemoDgOrders")
EbaDemoDgOrderItems = Class(name="EbaDemoDgOrderItems")

# EbaDemoDgDept class attributes and methods
EbaDemoDgDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoDgDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoDgDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoDgDept.attributes={EbaDemoDgDept_deptno, EbaDemoDgDept_dname, EbaDemoDgDept_loc}

# EbaDemoDgEmp class attributes and methods
EbaDemoDgEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoDgEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoDgEmp_job: Property = Property(name="job", type=StringType)
EbaDemoDgEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoDgEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoDgEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoDgEmp.attributes={EbaDemoDgEmp_comm, EbaDemoDgEmp_empno, EbaDemoDgEmp_ename, EbaDemoDgEmp_hiredate, EbaDemoDgEmp_job, EbaDemoDgEmp_sal}

# EbaDemoDgCustomers class attributes and methods
EbaDemoDgCustomers_customer_id: Property = Property(name="customer_id", type=IntegerType)
EbaDemoDgCustomers_full_name: Property = Property(name="full_name", type=StringType)
EbaDemoDgCustomers_email_address: Property = Property(name="email_address", type=StringType)
EbaDemoDgCustomers.attributes={EbaDemoDgCustomers_customer_id, EbaDemoDgCustomers_email_address, EbaDemoDgCustomers_full_name}

# EbaDemoDgProducts class attributes and methods
EbaDemoDgProducts_product_id: Property = Property(name="product_id", type=IntegerType)
EbaDemoDgProducts_product_name: Property = Property(name="product_name", type=StringType)
EbaDemoDgProducts_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgProducts_image_mime_type: Property = Property(name="image_mime_type", type=StringType)
EbaDemoDgProducts_image_filename: Property = Property(name="image_filename", type=StringType)
EbaDemoDgProducts_image_charset: Property = Property(name="image_charset", type=StringType)
EbaDemoDgProducts_image_last_updated: Property = Property(name="image_last_updated", type=DateType)
EbaDemoDgProducts.attributes={EbaDemoDgProducts_image_charset, EbaDemoDgProducts_image_filename, EbaDemoDgProducts_image_last_updated, EbaDemoDgProducts_image_mime_type, EbaDemoDgProducts_product_id, EbaDemoDgProducts_product_name, EbaDemoDgProducts_unit_price}

# EbaDemoDgOrders class attributes and methods
EbaDemoDgOrders_order_id: Property = Property(name="order_id", type=IntegerType)
EbaDemoDgOrders_order_datetime: Property = Property(name="order_datetime", type=DateTimeType)
EbaDemoDgOrders_order_status: Property = Property(name="order_status", type=StringType)
EbaDemoDgOrders.attributes={EbaDemoDgOrders_order_datetime, EbaDemoDgOrders_order_id, EbaDemoDgOrders_order_status}

# EbaDemoDgOrderItems class attributes and methods
EbaDemoDgOrderItems_line_item_id: Property = Property(name="line_item_id", type=IntegerType)
EbaDemoDgOrderItems_unit_price: Property = Property(name="unit_price", type=IntegerType)
EbaDemoDgOrderItems_quantity: Property = Property(name="quantity", type=IntegerType)
EbaDemoDgOrderItems.attributes={EbaDemoDgOrderItems_line_item_id, EbaDemoDgOrderItems_quantity, EbaDemoDgOrderItems_unit_price}

# Relationships
EbaDemoDgEmp_EbaDemoDgDept: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgDept",
    ends={
        Property(name="ebademodgdept", type=EbaDemoDgDept, multiplicity=Multiplicity(0, 1)),
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999))
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
EbaDemoDgEmp_EbaDemoDgEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoDgEmp_EbaDemoDgEmp",
    ends={
        Property(name="ebademodgemp", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademodgemp_mgr", type=EbaDemoDgEmp, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example3",
    types={EbaDemoDgDept, EbaDemoDgEmp, EbaDemoDgCustomers, EbaDemoDgProducts, EbaDemoDgOrders, EbaDemoDgOrderItems},
    associations={EbaDemoDgEmp_EbaDemoDgDept, EbaDemoDgOrders_EbaDemoDgCustomers, EbaDemoDgOrderItems_EbaDemoDgOrders, EbaDemoDgOrderItems_EbaDemoDgProducts, EbaDemoDgEmp_EbaDemoDgEmp},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

from besser.BUML.metamodel.gui import (
    GUIModel, Module, Screen,
    ViewComponent, ViewContainer,
    Button, ButtonType, ButtonActionType,
    Text, Image, Link, InputField, InputFieldType, SelectOption,
    Alert, AlertSeverity,
    Form, Menu, MenuItem, DataList,
    DataSource, DataSourceElement, EmbeddedContent,
    Styling, Size, Position, Color, Layout, LayoutType,
    UnitSize, PositionType, Alignment
)
from besser.BUML.metamodel.gui.dashboard import (
    LineChart, BarChart, PieChart, RadarChart, RadialBarChart, Table, AgentComponent,
    Column, FieldColumn, LookupColumn, ExpressionColumn, MetricCard, Series
)
from besser.BUML.metamodel.gui.events_actions import (
    Event, EventType, Transition, Create, Read, Update, Delete, Parameter
)
from besser.BUML.metamodel.gui.binding import DataBinding

# Module: example3

# Screen: About
about = Screen(name="About", description="", view_elements=set(), is_main_page=True, route_path="/About", screen_size="Medium")
about.view_elements = set()

example3 = Module(
    name="example3",
    screens={about}
)

# GUI Model
gui_model = GUIModel(
    name="example3",
    package="",
    versionCode="",
    versionName="",
    modules={example3},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition

# Restore fields omitted by the installed BESSER code builder.


from besser.BUML.metamodel.project import Project
project = Project(name='example3', models=[domain_model, gui_model])
