from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel


class EventType(str, Enum):
    INCOME = "INCOME"
    EXPENSE = "EXPENSE"


class Currency(str, Enum):
    INR = "INR"
    USD = "USD"
    EUR = "EUR"


class ExtractedTransaction(BaseModel):
    merchant: str
    amount: Decimal
    currency: Currency
    event_type: EventType
    description: str | None = None
    transaction_date: date | None = None


class ExtractionResponse(BaseModel):
    transactions: list[ExtractedTransaction]