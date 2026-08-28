####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType, DateType,
)

# ------------------------------------------------------------------
# Enumerations
# ------------------------------------------------------------------

Gender = Enumeration(
    name="Gender",
    literals={
        EnumerationLiteral(name="Female"),
        EnumerationLiteral(name="Male"),
        EnumerationLiteral(name="Other"),
    },
)

# ------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------

Hospital = Class(name="Hospital")
Person = Class(name="Person")
Department = Class(name="Department")
Patient = Class(name="Patient")          # generalizes Person
Staff = Class(name="Staff")              # generalizes Person
AdministrativeStaff = Class(name="AdministrativeStaff")   # generalizes Staff
OperationsStaff = Class(name="OperationsStaff")           # generalizes Staff
TechnicalStaff = Class(name="TechnicalStaff")             # generalizes Staff
Doctor = Class(name="Doctor")            # generalizes OperationsStaff
Nurse = Class(name="Nurse")              # generalizes OperationsStaff
Surgeon = Class(name="Surgeon")          # generalizes Doctor

# Hospital attributes
Hospital_name: Property = Property(name="name",    type=StringType)
Hospital_address: Property = Property(name="address", type=StringType)
Hospital_phone: Property = Property(name="phone",   type=StringType)
Hospital.attributes = {Hospital_name, Hospital_address, Hospital_phone}

# Person attributes
Person_givenName: Property = Property(name="givenName",   type=StringType)
Person_middleName: Property = Property(name="middleName",  type=StringType)
Person_familyName: Property = Property(name="familyName",  type=StringType)
Person_birthDate: Property = Property(name="birthDate",    type=DateType)
Person_gender: Property = Property(name="gender",          type=Gender)
Person_phone: Property = Property(name="phone",            type=StringType)
Person.attributes = {
    Person_givenName, Person_middleName, Person_familyName,
    Person_birthDate, Person_gender, Person_phone,
}

# Department – no own attributes
Department.attributes = set()

# Patient own attributes  (inherits Person attrs via generalization)
Patient_patientId: Property = Property(name="patientId",    type=StringType)
Patient_acceptedDate: Property = Property(name="acceptedDate", type=DateType)
Patient_sickness: Property = Property(name="sickness",      type=StringType)
Patient_allergies: Property = Property(name="allergies",    type=StringType)
Patient_specialReqs: Property = Property(name="specialReqs", type=StringType)
Patient.attributes = {
    Patient_patientId, Patient_acceptedDate, Patient_sickness,
    Patient_allergies, Patient_specialReqs,
}

# Staff own attributes  (inherits Person attrs via generalization)
Staff_joined: Property = Property(name="joined",           type=DateType)
Staff_education: Property = Property(name="education",     type=StringType)
Staff_certification: Property = Property(name="certification", type=StringType)
Staff_Language: Property = Property(name="Language",       type=StringType)
Staff.attributes = {Staff_joined, Staff_education, Staff_certification, Staff_Language}

# Doctor own attributes  (inherits OperationsStaff → Staff → Person attrs)
Doctor_speciality: Property = Property(name="speciality", type=StringType)
Doctor_location: Property = Property(name="location",     type=StringType)
Doctor.attributes = {Doctor_speciality, Doctor_location}

# Subclasses with no additional own attributes
AdministrativeStaff.attributes = set()
OperationsStaff.attributes = set()
TechnicalStaff.attributes = set()
Nurse.attributes = set()
Surgeon.attributes = set()

# ------------------------------------------------------------------
# Generalizations  (specific IS-A general)
# ------------------------------------------------------------------

gen_patient_person         = Generalization(general=Person,         specific=Patient)
gen_staff_person           = Generalization(general=Person,         specific=Staff)
gen_admin_staff            = Generalization(general=Staff,          specific=AdministrativeStaff)
gen_ops_staff              = Generalization(general=Staff,          specific=OperationsStaff)
gen_tech_staff             = Generalization(general=Staff,          specific=TechnicalStaff)
gen_doctor_ops             = Generalization(general=OperationsStaff, specific=Doctor)
gen_nurse_ops              = Generalization(general=OperationsStaff, specific=Nurse)
gen_surgeon_doctor         = Generalization(general=Doctor,         specific=Surgeon)

# ------------------------------------------------------------------
# Associations
# ------------------------------------------------------------------

# Person ↔ Hospital  (N:M  –  ReferenceSet)
Person_Hospital: BinaryAssociation = BinaryAssociation(
    name="Person_Hospital",
    ends={
        Property(name="person",   type=Person,   multiplicity=Multiplicity(0, "*")),
        Property(name="hospital", type=Hospital, multiplicity=Multiplicity(0, "*")),
    },
)

# Department ↔ Hospital  (N:1  –  Reference)
Department_Hospital: BinaryAssociation = BinaryAssociation(
    name="Department_Hospital",
    ends={
        Property(name="department", type=Department, multiplicity=Multiplicity(0, "*")),
        Property(name="hospital",   type=Hospital,   multiplicity=Multiplicity(1, 1)),
    },
)

# Staff ↔ Department  (N:1  –  Reference)
Staff_Department: BinaryAssociation = BinaryAssociation(
    name="Staff_Department",
    ends={
        Property(name="staff",      type=Staff,      multiplicity=Multiplicity(0, "*")),
        Property(name="department", type=Department, multiplicity=Multiplicity(1, 1)),
    },
)

# Patient ↔ OperationsStaff  (N:M  –  ReferenceSet)
Patient_OperationsStaff: BinaryAssociation = BinaryAssociation(
    name="Patient_OperationsStaff",
    ends={
        Property(name="patient",         type=Patient,         multiplicity=Multiplicity(0, "*")),
        Property(name="operationsstaff", type=OperationsStaff, multiplicity=Multiplicity(0, "*")),
    },
)

# ------------------------------------------------------------------
# Domain Model
# ------------------------------------------------------------------

hospital_domain_model = DomainModel(
    name="MyFirstModule",
    types={
        Hospital, Person, Department, Patient, Staff,
        AdministrativeStaff, OperationsStaff, TechnicalStaff,
        Doctor, Nurse, Surgeon,
        Gender,
    },
    associations={
        Person_Hospital, Department_Hospital,
        Staff_Department, Patient_OperationsStaff,
    },
    generalizations={
        gen_patient_person, gen_staff_person,
        gen_admin_staff, gen_ops_staff, gen_tech_staff,
        gen_doctor_ops, gen_nurse_ops, gen_surgeon_doctor,
    },
)
