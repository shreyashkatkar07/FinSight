from datetime import date
from decimal import Decimal

from apps.financial_events import service as financial_event_service

from apps.ingestion.schemas import (
    TextIngestionOut,
)

from shared.contracts.parsed_transaction import (
    ParsedTransaction,
)


CREDIT_KEYWORDS = {
    "salary",
    "credited",
    "received",
    "refund",
}


def parse_text(
    *,
    text: str,
) -> ParsedTransaction:
    tokens = text.split()

    merchant = tokens[0]

    amount = None
    amount_index = None

    for index, token in enumerate(tokens):
        try:
            amount = Decimal(token)
            amount_index = index
            break
        except Exception:
            continue

    if amount is None:
        raise ValueError(
            "Could not identify amount",
        )

    description_tokens = [
        token
        for index, token in enumerate(tokens)
        if index != 0 and index != amount_index
    ]

    description = " ".join(description_tokens)

    event_type = "DEBIT"

    lower_text = text.lower()

    if any(
        keyword in lower_text
        for keyword in CREDIT_KEYWORDS
    ):
        event_type = "CREDIT"

    return ParsedTransaction(
        amount=amount,
        merchant=merchant,
        description=description,
        transaction_date=date.today(),
        event_type=event_type,
        currency="INR",
    )


def ingest_text(
    *,
    user_id: int,
    text: str,
):
    parsed_transaction = parse_text(
        text=text,
    )

    financial_event = (
        financial_event_service.create_from_parsed_transaction(
            user_id=user_id,
            parsed_transaction=parsed_transaction,
        )
    )

    return TextIngestionOut(
        merchant=parsed_transaction.merchant,
        amount=parsed_transaction.amount,
        financial_event_uuid=financial_event.uuid,
    )