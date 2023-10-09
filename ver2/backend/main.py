# run:      uvicorn main:app 
# run-dev:  uvicorn main:app --reload 

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custon Function Imports
from functions.openai_requests import convert_audio_to_text, get_chat_response
from functions.database import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

# Initiate App
app = FastAPI()

# CORS - Origins
#   - dictate what domain urls to accept to the backend 
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000"
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# API Endpoints ==============================
@app.get("/health")
async def check_health():
    print("backend is healthy!")
    return {"message": "healthy"}

@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": "conversation reset"}

# use @get for testing, use @post later
@app.get("/post-audio-get")
async def get_audio():

    # Get saved audio
    audio_input = open("test-bmo1.mp3", "rb")
    print(audio_input)

    # Decode Audio + Guard
    message_decoded = convert_audio_to_text(audio_input)
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get ChatGPT Response + Guard
    chat_response = get_chat_response(message_decoded)
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get OpenAI chat response")

    # Store Messages
    store_messages(message_decoded, chat_response)

    # print(chat_response)

    # Convert chat response to audio + Guard
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get Eleven labs audio response")

    # Create a generator that yields chunks of data
    def iterfile():
        yield audio_output

    # Return audio file
    return StreamingResponse(iterfile(), media_type="audio/mpeg")

# # Post bot response
# # Note: Not playing in browser when using post request --> Play in React Application
# @app.post("/post-audio")
# async def post_audio(file: UploadFile = File(...)):

#     # write logic in get function

#     print("Test")