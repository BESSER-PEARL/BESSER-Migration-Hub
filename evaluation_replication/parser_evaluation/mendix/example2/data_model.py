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

# Classes
Content = Class(name="Content")
Feedback = Class(name="Feedback")
ContentAttachment = Class(name="ContentAttachment")
MendixSSOUser = Class(name="MendixSSOUser")

# Content class attributes and methods
Content_Title: Property = Property(name="Title", type=StringType)
Content_FreeText: Property = Property(name="FreeText", type=StringType)
Content_AverageRating: Property = Property(name="AverageRating", type=FloatType)
Content_URL: Property = Property(name="URL", type=StringType)
Content_PublishedOn: Property = Property(name="PublishedOn", type=DateType)
Content_Keyword1: Property = Property(name="Keyword1", type=StringType)
Content_Keyword2: Property = Property(name="Keyword2", type=StringType)
Content_Keyword3: Property = Property(name="Keyword3", type=StringType)
Content_Featured: Property = Property(name="Featured", type=BooleanType)
Content_Read: Property = Property(name="Read", type=BooleanType)
Content_Announcement: Property = Property(name="Announcement", type=BooleanType)
Content.attributes={Content_Announcement, Content_AverageRating, Content_Featured, Content_FreeText, Content_Keyword1, Content_Keyword2, Content_Keyword3, Content_PublishedOn, Content_Read, Content_Title, Content_URL}

# Feedback class attributes and methods
Feedback_Comment: Property = Property(name="Comment", type=StringType)
Feedback_Rating: Property = Property(name="Rating", type=FloatType)
Feedback_CommentDate: Property = Property(name="CommentDate", type=DateType)
Feedback.attributes={Feedback_Comment, Feedback_CommentDate, Feedback_Rating}

# ContentAttachment class attributes and methods

# MendixSSOUser class attributes and methods
MendixSSOUser_DisplayName: Property = Property(name="DisplayName", type=StringType)
MendixSSOUser_EmailAddress: Property = Property(name="EmailAddress", type=StringType)
MendixSSOUser_AvatarURL: Property = Property(name="AvatarURL", type=StringType)
MendixSSOUser_AvatarThumbURL: Property = Property(name="AvatarThumbURL", type=StringType)
MendixSSOUser.attributes={MendixSSOUser_AvatarThumbURL, MendixSSOUser_AvatarURL, MendixSSOUser_DisplayName, MendixSSOUser_EmailAddress}

# Relationships
Feedback_Content: BinaryAssociation = BinaryAssociation(
    name="Feedback_Content",
    ends={
        Property(name="content", type=Content, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="feedback", type=Feedback, multiplicity=Multiplicity(0, 9999))
    }
)
ContentAttachment_Content: BinaryAssociation = BinaryAssociation(
    name="ContentAttachment_Content",
    ends={
        Property(name="content", type=Content, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="contentattachment", type=ContentAttachment, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ContentPortal",
    types={Content, Feedback, ContentAttachment, MendixSSOUser},
    associations={Feedback_Content, ContentAttachment_Content},
    generalizations={},
    metadata=None
)


###############
#  GUI MODEL  #
###############

###############
#  GUI MODEL  #
###############

