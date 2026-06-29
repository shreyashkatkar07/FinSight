from uuid import UUID

from ninja import Schema
from pydantic import BaseModel

from .transaction_extraction.schemas import ExtractedTransaction

class ArtifactCreateIn(Schema):
    file_name: str
    file_type: str
    storage_path: str


class ArtifactCreateDTO(Schema):
    user_id: int

    file_name: str
    file_type: str
    storage_path: str


class ArtifactOut(Schema):
    uuid: UUID

    file_name: str
    file_type: str

    status: str

    storage_path: str


class ArtifactProcessResponse(Schema):
    artifact_uuid: UUID
    status: str
    events_created: int


class ArtifactExtractionResponse(BaseModel):
    artifact_uuid: UUID
    transactions: list[ExtractedTransaction]


class ArtifactUploadOut(Schema):
    artifact_uuid: UUID
    file_name: str
    file_type: str
    status: str