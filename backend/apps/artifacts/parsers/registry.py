from apps.artifacts.models import FileType

from .pdf_parser import PDFParser


PARSER_MAP = {
    FileType.PDF: PDFParser,
}


def get_parser(
    *,
    file_type: str,
):
    parser_class = PARSER_MAP.get(file_type)

    if not parser_class:
        raise ValueError(
            f"Unsupported file type: {file_type}"
        )

    return parser_class()