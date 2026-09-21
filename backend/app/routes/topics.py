from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.topic import TopicResponse, TopicDetailResponse
from app.services.topic_service import TopicService

router = APIRouter(tags=["Topics"])


def get_topic_service() -> TopicService:
    return TopicService()


@router.get("/api/subjects/{subject_slug}/topics", response_model=List[TopicResponse])
def get_topics_for_subject(
    subject_slug: str,
    service: TopicService = Depends(get_topic_service),
):
    """Get all topics belonging to a subject."""
    return service.get_topics_by_subject(subject_slug)


@router.get("/api/topics/{slug}", response_model=TopicDetailResponse)
def get_topic_by_slug(
    slug: str,
    service: TopicService = Depends(get_topic_service),
):
    """Get topic details and its lessons."""
    topic = service.get_topic_by_slug(slug)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Topic with slug '{slug}' not found",
        )
    return topic
