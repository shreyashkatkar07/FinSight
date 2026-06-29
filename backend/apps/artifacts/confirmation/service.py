from uuid import UUID

from django.db import transaction

from apps.artifacts.models import ArtifactStatus
from apps.artifacts.repository import (
    get_artifact_by_uuid_optional,
)

from apps.financial_events.repository import (
    create_financial_events,
)

from .mapper import (
    to_financial_event_create_dto,
)

from .schemas import (
    ConfirmExtractionRequest,
    ConfirmExtractionResponse,
)


def confirm_extraction(
    *,
    artifact_uuid: UUID,
    payload: ConfirmExtractionRequest,
) -> ConfirmExtractionResponse:

    artifact = get_artifact_by_uuid_optional(
        artifact_uuid=artifact_uuid,
    )

    if not artifact:
        raise ValueError(
            "Artifact not found",
        )

    if artifact.status != ArtifactStatus.REVIEW_PENDING:
        raise ValueError(
            "Artifact is not awaiting review",
        )

    create_dtos = [
        to_financial_event_create_dto(
            artifact=artifact,
            transaction=transaction,
        )
        for transaction in payload.transactions
    ]

    with transaction.atomic():

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

    return ConfirmExtractionResponse(
        artifact_uuid=artifact.uuid,
        status=ArtifactStatus.COMPLETED,
        events_created=len(create_dtos),
    )