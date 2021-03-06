import sys

from fastapi.testclient import TestClient
from loguru import logger

from app.main import app

# More information on how add tests:
# https://fastapi.tiangolo.com/tutorial/testing/#extended-testing-file


client = TestClient(app)


logger.configure(
    handlers=[{"sink": sys.stdout}]
)  # overwrite back-end native behaviour (log to stderr)


def test_read_item():
    response = client.get("/health")
    timestamp = response.json()["timestamp"]
    logger.info(f"Example of pytest log! Current time:{timestamp}")
    assert response.status_code == 200
