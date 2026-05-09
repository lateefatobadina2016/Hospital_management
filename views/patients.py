import streamlit as st
from models import Patient

def render_patients(hospital):
    st.title("Manage Patients")
    
    tab1, tab2 = st.tabs(["View Patients", "Add Patient"])
    
    with tab1:
        if hospital.patients:
            for p in hospital.patients:
                with st.expander(f"Patient: {p.name} (ID: {p.personal_id})"):
                    if p.medical_record.records:
                        for idx, rec in enumerate(p.medical_record.records, 1):
                            st.markdown(f"**Record {idx}:**")
                            st.write(f"- **Diagnosis:** {rec['diagnosis']}")
                            st.write(f"- **Recommendation:** {rec['recommendation']}")
                    else:
                        st.write("No medical records found.")
        else:
            st.info("No patients available.")
            
    with tab2:
        with st.form("add_pat_form"):
            name = st.text_input("Patient Name")
            pid = st.text_input("Personal ID")
            submit = st.form_submit_button("Add Patient")
            
            if submit:
                if name and pid:
                    # check if exists
                    if any(pat.personal_id == pid for pat in hospital.patients):
                        st.error("Patient ID already exists!")
                    else:
                        new_pat = Patient(name, pid)
                        success, msg = hospital.add_patient(new_pat)
                        st.success(msg)
                else:
                    st.warning("Please fill all fields.")
