from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def main():
    completion = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "When was Microsoft founded?"}
        ]
    )
    print(completion.choices[0].message.content)

action = input("[1/1] Run chat.completions demo? (y) ")
if action == "y":
    main()
else:
    print("Abort")