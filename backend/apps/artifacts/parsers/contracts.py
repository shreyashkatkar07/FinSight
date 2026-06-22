from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class ParsedTransaction(BaseModel):
    amount: Decimal
    description: str
    transaction_date: date
    event_type: str
    currency: str