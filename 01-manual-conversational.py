from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

deployment_name = "gpt-4.1-mini"

client = OpenAI()

try:
    conversation_history = [
        {
            "type": "message",
            "role": "user",
            "content": "What is AI Engineering"
        }
    ]

    # First Response
    response1 =  client.responses.create(
        model=deployment_name,
        input=conversation_history
    )

    print("Assistant:", response1.output_text)

    # Add the response to the history
    conversation_history += response1.output

    print(conversation_history)

except Exception as Ice:
    print(Ice)