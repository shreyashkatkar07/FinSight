# transaction_extraction/pipeline.py

from apps.artifacts.extractors.registry import (
    get_extractor,
)

from .mapper import (
    to_financial_event_dto,
)
from .service import (
    transaction_extraction_service,
)


class TransactionExtractionPipeline:

    def extract(
        self,
        *,
        artifact,
    ):
        extractor = get_extractor(
            file_type=artifact.file_type,
        )

        raw_text = extractor.extract(
            artifact=artifact,
        )

        print("=" * 50)
        print("RAW TEXT")
        print(repr(raw_text))
        print("=" * 50)

        extraction = (
            transaction_extraction_service
            .extract_transactions(
                raw_text=raw_text,
            )
        )

        return [
            to_financial_event_dto(
                transaction=transaction,
                artifact=artifact,
            )
            for transaction in extraction.transactions
        ]


transaction_extraction_pipeline = (
    TransactionExtractionPipeline()
)