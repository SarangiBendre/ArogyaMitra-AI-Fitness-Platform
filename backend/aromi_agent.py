from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Your_Groq_API_Key"))

def aromi_chat(message):

    prompt = f"""
    You are AROMI, an AI fitness and wellness coach.

    Help users with:
    - workout advice
    - travel fitness tips
    - motivation
    - healthy habits

    User message: {message}
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content