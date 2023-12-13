from gpt_module.gpt import generate_function
import json

def action(act):
    actions = {"stand-up", "move", "stop", "power-on", "power-off"}
    if act in actions:
        result = "spot will do the action " + act
    else:
        result = "error, action is not defined"
    return result

def execute_function_call(message):
    if message["tool_calls"][0]["function"]["name"] == "action":
        act = json.loads(message["tool_calls"][0]["function"]["arguments"])["action"]
        results = action(act)
    else:
        results = f"Error: function {message['tool_calls'][0]['function']['name']} does not exist"
    return results

user_input = "Hi, please change spot's position to upright"

chat_response = generate_function(user_input)
assistant_message = json.loads(chat_response.model_dump_json())["choices"][0]["message"]
assistant_message['content'] = str(assistant_message["tool_calls"][0]["function"])

if assistant_message.get("tool_calls"):
    results = execute_function_call(assistant_message)
    print(results)
