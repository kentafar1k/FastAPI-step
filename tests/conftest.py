from fastapi.testclient import TestClient
from app_db.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app)