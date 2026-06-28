from apps.artifacts.models import FileType

from .image_extractor import ImageExtractor
from .text_extractor import TextExtractor


EXTRACTOR_MAP = {
    FileType.IMAGE: ImageExtractor,
    FileType.TEXT: TextExtractor,
}


def get_extractor(
    *,
    file_type: str,
):
    extractor_class = EXTRACTOR_MAP.get(
        file_type,
    )

    if not extractor_class:
        raise ValueError(
            f"Unsupported file type: {file_type}",
        )

    return extractor_class()