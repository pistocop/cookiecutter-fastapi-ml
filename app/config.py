import logging
import os
import sys

from loguru import logger
from pydantic import BaseSettings

ENV_FILE = os.getenv("ENV_FILE", "app/.env")

# Load env variables from ENVIRONMENT and from ENV_FILE
class Settings(BaseSettings):
    app_name: str = "cookiecutter-fastapi-ml"
    app_description: str = "cookiecutter FastAPI back-end ML oriented"
    app_version: str = "0.1.0"
    api_prefix: str = ""
    models_file = "app/ml-models.json"
    debug: bool = False

    class Config:
        env_file = ENV_FILE


settings = Settings()

# Define logging level
LOGGING_LEVEL = logging.DEBUG if settings.debug else logging.INFO
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
logger.debug("Configuration parameteres loaded")

