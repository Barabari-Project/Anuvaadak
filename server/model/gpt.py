import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def translate(file, lang):
    text = "Translate this into 1. French, 2. Spanish and 3. Japanese:\n\nWhat rooms do you have available?\n\n1."
    text = READFILE()
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=text,
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response
