# run:      uvicorn main:app 
# run-dev:  uvicorn main:app --reload 

# Main Imports
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai

# Custon Function Imports
from functions.openai_requests import convert_audio_to_text

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


# use @get for testing, use @post later
@app.get("/post-audio-get")
async def get_audio():

    # Get saved audio
    audio_input = open("test-bmo1.mp3", "rb")
    print(audio_input)

    # Decode Audio
    message_decoded = convert_audio_to_text(audio_input)

    print(message_decoded)
    return {"message": message_decoded}

# # Post bot response
# # Note: Not playing in browser when using post request --> Play in React Application
# @app.post("/post-audio")
# async def post_audio(file: UploadFile = File(...)):

#     # write logic in get function

#     print("Test")