import pytest
from fastapi.testclient import TestClient
import mongomock
from app.main import app
from app.database.mongodb import db_manager
from scripts.seed import seed_database


@pytest.fixture(scope="session")
def mock_db():
    client = mongomock.MongoClient()
    db = client["learning_platform"]
    # Patch db_manager
    original_client = db_manager.client
    original_db = db_manager.db
    original_is_mock = db_manager.is_mock

    db_manager.client = client
    db_manager.db = db
    db_manager.is_mock = True

    # Seed mock db with full dataset
    seed_database()

    yield db

    db_manager.client = original_client
    db_manager.db = original_db
    db_manager.is_mock = original_is_mock


@pytest.fixture
def client(mock_db):
    return TestClient(app, raise_server_exceptions=True)


@pytest.fixture
def auth_headers():
    return {
        "X-Dev-User-Id": "user_test_12345",
        "Authorization": "Bearer mock_jwt_token_for_test"
    }
