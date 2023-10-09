import openai
from decouple import config

from functions.database import get_recent_messages

# Call API Keys
openai.api_key = config("OPEN_AI_KEY")
openai.organization = config("OPEN_AI_ORG")
elevenlabs_key = config("ELEVENLABS_KEY")

# Open AI - Whispter
# Convert Audio to Text 
def convert_audio_to_text(audio_file):
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file) 
        message_text = transcript["text"]
        return message_text
    except Exception as e:
        print(e)

# Open AI - ChatGPT
# Get response to our message
def get_chat_response(message_input):

    messages = get_recent_messages()
    user_message = {"role": "user", "content": message_input}
    messages.append(user_message)

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        message_text = response["choices"][0]['message']['content']
        return message_text
    except Exception as e:
        print(e)