from pydantic import BaseModel


class ExtractionResult(BaseModel):
    text: str
    confidence: float
    engine: str
    processing_time_ms: int