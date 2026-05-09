# 🏥 AI-Powered Hospital Management System

A modern, modular, and intuitive web application built with **Streamlit** for managing hospital operations. This system securely handles Doctors, Patients, and Appointments, while heavily leveraging **Llama AI** (via LiteLLM) to assist medical staff with diagnosis recommendations and general hospital queries.

## ✨ Features

- **📊 Interactive Dashboard:** Get a bird's-eye view of total departments, active doctors, registered patients, and pending appointments.
- **👨‍⚕️ Doctor Management:** Add and view doctors, assign them to specific departments, and track their assigned patients.
- **🩺 Patient Records:** Securely register patients and view their comprehensive medical history, including past diagnoses and AI-assisted recommendations.
- **📅 Appointment Scheduling:** Schedule appointments between doctors and patients.
- **🤖 AI Diagnosis Assistant:** When completing an appointment, doctors can input symptoms/findings, and the integrated Llama AI will automatically generate professional medical recommendations.
- **💬 General AI Assistant Chatbot:** A dedicated conversational interface for hospital staff to query medical information or summarize hospital data.

## 🛠️ Tech Stack

- **Frontend/UI:** [Streamlit](https://streamlit.io/) (with custom CSS for a premium aesthetic)
- **Backend Core:** Python (Modular Object-Oriented design)
- **AI Integration:** [LiteLLM](https://github.com/BerriAI/litellm) (Supports Ollama, Groq, OpenAI, etc.)
- **Environment Management:** `python-dotenv`

## 📁 Project Structure

The codebase is highly modular, ensuring ease of maintenance and scalability:

```text
├── app.py                   # Main entry point and Streamlit router
├── models.py                # Core data structures (Patient, Doctor, Appointment, etc.)
├── hospital_manager.py      # Main controller logic
├── requirements.txt         # Python dependencies
├── .env.example             # Template for API Keys
├── services/
│   └── ai_service.py        # Centralized LLM/AI inference logic
├── utils/
│   └── styles.py            # Custom CSS definitions
└── views/                   # Modular Streamlit UI pages
    ├── dashboard.py
    ├── doctors.py
    ├── patients.py
    ├── appointments.py
    └── assistant.py
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/lateefatobadina2016/Hospital_management.git
cd Hospital_management
```

### 2. Install Dependencies
It is recommended to use a virtual environment.
```bash
pip install -r requirements.txt
```

### 3. Configure the AI Environment
This application uses **LiteLLM**, meaning you can easily swap between a local, free AI (like Ollama) or a blazing fast cloud API (like Groq).

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open the `.env` file and configure your API keys. For example, if you are using a remote Ollama server:
   ```env
   OLLAMA_API_KEY=your_api_key_here
   OLLAMA_BASE_URL=https://ollama.com/api/v1
   ```
   *(Note: You can edit `services/ai_service.py` to change the specific model from `ollama/llama3` to `groq/llama3-8b-8192` if you prefer).*

### 4. Run the Application
```bash
streamlit run app.py
```
The application will automatically open in your default web browser at `http://localhost:8501`.

## 📄 License
This project was developed as part of a school project for WSB Merito Gdansk.
