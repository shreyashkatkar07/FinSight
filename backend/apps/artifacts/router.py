from uuid import UUID

from ninja import Router

from apps.artifacts import service

from apps.artifacts.schemas import (
    ArtifactCreateIn,
    ArtifactOut,
    ArtifactProcessResponse,
)

router = Router()

@router.post(
    "/",
    response=ArtifactOut,
)
def create_artifact(
    request,
    payload: ArtifactCreateIn,
):
    return service.create_artifact(
        user_id=1,
        artifact_data=payload,
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
    "/{artifact_uuid}/process",
    response=ArtifactProcessResponse,
)
def process_artifact(
    request,
    artifact_uuid: UUID,
):
    return service.process_artifact(
        artifact_uuid=artifact_uuid,
    )