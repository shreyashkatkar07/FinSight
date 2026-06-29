from uuid import UUID

from ninja import Router, File
from ninja.files import UploadedFile

from apps.artifacts import service

from apps.artifacts.schemas import (
    ArtifactOut,
    ArtifactUploadOut,
)

from apps.artifacts.transaction_extraction.schemas import (
    ExtractionResponse,
)

from apps.artifacts.confirmation.schemas import (
    ConfirmExtractionRequest,
    ConfirmExtractionResponse,
)

router = Router()


@router.post(
    "/upload",
    response=ArtifactUploadOut,
)
def upload_artifact(
    request,
    file: UploadedFile = File(...),
):
    return service.upload_artifact(
        user_id=1,
        file=file,
    )


@router.get(
    "/{artifact_uuid}",
    response=ArtifactOut,
)
def get_artifact(
    request,
    artifact_uuid: UUID,
):
    return service.get_artifact_by_uuid(
        artifact_uuid=artifact_uuid,
    )


@router.get(
    "/",
    response=list[ArtifactOut],
)
def get_artifacts(
    request,
):
    return service.get_artifacts(
        user_id=1,
    )


@router.post(
    "/{artifact_uuid}/extract",
    response=ExtractionResponse,
)
def process_artifact(
    request,
    artifact_uuid: UUID,
):
    return service.process_artifact(
        artifact_uuid=artifact_uuid,
    )


@router.post(
    "/{artifact_uuid}/confirm",
    response=ConfirmExtractionResponse,
)
def confirm_extraction(
    request,
    artifact_uuid: UUID,
    payload: ConfirmExtractionRequest,
):
    return service.confirm_extraction(
        artifact_uuid=artifact_uuid,
        payload=payload,
    )