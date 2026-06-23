from uuid import UUID

from django.db import transaction

from apps.artifacts.models import ArtifactStatus
from apps.artifacts.parsers.registry import get_parser
from apps.artifacts.repository import (
    get_artifact_by_uuid_optional,
)
from apps.financial_events.repository import (
    create_financial_events,
)
from apps.financial_events.schemas import (
    FinancialEventCreateDTO,
)


def process_artifact(
    *,
    artifact_uuid: UUID,
) -> int:
    artifact = get_artifact_by_uuid_optional(
        artifact_uuid=artifact_uuid,
    )

    if not artifact:
        raise ValueError("Artifact not found")

    if artifact.status == ArtifactStatus.PROCESSING:
        raise ValueError("Artifact is already processing")

    if artifact.status == ArtifactStatus.PROCESSED:
        raise ValueError("Artifact has already been processed")

    try:
        with transaction.atomic():
            artifact.status = ArtifactStatus.PROCESSING
            artifact.error_message = None
            artifact.save(
                update_fields=[
                    "status",
                    "error_message",
                ]
            )

            parser = get_parser(
                file_type=artifact.file_type,
            )

            parsed_transactions = parser.parse(
                artifact=artifact,
            )

            create_dtos = [
                FinancialEventCreateDTO(
                    user_id=artifact.user_id,
                    artifact_id=artifact.id,
                    amount=parsed_transaction.amount,
                    currency=parsed_transaction.currency,
                    event_type=parsed_transaction.event_type,
                    description=parsed_transaction.description,
                    transaction_date=parsed_transaction.transaction_date,
                )
                for parsed_transaction in parsed_transactions
            ]

            create_financial_events(
                create_dtos=create_dtos,
            )

            artifact.status = ArtifactStatus.PROCESSED
            artifact.error_message = None
            artifact.save(
                update_fields=[
                    "status",
                    "error_message",
                ]
            )

        return len(create_dtos)

    except Exception as error:
        artifact.status = ArtifactStatus.FAILED
        artifact.error_message = str(error)
        artifact.save(
            update_fields=[
                "status",
                "error_message",
            ]
        )

        raise