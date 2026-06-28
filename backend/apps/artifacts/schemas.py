from uuid import UUID

from ninja import Schema


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


class ArtifactUploadOut(Schema):
    artifact_uuid: UUID
    file_name: str
    file_type: str
    status: str