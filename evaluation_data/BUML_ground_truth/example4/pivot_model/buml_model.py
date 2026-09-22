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
EbaDemoTreeProjects = Class(name="EbaDemoTreeProjects")
EbaDemoTreeTask = Class(name="EbaDemoTreeTask")
EbaDemoTreeSubtask = Class(name="EbaDemoTreeSubtask")
EbaDemoTreeStocks = Class(name="EbaDemoTreeStocks")
EbaDemoTreePopulation = Class(name="EbaDemoTreePopulation")
EbaDemoTreeDept = Class(name="EbaDemoTreeDept")
EbaDemoTreeEmp = Class(name="EbaDemoTreeEmp")
EbaDemoTreeProjFiles = Class(name="EbaDemoTreeProjFiles")

# EbaDemoTreeProjects class attributes and methods
EbaDemoTreeProjects_completion_date: Property = Property(name="completion_date", type=DateType)
EbaDemoTreeProjects_status: Property = Property(name="status", type=IntegerType)
EbaDemoTreeProjects_description: Property = Property(name="description", type=StringType)
EbaDemoTreeProjects_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjects_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjects_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjects_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjects_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjects_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeProjects_project_name: Property = Property(name="project_name", type=StringType)
EbaDemoTreeProjects_start_date: Property = Property(name="start_date", type=DateType)
EbaDemoTreeProjects_estimated_completion: Property = Property(name="estimated_completion", type=DateType)
EbaDemoTreeProjects.attributes={EbaDemoTreeProjects_completion_date, EbaDemoTreeProjects_created, EbaDemoTreeProjects_created_by, EbaDemoTreeProjects_description, EbaDemoTreeProjects_estimated_completion, EbaDemoTreeProjects_proj_id, EbaDemoTreeProjects_project_name, EbaDemoTreeProjects_row_version_number, EbaDemoTreeProjects_start_date, EbaDemoTreeProjects_status, EbaDemoTreeProjects_updated, EbaDemoTreeProjects_updated_by}

# EbaDemoTreeTask class attributes and methods
EbaDemoTreeTask_proj_id: Property = Property(name="proj_id", type=IntegerType)
EbaDemoTreeTask_task_name: Property = Property(name="task_name", type=StringType)
EbaDemoTreeTask_task_start: Property = Property(name="task_start", type=DateType)
EbaDemoTreeTask_task_est_comp: Property = Property(name="task_est_comp", type=DateType)
EbaDemoTreeTask_task_comp: Property = Property(name="task_comp", type=DateType)
EbaDemoTreeTask_task_priority: Property = Property(name="task_priority", type=IntegerType)
EbaDemoTreeTask_task_status: Property = Property(name="task_status", type=IntegerType)
EbaDemoTreeTask_task_assign: Property = Property(name="task_assign", type=IntegerType)
EbaDemoTreeTask_task_desc: Property = Property(name="task_desc", type=StringType)
EbaDemoTreeTask_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeTask_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeTask_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeTask_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeTask_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeTask_task_id: Property = Property(name="task_id", type=IntegerType)
EbaDemoTreeTask.attributes={EbaDemoTreeTask_created, EbaDemoTreeTask_created_by, EbaDemoTreeTask_proj_id, EbaDemoTreeTask_row_version_number, EbaDemoTreeTask_task_assign, EbaDemoTreeTask_task_comp, EbaDemoTreeTask_task_desc, EbaDemoTreeTask_task_est_comp, EbaDemoTreeTask_task_id, EbaDemoTreeTask_task_name, EbaDemoTreeTask_task_priority, EbaDemoTreeTask_task_start, EbaDemoTreeTask_task_status, EbaDemoTreeTask_updated, EbaDemoTreeTask_updated_by}

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

# EbaDemoTreeStocks class attributes and methods
EbaDemoTreeStocks_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeStocks_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeStocks_stock_code: Property = Property(name="stock_code", type=StringType)
EbaDemoTreeStocks_stock_name: Property = Property(name="stock_name", type=StringType)
EbaDemoTreeStocks_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeStocks_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeStocks_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeStocks_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeStocks_pricing_date: Property = Property(name="pricing_date", type=DateType)
EbaDemoTreeStocks_opening_val: Property = Property(name="opening_val", type=IntegerType)
EbaDemoTreeStocks_high: Property = Property(name="high", type=IntegerType)
EbaDemoTreeStocks_low: Property = Property(name="low", type=IntegerType)
EbaDemoTreeStocks_closing_val: Property = Property(name="closing_val", type=IntegerType)
EbaDemoTreeStocks.attributes={EbaDemoTreeStocks_closing_val, EbaDemoTreeStocks_created, EbaDemoTreeStocks_created_by, EbaDemoTreeStocks_high, EbaDemoTreeStocks_id, EbaDemoTreeStocks_low, EbaDemoTreeStocks_opening_val, EbaDemoTreeStocks_pricing_date, EbaDemoTreeStocks_row_version_number, EbaDemoTreeStocks_stock_code, EbaDemoTreeStocks_stock_name, EbaDemoTreeStocks_updated, EbaDemoTreeStocks_updated_by}

# EbaDemoTreePopulation class attributes and methods
EbaDemoTreePopulation_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreePopulation_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreePopulation_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreePopulation_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreePopulation_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreePopulation_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreePopulation_state_name: Property = Property(name="state_name", type=StringType)
EbaDemoTreePopulation_state_code: Property = Property(name="state_code", type=StringType)
EbaDemoTreePopulation_population: Property = Property(name="population", type=IntegerType)
EbaDemoTreePopulation_region: Property = Property(name="region", type=IntegerType)
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

# EbaDemoTreeProjFiles class attributes and methods
EbaDemoTreeProjFiles_id: Property = Property(name="id", type=IntegerType)
EbaDemoTreeProjFiles_row_version_number: Property = Property(name="row_version_number", type=IntegerType)
EbaDemoTreeProjFiles_file_name: Property = Property(name="file_name", type=StringType)
EbaDemoTreeProjFiles_file_mimetype: Property = Property(name="file_mimetype", type=StringType)
EbaDemoTreeProjFiles_file_charset: Property = Property(name="file_charset", type=StringType)
EbaDemoTreeProjFiles_file_lastupd: Property = Property(name="file_lastupd", type=DateType)
EbaDemoTreeProjFiles_file_comments: Property = Property(name="file_comments", type=StringType)
EbaDemoTreeProjFiles_tags: Property = Property(name="tags", type=StringType)
EbaDemoTreeProjFiles_created: Property = Property(name="created", type=DateTimeType)
EbaDemoTreeProjFiles_created_by: Property = Property(name="created_by", type=StringType)
EbaDemoTreeProjFiles_updated: Property = Property(name="updated", type=DateTimeType)
EbaDemoTreeProjFiles_updated_by: Property = Property(name="updated_by", type=StringType)
EbaDemoTreeProjFiles.attributes={EbaDemoTreeProjFiles_created, EbaDemoTreeProjFiles_created_by, EbaDemoTreeProjFiles_file_charset, EbaDemoTreeProjFiles_file_comments, EbaDemoTreeProjFiles_file_lastupd, EbaDemoTreeProjFiles_file_mimetype, EbaDemoTreeProjFiles_file_name, EbaDemoTreeProjFiles_id, EbaDemoTreeProjFiles_row_version_number, EbaDemoTreeProjFiles_tags, EbaDemoTreeProjFiles_updated, EbaDemoTreeProjFiles_updated_by}

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
    name="OracleApexModel",
    types={EbaDemoTreeProjects, EbaDemoTreeTask, EbaDemoTreeSubtask, EbaDemoTreeStocks, EbaDemoTreePopulation, EbaDemoTreeDept, EbaDemoTreeEmp, EbaDemoTreeProjFiles},
    associations={EbaDemoTreeEmp_EbaDemoTreeEmp, EbaDemoTreeProjFiles_EbaDemoTreeProjects},
    generalizations={},
    metadata=None
)
