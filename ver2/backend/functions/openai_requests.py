import openai
from decouple import config


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
