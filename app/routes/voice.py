from fastapi import APIRouter
from schemas.reasoning_schema import ReasoningInput

from app.routes.reasoning import store
from services.transcription import transcribe_audio

router = APIRouter()

from fastapi import UploadFile, File
import os
from uuid import uuid4

AUDIO_DIR = "uploads/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

ENGINEERING_FIXES = {
    "bellman food": "Bellman Ford",
    "graft": "graph",
    "djikstra": "Dijkstra",
    "kirchoff": "Kirchhoff",
    "lap lash": "Laplace",
}


def clean_engineering_text(text: str) -> str:
    text = text.lower()
    for wrong, correct in ENGINEERING_FIXES.items():
        text = text.replace(wrong, correct)
    return text


@router.post("/omi-webhook")
async def omi_webhook(body: dict):
    segments = body.get("segments", [])
    if not segments:
        return {"error": "No segments"}

    transcript = " ".join([seg.get("text", "") for seg in segments])
    transcript = clean_engineering_text(transcript)

    # Subject classification based on text keywords
    subject = "General"
    lower = transcript.lower()

    if any(x in lower for x in ["graph", "dijkstra", "bellman"]):
        subject = "DSA"
    elif any(x in lower for x in ["laplace", "signal", "frequency"]):
        subject = "Signals"
    elif any(x in lower for x in ["voltage", "current", "kirchhoff"]):
        subject = "Electronics"

    payload = ReasoningInput(subject=subject, text=transcript)
    result = await store(payload)

    return {
        "message": "Stored",
        "subject": subject,
        "transcript": transcript,
        "storage": result,
    }

# ---------------------------------------------------------
# NEW: Upload raw WAV audio, save it, return metadata
# ---------------------------------------------------------
@router.post("/voice/upload")
async def upload_voice(file: UploadFile = File(...)):
    # ensure WAV
    allowed = [".wav", ".webm"]
    if not any(file.filename.lower().endswith(ext) for ext in allowed):
        return {"error": "Only WAV or WEBM files are supported"}

    audio_id = str(uuid4())
    save_path = os.path.join(AUDIO_DIR, f"{audio_id}.wav")

    # read audio bytes directly
    audio_bytes = await file.read()

    # Whisper local transcription
    transcript = transcribe_audio(audio_bytes)

    # still save WAV for audit/debug
    with open(save_path, "wb") as f:
        f.write(audio_bytes)
    subject = "Voice"

    payload = ReasoningInput(subject=subject, text=transcript)
    result = await store(payload)

    return {
        "audio_id": audio_id,
        "audio_path": save_path,
        "transcript": transcript,
        "storage": result,
    }
