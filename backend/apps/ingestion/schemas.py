from decimal import Decimal
from uuid import UUID

from ninja import Schema


class TextIngestionIn(Schema):
    text: str


class TextIngestionOut(Schema):
    merchant: str

    amount: Decimal

    financial_event_uuid: UUID