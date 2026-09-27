from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Create vendor store and upload a file
vector_store = client.vector_stores.create(name="policy-docs")
client.vector_stores.files.upload_and_poll(
    vector_store_id=vector_store.id,
    file=open("policy-sample.pdf", "rb")
)

response = client.responses.create(
    model = "gpt-4.1-mini",
    instructions="You are an AI assistant I made for learning Azure AI that provides information from the given sample policy documents.",
    input="Tell me a fact about Conflicts of Interest of our policy",
    tools=[{
        "type": "file_search",
        "vector_store_ids": [vector_store.id]
    }],
    include=["file_search_call.results"]
)

print(response.output_text)
