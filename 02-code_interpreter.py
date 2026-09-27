from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model = "gpt-4.1-mini",
    instructions="You are an AI assistant that provides information. Use the python tool to run code for math problems.",
    input="What is the square root of 56761156?",
    tools=[{"type": "code_interpreter",
            "container": {"type": "auto"}}]
)

print(response.output_text)
