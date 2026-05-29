import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Initialize Groq Whisper client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Transcribe audio using Groq Whisper Medium API.
    Supports WEBM and WAV (Streamlit mic input compatible).
    Does not require ffmpeg or local Whisper.
    """

    # Send audio bytes directly to Groq
    response = client.audio.transcriptions.create(
        file=("audio.webm", audio_bytes, "audio/webm"),
        model="whisper-large-v3",
        response_format="json"
    )

    # Temporary debug logs
    print("DEBUG_RESPONSE:", response)
    print("DEBUG_DIR:", dir(response))

    # Extract transcript
    transcript = response.text.strip()
    return transcript