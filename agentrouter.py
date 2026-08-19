from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AGENTROUTER_API_KEY"),
    base_url="https://co.agentrouter.org/v1"
)

models = client.models.list()

for model in models.data:
    print(model.id)