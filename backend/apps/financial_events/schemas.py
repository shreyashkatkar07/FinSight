from datetime import date
from decimal import Decimal
from uuid import UUID

from ninja import Schema


class FinancialEventCreateIn(Schema):
    merchant: str

    amount: Decimal

    event_type: str

    description: str

    transaction_date: date

    currency: str = "INR"


class FinancialEventCreateDTO(Schema):
    user_id: int

    artifact_id: int | None = None

    merchant: str

    amount: Decimal

    currency: str

    event_type: str

    category: str

    description: str

    transaction_date: date


class FinancialEventOut(Schema):
    uuid: UUID
    
    merchant: str

    amount: Decimal

    currency: str

    event_type: str

    category: str

    description: str

    transaction_date: date


class FinancialEventListFilter(Schema):
    event_type: str | None = None


class PeriodOut(Schema):
    start_date: date

    end_date: date


class FinancialSummaryOut(Schema):
    period: PeriodOut

    total_income: Decimal

    total_expense: Decimal

    net_flow: Decimal


class TopMerchantOut(Schema):
    merchant: str

    total_amount: Decimal


class InsightsOut(Schema):
    insights: list[str]