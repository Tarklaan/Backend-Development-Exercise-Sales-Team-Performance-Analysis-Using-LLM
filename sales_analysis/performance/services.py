import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY


def generate_feedback(data):
    response = openai.Completion.create(
        model="gpt-3.5-turbo",  
        prompt=f"Provide feedback based on the following data: {data}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()