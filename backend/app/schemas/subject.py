from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict


class SubjectBase(BaseModel):
    name: str
    slug: str
    description: str
    icon: str = "BookOpen"
    order: int = 0
    difficulty: str = "Beginner to Advanced"
    isPublished: bool = True


class SubjectSummaryResponse(SubjectBase):
    id: str = Field(alias="_id", default="")
    topic_count: int = 0
    lesson_count: int = 0
    estimated_hours: Optional[str] = "10+ hrs"
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    model_config = ConfigDict(populate_by_name=True)


class SubjectDetailResponse(SubjectSummaryResponse):
    topics: List[dict] = []
