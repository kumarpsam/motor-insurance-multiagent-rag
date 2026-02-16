import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3:mini"

def call_llm(prompt, max_tokens=50):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens,
                "temperature": 0,
                "top_p": 0.8,
                "stop": ["\n\n", "Note", "("]
            }
        }
    )
    
    return response.json()["response"].strip()
