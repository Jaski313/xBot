from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv()
client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)


def getResponse(prompt: str, input: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input},
            ]
    )
    return response.choices[0].message.content
