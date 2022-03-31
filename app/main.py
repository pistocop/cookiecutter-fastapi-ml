import os

import uvicorn
from fastapi import FastAPI

from app.api.main_router import main_router
from app.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=settings.app_description,
)

# Include routes, one for each family of APIs
app.include_router(main_router, prefix=settings.api_prefix)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8080, reload=True)
