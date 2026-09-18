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
    # print(response.output_text)
    print(f"answer: {response.output[0].content[0].text}")

asyncio.run(main())