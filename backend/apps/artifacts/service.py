from pathlib import Path

from apps.artifacts.models import FileType

from ninja.files import UploadedFile

from shared.storage.service import storage_service

from apps.artifacts import repository

from apps.artifacts.schemas import (
    ArtifactCreateDTO,
    ArtifactCreateIn,
    ArtifactUploadOut,
)

from apps.artifacts.extraction_service import (
    extract_artifact as extract_artifact_workflow,
)

from apps.artifacts.confirmation.service import (
    confirm_extraction as confirm_extraction_workflow,
)

from apps.artifacts.transaction_extraction.schemas import (
    ExtractionResponse,
)

from apps.artifacts.confirmation.schemas import (
    ConfirmExtractionRequest,
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


def process_artifact(
    *,
    artifact_uuid,
) -> ExtractionResponse:
    return extract_artifact_workflow(
        artifact_uuid=artifact_uuid,
    )


def _get_file_type(
    *,
    file: UploadedFile,
) -> FileType:
    extension = (
        Path(file.name)
        .suffix
        .lower()
    )

    mapping = {
        ".png": FileType.IMAGE,
        ".jpg": FileType.IMAGE,
        ".jpeg": FileType.IMAGE,
        ".pdf": FileType.PDF,
        ".csv": FileType.CSV,
        ".xlsx": FileType.XLSX,
    }

    try:
        return mapping[extension]
    except KeyError:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )


def upload_artifact(
    *,
    user_id: int,
    file: UploadedFile,
):
    storage_path = (
        storage_service.save_file(
            file=file,
        )
    )

    create_dto = ArtifactCreateDTO(
        user_id=user_id,
        file_name=file.name,
        file_type=_get_file_type(
            file=file,
        ),
        storage_path=storage_path,
    )

    artifact = repository.create_artifact(
        create_dto=create_dto,
    )

    return ArtifactUploadOut(
        artifact_uuid=artifact.uuid,
        file_name=artifact.file_name,
        file_type=artifact.file_type,
        status=artifact.status,
    )


def confirm_extraction(
    *,
    artifact_uuid,
    payload: ConfirmExtractionRequest,
):
    return confirm_extraction_workflow(
        artifact_uuid=artifact_uuid,
        payload=payload,
    )