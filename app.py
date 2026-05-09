import streamlit as st
from hospital_manager import get_initial_hospital
from utils.styles import apply_custom_styles
from views.dashboard import render_dashboard
from views.doctors import render_doctors
from views.patients import render_patients
from views.appointments import render_appointments
from views.assistant import render_assistant
from dotenv import load_dotenv

# Load environment variables (like API keys)
load_dotenv()

# --- Configuration & Styling ---
st.set_page_config(page_title="Hospital Management System", page_icon="🏥", layout="wide")
apply_custom_styles()

# --- State Management ---
if 'hospital' not in st.session_state:
    st.session_state['hospital'] = get_initial_hospital()
hospital = st.session_state['hospital']

# --- Navigation ---
st.sidebar.title("🏥 HMS Navigation")
menu = ["📊 Dashboard", "👨‍⚕️ Doctors", "🩺 Patients", "📅 Appointments", "🤖 AI Assistant"]
choice = st.sidebar.radio("Go to", menu)

st.sidebar.markdown("---")
st.sidebar.info("Using **Llama AI** for intelligent assistance.")

# --- Page Routing ---
if choice == "📊 Dashboard":
    render_dashboard(hospital)
elif choice == "👨‍⚕️ Doctors":
    render_doctors(hospital)
elif choice == "🩺 Patients":
    render_patients(hospital)
elif choice == "📅 Appointments":
    render_appointments(hospital)
elif choice == "🤖 AI Assistant":
    render_assistant(hospital)
