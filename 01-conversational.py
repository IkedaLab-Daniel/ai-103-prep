from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

deployment_name = "gpt-4.1-mini"

client = OpenAI()

response1 = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="What is machine learning?"
)

print("Assistant: ", response1.output_text)

response2 = client.responses.create(
    model=deployment_name,
    instructions="You are a helpful AI assistant that explains technology concepts clearly.",
    input="Can you give me an example?",
    previous_response_id=response1.id
)

print("Assistant: ", response2.output_text)

# Behind the scene, it's a loop that links last response to the current query:

# Track responses
# last_response_id = None

# Loop until the user wants to quit
# print("Assistant: Enter a prompt (or type 'quit' to exit)")
# while True:
#     input_text = input('\nYou: ')
#     if input_text.lower() == "quit":
#         print("Assistant: Goodbye!")
#         break

#     # Get a response
#     response = openai_client.responses.create(
#                 model=model_name,
#                 instructions="You are a helpful AI assistant that explains technology concepts clearly.",
#                 input=input_text,
#                 previous_response_id=last_response_id
#     )
#     assistant_text = response.output_text
#     print("\nAssistant:", assistant_text)
#     last_response_id = response.id