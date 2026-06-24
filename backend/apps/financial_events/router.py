from ninja import Router
from uuid import UUID

from apps.financial_events.schemas import (
    FinancialEventCreateIn,
    FinancialEventOut,
    FinancialSummaryOut,
    TopMerchantOut,
    InsightsOut,
)

from apps.financial_events import (
    service,
    analytics_service,
    insights_service,
)


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
    return analytics_service.get_summary(
        user_id=1,
    )

@router.get(
    "/top-merchants",
    response=list[TopMerchantOut],
)
def get_top_merchants(
    request,
):
    return analytics_service.get_top_merchants(
        user_id=1,
    )


@router.get(
    "/insights",
    response=InsightsOut,
)
def get_insights(
    request,
):
    return insights_service.get_insights(
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