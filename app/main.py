from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.analytics import router as analytics
from app.routes.comparison import router as comparison
from app.routes.reasoning import router as reasoning
from app.routes.retrieval import router as retrieval
from app.routes.timeline import router as timeline
from app.routes.voice import router as voice
from memory.qdrant_client import initialize_qdrant
from datetime import datetime
app = FastAPI(
    title="Engineering Context AI",
    description="Persistent Engineering Memory + Voice Context AI",
    version="1.0.0",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Vector DB
initialize_qdrant()

# Register Routers
app.include_router(reasoning, tags=["Reasoning"])
app.include_router(retrieval, tags=["Retrieval"])
app.include_router(voice, tags=["Voice"])
app.include_router(analytics, tags=["Analytics"])
app.include_router(timeline, tags=["Timeline"])
app.include_router(comparison, tags=["Comparison"])


@app.get("/")
async def health():
    return {
        "message": "Engineering Context AI Running for Upcoming Engineers 24x7",
        "status": "healthy",
        "services": {
            "qdrant": "connected",
            "lyzr": "active",
        },
        "time": datetime.utcnow().isoformat(),
    }