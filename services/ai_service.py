import litellm
import os
from dotenv import load_dotenv

# Load environment variables (e.g. OPENAI_API_KEY, GROQ_API_KEY) from .env
load_dotenv()

def get_ai_response(prompt, system_message="You are a helpful hospital management assistant."):
    """
    Centralized function to handle AI inference via litellm.
    """
    try:
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        api_key = os.getenv("OLLAMA_API_KEY", "")
        
        # litellm expects custom API keys to be passed in if using a remote ollama server
        response = litellm.completion(
            model="ollama/llama3",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            api_base=base_url,
            api_key=api_key
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Error (Ensure Ollama is running or configure API key): {str(e)}"
