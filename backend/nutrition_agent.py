from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Your_Groq_API_Key"))

def generate_meal_plan(diet, calories):

    prompt = f"""
    Create a 7 day healthy meal plan.

    Diet type: {diet}
    Daily calories: {calories}

    Include breakfast, lunch, dinner and snacks.
    """

    response = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile"
    )

    return response.choices[0].message.content