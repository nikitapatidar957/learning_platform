import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.database.mongodb import db_manager
from app.routes.auth import router as auth_router
from app.routes.subjects import router as subjects_router
from app.routes.topics import router as topics_router
from app.routes.lessons import router as lessons_router
from app.routes.progress import router as progress_router
from app.routes.search import router as search_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("learning_platform")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Initializing Learning Platform Backend...")
    try:
        db_manager.connect()
        db_manager.create_indexes()
        logger.info("MongoDB initialized and indexes verified.")
    except Exception as e:
        logger.error("Failed to connect to MongoDB during startup: %s", str(e))
    yield
    logger.info("Shutting down Learning Platform Backend...")
    db_manager.close()


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Modern Interactive Learning Platform API for DSA, Machine Learning, Deep Learning, SQL, MongoDB, LLMs, Generative AI, and Agentic AI.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register Routers
app.include_router(auth_router)
app.include_router(subjects_router)
app.include_router(topics_router)
app.include_router(lessons_router)
app.include_router(progress_router)
app.include_router(search_router)


@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "app": settings.PROJECT_NAME,
        "docs": "/docs",
        "version": "1.0.0",
    }


@app.get("/api/health", tags=["Health"])
def health_check():
    db_status = "connected" if db_manager.client is not None else "disconnected"
    return {
        "status": "healthy",
        "database": db_status,
        "database_type": db_manager.connection_type,
        "database_host": db_manager.host_display,
        "database_name": settings.MONGODB_DB_NAME,
        "environment": settings.ENVIRONMENT,
    }
