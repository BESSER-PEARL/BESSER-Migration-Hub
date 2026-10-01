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
Gender: Enumeration = Enumeration(
    name="Gender",
    literals={
            EnumerationLiteral(name="Male"),
			EnumerationLiteral(name="Female"),
			EnumerationLiteral(name="Other")
    }
)

# Classes
Nurse = Class(name="Nurse")
Surgeon = Class(name="Surgeon")
Hospital = Class(name="Hospital")
Department = Class(name="Department")
Person = Class(name="Person")
Patient = Class(name="Patient")
Staff = Class(name="Staff")
OperationsStaff = Class(name="OperationsStaff")
AdministrativeStaff = Class(name="AdministrativeStaff")
TechnicalStaff = Class(name="TechnicalStaff")
Doctor = Class(name="Doctor")

# Nurse class attributes and methods

# Surgeon class attributes and methods

# Hospital class attributes and methods
Hospital_name: Property = Property(name="name", type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone", type=StringType)
Hospital.attributes={Hospital_address, Hospital_name, Hospital_phone}

# Department class attributes and methods

# Person class attributes and methods
Person_givenName: Property = Property(name="givenName", type=StringType)
Person_middleName: Property = Property(name="middleName", type=StringType)
Person_familyName: Property = Property(name="familyName", type=StringType)
Person_birthDate: Property = Property(name="birthDate", type=DateType)
Person_gender: Property = Property(name="gender", type=Gender)
Person_phone: Property = Property(name="phone", type=StringType)
Person.attributes={Person_birthDate, Person_familyName, Person_gender, Person_givenName, Person_middleName, Person_phone}

# Patient class attributes and methods
Patient_patientId: Property = Property(name="patientId", type=StringType)
Patient_acceptedDate: Property = Property(name="acceptedDate", type=DateType)
Patient_sickness: Property = Property(name="sickness", type=StringType)
Patient_allergies: Property = Property(name="allergies", type=StringType)
Patient_specialReqs: Property = Property(name="specialReqs", type=StringType)
Patient.attributes={Patient_acceptedDate, Patient_allergies, Patient_patientId, Patient_sickness, Patient_specialReqs}

# Staff class attributes and methods
Staff_joined: Property = Property(name="joined", type=DateType)
Staff_education: Property = Property(name="education", type=StringType)
Staff_certification: Property = Property(name="certification", type=StringType)
Staff_Language: Property = Property(name="Language", type=StringType)
Staff.attributes={Staff_Language, Staff_certification, Staff_education, Staff_joined}

# OperationsStaff class attributes and methods

# AdministrativeStaff class attributes and methods

# TechnicalStaff class attributes and methods

# Doctor class attributes and methods
Doctor_speciality: Property = Property(name="speciality", type=StringType)
Doctor_location: Property = Property(name="location", type=StringType)
Doctor.attributes={Doctor_location, Doctor_speciality}

# Relationships
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="person", type=Person, multiplicity=Multiplicity(0, 9999)),
        Property(name="hospital", type=Hospital, multiplicity=Multiplicity(0, 9999))
    }
)
Department_Hospital: BinaryAssociation = BinaryAssociation(
    name="Department_Hospital",
    ends={
        Property(name="hospital", type=Hospital, multiplicity=Multiplicity(1, 1)),
        Property(name="department", type=Department, multiplicity=Multiplicity(0, 9999))
    }
)
Staff_Department: BinaryAssociation = BinaryAssociation(
    name="Staff_Department",
    ends={
        Property(name="staff", type=Staff, multiplicity=Multiplicity(0, 9999)),
        Property(name="department", type=Department, multiplicity=Multiplicity(1, 1))
    }
)
Patient_OperationsStaff: BinaryAssociation = BinaryAssociation(
    name="Patient_OperationsStaff",
    ends={
        Property(name="patient", type=Patient, multiplicity=Multiplicity(0, 9999)),
        Property(name="operationsstaff", type=OperationsStaff, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_Staff_Person = Generalization(general=Person, specific=Staff)
gen_OperationsStaff_Staff = Generalization(general=Staff, specific=OperationsStaff)
gen_AdministrativeStaff_Staff = Generalization(general=Staff, specific=AdministrativeStaff)
gen_TechnicalStaff_Staff = Generalization(general=Staff, specific=TechnicalStaff)
gen_Doctor_OperationsStaff = Generalization(general=OperationsStaff, specific=Doctor)
gen_Nurse_OperationsStaff = Generalization(general=OperationsStaff, specific=Nurse)
gen_Surgeon_Doctor = Generalization(general=Doctor, specific=Surgeon)
gen_Patient_Person = Generalization(general=Person, specific=Patient)

# Domain Model
domain_model = DomainModel(
    name="MyFirstModule",
    types={Nurse, Surgeon, Hospital, Department, Person, Patient, Staff, OperationsStaff, AdministrativeStaff, TechnicalStaff, Doctor, Gender},
    associations={Person_Hospital, Department_Hospital, Staff_Department, Patient_OperationsStaff},
    generalizations={gen_Staff_Person, gen_OperationsStaff_Staff, gen_AdministrativeStaff_Staff, gen_TechnicalStaff_Staff, gen_Doctor_OperationsStaff, gen_Nurse_OperationsStaff, gen_Surgeon_Doctor, gen_Patient_Person},
    metadata=None
)
