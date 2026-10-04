"""Build Agent using Microsoft Agent Framework in Python
# Run this python script
> pip install agent-framework==1.0.0rc6
> python <this-script-path>.py
"""

import asyncio
import os
from dotenv import load_dotenv

from agent_framework_foundry import FoundryAgent
from azure.identity.aio import DefaultAzureCredential

load_dotenv()

# User inputs for the conversation
USER_INPUTS = [
    "Hello",
]

async def main() -> None:
    # For authentication, DefaultAzureCredential supports multiple authentication methods. Run `az login` in terminal for Azure CLI auth.
    async with FoundryAgent(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        agent_name="first-agent",
        agent_version="1",
        credential=DefaultAzureCredential(),
    ) as agent:
    
        # Process user messages
        for user_input in USER_INPUTS:
            print(f"\n# User: '{user_input}'")
            printed_tool_calls = set()
            async for chunk in agent.run(user_input, stream=True):
                # log tool calls if any
                function_calls = [
                    c for c in chunk.contents
                    if c.type == "function_call"
                ]
                for call in function_calls:
                    if call.call_id not in printed_tool_calls:
                        print(f"Tool calls: {call.name}")
                        printed_tool_calls.add(call.call_id)
                if chunk.text:
                    print(chunk.text, end="", flush=True)
            print("")

        print("\n--- All tasks completed successfully ---")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Program finished.")
