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

# Enumerations
ENUM_Priority: Enumeration = Enumeration(
    name="ENUM_Priority",
    literals={
            EnumerationLiteral(name="Low"),
			EnumerationLiteral(name="High"),
			EnumerationLiteral(name="Medium")
    }
)

ENUM_Status: Enumeration = Enumeration(
    name="ENUM_Status",
    literals={
            EnumerationLiteral(name="To_Do"),
			EnumerationLiteral(name="Running"),
			EnumerationLiteral(name="Review"),
			EnumerationLiteral(name="Done")
    }
)

# Classes
Task = Class(name="Task")
Comment = Class(name="Comment")
FileUpload = Class(name="FileUpload")
PageHelper = Class(name="PageHelper")
CommentHelper = Class(name="CommentHelper")

# Task class attributes and methods
Task_Title: Property = Property(name="Title", type=StringType)
Task_Description: Property = Property(name="Description", type=StringType)
Task_DueDate: Property = Property(name="DueDate", type=DateType)
Task_Priority: Property = Property(name="Priority", type=ENUM_Priority)
Task_Status: Property = Property(name="Status", type=ENUM_Status)
Task.attributes={Task_Description, Task_DueDate, Task_Priority, Task_Status, Task_Title}

# Comment class attributes and methods
Comment_Content: Property = Property(name="Content", type=StringType)
Comment.attributes={Comment_Content}

# FileUpload class attributes and methods

# PageHelper class attributes and methods
PageHelper_TeamProgress: Property = Property(name="TeamProgress", type=FloatType)
PageHelper_AssignedTasks: Property = Property(name="AssignedTasks", type=IntegerType)
PageHelper.attributes={PageHelper_AssignedTasks, PageHelper_TeamProgress}

# CommentHelper class attributes and methods
CommentHelper_Content: Property = Property(name="Content", type=StringType)
CommentHelper.attributes={CommentHelper_Content}

# Relationships
Comment_Task: BinaryAssociation = BinaryAssociation(
    name="Comment_Task",
    ends={
        Property(name="task", type=Task, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="comment", type=Comment, multiplicity=Multiplicity(0, 9999))
    }
)
FileUpload_Task: BinaryAssociation = BinaryAssociation(
    name="FileUpload_Task",
    ends={
        Property(name="task", type=Task, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="fileupload", type=FileUpload, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TaskTracker",
    types={Task, Comment, FileUpload, PageHelper, CommentHelper, ENUM_Priority, ENUM_Status},
    associations={Comment_Task, FileUpload_Task},
    generalizations={},
    metadata=None
)
