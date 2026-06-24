from uuid import UUID
from datetime import date

from apps.financial_events.schemas import (
    FinancialEventCreateDTO,
    FinancialEventCreateIn,
    FinancialSummaryOut,
    PeriodOut,
)

from apps.financial_events import repository

from shared.contracts.parsed_transaction import (
    ParsedTransaction,
)

def create_financial_event(
    *,
    user_id: int,
    event_data: FinancialEventCreateIn,
):
    create_dto = FinancialEventCreateDTO(
        user_id=user_id,
        merchant=event_data.merchant,
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


def create_from_parsed_transaction(
    *,
    user_id: int,
    parsed_transaction: ParsedTransaction,
):
    create_dto = FinancialEventCreateDTO(
        user_id=user_id,
        merchant=parsed_transaction.merchant,
        amount=parsed_transaction.amount,
        currency=parsed_transaction.currency,
        event_type=parsed_transaction.event_type,
        description=parsed_transaction.description,
        transaction_date=parsed_transaction.transaction_date,
    )

    return repository.create_financial_event(
        create_dto=create_dto,
    )

