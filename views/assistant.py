import streamlit as st
from services.ai_service import get_ai_response

def render_assistant(hospital):
    st.title("Hospital AI Assistant")
    st.markdown("Chat with the Llama-powered AI for general queries or to summarize patient data.")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Hello! I am your HMS AI assistant. How can I help you today?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask something (e.g., 'What are the common symptoms of flu?'):"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # Build context about hospital state
            context = f"Hospital has {len(hospital.doctors)} doctors and {len(hospital.patients)} patients. "
            system_msg = "You are a medical assistant helping staff manage a hospital. " + context
            
            response = get_ai_response(prompt, system_message=system_msg)
            message_placeholder.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
