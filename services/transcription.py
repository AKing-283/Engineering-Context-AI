import tempfile
import whisper
import os

# Load Whisper model ONCE (base = fast + accurate for hackathon)
model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes) -> str:
    """
    Transcribe audio from WEBM or WAV bytes using local Whisper.
    Works fully offline.
    """

    # Create a temporary file for Whisper
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        # Run Whisper transcription
        result = model.transcribe(tmp_path)

        # Extract text
        transcript = result.get("text", "").strip()

        return transcript

    finally:
        # Cleanup temp file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)