import os
from dotenv import load_dotenv

# import namespaces
from openai import OpenAI

def main(): 
    # Clear the console
    # os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get configuration settings 
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Initialize the OpenAI client
        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=azure_openai_api_key,
        )

        last_response_id = None

        # Loop until the user wants to quit
        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            # ! Get a response - chat completions
            # completion = openai_client.chat.completions.create(
            #     model=model_deployment,
            #     messages=[
            #         {
            #             "role": "system",
            #             "content": "You are a helpful AI assistant that answers questions and provides information."
            #         },
            #         {
            #             "role": "user",
            #             "content": input_text
            #         }
            #     ]
            # )
            # print(completion.choices[0].message.content)

            # ? Response()
            response = openai_client.responses.create(
                model=model_deployment,
                instructions="You're a friendly chatmate",
                input=input_text,
                previous_response_id=last_response_id
            )

            print(response.output_text)
            last_response_id = response.id

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
