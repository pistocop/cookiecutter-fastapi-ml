from fastapi import APIRouter

from app.api.models_manager import models_manager

ml_router = APIRouter()


@ml_router.get(
    "/models-info",
    summary="Get models info",
    description="Return ML models info loaded from `ml-models.json` file",
)
async def model_info():
    return models_manager.get_models_info()