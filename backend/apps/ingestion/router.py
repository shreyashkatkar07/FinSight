from ninja import Router

from apps.ingestion import service

from apps.ingestion.schemas import (
    TextIngestionIn,
    TextIngestionOut,
)

router = Router()


@router.post(
    "/text",
    response=TextIngestionOut,
)
def ingest_text(
    request,
    payload: TextIngestionIn,
):
    return service.ingest_text(
        user_id=1,
        text=payload.text,
    )