from typing import Optional, List
from pydantic import BaseModel, Field, ConfigDict, computed_field


class TopicBase(BaseModel):
    subjectId: str
    subjectSlug: str
    title: str
    slug: str
    description: str
    order: int = 0
    isPublished: bool = True


class TopicResponse(TopicBase):
    id: str = Field(default="")
    lesson_count: int = 0
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    @computed_field
    @property
    def _id(self) -> str:
        return self.id

    model_config = ConfigDict(populate_by_name=True)


class TopicDetailResponse(TopicResponse):
    lessons: List[dict] = []
