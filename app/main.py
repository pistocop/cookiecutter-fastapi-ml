import os

import uvicorn
from fastapi import FastAPI

from app.api import health
from app.config import settings

prefix = os.getenv("CLUSTER_ROUTE_PREFIX", "").rstrip("/")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)

app.include_router(health.router, tags=["health"], prefix="/health")
app.include_router(health.router, tags=["ML"], prefix="/ml")


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, log_level="info", reload=True)
