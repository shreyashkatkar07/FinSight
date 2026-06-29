from datetime import date
from decimal import Decimal
from enum import Enum

from pydantic import BaseModel
from shared.enums import Category


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
    confidence: float
    category: Category
    description: str | None = None
    transaction_date: date | None = None


class ExtractionResponse(BaseModel):
    transactions: list[ExtractedTransaction]