####################
# STRUCTURAL MODEL #
####################

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
ENUM_Status: Enumeration = Enumeration(
    name="ENUM_Status",
    literals={
            EnumerationLiteral(name="To_Do"),
			EnumerationLiteral(name="Running"),
			EnumerationLiteral(name="Review"),
			EnumerationLiteral(name="Done")
    }
)

ENUM_Priority: Enumeration = Enumeration(
    name="ENUM_Priority",
    literals={
            EnumerationLiteral(name="High"),
			EnumerationLiteral(name="Medium"),
			EnumerationLiteral(name="Low")
    }
)

# Classes
Task = Class(name="Task")
Comment = Class(name="Comment")
FileUpload = Class(name="FileUpload")
PageHelper = Class(name="PageHelper")
CommentHelper = Class(name="CommentHelper")
MendixSSOUser = Class(name="MendixSSOUser")

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

# MendixSSOUser class attributes and methods
MendixSSOUser_DisplayName: Property = Property(name="DisplayName", type=StringType)
MendixSSOUser_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
MendixSSOUser_AvatarURL: Property = Property(name="AvatarURL", type=StringType)
MendixSSOUser_AvatarThumbURL: Property = Property(name="AvatarThumbURL", type=StringType)
MendixSSOUser.attributes={MendixSSOUser_AvatarThumbURL, MendixSSOUser_AvatarURL, MendixSSOUser_DisplayName, MendixSSOUser_EmailAddress}

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
    types={Task, Comment, FileUpload, PageHelper, CommentHelper, MendixSSOUser, ENUM_Status, ENUM_Priority},
    associations={Comment_Task, FileUpload_Task},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

###############
#  GUI MODEL  #
###############

