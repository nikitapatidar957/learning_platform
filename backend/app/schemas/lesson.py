from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, ConfigDict


class LessonSection(BaseModel):
    type: str  # explanation | code | visualization | callout | quiz | practice
    title: Optional[str] = None
    content: Optional[str] = None
    language: Optional[str] = None
    code: Optional[str] = None
    variant: Optional[str] = None  # tip | info | warning
    component: Optional[str] = None
    initialState: Optional[Dict[str, Any]] = None


class LessonContent(BaseModel):
    sections: List[LessonSection] = []


class LessonSummaryResponse(BaseModel):
    id: str = Field(alias="_id", default="")
    topicId: str
    topicSlug: str
    subjectSlug: str
    title: str
    slug: str
    description: str
    estimatedTime: str = "15 min"
    difficulty: str = "Beginner"
    order: int = 0
    isPublished: bool = True
    interactiveType: Optional[str] = None
    status: Optional[str] = "not_started"

    model_config = ConfigDict(populate_by_name=True)


class LessonDetailResponse(LessonSummaryResponse):
    content: LessonContent
    previous_lesson: Optional[Dict[str, str]] = None
    next_lesson: Optional[Dict[str, str]] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None
