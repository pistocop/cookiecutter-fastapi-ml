import json
from typing import List

from loguru import logger

from app.config import settings


class ModelsManager:
    def __init__(self, models_file: str) -> None:
        self.models_info: List[dict] = self._load_models_info(models_file)
        self.models = self._load_models(self.models_info)
        logger.debug(f"Loaded {len(self.models_info)}# models")

    def get_models_info(self) -> List[dict]:
        return self.models_info

    @staticmethod
    def _load_models_info(models_file) -> List[dict]:
        models_info = json.load(open(models_file, "r"))
        return models_info

    @staticmethod
    def _load_models(models_info: List[dict]) -> dict:
        models = {}
        for model_info in models_info:
            id = model_info["model_id"]
            models[id] = ModelsManager._load_model(model_info)
        return models

    @staticmethod
    def _load_model(model_info: dict):
        pass


models_manager = ModelsManager(settings.models_file)
