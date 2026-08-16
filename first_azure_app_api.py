import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
)

user_input = input("You: ") 

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
)

print("\nAzure ni Callejas: ", response.choices[0].message.content)