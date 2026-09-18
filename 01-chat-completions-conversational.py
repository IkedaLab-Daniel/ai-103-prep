from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

# Initial messages
conversation_messages=[
    {
        "role": "system",
        "content": "You are a helpful AI assistant that answers questions and provides information."
    }
]

# Add the first user message
conversation_messages.append(
    {"role": "user",
    "content": "When was Microsoft founded?"}
)

completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=conversation_messages
)

assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_message)

# Add the next user message
conversation_messages.append(
    {"role": "user",
    "content": "Who founded it?"}
)

# Get a completion
completion = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=conversation_messages
)
assistant_message = completion.choices[0].message.content
print("Assistant:", assistant_message)