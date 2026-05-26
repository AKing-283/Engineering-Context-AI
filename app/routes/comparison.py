from fastapi import APIRouter

from agents.comparison_agent import compare

router = APIRouter()


@router.post("/compare")
async def compare_api(body: dict):
    # Safe lookup with fallback keys if "a" or "b" are missing in the payload
    concept_a = body.get("a", "")
    concept_b = body.get("b", "")

    return {"comparison": compare(concept_a, concept_b)}