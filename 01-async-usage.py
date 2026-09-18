import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv
load_dotenv()

client = AsyncOpenAI()

async def main():
    response = await client.responses.create(
        model="gpt-4.1-mini",
        input="Explain how AI Engineering relates to Web Development"
    )
    print(response.output_text)

# Run
action = input('[1/2] Enter "y" to run async demo: ')
if action == "y":
    asyncio.run(main())

# * Async streaming ——————————————————————————————————————————————————————

async def stream_response():
    streams = await client.responses.create(
        model="gpt-4.1-mini",
        input="Explain how AI Engineering relates to Web Development",
        stream=True
    )

    async for event in streams:
        if event.type == "response.output_text.delta":
            print(event.delta, end="", flush=True)

action = input('[2/2] Enter "y" to run async streaming demo: ')
if action == "y":
    asyncio.run(stream_response())


    