from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, computed_field


class SubjectBase(BaseModel):
    name: str
    slug: str
    description: str
    icon: str = "BookOpen"
    order: int = 0
    difficulty: str = "Beginner to Advanced"
    isPublished: bool = True


class SubjectSummaryResponse(SubjectBase):
    id: str = Field(default="")
    topic_count: int = 0
    lesson_count: int = 0
    estimated_hours: Optional[str] = "10+ hrs"
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    @computed_field
    @property
    def _id(self) -> str:
        return self.id

    model_config = ConfigDict(populate_by_name=True)


class SubjectDetailResponse(SubjectSummaryResponse):
    topics: List[dict] = []
