from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

'''AI tuning'''
function_description = "Command a robot do to a given action"
function_name = "action"
# parameters
param_description = "The command that the robot is going to act. Example: stand-up, stop, etc."
actions = ["stand-up", "move", "stop", "power-on", "power-off"]

# set the output location
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'src', 'gpt_module', 'output.json')

tools = [
  {
    "type": "function",
    "function": {
      "name": function_name,
      "description": function_description,
      "parameters": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "description": param_description,
            "enum": actions
          },
        },
        "required": ["action"],
      },
    }
  }
]

def generate_function(input):
  '''
  Call gpt using the current settings
  if input prompt is valid:
    gpt will create a response of the current function_name with arguments parameter based of actions
    completion.choices[0] need to be == tool_calls to generate this valid response
  '''
  messages = [{"role": "user", "content": input}]
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    tools=tools,
    tool_choice="auto",
    max_tokens=25
  )

  with open(file_path, "w") as outfile: ## Write the response to output.json
      outfile.write(completion.model_dump_json())
  
  return completion