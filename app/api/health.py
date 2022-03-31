from asyncio.log import logger
from datetime import datetime

from fastapi import APIRouter

from app.models.health import HealthCheck

router = APIRouter()


@router.get(
    "",
    response_model=HealthCheck,
    name="health:check",
    description="Return current timestamp in ISO-8601 format.",
)
async def healthz_check() -> HealthCheck:
    return HealthCheck(timestamp=datetime.now().isoformat())
