from ninja import NinjaAPI

from apps.financial_events.router import router as financial_event_router
from apps.artifacts.router import router as artifact_router
from apps.ingestion.router import router as ingestion_router

api = NinjaAPI()

api.add_router(
    "/financial-events/",
    financial_event_router,
)
api.add_router(
    "/artifacts/",
    artifact_router,
)
api.add_router(
    "/ingestion/",
    ingestion_router,
)