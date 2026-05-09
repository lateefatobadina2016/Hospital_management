import streamlit as st
from models import Doctor

def render_doctors(hospital):
    st.title("Manage Doctors")
    
    tab1, tab2 = st.tabs(["View Doctors", "Add Doctor"])
    
    with tab1:
        if hospital.doctors:
            for doc in hospital.doctors:
                with st.expander(f"Dr. {doc.name} - {doc.specialization}"):
                    st.write(f"**Patients:** {len(doc.patients)}")
                    for p in doc.patients:
                        st.write(f"- {p.name} (ID: {p.personal_id})")
        else:
            st.info("No doctors available. Add one in the next tab.")
            
    with tab2:
        with st.form("add_doc_form"):
            name = st.text_input("Doctor's Name")
            spec = st.text_input("Specialization")
            dept = st.selectbox("Department", [d.name for d in hospital.departments])
            submit = st.form_submit_button("Add Doctor")
            
            if submit:
                if name and spec and dept:
                    new_doc = Doctor(name, spec)
                    success, msg = hospital.add_doctor(new_doc, dept)
                    if success: 
                        st.success(msg)
                    else: 
                        st.error(msg)
                else:
                    st.warning("Please fill all fields.")
