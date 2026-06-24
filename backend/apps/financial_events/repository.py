from uuid import UUID
from decimal import Decimal

from django.db.models import (
    Sum,
    Case,
    When,
    Value,
    DecimalField,
)

from apps.financial_events.models import FinancialEvent
from apps.financial_events.schemas import FinancialEventCreateDTO


def create_financial_event(
    *,
    create_dto: FinancialEventCreateDTO,
) -> FinancialEvent:
    return FinancialEvent.objects.create(
        user_id=create_dto.user_id,
        artifact_id=create_dto.artifact_id,
        merchant=create_dto.merchant,
        amount=create_dto.amount,
        currency=create_dto.currency,
        event_type=create_dto.event_type,
        description=create_dto.description,
        transaction_date=create_dto.transaction_date,
    )


def create_financial_events(
    *,
    create_dtos: list[FinancialEventCreateDTO],
):
    events = [
        FinancialEvent(
            user_id=create_dto.user_id,
            artifact_id=create_dto.artifact_id,
            merchant=create_dto.merchant,
            amount=create_dto.amount,
            currency=create_dto.currency,
            event_type=create_dto.event_type,
            description=create_dto.description,
            transaction_date=create_dto.transaction_date,
        )
        for create_dto in create_dtos
    ]

    return FinancialEvent.objects.bulk_create(
        events,
    )


def get_financial_event_by_uuid_optional(
    *,
    event_uuid: UUID,
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


def get_summary(
    *,
    user_id: int,
    start_date,
    end_date,
):
    summary = (
        FinancialEvent.objects.filter(
            user_id=user_id,
            is_active=True,
            transaction_date__gte=start_date,
            transaction_date__lte=end_date,
        )
        .aggregate(
            total_income=Sum(
                Case(
                    When(
                        event_type="CREDIT",
                        then="amount",
                    ),
                    default=Value(0),
                    output_field=DecimalField(),
                )
            ),
            total_expense=Sum(
                Case(
                    When(
                        event_type="DEBIT",
                        then="amount",
                    ),
                    default=Value(0),
                    output_field=DecimalField(),
                )
            ),
        )
    )

    return {
        "total_income": summary["total_income"]
        or Decimal("0"),
        "total_expense": summary["total_expense"]
        or Decimal("0"),
    }


def get_top_merchants(
    *,
    user_id: int,
    limit: int = 10,
):
    return (
        FinancialEvent.objects.filter(
            user_id=user_id,
            is_active=True,
            event_type="DEBIT",
        )
        .values("merchant")
        .annotate(
            total_amount=Sum("amount"),
        )
        .order_by("-total_amount")[:limit]
    )