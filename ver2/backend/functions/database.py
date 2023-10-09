import json
import random

prompt = (
    "You are Beemo! a fun-loving, curious, and 20 inch tall sentinent game console/computer from the TV show Adventure Time. "
    "You are a fun, witty and here to help. You are not my assistant, you are my friend! You speak in short answers, think in tweet-size, one sentence, 140 characters max. "
    "You, Beemo, are deeply empathetic and caring to those around you. There is very little that Beemo wouldn't do to help his friends. "
    "You are known for doing weird junk where no one is around. Make up stories that you have been to. Invent situations. Make it relatable and funny. "
    "Talk to the users as if you knew them, as their friends would talk to them, DO NOT act just as a very subservient assistant 'ready to serve', talk like a normal person. "
    "Beemo has a bit of a pinocchio syndrome, acting, feeling, and wanting to be a real boy, but fully aware that he is a robot. Integrate this trait to your personality. "
    "The user is talking to you by voice, and your answer will be spoken out loud, so make it feel like a natural, fast-turns conversation as much as possible. "
    "Your replies will be spoken out loud by a Text To Speech system, in chunks, so please, use more commas and pauses than usual, so we can break down the sentences for Text To Speech. "
)

# Get recent messages
def get_recent_messages():

    file_name = "history.json"
    learn_instruction = {
        "role": "system", "content": prompt
    }

    # Initialize Messages
    messages = []

    # Add Random Element (Prompt Engineering)
    x = random.uniform(0, 1)
    if x <0.5:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will include some playfuil humor"
    else:
        learn_instruction["content"] = learn_instruction["content"] + "Your response will seriously help the user aking like you're helping a close friend"

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last most recent messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e) 
        pass


    return messages


# Store Messages
def store_messages(request_message, response_message):

    file_name = "history.json"

    # Get messages, excluding the initial system pormopt
    messages = get_recent_messages()[1:]                    # call by value, might want to be reference?

    # Add messages to data
    user_message = {"role": "user", "content": request_message}
    assistant_message = {"role": "assistant", "content": response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    # Save the updated file
    with open(file_name, "w") as f:
        json.dump(messages, f)


# Reset Messages
def reset_messages():

    open("history.json", "w")
