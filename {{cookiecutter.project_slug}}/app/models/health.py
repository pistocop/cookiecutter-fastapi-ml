from pydantic import BaseModel


class HealthCheck(BaseModel):
    timestamp: str
