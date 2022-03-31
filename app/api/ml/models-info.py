from asyncio.log import logger
from datetime import datetime

from fastapi import APIRouter

from app.models.health import HealthCheck

router = APIRouter()

@router.get(
    "/models-info",
    response_model=HealthCheck,
    summary="Get models info",
    description="Return ML models info loaded from `ml-models.json` file",
)
async def model_info():
    return HealthCheck(timestamp=datetime.now().isoformat())
