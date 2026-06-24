from google import genai

from django.conf import settings

from apps.financial_events import analytics_service


client = genai.Client(
    api_key=settings.GEMINI_API_KEY,
)


def build_prompt(
    *,
    facts: dict,
):
    return f"""
    You are a personal finance analyst.

    Generate:

    1. One cash-flow insight
    2. One merchant insight
    3. One spending-pattern insight

    Do not repeat themes.

    Rules:
    - Do not simply repeat the facts.
    - Focus on spending patterns.
    - Mention spending concentration when relevant.
    - Mention cash-flow status when relevant.
    - Use only the provided facts.
    - Do not perform calculations.
    - Do not invent percentages.
    - Do not invent trends.
    - Keep each insight under 20 words.
    - Return exactly 3 insights.
    - Return one insight per line.
    - Do not use bullet points.

    Facts:

    Total Income: ₹{facts['total_income']}
    Total Expense: ₹{facts['total_expense']}

    Cash Flow Status:
    {facts['cash_flow_status']}

    Merchant Count:
    {facts['merchant_count']}

    Top Merchants:
    {facts['merchant_lines']}
    """


def build_insight_facts(
    *,
    summary,
    top_merchants,
):
    if summary.net_flow >= 0:
        cash_flow_status = (
            f"Positive cash flow of "
            f"₹{summary.net_flow}"
        )
    else:
        cash_flow_status = (
            f"Negative cash flow of "
            f"₹{abs(summary.net_flow)}"
        )

    merchant_lines = "\n".join(
        [
            (
                f"- {merchant['merchant']}: "
                f"₹{merchant['total_amount']}"
            )
            for merchant in top_merchants
        ]
    )

    return {
        "total_income": str(summary.total_income),
        "total_expense": str(summary.total_expense),
        "cash_flow_status": cash_flow_status,
        "merchant_count": len(top_merchants),
        "merchant_lines": merchant_lines,
    }


def get_insights(
    *,
    user_id: int,
):
    try:
        summary = analytics_service.get_summary(
            user_id=user_id,
        )

        top_merchants = analytics_service.get_top_merchants(
            user_id=user_id,
        )

        if not top_merchants:
            return {
                "insights": [
                    "No spending data available yet.",
                    "Add transactions to unlock insights.",
                    "More activity improves analysis quality.",
                ]
            }

        facts = build_insight_facts(
            summary=summary,
            top_merchants=top_merchants,
        )

        prompt = build_prompt(
            facts=facts,
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        insights_text = (
            response.text
            if response.text
            else ""
        )

        insights = [
            line.strip()
            .lstrip("-")
            .lstrip("•")
            .strip()
            for line in insights_text.split("\n")
            if line.strip()
        ]

        return {
            "insights": insights[:3],
        }

    except Exception as e:
        print(
            f"Insights generation failed: {e}"
        )

        return {
            "insights": [],
        }