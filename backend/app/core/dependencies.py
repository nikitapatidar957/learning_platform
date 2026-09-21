from pymongo.database import Database
from app.database.mongodb import get_db
from app.core.auth import get_current_user, get_optional_current_user, CurrentUser


def get_database() -> Database:
    """Dependency that returns MongoDB Database instance."""
    return get_db()
