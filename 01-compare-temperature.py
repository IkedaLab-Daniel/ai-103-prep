from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

model_name = "gpt-4.1-mini"

# ? High Temperature
print("High Temperature")
for i in range(3):
    response_1 = client.responses.create(
        model=model_name,
        instructions="Complete the sentence.",
        input="I don't like ",
        temperature=0.9,
        max_output_tokens=30
    )

    print(response_1.output[0].content[0].text)

# ————————————————————————————————————————————————————————————————————

# ! Low Temperature
print("Low Temperature")
for i in range(3):
    response_1 = client.responses.create(
        model=model_name,
        instructions="Complete the sentence.",
        input="I don't like ",
        temperature=0.1,
        max_output_tokens=30
    )

    print(response_1.output[0].content[0].text)
