from uuid import UUID

from apps.financial_events.schemas import (
    FinancialEventCreateDTO,
    FinancialEventCreateIn,
)

from apps.financial_events import repository


def create_financial_event(
    *,
    user_id: int,
    event_data: FinancialEventCreateIn,
):
    create_dto = FinancialEventCreateDTO(
        user_id=user_id,
        amount=event_data.amount,
        currency=event_data.currency,
        event_type=event_data.event_type,
        description=event_data.description,
        transaction_date=event_data.transaction_date,
    )

    return repository.create_financial_event(
        create_dto=create_dto,
    )


def get_financial_event_by_uuid(
    *,
    event_uuid: UUID,
):
    financial_event = (
        repository.get_financial_event_by_uuid_optional(
            event_uuid=event_uuid,
        )
    )

    if not financial_event:
        raise ValueError(
            "Financial event not found"
        )

    return financial_event


def get_financial_events(
    *,
    user_id: int,
):
    return repository.get_financial_events(
        user_id=user_id,
    )