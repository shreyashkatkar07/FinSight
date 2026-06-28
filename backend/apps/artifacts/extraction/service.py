import time
from pathlib import Path

from django.conf import settings

from .ocr import reader
from .schemas import ExtractionResult


class ExtractionService:

    def extract(
        self,
        *,
        artifact,
    ) -> ExtractionResult:

        start = time.perf_counter()

        image_path = (
            Path(settings.MEDIA_ROOT)
            / artifact.storage_path
        )

        result = reader.readtext(
            str(image_path),
        )

        lines = []
        confidences = []

        for _, text, confidence in result:
            lines.append(text)
            confidences.append(confidence)

        average = (
            sum(confidences) / len(confidences)
            if confidences
            else 0.0
        )

        end = time.perf_counter()

        return ExtractionResult(
            text="\n".join(lines),
            confidence=round(
                average,
                2,
            ),
            engine="easyocr",
            processing_time_ms=int(
                (end - start) * 1000
            ),
        )