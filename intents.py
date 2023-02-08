import json
	
# Data to be written
intents ={"intents": []}


# Serializing json
json_object = json.dumps(intents, indent = 4)
print(json_object)


        # {
        #     "group": "greetings",
        #     "patterns": ["Hi", "Hello", "Is anyone there", "Good day", "greetings", "."],
        #     "responses": ["Hello!", "Hi there, how can I help you?"],
        #     "context_set": ""
        # }