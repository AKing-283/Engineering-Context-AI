from datetime import datetime

from fastapi import APIRouter

from memory.qdrant_client import COLLECTION, client

router = APIRouter()


@router.get("/timeline")
async def timeline():
    result = client.scroll(
        collection_name=COLLECTION,
        limit=100,
        with_payload=True,
    )

    memories = []

    for point in result[0]:
        payload = point.payload or {}
        parsed = payload.get("parsed", {})
        ts = payload.get("timestamp")

        try:
            parsed_ts = datetime.fromisoformat(ts) if ts else datetime.min
        except (ValueError, TypeError):
            # Catching specific exceptions instead of a bare except clause
            parsed_ts = datetime.min

        memories.append({
            "subject": payload.get("subject"),
            "concept": parsed.get("concept"),
            "reason": parsed.get("reason"),
            "timestamp": ts,
            "_sort": parsed_ts,
        })

    # Sort memories chronologically (newest first)
    memories.sort(key=lambda x: x["_sort"], reverse=True)

    # Clean up internal sorting keys before returning the response
    for m in memories:
        del m["_sort"]

    return {"count": len(memories), "timeline": memories}