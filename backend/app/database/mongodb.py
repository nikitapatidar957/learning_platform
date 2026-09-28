import logging
from typing import Optional
import certifi
from pymongo import MongoClient, ASCENDING, TEXT
from pymongo.database import Database
import mongomock
from app.core.config import settings

logger = logging.getLogger("learning_platform.database")


class MongoDBManager:
    client: Optional[MongoClient] = None
    db: Optional[Database] = None
    is_mock: bool = False
    connection_type: str = "disconnected"
    host_display: str = ""

    def connect(self, uri: Optional[str] = None, db_name: Optional[str] = None) -> Database:
        if self.db is not None:
            return self.db

        mongodb_uri = uri or settings.MONGODB_URI
        database_name = db_name or settings.MONGODB_DB_NAME
        is_atlas = "mongodb+srv://" in mongodb_uri or "mongodb.net" in mongodb_uri
        host_display = mongodb_uri.split("@")[-1] if "@" in mongodb_uri else mongodb_uri

        # 1. Try primary configured URI (Atlas / custom)
        try:
            logger.info("Connecting to MongoDB at: %s", host_display)
            client_kwargs = {
                "serverSelectionTimeoutMS": 10000 if is_atlas else 3000,
            }
            if is_atlas or "ssl=true" in mongodb_uri.lower() or "tls=true" in mongodb_uri.lower():
                try:
                    client_kwargs["tlsCAFile"] = certifi.where()
                except Exception as cert_err:
                    logger.debug("Certifi tlsCAFile not applied: %s", cert_err)

            client = MongoClient(mongodb_uri, **client_kwargs)
            client.admin.command("ping")
            self.client = client
            self.db = client[database_name]
            self.is_mock = False
            self.connection_type = "atlas" if is_atlas else "custom"
            self.host_display = host_display
            logger.info("Successfully connected to primary MongoDB database '%s' at %s", database_name, host_display)
            return self.db
        except Exception as e:
            logger.warning(
                "Could not connect to primary MongoDB (%s): %s. Checking local MongoDB daemon...",
                host_display,
                str(e)
            )

        # 2. Try local MongoDB service (mongodb://localhost:27017)
        try:
            local_uri = "mongodb://localhost:27017"
            client = MongoClient(local_uri, serverSelectionTimeoutMS=2000)
            client.admin.command("ping")
            self.client = client
            self.db = client[database_name]
            self.is_mock = False
            self.connection_type = "local"
            self.host_display = "localhost:27017"
            logger.info("Successfully connected to local MongoDB instance at localhost:27017")
            return self.db
        except Exception as e_local:
            logger.warning(
                "Local MongoDB unavailable (%s). Falling back to in-memory MongoMock engine.",
                str(e_local)
            )

        # 3. Fallback to resilient in-memory MongoMock
        mock_client = mongomock.MongoClient()
        self.client = mock_client
        self.db = mock_client[database_name]
        self.is_mock = True
        self.connection_type = "mock"
        self.host_display = "in-memory (mongomock)"
        logger.info("Using in-memory MongoMock database.")
        return self.db

    def close(self):
        if self.client and not self.is_mock:
            self.client.close()
            self.client = None
            self.db = None
            self.connection_type = "disconnected"
            self.host_display = ""
            logger.info("Closed MongoDB connection.")

    def get_database(self) -> Database:
        if self.db is None:
            return self.connect()
        return self.db

    def create_indexes(self):
        db = self.get_database()
        logger.info("Creating MongoDB indexes...")

        try:
            # 1. users
            db.users.create_index([("clerk_user_id", ASCENDING)], unique=True)
            db.users.create_index([("email", ASCENDING)])

            # 2. subjects
            db.subjects.create_index([("slug", ASCENDING)], unique=True)
            db.subjects.create_index([("order", ASCENDING)])
            db.subjects.create_index([("isPublished", ASCENDING)])

            # 3. topics
            db.topics.create_index([("slug", ASCENDING)], unique=True)
            db.topics.create_index([("subjectId", ASCENDING)])
            db.topics.create_index([("subjectSlug", ASCENDING)])
            db.topics.create_index([("order", ASCENDING)])

            # 4. lessons
            db.lessons.create_index([("slug", ASCENDING)], unique=True)
            db.lessons.create_index([("topicId", ASCENDING)])
            db.lessons.create_index([("topicSlug", ASCENDING)])
            db.lessons.create_index([("subjectSlug", ASCENDING)])
            db.lessons.create_index([("order", ASCENDING)])
            
            try:
                db.lessons.create_index([
                    ("title", TEXT),
                    ("description", TEXT),
                ], name="lesson_search_index")
            except Exception:
                db.lessons.create_index([("title", ASCENDING)])

            # 5. progress
            db.progress.create_index(
                [("user_id", ASCENDING), ("lesson_id", ASCENDING)],
                unique=True
            )
            db.progress.create_index([("user_id", ASCENDING)])
            db.progress.create_index([("status", ASCENDING)])
            logger.info("MongoDB indexes verified and ready.")
        except Exception as e:
            logger.warning("Index creation notice: %s", str(e))


db_manager = MongoDBManager()


def get_db() -> Database:
    return db_manager.get_database()
