import imp
from fastapi import APIRouter
from app.api.health import health_router
from app.api.ml.models_info import ml_router

main_router = APIRouter()
main_router.include_router(health_router, tags=["health"], prefix="/health")
main_router.include_router(ml_router, tags=["ml"], prefix="/ml")




