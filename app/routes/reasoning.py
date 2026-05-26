from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from agents.context_agent import extract_reasoning
from agents.explanation_agent import explain
from memory.embeddings import create_embedding
from memory.qdrant_client import COLLECTION, client
from schemas.reasoning_schema import ReasoningInput
from services.context_optimizer import optimize_context
from services.guardrails import validate_query
from services.memory_ranker import engineering_priority
from services.token_budget import limit_context

router = APIRouter()


@router.post("/store-reasoning")
async def store(data: ReasoningInput):
    embedding = create_embedding(data.text)

    # Check for duplicates
    existing = client.query_points(
        collection_name=COLLECTION, 
        query=embedding, 
        limit=10, 
        with_payload=True
    )

    for point in existing.points:
        payload = point.payload or {}
        stored = payload.get("raw", "")
        if stored.lower() == data.text.lower():
            return {"message": "Already Stored"}

    # Process and record new entry
    parsed = extract_reasoning(data.text)
    
    client.upsert(
        collection_name=COLLECTION,
        points=[{
            "id": str(uuid4()),
            "vector": embedding,
            "payload": {
                "subject": data.subject,
                "raw": data.text,
                "parsed": parsed,
                "timestamp": datetime.utcnow().isoformat(),
            },
        }],
    )

    return {"message": "Stored"}


@router.post("/answer")
async def answer(body: dict):
    query = body.get("query")
    if not query:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Query missing"
        )

    # Safety Guardrails
    safe, msg = validate_query(query)
    if not safe:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail=msg
        )

    # Vector Retrieval
    embedding = create_embedding(query)
    result = client.query_points(
        collection_name=COLLECTION, 
        query=embedding, 
        limit=5, 
        with_payload=True
    )

    # Context Pipeline Processing
    memories = [point.payload for point in result.points if point.payload]
    memories = engineering_priority(memories, query)
    memories = optimize_context(memories)
    memories = limit_context(memories)

    # Generate Response
    response = explain(query, memories)
    confidence = min(90 + len(memories) * 2, 99)

    sources = []
    for memory in memories:
        parsed = memory.get("parsed", {})
        concept = parsed.get("concept")
        reason = parsed.get("reason")

        if concept:
            sources.append(f"{concept} → {reason}")

    return {
        "response": response,
        "confidence": confidence,
        "sources": sources[:3],  
    }