from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.progress import (
    ProgressResponse,
    ProgressCreateRequest,
    ProgressUpdateRequest,
    OverallProgressResponse,
)
from app.services.progress_service import ProgressService
from app.core.auth import get_current_user, CurrentUser

router = APIRouter(prefix="/api/progress", tags=["Progress"])


def get_progress_service() -> ProgressService:
    return ProgressService()


@router.get("", response_model=OverallProgressResponse)
def get_user_progress(
    current_user: CurrentUser = Depends(get_current_user),
    service: ProgressService = Depends(get_progress_service),
):
    """Get the authenticated user's overall learning progress and stats."""
    return service.get_user_overall_progress(user_id=current_user.clerk_user_id)


@router.get("/{lesson_id}", response_model=ProgressResponse)
def get_lesson_progress(
    lesson_id: str,
    current_user: CurrentUser = Depends(get_current_user),
    service: ProgressService = Depends(get_progress_service),
):
    """Get progress for a specific lesson."""
    return service.get_lesson_progress(
        user_id=current_user.clerk_user_id,
        lesson_id=lesson_id,
    )


@router.post("/{lesson_id}", response_model=ProgressResponse)
def start_or_update_progress(
    lesson_id: str,
    payload: ProgressCreateRequest,
    current_user: CurrentUser = Depends(get_current_user),
    service: ProgressService = Depends(get_progress_service),
):
    """Mark a lesson as in-progress or update progress percentage."""
    if not lesson_id or lesson_id in ("undefined", "null"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid lesson identifier",
        )
    return service.update_progress(
        user_id=current_user.clerk_user_id,
        lesson_id=lesson_id,
        status=payload.status,
        progress_percentage=payload.progress_percentage,
    )


@router.patch("/{lesson_id}", response_model=ProgressResponse)
def patch_lesson_progress(
    lesson_id: str,
    payload: ProgressUpdateRequest,
    current_user: CurrentUser = Depends(get_current_user),
    service: ProgressService = Depends(get_progress_service),
):
    """Mark a lesson as completed (or update progress)."""
    if not lesson_id or lesson_id in ("undefined", "null"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid lesson identifier",
        )
    return service.update_progress(
        user_id=current_user.clerk_user_id,
        lesson_id=lesson_id,
        status=payload.status or "completed",
        progress_percentage=payload.progress_percentage if payload.progress_percentage is not None else 100,
    )
