from typing import List, Optional, Dict
from bson import ObjectId
from pymongo import ASCENDING
from pymongo.database import Database
from app.database.mongodb import get_db
from app.schemas.lesson import LessonSummaryResponse, LessonDetailResponse, LessonContent


class LessonService:
    def __init__(self, db: Database = None):
        self.db = db or get_db()

    def get_lessons_by_topic(self, topic_slug: str, user_id: Optional[str] = None) -> List[LessonSummaryResponse]:
        lessons_cursor = self.db.lessons.find(
            {"topicSlug": topic_slug, "isPublished": True}
        ).sort("order", ASCENDING)

        completed_set = set()
        if user_id:
            progress_docs = self.db.progress.find({"user_id": user_id, "topic_slug": topic_slug})
            for p in progress_docs:
                if p.get("status") == "completed":
                    completed_set.add(str(p.get("lesson_id")))

        results = []
        for l in lessons_cursor:
            l_id = str(l["_id"])
            status = "completed" if l_id in completed_set else "not_started"
            results.append(
                LessonSummaryResponse(
                    id=l_id,
                    topicId=str(l.get("topicId", "")),
                    topicSlug=l["topicSlug"],
                    subjectSlug=l["subjectSlug"],
                    title=l["title"],
                    slug=l["slug"],
                    description=l.get("description", ""),
                    estimatedTime=l.get("estimatedTime", "15 min"),
                    difficulty=l.get("difficulty", "Beginner"),
                    order=l.get("order", 0),
                    isPublished=l.get("isPublished", True),
                    interactiveType=l.get("interactiveType"),
                    status=status,
                )
            )
        return results

    def get_lesson_by_slug(self, slug: str, user_id: Optional[str] = None) -> Optional[LessonDetailResponse]:
        lesson = self.db.lessons.find_one({"slug": slug, "isPublished": True})
        if not lesson:
            return None

        lesson_id = str(lesson["_id"])
        topic_slug = lesson["topicSlug"]
        subject_slug = lesson["subjectSlug"]

        # Determine user progress state
        status = "not_started"
        if user_id:
            user_prog = self.db.progress.find_one({"user_id": user_id, "lesson_id": lesson_id})
            if user_prog:
                status = user_prog.get("status", "not_started")

        # Find previous and next lessons in the same topic or subject
        all_topic_lessons = list(
            self.db.lessons.find(
                {"topicSlug": topic_slug, "isPublished": True},
                {"slug": 1, "title": 1, "order": 1, "topicSlug": 1, "subjectSlug": 1}
            ).sort("order", ASCENDING)
        )

        prev_lesson = None
        next_lesson = None
        for idx, item in enumerate(all_topic_lessons):
            if item["slug"] == slug:
                if idx > 0:
                    p = all_topic_lessons[idx - 1]
                    prev_lesson = {"slug": p["slug"], "title": p["title"], "topicSlug": p["topicSlug"], "subjectSlug": p["subjectSlug"]}
                if idx < len(all_topic_lessons) - 1:
                    n = all_topic_lessons[idx + 1]
                    next_lesson = {"slug": n["slug"], "title": n["title"], "topicSlug": n["topicSlug"], "subjectSlug": n["subjectSlug"]}
                break

        content_dict = lesson.get("content", {})
        if isinstance(content_dict, dict) and "sections" in content_dict:
            parsed_content = LessonContent(sections=content_dict["sections"])
        else:
            parsed_content = LessonContent(sections=[])

        return LessonDetailResponse(
            id=lesson_id,
            topicId=str(lesson.get("topicId", "")),
            topicSlug=topic_slug,
            subjectSlug=subject_slug,
            title=lesson["title"],
            slug=lesson["slug"],
            description=lesson.get("description", ""),
            estimatedTime=lesson.get("estimatedTime", "15 min"),
            difficulty=lesson.get("difficulty", "Beginner"),
            order=lesson.get("order", 0),
            isPublished=lesson.get("isPublished", True),
            interactiveType=lesson.get("interactiveType"),
            status=status,
            content=parsed_content,
            previous_lesson=prev_lesson,
            next_lesson=next_lesson,
            createdAt=lesson.get("createdAt"),
            updatedAt=lesson.get("updatedAt"),
        )
