from datetime import date

from apps.artifacts.models import Artifact

from .base import BaseParser
from .contracts import ParsedTransaction


class PDFParser(BaseParser):

    def parse(
        self,
        artifact: Artifact,
    ):
        return [
            ParsedTransaction(
                amount=50000,
                description="Salary",
                transaction_date=date.today(),
                event_type="CREDIT",
                currency="INR",
            ),
            ParsedTransaction(
                amount=450,
                description="Swiggy",
                transaction_date=date.today(),
                event_type="DEBIT",
                currency="INR",
            ),
        ]