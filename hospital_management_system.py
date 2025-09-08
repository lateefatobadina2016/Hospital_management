class MedicalRecord:
    def __init__(self):
        self.records = []

    def add_record(self, diagnosis, recommendation):
        self.records.append({
            "diagnosis": diagnosis,
            "recommendation": recommendation
        })

    def display_records(self):
        for idx, record in enumerate(self.records, 1):
            print(f"\nRecord {idx}:")
            print("Diagnosis:", record["diagnosis"])
            print("Recommendation:", record["recommendation"])


class Patient:
    def __init__(self, name, personal_id):
        self.name = name
        self.personal_id = personal_id
        self.appointment_history = []
        self.medical_record = MedicalRecord()

    def add_appointment(self, appointment):
        self.appointment_history.append(appointment)


class Doctor:
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
        self.patients = []

    def add_patient(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)

    def list_patients(self):
        print(f"\nPatients of Dr. {self.name}:")
        for patient in self.patients:
            print(f"- {patient.name} (ID: {patient.personal_id})")


class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.status = "Scheduled"

    def complete(self, diagnosis, recommendation):
        self.status = "Completed"
        self.patient.medical_record.add_record(diagnosis, recommendation)
        print(f"\nAppointment on {self.date} completed with diagnosis: {diagnosis}")


class Department:
    def __init__(self, name):
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)


class Hospital:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_department(self, department):
        self.departments.append(department)

    def add_doctor(self, doctor, department_name):
        for dept in self.departments:
            if dept.name.lower() == department_name.lower():
                dept.add_doctor(doctor)
                self.doctors.append(doctor)
                print(f"Added Dr. {doctor.name} to {department_name} department.")
                return
        print("Department not found!")

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, doctor_name, patient_id, date):
        doctor = next((d for d in self.doctors if d.name.lower() == doctor_name.lower()), None)
        patient = next((p for p in self.patients if p.personal_id == patient_id), None)
        if doctor and patient:
            appointment = Appointment(doctor, patient, date)
            patient.add_appointment(appointment)
            doctor.add_patient(patient)
            self.appointments.append(appointment)
            print("Appointment scheduled.")
        else:
            print("Doctor or patient not found.")

    def complete_appointment(self, patient_id, date, diagnosis, recommendation):
        for appt in self.appointments:
            if appt.patient.personal_id == patient_id and appt.date == date:
                appt.complete(diagnosis, recommendation)
                return
        print("Appointment not found.")

    def view_doctor_patients(self, doctor_name):
        doctor = next((d for d in self.doctors if d.name.lower() == doctor_name.lower()), None)
        if doctor:
            doctor.list_patients()
        else:
            print("Doctor not found.")

    def view_patient_history(self, patient_id):
        patient = next((p for p in self.patients if p.personal_id == patient_id), None)
        if patient:
            print(f"\nMedical History of {patient.name}:")
            patient.medical_record.display_records()
        else:
            print("Patient not found.")



# Main Menu Loop

hospital = Hospital("General Hospital")
hospital.add_department(Department("Cardiology"))
hospital.add_department(Department("Orthopedics"))
hospital.add_department(Department("Dermatology"))
hospital.add_department(Department("Psychiatry"))
hospital.add_department(Department("Ophthalmology"))


while True:
    print("\n--- Hospital Management Menu ---")
    print("1. Add Doctor")
    print("2. Add Patient")
    print("3. Schedule Appointment")
    print("4. Complete Appointment")
    print("5. View Doctor’s Patients")
    print("6. View Patient’s Medical History")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter doctor's name: ")
        specialization = input("Enter specialization: ")
        dept = input("Enter department name: ")
        doctor = Doctor(name, specialization)
        hospital.add_doctor(doctor, dept)

    elif choice == '2':
        name = input("Enter patient name: ")
        pid = input("Enter personal ID: ")
        patient = Patient(name, pid)
        hospital.add_patient(patient)
        print("Patient added.")

    elif choice == '3':
        doc_name = input("Enter doctor's name: ")
        pid = input("Enter patient ID: ")
        date = input("Enter appointment date (YYYY-MM-DD): ")
        hospital.schedule_appointment(doc_name, pid, date)

    elif choice == '4':
        pid = input("Enter patient ID: ")
        date = input("Enter appointment date to complete: ")
        diagnosis = input("Enter diagnosis: ")
        recommendation = input("Enter recommendation: ")
        hospital.complete_appointment(pid, date, diagnosis, recommendation)

    elif choice == '5':
        doc_name = input("Enter doctor's name: ")
        hospital.view_doctor_patients(doc_name)

    elif choice == '6':
        pid = input("Enter patient ID: ")
        hospital.view_patient_history(pid)

    elif choice == '7':
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
