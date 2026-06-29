from apps.financial_events.schemas import (
    FinancialEventCreateDTO,
)


def to_financial_event_create_dto(
    *,
    artifact,
    transaction,
) -> FinancialEventCreateDTO:

    return FinancialEventCreateDTO(
        user_id=artifact.user_id,
        artifact_id=artifact.id,
        merchant=transaction.merchant,
        amount=transaction.amount,
        currency=transaction.currency.value,
        event_type=transaction.event_type.value,
        category=transaction.category.value,
        description=transaction.description,
        transaction_date=transaction.transaction_date,
    )