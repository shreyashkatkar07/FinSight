# apps/financial_events/analytics_service.py

from datetime import date

from apps.financial_events import repository
from apps.financial_events.schemas import (
    FinancialSummaryOut,
    PeriodOut,
)


def get_summary(
    *,
    user_id: int,
):
    today = date.today()

    start_date = date(
        year=today.year,
        month=today.month,
        day=1,
    )

    summary = repository.get_summary(
        user_id=user_id,
        start_date=start_date,
        end_date=today,
    )

    total_income = summary["total_income"]

    total_expense = summary["total_expense"]

    return FinancialSummaryOut(
        period=PeriodOut(
            start_date=start_date,
            end_date=today,
        ),
        total_income=total_income,
        total_expense=total_expense,
        net_flow=(
            total_income
            - total_expense
        ),
    )


def get_top_merchants(
    *,
    user_id: int,
):
    return repository.get_top_merchants(
        user_id=user_id,
    )