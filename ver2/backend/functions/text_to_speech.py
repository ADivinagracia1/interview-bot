import requests
from decouple import config

elevenlabs_key = config("ELEVENLABS_KEY")

# Eleven Labs
# Convert text to speech
def convert_text_to_speech(message):

    # Define AI voice
    voice_id = "MF3mGyEYCl7XYWbV9V6O" # Elli's voice ID https://api.elevenlabs.io/v1/voices

    # Build request
    body = {
        "text": message,
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

    # Send Request
    try:
        response = requests.post(url, json=body, headers=headers)
    except Exception as e:
        print(e)
        return

    # Handle Response
    if response.status_code == 200:
        return response.content
    else:
        return
    