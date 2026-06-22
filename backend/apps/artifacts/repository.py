from uuid import UUID

from apps.artifacts.models import Artifact
from apps.artifacts.schemas import ArtifactCreateDTO


def create_artifact(
    *,
    create_dto: ArtifactCreateDTO,
) -> Artifact:
    return Artifact.objects.create(
        user_id=create_dto.user_id,
        file_name=create_dto.file_name,
        file_type=create_dto.file_type,
        storage_path=create_dto.storage_path,
    )


def get_artifact_by_uuid_optional(
    *,
    artifact_uuid: UUID,
):
    return Artifact.objects.filter(
        uuid=artifact_uuid,
        is_active=True,
    ).first()


def get_artifacts(
    *,
    user_id: int,
):
    return Artifact.objects.filter(
        user_id=user_id,
        is_active=True,
    )