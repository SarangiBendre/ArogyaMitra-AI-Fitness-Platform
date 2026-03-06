from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Your_Groq_API_Key"))

def generate_workout(goal, minutes):

    prompt = f"""
    Create a simple 7 day workout plan.

    Goal: {goal}
    Daily time: {minutes} minutes

    Include:
    - Warmup
    - Exercises
    - Rest
    - Short tip
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content