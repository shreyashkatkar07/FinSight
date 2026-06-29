from apps.artifacts.extractors.registry import (
    get_extractor,
)

from .service import (
    transaction_extraction_service,
)
from .schemas import ExtractionResponse


class TransactionExtractionPipeline:

    def extract(
        self,
        *,
        artifact,
    ) -> ExtractionResponse:
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

        return extraction


transaction_extraction_pipeline = (
    TransactionExtractionPipeline()
)