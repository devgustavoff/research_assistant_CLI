from google import genai
import os

client = genai.Client(api_key=os.environ("GOOGLE_APY_KEY"))

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="O que é RAG em AI engineering?"
)

print(response.text)