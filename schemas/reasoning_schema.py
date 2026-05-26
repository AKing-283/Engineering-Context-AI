from pydantic import BaseModel


class ReasoningInput(BaseModel):
    """Pydantic schema to validate incoming request data for reasoning operations."""
    subject: str
    text: str