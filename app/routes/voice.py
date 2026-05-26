from fastapi import APIRouter
from schemas.reasoning_schema import ReasoningInput

from app.routes.reasoning import store

router = APIRouter()

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