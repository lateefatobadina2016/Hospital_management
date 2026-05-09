import streamlit as st

def render_dashboard(hospital):
    st.title("Hospital Overview")
    st.markdown("Welcome to the **General Hospital Management System**. Use the sidebar to navigate.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='metric-card'><h3>Departments</h3><h1>{len(hospital.departments)}</h1></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='metric-card'><h3>Doctors</h3><h1>{len(hospital.doctors)}</h1></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='metric-card'><h3>Patients</h3><h1>{len(hospital.patients)}</h1></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='metric-card'><h3>Appointments</h3><h1>{len(hospital.appointments)}</h1></div>", unsafe_allow_html=True)
