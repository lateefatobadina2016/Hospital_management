import litellm
import os
from dotenv import load_dotenv

# Load environment variables (e.g. OPENAI_API_KEY, GROQ_API_KEY) from .env
load_dotenv()

def get_ai_response(prompt, system_message="You are a helpful hospital management assistant."):
    """
    Centralized function to handle AI inference via litellm.
    Supports multiple providers: OpenAI, Groq, and Ollama.
    Auto-selects the best available provider based on configured API keys.
    """
    try:
        # Check which provider is configured
        openai_key = os.getenv("OPENAI_API_KEY", "").strip()
        groq_key = os.getenv("GROQ_API_KEY", "").strip()
        ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").strip()
        
        # Priority: OpenAI > Groq > Ollama
        if openai_key:
            response = litellm.completion(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                api_key=openai_key
            )
            return response.choices[0].message.content
        
        elif groq_key:
            response = litellm.completion(
                model="groq/llama-3.1-70b-versatile",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                api_key=groq_key
            )
            return response.choices[0].message.content
        
        else:
            # Default to Ollama (local)
            response = litellm.completion(
                model="ollama/llama2",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                api_base=ollama_url,
                api_key=""
            )
            return response.choices[0].message.content
            
    except Exception as e:
        error_msg = str(e)
        
        # Provide helpful error messages
        if "Cannot assign requested address" in error_msg or "Connection refused" in error_msg:
            return "❌ **Connection Error**: Cannot reach Ollama at " + os.getenv("OLLAMA_BASE_URL", "http://localhost:11434") + "\n\n**Solutions:**\n1. Start Ollama: `ollama serve`\n2. OR add `OPENAI_API_KEY` to .env\n3. OR add `GROQ_API_KEY` to .env"
        elif "Invalid API key" in error_msg or "Unauthorized" in error_msg:
            return "❌ **Authentication Error**: Invalid API key. Please check your .env file configuration."
        elif "model" in error_msg.lower():
            return "❌ **Model Error**: The specified model is not available. Please check your configuration."
        else:
            return f"❌ **AI Error**: {error_msg}"
