import os

from dotenv import load_dotenv
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider


# Load environment variables
load_dotenv()


# Create Azure credential
credential = DefaultAzureCredential()


# Create a token provider for Azure AI
token_provider = get_bearer_token_provider(
    credential,
    "https://ai.azure.com/.default"
)


# Create OpenAI client using Microsoft Entra ID authentication
client = OpenAI(
    # base_url=os.getenv("AZURE_OPENAI_ENDPOINT"),
    base_url="https://ikedalabdaniel-resource.services.ai.azure.com/openai/v1/",
    api_key=token_provider,
)


# Get user input
user_input = input("You: ")


# Send request
response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {
            "role": "user",
            "content": user_input,
        }
    ],
)


print("\nAzure ni Callejas:", response.choices[0].message.content)