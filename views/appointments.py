import streamlit as st
from services.ai_service import get_ai_response

def render_appointments(hospital):
    st.title("Manage Appointments")
    
    tab1, tab2, tab3 = st.tabs(["Schedule", "Complete (AI Assisted)", "View All"])
    
    with tab1:
        with st.form("schedule_appt_form"):
            doc_names = [d.name for d in hospital.doctors]
            pat_ids = [f"{p.name} ({p.personal_id})" for p in hospital.patients]
            
            sel_doc = st.selectbox("Select Doctor", doc_names) if doc_names else None
            sel_pat = st.selectbox("Select Patient", pat_ids) if pat_ids else None
            date = st.date_input("Appointment Date")
            
            submit = st.form_submit_button("Schedule")
            if submit:
                if sel_doc and sel_pat:
                    pid = sel_pat.split("(")[-1].replace(")", "")
                    success, msg = hospital.schedule_appointment(sel_doc, pid, str(date))
                    if success: 
                        st.success(msg)
                    else: 
                        st.error(msg)
                else:
                    st.warning("Ensure both doctors and patients exist.")

    with tab2:
        st.markdown("### Complete Appointment")
        st.caption("Use Llama AI to suggest recommendations based on diagnosis.")
        
        pending_appts = [a for a in hospital.appointments if a.status == "Scheduled"]
        if pending_appts:
            appt_options = [f"{a.date} - Dr. {a.doctor.name} & Patient {a.patient.name} ({a.patient.personal_id})" for a in pending_appts]
            sel_appt_str = st.selectbox("Select Appointment", appt_options)
            
            diagnosis = st.text_area("Diagnosis (Symptoms/Findings)")
            
            col1, col2 = st.columns(2)
            with col1:
                generate_ai = st.button("🤖 Generate AI Recommendation")
            
            recommendation = st.session_state.get("ai_rec", "")
            
            if generate_ai and diagnosis:
                with st.spinner("Llama AI is thinking..."):
                    prompt = f"Given the patient diagnosis: '{diagnosis}', provide a brief, professional medical recommendation and next steps (max 3 sentences)."
                    recommendation = get_ai_response(prompt)
                    st.session_state["ai_rec"] = recommendation
            
            rec_input = st.text_area("Recommendation", value=recommendation, height=100)
            
            if st.button("Mark as Completed"):
                if diagnosis and rec_input:
                    # extract pid and date
                    parts = sel_appt_str.split(" - ")
                    date_part = parts[0]
                    pid_part = parts[1].split("(")[-1].replace(")", "")
                    
                    success, msg = hospital.complete_appointment(pid_part, date_part, diagnosis, rec_input)
                    if success:
                        st.success(msg)
                        if "ai_rec" in st.session_state: 
                            del st.session_state["ai_rec"]
                    else:
                        st.error(msg)
                else:
                    st.warning("Please provide both diagnosis and recommendation.")
        else:
            st.info("No pending appointments.")

    with tab3:
        if hospital.appointments:
            for appt in hospital.appointments:
                status_color = "green" if appt.status == "Completed" else "orange"
                st.markdown(f"**{appt.date}** | Dr. {appt.doctor.name} & {appt.patient.name} | Status: <span style='color:{status_color}'>{appt.status}</span>", unsafe_allow_html=True)
        else:
            st.info("No appointments scheduled.")
