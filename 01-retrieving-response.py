from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
model = "gpt-4.1-mini"
prev_conversation_id = "resp_05dd4b3889131bf8006aac4516aa708197a5e70130fbcfa168"

try:   
    # Retrieve a previous response
    response_id = prev_conversation_id
    previous_response = client.responses.retrieve(response_id)

    print(f"Previous response: {previous_response.output_text}")

except Exception as ex:
    print(f"Error: {ex}")