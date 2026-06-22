from apps.artifacts import repository

from apps.artifacts.schemas import (
    ArtifactCreateDTO,
    ArtifactCreateIn,
)


def create_artifact(
    *,
    user_id: int,
    artifact_data: ArtifactCreateIn,
):
    create_dto = ArtifactCreateDTO(
        user_id=user_id,
        file_name=artifact_data.file_name,
        file_type=artifact_data.file_type,
        storage_path=artifact_data.storage_path,
    )

    return repository.create_artifact(
        create_dto=create_dto,
    )


def get_artifact_by_uuid(
    *,
    artifact_uuid,
):
    artifact = repository.get_artifact_by_uuid_optional(
        artifact_uuid=artifact_uuid,
    )

    if not artifact:
        raise ValueError(
            "Artifact not found",
        )

    return artifact


def get_artifacts(
    *,
    user_id: int,
):
    return repository.get_artifacts(
        user_id=user_id,
    )