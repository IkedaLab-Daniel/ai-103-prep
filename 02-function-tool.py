import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


# function that gets current time
def get_time():
    return f"The time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}"


def main():
    client = OpenAI()

    function_tools = [
        {
            "type": "function",
            "name": "get_time",
            "description": "Get the current time"
        }
    ]

    # Init message with system prompt
    messages = [
        {"role": "developer", "content": "You are an AI assistant that provides information."},
    ]

    # loop until quit
    while True:
        prompt = input("\nEnter a prompt (or type 'quit' to exit)\n")
        if prompt.lower() == "quit":
            break

        # Append the user prompt to the messages
        messages.append({"role": "user", "content": prompt})

        # Get initial response
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=messages,
            tools=function_tools
        )

        # append message
        messages += response.output

        # ? Was there aa functionc all?
        for item in response.output:
            if item.type == "function_call" and item.name == "get_time":
                current_time = get_time()
                messages.append({
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": current_time
                })

                # get a follow up response
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    instructions="Answer only with the tool output.",
                    input=messages,
                    tools=function_tools
                )

        print(response.output_text)

# Run the main function when the script starts
if __name__ == '__main__':
    main()