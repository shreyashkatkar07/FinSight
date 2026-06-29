from uuid import UUID

from apps.artifacts.models import ArtifactStatus
from apps.artifacts.repository import (
    get_artifact_by_uuid_optional,
)
from apps.artifacts.transaction_extraction.pipeline import (
    transaction_extraction_pipeline,
)
from apps.artifacts.transaction_extraction.schemas import (
    ExtractionResponse,
)


def extract_artifact(
    *,
    artifact_uuid: UUID,
) -> ExtractionResponse:
    artifact = get_artifact_by_uuid_optional(
        artifact_uuid=artifact_uuid,
    )

    if not artifact:
        raise ValueError(
            "Artifact not found",
        )

    if artifact.status == ArtifactStatus.PROCESSING:
        raise ValueError(
            "Artifact is already processing",
        )

    if artifact.status == ArtifactStatus.REVIEW_PENDING:
        raise ValueError(
            "Artifact is awaiting review",
        )

    if artifact.status == ArtifactStatus.COMPLETED:
        raise ValueError(
            "Artifact has already been completed",
        )

    artifact.status = ArtifactStatus.PROCESSING
    artifact.error_message = None

    artifact.save(
        update_fields=[
            "status",
            "error_message",
        ],
    )

    try:
        extraction = (
            transaction_extraction_pipeline.extract(
                artifact=artifact,
            )
        )

        artifact.status = ArtifactStatus.REVIEW_PENDING

        artifact.save(
            update_fields=[
                "status",
            ],
        )

        return extraction

    except Exception as error:

        artifact.status = ArtifactStatus.FAILED
        artifact.error_message = str(error)

        artifact.save(
            update_fields=[
                "status",
                "error_message",
            ],
        )

        raise