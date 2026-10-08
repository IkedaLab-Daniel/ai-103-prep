import os
import json
from dotenv import load_dotenv

# Add references
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import PromptAgentDefinition, FunctionTool
from openai.types.responses.response_input_param import FunctionCallOutput, ResponseInputParam

def main(): 
    # Clear the console
    os.system('cls' if os.name=='nt' else 'clear')

    # Load environment variables from .env file
    load_dotenv()
    project_endpoint = os.getenv("PROJECT_ENDPOINT")
    model_deployment = os.getenv("MODEL_DEPLOYMENT_NAME")

    # Connect to the project client
    with (
        DefaultAzureCredential() as credential,
        AIProjectClient(endpoint=project_endpoint, credential=credential) as project_client,
        project_client.get_openai_client() as openai_client,
    ):
        # Define the event function tool
        

        # Define the observation cost function tool
        

        # Define the observation report generation function tool
        

        # Create a new agent with the function tools
        
        
        # Create a thread for the chat session
        

        while True:
            user_input = input("Enter a prompt for the astronomy agent. Use 'quit' to exit.\nUSER: ").strip()
            if user_input.lower() == "quit":
                print("Exiting chat.")
                break

            # Create a list to hold function call outputs that will be sent back as input to the agent
            event_tool = FunctionTool(
                name="next_visible_event",
                description="Get the next visible event in a given location",
                parameters={
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "continent to find the next visible event in (e.g. 'north_america', 'south_america', 'australia')",
                        },
                    },
                    "required": ["location"],
                    "additionalProperties": False,
                },
                strict=True,
            )

            # Send a prompt to the agent
           
        
            # Retrieve the agent's response, which may include function calls


            # Process function calls
            

            # Send function call outputs back to the model and retrieve a response
            

        # Delete the agent when done
        

if __name__ == '__main__': 
    main()