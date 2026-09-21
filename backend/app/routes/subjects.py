from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.subject import SubjectSummaryResponse, SubjectDetailResponse
from app.services.subject_service import SubjectService
from app.core.auth import get_optional_current_user, CurrentUser

router = APIRouter(prefix="/api/subjects", tags=["Subjects"])


def get_subject_service() -> SubjectService:
    return SubjectService()


@router.get("", response_model=List[SubjectSummaryResponse])
def get_subjects(
    published_only: bool = True,
    service: SubjectService = Depends(get_subject_service),
):
    """List all available subjects in the platform."""
    return service.list_subjects(published_only=published_only)


@router.get("/{slug}", response_model=SubjectDetailResponse)
def get_subject_by_slug(
    slug: str,
    service: SubjectService = Depends(get_subject_service),
    current_user: Optional[CurrentUser] = Depends(get_optional_current_user),
):
    """Get subject details including ordered topic curriculum."""
    user_id = current_user.clerk_user_id if current_user else None
    subject = service.get_subject_by_slug(slug=slug, user_id=user_id)
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Subject with slug '{slug}' not found",
        )
    return subject
