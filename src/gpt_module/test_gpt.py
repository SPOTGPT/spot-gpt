from openai import OpenAI
from dotenv import load_dotenv
import os

'''
Test gpt prompt here
check the api reference for examples here: https://platform.openai.com/docs/api-reference/chat/object?lang=python
'''

load_dotenv()
client = OpenAI()

tools = [
  {
    "type": "function",
    "function": {
      "name": "action",
      "description": "Command a robot do to a given action",  # describe when gpt should try to generate a function
      "parameters": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "description": "The command that the robot is going to act. Example: stand-up, stop, etc.", # describe the parameter
            "enum": ["stand-up", "move", "stop", "power-on", "power-off"] # the type of arguments gpt can 'call'
          },
        },
        "required": ["action"],
      },
    }
  }
]
messages = [{"role": "user", "content": "Can you please turn on the robot and then turn it off?"}]  # user input
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=messages,
  tools=tools,
  tool_choice="auto",
  max_tokens=25
)

# set the output location
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'src', 'gpt_module', 'test_output.json')

with open(file_path, "w") as outfile: ## write the response to test_output.json
    outfile.write("completion.model_dump_json()")