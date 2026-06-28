from uuid import UUID

from django.db import transaction

from apps.artifacts.transaction_extraction.pipeline import (
    transaction_extraction_pipeline,
)
from apps.artifacts.models import ArtifactStatus
from apps.artifacts.repository import (
    get_artifact_by_uuid_optional,
)
from apps.financial_events.repository import (
    create_financial_events,
)


def process_artifact(
    *,
    artifact_uuid: UUID,
) -> int:
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

    if artifact.status == ArtifactStatus.COMPLETED:
        raise ValueError(
            "Artifact has already been completed",
        )

    try:
        with transaction.atomic():

            artifact.status = ArtifactStatus.PROCESSING
            artifact.error_message = None

            artifact.save(
                update_fields=[
                    "status",
                    "error_message",
                ],
            )

            create_dtos = (
                transaction_extraction_pipeline.extract(
                artifact=artifact,
            )
)

            create_financial_events(
                create_dtos=create_dtos,
            )

            artifact.status = ArtifactStatus.COMPLETED
            artifact.error_message = None

            artifact.save(
                update_fields=[
                    "status",
                    "error_message",
                ],
            )

        return len(create_dtos)

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