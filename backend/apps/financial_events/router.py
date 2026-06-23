from ninja import Router
from uuid import UUID

from apps.financial_events.schemas import (
    FinancialEventCreateIn,
    FinancialEventOut,
    FinancialSummaryOut,
)

from apps.financial_events import service

router = Router()


@router.post(
    "/",
    response=FinancialEventOut,
)
def create_financial_event(
    request,
    payload: FinancialEventCreateIn,
):
    return service.create_financial_event(
        user_id=1,
        event_data=payload,
    )


@router.get(
    "/summary",
    response=FinancialSummaryOut,
)
def get_summary(
    request,
):
    return service.get_summary(
        user_id=1,
    )


@router.get(
    "/{event_uuid}",
    response=FinancialEventOut,
)
def get_financial_event(
    request,
    event_uuid: UUID,
):
    return service.get_financial_event_by_uuid(
        event_uuid=event_uuid,
    )


@router.get(
    "/",
    response=list[FinancialEventOut],
)
def get_financial_events(
    request,
):
    return service.get_financial_events(
        user_id=1,
    )