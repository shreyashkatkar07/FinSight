from datetime import date
from decimal import Decimal
from uuid import UUID

from ninja import Schema


class FinancialEventCreateIn(Schema):
    amount: Decimal
    event_type: str
    description: str
    transaction_date: date
    currency: str = "INR"


class FinancialEventCreateDTO(Schema):
    user_id: int

    amount: Decimal

    currency: str

    event_type: str

    description: str

    transaction_date: date


class FinancialEventOut(Schema):
    uuid: UUID

    amount: Decimal

    currency: str

    event_type: str

    description: str

    transaction_date: date


class FinancialEventListFilter(Schema):
    event_type: str | None = None