from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

stream = client.responses.create(
    model="gpt-4.1-mini",
    input="Write a caption for my tiktok study timelapse post\n" \
    "What actually happened:\n" \
    "- I was busy all day sleeping trying to cope up sleep\n" \
    "- Studied Azure AI Apps and Agents Developer Associate module for an hour\n" \
    "- tried lots of AI stuff, experimenting with Response client",
    stream=True
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)

# ? result: From catching up on sleep to diving into Azure AI Apps—an hour of focused study plus some fun AI experiments!

# ————————————————————————————————————

# If you're tracking conversation history when streaming, 
# you can get the response ID when the stream ends, like this:

stream2 = client.responses.create(
    model="gpt-4.1-mini",
    input="Some tips for night owls to prevent getting acne breakout",
    stream=True
)

for event2 in stream2:
    if event2.type == "response.output_text.delta":
        print(event2.delta, end="")
    elif event2.type == "response.completed":
        response_id = event2.response.id
        print(response_id)