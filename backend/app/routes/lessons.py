from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.lesson import LessonSummaryResponse, LessonDetailResponse
from app.services.lesson_service import LessonService
from app.core.auth import get_optional_current_user, CurrentUser

router = APIRouter(tags=["Lessons"])


def get_lesson_service() -> LessonService:
    return LessonService()


@router.get("/api/topics/{topic_slug}/lessons", response_model=List[LessonSummaryResponse])
def get_lessons_for_topic(
    topic_slug: str,
    service: LessonService = Depends(get_lesson_service),
    current_user: Optional[CurrentUser] = Depends(get_optional_current_user),
):
    """List all lessons in a given topic."""
    user_id = current_user.clerk_user_id if current_user else None
    return service.get_lessons_by_topic(topic_slug, user_id=user_id)


@router.get("/api/lessons/{slug}", response_model=LessonDetailResponse)
def get_lesson_by_slug(
    slug: str,
    service: LessonService = Depends(get_lesson_service),
    current_user: Optional[CurrentUser] = Depends(get_optional_current_user),
):
    """Get full lesson content, sections, interactive component config, and adjacent lesson links."""
    user_id = current_user.clerk_user_id if current_user else None
    lesson = service.get_lesson_by_slug(slug, user_id=user_id)
    if not lesson:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Lesson with slug '{slug}' not found",
        )
    return lesson
