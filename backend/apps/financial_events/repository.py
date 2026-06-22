from uuid import UUID

from apps.financial_events.models import FinancialEvent
from apps.financial_events.schemas import FinancialEventCreateDTO


def create_financial_event(
    *,
    create_dto: FinancialEventCreateDTO,
) -> FinancialEvent:
    return FinancialEvent.objects.create(
        user_id=create_dto.user_id,
        amount=create_dto.amount,
        currency=create_dto.currency,
        event_type=create_dto.event_type,
        description=create_dto.description,
        transaction_date=create_dto.transaction_date,
    )


def get_financial_event_by_uuid_optional(
    *,
    event_uuid,
):
    return FinancialEvent.objects.filter(
        uuid=event_uuid,
        is_active=True,
    ).first()


def get_financial_events(
    *,
    user_id: int,
):
    return FinancialEvent.objects.filter(
        user_id=user_id,
        is_active=True,
    )