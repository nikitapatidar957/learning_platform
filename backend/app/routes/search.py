from fastapi import APIRouter, Depends, Query
from app.schemas.search import SearchResponse
from app.services.search_service import SearchService

router = APIRouter(prefix="/api/search", tags=["Search"])


def get_search_service() -> SearchService:
    return SearchService()


@router.get("", response_model=SearchResponse)
def search_content(
    q: str = Query("", description="Search term for subjects, topics, or lessons"),
    limit: int = Query(20, ge=1, le=50),
    service: SearchService = Depends(get_search_service),
):
    """
    Global search endpoint.
    Searches across subjects, topics, and lessons.
    """
    return service.search(query=q, limit=limit)
