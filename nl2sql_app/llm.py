import requests
from prompt import SCHEMA_CONTEXT

def generate_sql(user_query):
    prompt = f"""
    {SCHEMA_CONTEXT}

    User Question:
    {user_query}
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()