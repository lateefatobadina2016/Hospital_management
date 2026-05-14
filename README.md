# 🏥 AI-Powered Hospital Management System

![HMS Dashboard Preview](C:\Users\user\.gemini\antigravity\brain\15958bb7-2eb6-429e-aae8-78373e3b2acd\hms_dashboard_preview_1778707368802.png)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A state-of-the-art, modular web application built with **Streamlit** for seamless hospital operations management. This system integrates **Llama AI** (via LiteLLM) to empower medical professionals with intelligent diagnosis recommendations and automated administrative assistance.

---

## 🌟 Key Features

*   **📊 Dynamic Dashboard:** Real-time analytics on hospital performance, patient flow, and resource allocation.
*   **👨‍⚕️ Advanced Doctor Portal:** Comprehensive management of medical staff across specialized departments.
*   **🩺 Secure Patient Records:** HIPAA-inspired digital health records with AI-augmented diagnosis history.
*   **📅 Smart Appointments:** Streamlined scheduling system connecting patients with the right specialists.
*   **🤖 Llama AI Assistant:** 
    *   **Automated Diagnosis:** Generates professional medical insights based on symptoms.
    *   **Staff Chatbot:** Interactive knowledge base for hospital protocols and medical queries.

---

## 🛠️ Technology Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) with Premium CSS |
| **Intelligence** | [LiteLLM](https://github.com/BerriAI/litellm) (Llama 3.3) |
| **Logic** | Python 3.x (Object-Oriented Architecture) |
| **Environment** | `python-dotenv` |

---

## 📁 Architecture Overview

```text
├── app.py                   # Central Routing & UI Entry Point
├── models.py                # Core Entities (Patient, Doctor, etc.)
├── hospital_manager.py      # Business Logic Controller
├── services/
│   └── ai_service.py        # AI Inference Layer (LiteLLM)
├── views/                   # Modular Page Components
│   ├── dashboard.py
│   └── assistant.py
└── utils/
    └── styles.py            # Global Design System
```

---

## 🚀 Quick Start

### 1. Installation
```bash
git clone https://github.com/lateefatobadina2016/Hospital_management.git
cd Hospital_management
pip install -r requirements.txt
```

### 2. Configuration
Create a `.env` file from the template:
```bash
cp .env.example .env
```
Add your AI provider credentials (Ollama, Groq, or OpenAI) in the `.env` file.

### 3. Launch
```bash
streamlit run app.py
```

---

## ☁️ Deployment

### 🟢 Option A: Streamlit Community Cloud (Recommended)
1. Push your code to a GitHub repository.
2. Visit [share.streamlit.io](https://share.streamlit.io/).
3. Connect your repo and deploy. **It's free and handles everything!**

### 🟡 Option B: Vercel (Experimental)
While Vercel is optimized for static sites, you can deploy using a Python runtime. 
1. Install the [Vercel CLI](https://vercel.com/download).
2. Run `vercel` in the project root.
3. *Note: Streamlit on Vercel requires specific `vercel.json` routing which may impact performance.*

---

## 🎓 Academic Context
This project was developed as a capstone project for an **AI Engineering Bootcamp**.

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.
