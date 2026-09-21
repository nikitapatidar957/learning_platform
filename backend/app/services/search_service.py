import re
from typing import List
from pymongo.database import Database
from app.database.mongodb import get_db
from app.schemas.search import SearchResponse, SearchResultItem


class SearchService:
    def __init__(self, db: Database = None):
        self.db = db or get_db()

    def search(self, query: str, limit: int = 20) -> SearchResponse:
        clean_query = query.strip()
        if not clean_query:
            return SearchResponse(query=query, total=0, results=[])

        regex = re.compile(re.escape(clean_query), re.IGNORECASE)
        results: List[SearchResultItem] = []

        # 1. Search Subjects
        subjects = self.db.subjects.find(
            {"$or": [{"name": regex}, {"description": regex}, {"slug": regex}], "isPublished": True}
        ).limit(5)
        for s in subjects:
            results.append(
                SearchResultItem(
                    id=str(s["_id"]),
                    type="subject",
                    title=s["name"],
                    slug=s["slug"],
                    description=s.get("description"),
                    url=f"/courses/{s['slug']}"
                )
            )

        # 2. Search Topics
        topics = self.db.topics.find(
            {"$or": [{"title": regex}, {"description": regex}, {"slug": regex}], "isPublished": True}
        ).limit(5)
        for t in topics:
            results.append(
                SearchResultItem(
                    id=str(t["_id"]),
                    type="topic",
                    title=t["title"],
                    slug=t["slug"],
                    description=t.get("description"),
                    subjectSlug=t.get("subjectSlug"),
                    url=f"/courses/{t.get('subjectSlug')}"
                )
            )

        # 3. Search Lessons
        lessons = self.db.lessons.find(
            {
                "$or": [
                    {"title": regex},
                    {"description": regex},
                    {"slug": regex},
                    {"content.sections.content": regex}
                ],
                "isPublished": True
            }
        ).limit(10)
        for l in lessons:
            results.append(
                SearchResultItem(
                    id=str(l["_id"]),
                    type="lesson",
                    title=l["title"],
                    slug=l["slug"],
                    description=l.get("description"),
                    subjectSlug=l.get("subjectSlug"),
                    topicSlug=l.get("topicSlug"),
                    difficulty=l.get("difficulty", "Beginner"),
                    estimatedTime=l.get("estimatedTime", "15 min"),
                    url=f"/courses/{l.get('subjectSlug')}/{l.get('topicSlug')}/{l['slug']}"
                )
            )

        return SearchResponse(
            query=clean_query,
            total=len(results),
            results=results[:limit]
        )
