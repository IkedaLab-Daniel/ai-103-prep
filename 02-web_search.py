from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model = "gpt-4.1-mini",
    instructions="You are an AI assistant. Use web search when current information is required.",
    input="What are three major announcements from Microsoft Build this week?",
    tools=[{"type": "web_search"}]
)

print(response.output_text)
