from models import Department, Appointment

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
                return True, f"Added Dr. {doctor.name} to {department_name} department."
        return False, "Department not found!"

    def add_patient(self, patient):
        self.patients.append(patient)
        return True, "Patient added successfully."

    def schedule_appointment(self, doctor_name, patient_id, date):
        doctor = next((d for d in self.doctors if d.name.lower() == doctor_name.lower()), None)
        patient = next((p for p in self.patients if p.personal_id == patient_id), None)
        if doctor and patient:
            appointment = Appointment(doctor, patient, date)
            patient.add_appointment(appointment)
            doctor.add_patient(patient)
            self.appointments.append(appointment)
            return True, "Appointment scheduled successfully."
        else:
            return False, "Doctor or patient not found."

    def complete_appointment(self, patient_id, date, diagnosis, recommendation):
        for appt in self.appointments:
            if appt.patient.personal_id == patient_id and appt.date == date:
                return appt.complete(diagnosis, recommendation)
        return False, "Appointment not found."

def get_initial_hospital():
    hospital = Hospital("General Hospital")
    hospital.add_department(Department("Cardiology"))
    hospital.add_department(Department("Orthopedics"))
    hospital.add_department(Department("Dermatology"))
    hospital.add_department(Department("Psychiatry"))
    hospital.add_department(Department("Ophthalmology"))
    return hospital
