from google import genai
from dotenv import load_dotenv
import json
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def assistant(user_input, last_interaction_id, history):
    history.append({
            "type": "user_input",
            "content": [{"type": "text", "text": user_input}]
        })
    
    kwargs = {
        "model": "gemini-3.5-flash",
        "input": history,
    }

    if last_interaction_id:
        kwargs["previous_interaction_id"] = last_interaction_id

    interaction = client.interactions.create(**kwargs)

    print(interaction.steps[-1].content[0].text)

    for step in interaction.steps:
        history.append(step.model_dump())

    return interaction.id, history