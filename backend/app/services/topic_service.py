from typing import List, Optional
from pymongo import ASCENDING
from pymongo.database import Database
from app.database.mongodb import get_db
from app.schemas.topic import TopicResponse, TopicDetailResponse


class TopicService:
    def __init__(self, db: Database = None):
        self.db = db or get_db()

    def get_topics_by_subject(self, subject_slug: str) -> List[TopicResponse]:
        topics_cursor = self.db.topics.find(
            {"subjectSlug": subject_slug, "isPublished": True}
        ).sort("order", ASCENDING)

        results = []
        for t in topics_cursor:
            lesson_count = self.db.lessons.count_documents(
                {"topicSlug": t["slug"], "isPublished": True}
            )
            results.append(
                TopicResponse(
                    id=str(t["_id"]),
                    subjectId=str(t.get("subjectId", "")),
                    subjectSlug=t["subjectSlug"],
                    title=t["title"],
                    slug=t["slug"],
                    description=t.get("description", ""),
                    order=t.get("order", 0),
                    isPublished=t.get("isPublished", True),
                    lesson_count=lesson_count,
                    createdAt=t.get("createdAt"),
                    updatedAt=t.get("updatedAt"),
                )
            )
        return results

    def get_topic_by_slug(self, slug: str) -> Optional[TopicDetailResponse]:
        t = self.db.topics.find_one({"slug": slug, "isPublished": True})
        if not t:
            return None

        lessons_cursor = self.db.lessons.find(
            {"topicSlug": slug, "isPublished": True},
            {"content": 0}
        ).sort("order", ASCENDING)

        lessons = []
        for l in lessons_cursor:
            lessons.append({
                "id": str(l["_id"]),
                "title": l["title"],
                "slug": l["slug"],
                "description": l.get("description", ""),
                "estimatedTime": l.get("estimatedTime", "15 min"),
                "difficulty": l.get("difficulty", "Beginner"),
                "order": l.get("order", 0),
                "interactiveType": l.get("interactiveType"),
            })

        return TopicDetailResponse(
            id=str(t["_id"]),
            subjectId=str(t.get("subjectId", "")),
            subjectSlug=t["subjectSlug"],
            title=t["title"],
            slug=t["slug"],
            description=t.get("description", ""),
            order=t.get("order", 0),
            isPublished=t.get("isPublished", True),
            lesson_count=len(lessons),
            lessons=lessons,
            createdAt=t.get("createdAt"),
            updatedAt=t.get("updatedAt"),
        )
