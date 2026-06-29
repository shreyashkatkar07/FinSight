from uuid import UUID

from pydantic import BaseModel

from apps.artifacts.transaction_extraction.schemas import (
    ExtractedTransaction,
)


class ConfirmExtractionRequest(BaseModel):
    transactions: list[ExtractedTransaction]


class ConfirmExtractionResponse(BaseModel):
    artifact_uuid: UUID
    status: str
    events_created: int