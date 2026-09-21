from typing import List, Optional
from pydantic import BaseModel


class SearchResultItem(BaseModel):
    id: str
    type: str  # subject | topic | lesson
    title: str
    slug: str
    description: Optional[str] = None
    subjectSlug: Optional[str] = None
    topicSlug: Optional[str] = None
    difficulty: Optional[str] = None
    estimatedTime: Optional[str] = None
    url: str


class SearchResponse(BaseModel):
    query: str
    total: int
    results: List[SearchResultItem] = []
