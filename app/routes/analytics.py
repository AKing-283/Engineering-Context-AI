from collections import Counter
from fastapi import APIRouter
from memory.qdrant_client import COLLECTION, client

router = APIRouter()


@router.get("/analytics")
async def analytics():
    result = client.scroll(
        collection_name=COLLECTION, 
        limit=100, 
        with_payload=True
    )

    points = result[0]
    subjects = []
    concepts = []

    for point in points:
        payload = point.payload or {}
        parsed = payload.get("parsed", {})

        subject = payload.get("subject")
        concept = parsed.get("concept")

        if subject:
            subjects.append(subject)
        if concept:
            concepts.append(concept)

    return {
        "total_memories": len(points),
        "subjects": dict(Counter(subjects)),
        "concepts": dict(Counter(concepts)),
    }

