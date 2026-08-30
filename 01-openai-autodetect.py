from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# set OPENAI_BASE_URL and OPENAI_API_KEY environment variables, the client uses them automatically
# Need to import and load dote env to work

from dotenv import load_dotenv
load_dotenv()

deployment_name = "gpt-4.1-mini"
# token_provider = get_bearer_token_provider(DefaultAzureCredential(), "https://ai.azure.com/.default")

client = OpenAI()

response = client.responses.create(
    model=deployment_name,
    input="What is the capital of France?",
)

print(f"answer: {response.output[0].content[0].text}")
