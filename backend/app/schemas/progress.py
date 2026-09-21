from typing import Optional, List, Dict
from pydantic import BaseModel, Field, ConfigDict


class ProgressCreateRequest(BaseModel):
    status: str = "in_progress"
    progress_percentage: int = Field(default=50, ge=0, le=100)


class ProgressUpdateRequest(BaseModel):
    status: Optional[str] = "completed"
    progress_percentage: Optional[int] = Field(default=100, ge=0, le=100)


class ProgressResponse(BaseModel):
    id: str = Field(alias="_id", default="")
    user_id: str
    lesson_id: str
    lesson_slug: Optional[str] = None
    subject_slug: Optional[str] = None
    topic_slug: Optional[str] = None
    status: str
    progress_percentage: int
    started_at: Optional[str] = None
    last_accessed_at: Optional[str] = None
    completed_at: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class SubjectProgressSummary(BaseModel):
    subject_slug: str
    subject_name: str
    completed_lessons: int
    total_lessons: int
    percentage: int


class OverallProgressResponse(BaseModel):
    total_completed: int
    total_in_progress: int
    total_lessons: int
    overall_percentage: int
    subjects_progress: List[SubjectProgressSummary] = []
    recently_viewed: List[Dict] = []
    current_lesson: Optional[Dict] = None
