import time

from fastapi import APIRouter
from pydantic import BaseModel

from memory.embeddings import create_embedding
from memory.qdrant_client import COLLECTION, client
from services.memory_ranker import engineering_priority

router = APIRouter()

SIMILARITY_THRESHOLD = 0.45


class Query(BaseModel):
    query: str


def normalize(concept: str) -> str:
    if not concept:
        return ""

    concept = concept.lower().strip()

    fixes = {
        "djikstra": "dijkstra",
        "djikstra's algorithm": "dijkstra",
        "dijkstra's algorithm": "dijkstra",
        "bellman ford": "bellman-ford",
        "bellman ford algorithm": "bellman-ford",
    }

    return fixes.get(concept, concept)


@router.post("/retrieve")
async def retrieve(body: Query):
    start = time.time()

    embedding = create_embedding(body.query)

    result = client.query_points(
        collection_name=COLLECTION,
        query=embedding,
        limit=15,
        with_payload=True,
        with_vectors=False,
    )

    memory = []
    seen = set()

    for point in result.points:
        score = point.score

        if score < SIMILARITY_THRESHOLD:
            continue

        payload = point.payload or {}
        parsed = payload.get("parsed", {})
        raw_concept = parsed.get("concept")

        normalized = normalize(raw_concept)

        if not normalized or normalized in seen:
            continue

        seen.add(normalized)

        memory.append({
            "subject": payload.get("subject"),
            "concept": raw_concept,
            "reason": parsed.get("reason"),
            "timestamp": payload.get("timestamp"),
            "score": round(score, 3),
        })

    # Engineering-aware rerank
    memory = engineering_priority(memory, body.query)

    # Final semantic score sort
    memory.sort(
        key=lambda x: (
            x["score"],
            "negative" in str(x).lower(),
            "positive" in str(x).lower(),
        ),
        reverse=True,
    )

    latency = round(time.time() - start, 3)

    return {
        "memory": memory,
        "memory_count": len(memory),
        "latency": f"{latency}s",
    }