# MAIN FUNCTIONS OF THIS PORJECT
# 1. Send audio, have it transcribed 
# 2. Send transcribed audio to chatGPT and get a response
# 3. Save chat histroy to send back and forth (ChatGPT has no history)

from fastapi import FastAPI, UploadFile
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv

import os
import openai
import json
import requests

load_dotenv() 

openai.api_key = os.getenv("OPEN_AI_KEY")
openai.organization = os.getenv("OPEN_AI_ORG")
elevenlabs_key = os.getenv("ELEVENLABS_KEY")
app = FastAPI()

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

@app.get("/")
async def root():
    print("we out here")
    return {"message": "Hello World"}

# Note: use Postman and send a Post request to `http://localhost:8000/talk` to run post_audio()
@app.post("/talk")
async def post_audio(file: UploadFile):
    user_message = transcribe_audio(file)               # OpenAI
    chat_response = get_chat_response(user_message)     # OpenAI
    audio_output = text_to_speech(chat_response)        # 11ElevenLabs

    def iterfile():
            yield audio_output

    return StreamingResponse(iterfile(), media_type="audio/mpeg")


# Fuctions

# 1. Send audio, have it transcribed 
def transcribe_audio(file):
    audio_file= open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)   # add try-except
    # transcript = {'text': 'Hi brooke, how are you today?'}
    # print(transcript)
    return transcript

def get_chat_response(user_message):
    # load messages 
    messages = load_messages()

    # add new message to loaded messages
    messages.append({"role": "user", "content": user_message['text']})

    # Send to OpenAI/ChatGPT
    gpt_response = openai.ChatCompletion.create(    # add try-except
        model="gpt-3.5-turbo",
        messages=messages
    )

    parsed_gpt_response = gpt_response['choices'][0]['message']['content']

    save_messages(user_message['text'], parsed_gpt_response)    

    return parsed_gpt_response


def load_messages():
    messages = []
    file = 'database.json'

    empty = os.stat(file).st_size == 0

    # If file not empty, loop through history and add to message
    if not empty:
        with open(file) as db_file:
            data = json.load(db_file)
            for item in data:
                messages.append(item)

    # If file is empty, add the context (system role)
    else: 
        messages.append(
            {"role": "system", "content": prompt}
        )

    return messages

def save_messages(user_message, gpt_response):
    file = 'database.json'
    messages = load_messages()
    messages.append({"role": "user", "content": user_message})
    messages.append({"role": "assistant", "content": gpt_response})

    with open(file, 'w') as f:
        json.dump(messages, f)

def text_to_speech(text):

    voice_id = "MF3mGyEYCl7XYWbV9V6O" # Elli's voice ID https://api.elevenlabs.io/v1/voices

    body = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
            "style": 0,
            "use_speaker_boost": True
        }
    }
    
    headers = {
        "Content-Type": "application/json",
        "accept": "audio/mpeg",
        "xi-api-key": elevenlabs_key
    }

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    try:
        response = requests.post(url, json=body, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            print("Something went wrong")
    except Exception as e:
        print(e)

