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
EbaDemoTreeTask = Class(name="EbaDemoTreeTask")
EbaDemoTreeSubtask = Class(name="EbaDemoTreeSubtask")
EbaDemoTreeProjects = Class(name="EbaDemoTreeProjects")
EbaDemoTreeProjFiles = Class(name="EbaDemoTreeProjFiles")
EbaDemoTreeStocks = Class(name="EbaDemoTreeStocks")
EbaDemoTreePopulation = Class(name="EbaDemoTreePopulation")
EbaDemoTreeDept = Class(name="EbaDemoTreeDept")
EbaDemoTreeEmp = Class(name="EbaDemoTreeEmp")

# EbaDemoTreeTask class attributes and methods
EbaDemoTreeTask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeTask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeTask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeTask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeTask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeTask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeTask_task_name: Property = Property(name="task_name", type=StringType)
EbaDemoTreeTask_task_start: Property = Property(name="task_start", type=DateType)
EbaDemoTreeTask_task_est_comp: Property = Property(name="task_est_comp", type=DateType)
EbaDemoTreeTask_task_comp: Property = Property(name="task_comp", type=DateType)
EbaDemoTreeTask_task_priority: Property = Property(name="task_priority", type=IntegerType)
EbaDemoTreeTask_task_status: Property = Property(name="task_status", type=IntegerType)
EbaDemoTreeTask_task_assign: Property = Property(name="task_assign", type=IntegerType)
EbaDemoTreeTask_task_desc: Property = Property(name="task_desc", type=StringType)
EbaDemoTreeTask.attributes={EbaDemoTreeTask_created, EbaDemoTreeTask_created_by, EbaDemoTreeTask_row_version_number, EbaDemoTreeTask_task_assign, EbaDemoTreeTask_task_comp, EbaDemoTreeTask_task_desc, EbaDemoTreeTask_task_est_comp, EbaDemoTreeTask_task_id, EbaDemoTreeTask_task_name, EbaDemoTreeTask_task_priority, EbaDemoTreeTask_task_start, EbaDemoTreeTask_task_status, EbaDemoTreeTask_updated, EbaDemoTreeTask_updated_by}

# EbaDemoTreeSubtask class attributes and methods
EbaDemoTreeSubtask_sub_id: Property = Property(name="sub_id", type=IntegerType)
EbaDemoTreeSubtask_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeSubtask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeSubtask_sub_name: Property = Property(name="sub_name", type=StringType)
EbaDemoTreeSubtask_sub_start: Property = Property(name="sub_start", type=DateType)
EbaDemoTreeSubtask_sub_est_comp: Property = Property(name="sub_est_comp", type=DateType)
EbaDemoTreeSubtask_sub_comp: Property = Property(name="sub_comp", type=DateType)
EbaDemoTreeSubtask_sub_priority: Property = Property(name="sub_priority", type=StringType)
EbaDemoTreeSubtask_sub_status: Property = Property(name="sub_status", type=StringType)
EbaDemoTreeSubtask_sub_assign: Property = Property(name="sub_assign", type=StringType)
EbaDemoTreeSubtask_sub_desc: Property = Property(name="sub_desc", type=StringType)
EbaDemoTreeSubtask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeSubtask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeSubtask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeSubtask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeSubtask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeSubtask.attributes={EbaDemoTreeSubtask_created, EbaDemoTreeSubtask_created_by, EbaDemoTreeSubtask_proj_id, EbaDemoTreeSubtask_row_version_number, EbaDemoTreeSubtask_sub_assign, EbaDemoTreeSubtask_sub_comp, EbaDemoTreeSubtask_sub_desc, EbaDemoTreeSubtask_sub_est_comp, EbaDemoTreeSubtask_sub_id, EbaDemoTreeSubtask_sub_name, EbaDemoTreeSubtask_sub_priority, EbaDemoTreeSubtask_sub_start, EbaDemoTreeSubtask_sub_status, EbaDemoTreeSubtask_task_id, EbaDemoTreeSubtask_updated, EbaDemoTreeSubtask_updated_by}

# EbaDemoTreeProjects class attributes and methods
EbaDemoTreeProjects_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeProjects_project_name: Property = Property(name="project_name", type=StringType)
EbaDemoTreeProjects_start_date: Property = Property(name="start_date", type=DateType)
EbaDemoTreeProjects_estimated_completion: Property = Property(name="estimated_completion", type=DateType)
EbaDemoTreeProjects_completion_date: Property = Property(name="completion_date", type=DateType)
EbaDemoTreeProjects_status: Property = Property(name="status", type=IntegerType)
EbaDemoTreeProjects_description: Property = Property(name="description", type=StringType)
EbaDemoTreeProjects_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjects_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjects_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjects_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjects_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjects.attributes={EbaDemoTreeProjects_completion_date, EbaDemoTreeProjects_created, EbaDemoTreeProjects_created_by, EbaDemoTreeProjects_description, EbaDemoTreeProjects_estimated_completion, EbaDemoTreeProjects_proj_id, EbaDemoTreeProjects_project_name, EbaDemoTreeProjects_row_version_number, EbaDemoTreeProjects_start_date, EbaDemoTreeProjects_status, EbaDemoTreeProjects_updated, EbaDemoTreeProjects_updated_by}

# EbaDemoTreeProjFiles class attributes and methods
EbaDemoTreeProjFiles_file_charset: Property = Property(name="file_charset", type=StringType)
EbaDemoTreeProjFiles_file_lastupd: Property = Property(name="file_lastupd", type=DateType)
EbaDemoTreeProjFiles_file_comments: Property = Property(name="file_comments", type=StringType)
EbaDemoTreeProjFiles_tags: Property = Property(name="tags", type=StringType)
EbaDemoTreeProjFiles_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjFiles_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjFiles_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjFiles_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjFiles_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeProjFiles_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjFiles_file_name: Property = Property(name="file_name", type=StringType)
EbaDemoTreeProjFiles_file_mimetype: Property = Property(name="file_mimetype", type=StringType)
EbaDemoTreeProjFiles.attributes={EbaDemoTreeProjFiles_created, EbaDemoTreeProjFiles_created_by, EbaDemoTreeProjFiles_file_charset, EbaDemoTreeProjFiles_file_comments, EbaDemoTreeProjFiles_file_lastupd, EbaDemoTreeProjFiles_file_mimetype, EbaDemoTreeProjFiles_file_name, EbaDemoTreeProjFiles_id, EbaDemoTreeProjFiles_row_version_number, EbaDemoTreeProjFiles_tags, EbaDemoTreeProjFiles_updated, EbaDemoTreeProjFiles_updated_by}

# EbaDemoTreeStocks class attributes and methods
EbaDemoTreeStocks_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeStocks_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeStocks_stock_code: Property = Property(name="stock_code", type=StringType)
EbaDemoTreeStocks_stock_name: Property = Property(name="stock_name", type=StringType)
EbaDemoTreeStocks_pricing_date: Property = Property(name="pricing_date", type=DateType)
EbaDemoTreeStocks_opening_val: Property = Property(name="opening_val", type=IntegerType)
EbaDemoTreeStocks_high: Property = Property(name="high", type=IntegerType)
EbaDemoTreeStocks_low: Property = Property(name="low", type=IntegerType)
EbaDemoTreeStocks_closing_val: Property = Property(name="closing_val", type=IntegerType)
EbaDemoTreeStocks_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeStocks_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeStocks_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeStocks_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeStocks.attributes={EbaDemoTreeStocks_closing_val, EbaDemoTreeStocks_created, EbaDemoTreeStocks_created_by, EbaDemoTreeStocks_high, EbaDemoTreeStocks_id, EbaDemoTreeStocks_low, EbaDemoTreeStocks_opening_val, EbaDemoTreeStocks_pricing_date, EbaDemoTreeStocks_row_version_number, EbaDemoTreeStocks_stock_code, EbaDemoTreeStocks_stock_name, EbaDemoTreeStocks_updated, EbaDemoTreeStocks_updated_by}

# EbaDemoTreePopulation class attributes and methods
EbaDemoTreePopulation_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreePopulation_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreePopulation_state_name: Property = Property(name="state_name", type=StringType)
EbaDemoTreePopulation_state_code: Property = Property(name="state_code", type=StringType)
EbaDemoTreePopulation_population: Property = Property(name="population", type=IntegerType)
EbaDemoTreePopulation_region: Property = Property(name="region", type=IntegerType)
EbaDemoTreePopulation_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreePopulation_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreePopulation_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreePopulation_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreePopulation.attributes={EbaDemoTreePopulation_created, EbaDemoTreePopulation_created_by, EbaDemoTreePopulation_id, EbaDemoTreePopulation_population, EbaDemoTreePopulation_region, EbaDemoTreePopulation_row_version_number, EbaDemoTreePopulation_state_code, EbaDemoTreePopulation_state_name, EbaDemoTreePopulation_updated, EbaDemoTreePopulation_updated_by}

# EbaDemoTreeDept class attributes and methods
EbaDemoTreeDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoTreeDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoTreeDept.attributes={EbaDemoTreeDept_deptno, EbaDemoTreeDept_dname, EbaDemoTreeDept_loc}

# EbaDemoTreeEmp class attributes and methods
EbaDemoTreeEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoTreeEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoTreeEmp_job: Property = Property(name="job", type=StringType)
EbaDemoTreeEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoTreeEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoTreeEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoTreeEmp_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeEmp.attributes={EbaDemoTreeEmp_comm, EbaDemoTreeEmp_deptno, EbaDemoTreeEmp_empno, EbaDemoTreeEmp_ename, EbaDemoTreeEmp_hiredate, EbaDemoTreeEmp_job, EbaDemoTreeEmp_sal}

# Relationships
EbaDemoTreeEmp_EbaDemoTreeEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeEmp_EbaDemoTreeEmp",
    ends={
        Property(name="ebademotreeemp", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeemp_mgr", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoTreeProjFiles_EbaDemoTreeProjects: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeProjFiles_EbaDemoTreeProjects",
    ends={
        Property(name="ebademotreeprojfiles", type=EbaDemoTreeProjFiles, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeprojects", type=EbaDemoTreeProjects, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example4",
    types={EbaDemoTreeTask, EbaDemoTreeSubtask, EbaDemoTreeProjects, EbaDemoTreeProjFiles, EbaDemoTreeStocks, EbaDemoTreePopulation, EbaDemoTreeDept, EbaDemoTreeEmp},
    associations={EbaDemoTreeEmp_EbaDemoTreeEmp, EbaDemoTreeProjFiles_EbaDemoTreeProjects},
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
EbaDemoTreeTask = Class(name="EbaDemoTreeTask")
EbaDemoTreeSubtask = Class(name="EbaDemoTreeSubtask")
EbaDemoTreeProjects = Class(name="EbaDemoTreeProjects")
EbaDemoTreeProjFiles = Class(name="EbaDemoTreeProjFiles")
EbaDemoTreeStocks = Class(name="EbaDemoTreeStocks")
EbaDemoTreePopulation = Class(name="EbaDemoTreePopulation")
EbaDemoTreeDept = Class(name="EbaDemoTreeDept")
EbaDemoTreeEmp = Class(name="EbaDemoTreeEmp")

# EbaDemoTreeTask class attributes and methods
EbaDemoTreeTask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeTask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeTask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeTask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeTask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeTask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeTask_task_name: Property = Property(name="task_name", type=StringType)
EbaDemoTreeTask_task_start: Property = Property(name="task_start", type=DateType)
EbaDemoTreeTask_task_est_comp: Property = Property(name="task_est_comp", type=DateType)
EbaDemoTreeTask_task_comp: Property = Property(name="task_comp", type=DateType)
EbaDemoTreeTask_task_priority: Property = Property(name="task_priority", type=IntegerType)
EbaDemoTreeTask_task_status: Property = Property(name="task_status", type=IntegerType)
EbaDemoTreeTask_task_assign: Property = Property(name="task_assign", type=IntegerType)
EbaDemoTreeTask_task_desc: Property = Property(name="task_desc", type=StringType)
EbaDemoTreeTask.attributes={EbaDemoTreeTask_created, EbaDemoTreeTask_created_by, EbaDemoTreeTask_row_version_number, EbaDemoTreeTask_task_assign, EbaDemoTreeTask_task_comp, EbaDemoTreeTask_task_desc, EbaDemoTreeTask_task_est_comp, EbaDemoTreeTask_task_id, EbaDemoTreeTask_task_name, EbaDemoTreeTask_task_priority, EbaDemoTreeTask_task_start, EbaDemoTreeTask_task_status, EbaDemoTreeTask_updated, EbaDemoTreeTask_updated_by}

# EbaDemoTreeSubtask class attributes and methods
EbaDemoTreeSubtask_sub_id: Property = Property(name="sub_id", type=IntegerType)
EbaDemoTreeSubtask_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeSubtask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeSubtask_sub_name: Property = Property(name="sub_name", type=StringType)
EbaDemoTreeSubtask_sub_start: Property = Property(name="sub_start", type=DateType)
EbaDemoTreeSubtask_sub_est_comp: Property = Property(name="sub_est_comp", type=DateType)
EbaDemoTreeSubtask_sub_comp: Property = Property(name="sub_comp", type=DateType)
EbaDemoTreeSubtask_sub_priority: Property = Property(name="sub_priority", type=StringType)
EbaDemoTreeSubtask_sub_status: Property = Property(name="sub_status", type=StringType)
EbaDemoTreeSubtask_sub_assign: Property = Property(name="sub_assign", type=StringType)
EbaDemoTreeSubtask_sub_desc: Property = Property(name="sub_desc", type=StringType)
EbaDemoTreeSubtask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeSubtask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeSubtask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeSubtask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeSubtask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeSubtask.attributes={EbaDemoTreeSubtask_created, EbaDemoTreeSubtask_created_by, EbaDemoTreeSubtask_proj_id, EbaDemoTreeSubtask_row_version_number, EbaDemoTreeSubtask_sub_assign, EbaDemoTreeSubtask_sub_comp, EbaDemoTreeSubtask_sub_desc, EbaDemoTreeSubtask_sub_est_comp, EbaDemoTreeSubtask_sub_id, EbaDemoTreeSubtask_sub_name, EbaDemoTreeSubtask_sub_priority, EbaDemoTreeSubtask_sub_start, EbaDemoTreeSubtask_sub_status, EbaDemoTreeSubtask_task_id, EbaDemoTreeSubtask_updated, EbaDemoTreeSubtask_updated_by}

# EbaDemoTreeProjects class attributes and methods
EbaDemoTreeProjects_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeProjects_project_name: Property = Property(name="project_name", type=StringType)
EbaDemoTreeProjects_start_date: Property = Property(name="start_date", type=DateType)
EbaDemoTreeProjects_estimated_completion: Property = Property(name="estimated_completion", type=DateType)
EbaDemoTreeProjects_completion_date: Property = Property(name="completion_date", type=DateType)
EbaDemoTreeProjects_status: Property = Property(name="status", type=IntegerType)
EbaDemoTreeProjects_description: Property = Property(name="description", type=StringType)
EbaDemoTreeProjects_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjects_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjects_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjects_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjects_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjects.attributes={EbaDemoTreeProjects_completion_date, EbaDemoTreeProjects_created, EbaDemoTreeProjects_created_by, EbaDemoTreeProjects_description, EbaDemoTreeProjects_estimated_completion, EbaDemoTreeProjects_proj_id, EbaDemoTreeProjects_project_name, EbaDemoTreeProjects_row_version_number, EbaDemoTreeProjects_start_date, EbaDemoTreeProjects_status, EbaDemoTreeProjects_updated, EbaDemoTreeProjects_updated_by}

# EbaDemoTreeProjFiles class attributes and methods
EbaDemoTreeProjFiles_file_charset: Property = Property(name="file_charset", type=StringType)
EbaDemoTreeProjFiles_file_lastupd: Property = Property(name="file_lastupd", type=DateType)
EbaDemoTreeProjFiles_file_comments: Property = Property(name="file_comments", type=StringType)
EbaDemoTreeProjFiles_tags: Property = Property(name="tags", type=StringType)
EbaDemoTreeProjFiles_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjFiles_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjFiles_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjFiles_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjFiles_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeProjFiles_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjFiles_file_name: Property = Property(name="file_name", type=StringType)
EbaDemoTreeProjFiles_file_mimetype: Property = Property(name="file_mimetype", type=StringType)
EbaDemoTreeProjFiles.attributes={EbaDemoTreeProjFiles_created, EbaDemoTreeProjFiles_created_by, EbaDemoTreeProjFiles_file_charset, EbaDemoTreeProjFiles_file_comments, EbaDemoTreeProjFiles_file_lastupd, EbaDemoTreeProjFiles_file_mimetype, EbaDemoTreeProjFiles_file_name, EbaDemoTreeProjFiles_id, EbaDemoTreeProjFiles_row_version_number, EbaDemoTreeProjFiles_tags, EbaDemoTreeProjFiles_updated, EbaDemoTreeProjFiles_updated_by}

# EbaDemoTreeStocks class attributes and methods
EbaDemoTreeStocks_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeStocks_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeStocks_stock_code: Property = Property(name="stock_code", type=StringType)
EbaDemoTreeStocks_stock_name: Property = Property(name="stock_name", type=StringType)
EbaDemoTreeStocks_pricing_date: Property = Property(name="pricing_date", type=DateType)
EbaDemoTreeStocks_opening_val: Property = Property(name="opening_val", type=IntegerType)
EbaDemoTreeStocks_high: Property = Property(name="high", type=IntegerType)
EbaDemoTreeStocks_low: Property = Property(name="low", type=IntegerType)
EbaDemoTreeStocks_closing_val: Property = Property(name="closing_val", type=IntegerType)
EbaDemoTreeStocks_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeStocks_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeStocks_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeStocks_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeStocks.attributes={EbaDemoTreeStocks_closing_val, EbaDemoTreeStocks_created, EbaDemoTreeStocks_created_by, EbaDemoTreeStocks_high, EbaDemoTreeStocks_id, EbaDemoTreeStocks_low, EbaDemoTreeStocks_opening_val, EbaDemoTreeStocks_pricing_date, EbaDemoTreeStocks_row_version_number, EbaDemoTreeStocks_stock_code, EbaDemoTreeStocks_stock_name, EbaDemoTreeStocks_updated, EbaDemoTreeStocks_updated_by}

# EbaDemoTreePopulation class attributes and methods
EbaDemoTreePopulation_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreePopulation_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreePopulation_state_name: Property = Property(name="state_name", type=StringType)
EbaDemoTreePopulation_state_code: Property = Property(name="state_code", type=StringType)
EbaDemoTreePopulation_population: Property = Property(name="population", type=IntegerType)
EbaDemoTreePopulation_region: Property = Property(name="region", type=IntegerType)
EbaDemoTreePopulation_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreePopulation_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreePopulation_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreePopulation_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreePopulation.attributes={EbaDemoTreePopulation_created, EbaDemoTreePopulation_created_by, EbaDemoTreePopulation_id, EbaDemoTreePopulation_population, EbaDemoTreePopulation_region, EbaDemoTreePopulation_row_version_number, EbaDemoTreePopulation_state_code, EbaDemoTreePopulation_state_name, EbaDemoTreePopulation_updated, EbaDemoTreePopulation_updated_by}

# EbaDemoTreeDept class attributes and methods
EbaDemoTreeDept_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeDept_dname: Property = Property(name="dname", type=StringType)
EbaDemoTreeDept_loc: Property = Property(name="loc", type=StringType)
EbaDemoTreeDept.attributes={EbaDemoTreeDept_deptno, EbaDemoTreeDept_dname, EbaDemoTreeDept_loc}

# EbaDemoTreeEmp class attributes and methods
EbaDemoTreeEmp_empno: Property = Property(name="empno", type=IntegerType)
EbaDemoTreeEmp_ename: Property = Property(name="ename", type=StringType)
EbaDemoTreeEmp_job: Property = Property(name="job", type=StringType)
EbaDemoTreeEmp_hiredate: Property = Property(name="hiredate", type=DateType)
EbaDemoTreeEmp_sal: Property = Property(name="sal", type=IntegerType)
EbaDemoTreeEmp_comm: Property = Property(name="comm", type=IntegerType)
EbaDemoTreeEmp_deptno: Property = Property(name="deptno", type=IntegerType)
EbaDemoTreeEmp.attributes={EbaDemoTreeEmp_comm, EbaDemoTreeEmp_deptno, EbaDemoTreeEmp_empno, EbaDemoTreeEmp_ename, EbaDemoTreeEmp_hiredate, EbaDemoTreeEmp_job, EbaDemoTreeEmp_sal}

# Relationships
EbaDemoTreeEmp_EbaDemoTreeEmp: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeEmp_EbaDemoTreeEmp",
    ends={
        Property(name="ebademotreeemp", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeemp_mgr", type=EbaDemoTreeEmp, multiplicity=Multiplicity(0, 1))
    }
)
EbaDemoTreeProjFiles_EbaDemoTreeProjects: BinaryAssociation = BinaryAssociation(
    name="EbaDemoTreeProjFiles_EbaDemoTreeProjects",
    ends={
        Property(name="ebademotreeprojfiles", type=EbaDemoTreeProjFiles, multiplicity=Multiplicity(0, 9999)),
        Property(name="ebademotreeprojects", type=EbaDemoTreeProjects, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example4",
    types={EbaDemoTreeTask, EbaDemoTreeSubtask, EbaDemoTreeProjects, EbaDemoTreeProjFiles, EbaDemoTreeStocks, EbaDemoTreePopulation, EbaDemoTreeDept, EbaDemoTreeEmp},
    associations={EbaDemoTreeEmp_EbaDemoTreeEmp, EbaDemoTreeProjFiles_EbaDemoTreeProjects},
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

# Module: example4

# Screen: Administration
administration = Screen(name="Administration", description="", view_elements=set(), is_main_page=True, route_path="/Administration", screen_size="Medium")
administration.view_elements = set()


# Screen: Application_Theme_Style_Form
application_theme_style_form = Screen(name="Application_Theme_Style_Form", description="", view_elements=set(), is_main_page=True, route_path="/Application_Theme_Style_Form", screen_size="Medium")
p8_desktop_theme_style_id = InputField(
    name="P8_DESKTOP_THEME_STYLE_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Desktop Theme Style",
    required=True
)
application_theme_style_fields_1 = Form(name="Application_Theme_Style_fields_1", description="", inputFields={p8_desktop_theme_style_id})
cancel = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
application_theme_style_form.view_elements = {application_theme_style_fields_1, cancel}


# Screen: Create_Edit_Project_Form
create_edit_project_form = Screen(name="Create_Edit_Project_Form", description="", view_elements=set(), route_path="/Create_Edit_Project_Form", screen_size="Medium")
cancel_1 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p7_estimated_completion = InputField(
    name="P7_ESTIMATED_COMPLETION",
    description="",
    field_type=InputFieldType.Date,
    label="Estimated Completion"
)
p7_updated = InputField(name="P7_UPDATED", description="", field_type=InputFieldType.Hidden)
p7_status = InputField(
    name="P7_STATUS",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Status"
)
p7_completion_date = InputField(
    name="P7_COMPLETION_DATE",
    description="",
    field_type=InputFieldType.Date,
    label="Completion Date"
)
p7_project_name = InputField(
    name="P7_PROJECT_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Project Name",
    required=True
)
p7_proj_id = InputField(name="P7_PROJ_ID", description="", field_type=InputFieldType.Hidden)
p7_start_date = InputField(
    name="P7_START_DATE",
    description="",
    field_type=InputFieldType.Date,
    label="Start Date"
)
create_edit_project_fields_1 = Form(name="Create_Edit_Project_fields_1", description="", inputFields={p7_estimated_completion, p7_updated, p7_status, p7_completion_date, p7_project_name, p7_proj_id, p7_start_date})
delete = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
save = Button(
    name="Save",
    description="",
    label="Apply Changes",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_edit_project_form.view_elements = {cancel_1, create_edit_project_fields_1, delete, save}


# Screen: Create_Edit_Tasks_Form
create_edit_tasks_form = Screen(name="Create_Edit_Tasks_Form", description="", view_elements=set(), is_main_page=True, route_path="/Create_Edit_Tasks_Form", screen_size="Medium")
cancel_2 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
p9_task_start = InputField(
    name="P9_TASK_START",
    description="",
    field_type=InputFieldType.Date,
    label="Start Date"
)
p9_task_id = InputField(name="P9_TASK_ID", description="", field_type=InputFieldType.Hidden)
p9_task_status = InputField(
    name="P9_TASK_STATUS",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Status"
)
p9_task_priority = InputField(
    name="P9_TASK_PRIORITY",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Priority"
)
p9_task_est_comp = InputField(
    name="P9_TASK_EST_COMP",
    description="",
    field_type=InputFieldType.Date,
    label="Estimated Completion"
)
p9_task_id_next = InputField(name="P9_TASK_ID_NEXT", description="", field_type=InputFieldType.Hidden)
p9_task_comp = InputField(
    name="P9_TASK_COMP",
    description="",
    field_type=InputFieldType.Date,
    label="Completed"
)
p9_proj_id = InputField(
    name="P9_PROJ_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Project:",
    required=True
)
p9_task_id_prev = InputField(name="P9_TASK_ID_PREV", description="", field_type=InputFieldType.Hidden)
p9_task_name = InputField(
    name="P9_TASK_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Task Name",
    required=True
)
p9_task_id_count = InputField(name="P9_TASK_ID_COUNT", description="", field_type=InputFieldType.Hidden)
p9_task_assign = InputField(
    name="P9_TASK_ASSIGN",
    description="",
    field_type=InputFieldType.Text,
    label="Task Assign"
)
p9_task_desc = InputField(
    name="P9_TASK_DESC",
    description="",
    field_type=InputFieldType.TextArea,
    label="Details"
)
create_edit_tasks_fields_1 = Form(name="Create_Edit_Tasks_fields_1", description="", inputFields={p9_task_start, p9_task_id, p9_task_status, p9_task_priority, p9_task_est_comp, p9_task_id_next, p9_task_comp, p9_proj_id, p9_task_id_prev, p9_task_name, p9_task_id_count, p9_task_assign, p9_task_desc})
create_subtask = Button(
    name="Create_Subtask",
    description="",
    label="Create Subtask",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_1 = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
get_next_task_id = Button(
    name="Get_Next_Task_Id",
    description="",
    label="&gt;",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
get_previous_task_id = Button(
    name="Get_Previous_Task_Id",
    description="",
    label="&lt;",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
save_1 = Button(
    name="Save",
    description="",
    label="Apply Changes",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
create_edit_tasks_form.view_elements = {cancel_2, create_edit_tasks_fields_1, create_subtask, delete_1, get_next_task_id, get_previous_task_id, save_1}


# Screen: Help
help = Screen(name="Help", description="", view_elements=set(), is_main_page=True, route_path="/Help", screen_size="Medium")
help.view_elements = set()


# Screen: Manage_Sample_Data
manage_sample_data = Screen(name="Manage_Sample_Data", description="", view_elements=set(), is_main_page=True, route_path="/Manage_Sample_Data", screen_size="Medium")
cancel_3 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_data = Button(
    name="Reset_Data",
    description="",
    label="Reset Data",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
manage_sample_data.view_elements = {cancel_3, reset_data}


# Screen: Modify_Subtask_Information_Form
modify_subtask_information_form = Screen(name="Modify_Subtask_Information_Form", description="", view_elements=set(), route_path="/Modify_Subtask_Information_Form", screen_size="Medium")
cancel_4 = Button(
    name="Cancel",
    description="",
    label="Cancel",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
delete_2 = Button(
    name="Delete",
    description="",
    label="Delete",
    buttonType=ButtonType.OutlinedButton,
    actionType=ButtonActionType.Delete
)
p10_sub_comp = InputField(
    name="P10_SUB_COMP",
    description="",
    field_type=InputFieldType.Date,
    label="Completed"
)
p10_task_id = InputField(
    name="P10_TASK_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Task",
    required=True
)
p10_created = InputField(name="P10_CREATED", description="", field_type=InputFieldType.Hidden)
p10_sub_status = InputField(
    name="P10_SUB_STATUS",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Status"
)
p10_sub_est_comp = InputField(
    name="P10_SUB_EST_COMP",
    description="",
    field_type=InputFieldType.Date,
    label="Estimated Completion"
)
p10_rowid = InputField(name="P10_ROWID", description="", field_type=InputFieldType.Hidden)
p10_sub_assign = InputField(
    name="P10_SUB_ASSIGN",
    description="",
    field_type=InputFieldType.Text,
    label="Assignee"
)
p10_sub_priority = InputField(
    name="P10_SUB_PRIORITY",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Priority"
)
p10_sub_id = InputField(name="P10_SUB_ID", description="", field_type=InputFieldType.Hidden)
p10_sub_name = InputField(
    name="P10_SUB_NAME",
    description="",
    field_type=InputFieldType.Text,
    label="Name",
    required=True
)
p10_updated = InputField(name="P10_UPDATED", description="", field_type=InputFieldType.Hidden)
p10_proj_id = InputField(
    name="P10_PROJ_ID",
    description="",
    field_type=InputFieldType.Dropdown,
    label="Project:",
    required=True
)
p10_sub_desc = InputField(
    name="P10_SUB_DESC",
    description="",
    field_type=InputFieldType.TextArea,
    label="Description"
)
p10_sub_start = InputField(
    name="P10_SUB_START",
    description="",
    field_type=InputFieldType.Date,
    label="Start Date"
)
modify_subtask_information_fields_1 = Form(name="Modify_Subtask_Information_fields_1", description="", inputFields={p10_sub_comp, p10_task_id, p10_created, p10_sub_status, p10_sub_est_comp, p10_rowid, p10_sub_assign, p10_sub_priority, p10_sub_id, p10_sub_name, p10_updated, p10_proj_id, p10_sub_desc, p10_sub_start})
save_2 = Button(
    name="Save",
    description="",
    label="Apply Changes",
    buttonType=ButtonType.RaisedButton,
    actionType=ButtonActionType.Save
)
modify_subtask_information_form.view_elements = {cancel_4, delete_2, modify_subtask_information_fields_1, save_2}


# Screen: Project_Dashboard
project_dashboard = Screen(name="Project_Dashboard", description="", view_elements=set(), is_main_page=True, route_path="/Project_Dashboard", screen_size="Medium")
create = Button(
    name="Create",
    description="",
    label="Create",
    buttonType=ButtonType.FloatingActionButton,
    actionType=ButtonActionType.Add
)
project_dashboard.view_elements = {create}


# Screen: Project_Tracking
project_tracking = Screen(name="Project_Tracking", description="", view_elements=set(), is_main_page=True, route_path="/Project_Tracking", screen_size="Medium")
contract_all = Button(
    name="Contract_All",
    description="",
    label="Collapse All",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
expand_all = Button(
    name="Expand_All",
    description="",
    label="Expand All",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
reset_tree = Button(
    name="Reset_Tree",
    description="",
    label="Reset Tree",
    buttonType=ButtonType.TextButton,
    actionType=ButtonActionType.Cancel
)
project_tracking.view_elements = {contract_all, expand_all, reset_tree}

example4 = Module(
    name="example4",
    screens={administration, application_theme_style_form, create_edit_project_form, create_edit_tasks_form, help, manage_sample_data, modify_subtask_information_form, project_dashboard, project_tracking}
)

# GUI Model
gui_model = GUIModel(
    name="example4",
    package="",
    versionCode="",
    versionName="",
    modules={example4},
    description=""
)

from besser.BUML.metamodel.gui.events_actions import Event, EventType, Transition

# Restore fields omitted by the installed BESSER code builder.
application_theme_style_fields_1.title = 'Application Theme Style'
application_theme_style_fields_1.submit_label = 'Apply Changes'
create_edit_project_fields_1.title = 'Create/Edit Project'
create_edit_project_fields_1.submit_label = 'Create'
create_edit_project_fields_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoTreeProjects'))
create_edit_tasks_fields_1.title = 'Create/Edit Tasks'
create_edit_tasks_fields_1.submit_label = 'Create'
create_edit_tasks_fields_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoTreeTask'))
modify_subtask_information_fields_1.title = 'Modify Subtask Information'
modify_subtask_information_fields_1.submit_label = 'Create Subtask'
modify_subtask_information_fields_1.data_binding = DataBinding(domain_concept=domain_model.get_class_by_name('EbaDemoTreeSubtask'))

from besser.BUML.metamodel.project import Project
project = Project(name='example4', models=[domain_model, gui_model])
