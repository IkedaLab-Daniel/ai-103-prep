import os
from dotenv import load_dotenv
load_dotenv()
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT", "gpt-4.1-mini")
token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI(
    base_url=endpoint,
    api_key=token_provider
)

user_prompt = input("Enter prompt: ")

response = client.responses.create(
    model=deployment_name,
    input=user_prompt,
)

print(f"answer: {response.output[0]}")
