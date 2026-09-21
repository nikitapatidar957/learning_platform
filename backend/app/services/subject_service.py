from typing import List, Optional, Dict
from bson import ObjectId
from pymongo import ASCENDING
from pymongo.database import Database
from app.database.mongodb import get_db
from app.schemas.subject import SubjectSummaryResponse, SubjectDetailResponse


class SubjectService:
    def __init__(self, db: Database = None):
        self.db = db or get_db()

    def list_subjects(self, published_only: bool = True) -> List[SubjectSummaryResponse]:
        query = {"isPublished": True} if published_only else {}
        subjects_cursor = self.db.subjects.find(query).sort("order", ASCENDING)
        
        results = []
        for s in subjects_cursor:
            s_id = str(s["_id"])
            s_slug = s["slug"]
            
            # Count topics and lessons
            topic_count = self.db.topics.count_documents({"subjectSlug": s_slug, "isPublished": True})
            lesson_count = self.db.lessons.count_documents({"subjectSlug": s_slug, "isPublished": True})
            
            results.append(
                SubjectSummaryResponse(
                    id=s_id,
                    name=s["name"],
                    slug=s_slug,
                    description=s.get("description", ""),
                    icon=s.get("icon", "BookOpen"),
                    order=s.get("order", 0),
                    difficulty=s.get("difficulty", "Beginner to Advanced"),
                    isPublished=s.get("isPublished", True),
                    topic_count=topic_count,
                    lesson_count=lesson_count,
                    estimated_hours=s.get("estimated_hours", f"{max(5, topic_count * 2)}+ hrs"),
                    createdAt=s.get("createdAt"),
                    updatedAt=s.get("updatedAt"),
                )
            )
        return results

    def get_subject_by_slug(self, slug: str, user_id: Optional[str] = None) -> Optional[SubjectDetailResponse]:
        subject = self.db.subjects.find_one({"slug": slug, "isPublished": True})
        if not subject:
            return None

        # Fetch topics for this subject
        topics_cursor = self.db.topics.find(
            {"subjectSlug": slug, "isPublished": True}
        ).sort("order", ASCENDING)

        topics_list = []
        total_lessons = 0

        # Load user progress if logged in
        completed_lessons = set()
        if user_id:
            user_progress = self.db.progress.find({"user_id": user_id, "subject_slug": slug})
            for p in user_progress:
                if p.get("status") == "completed":
                    completed_lessons.add(str(p.get("lesson_id")))

        for t in topics_cursor:
            t_id = str(t["_id"])
            t_slug = t["slug"]
            
            # Fetch lessons under this topic
            lessons_cursor = self.db.lessons.find(
                {"topicSlug": t_slug, "isPublished": True},
                {"content": 0}  # omit heavy content in topic overview
            ).sort("order", ASCENDING)
            
            lessons_data = []
            for l in lessons_cursor:
                l_id = str(l["_id"])
                total_lessons += 1
                l_status = "completed" if l_id in completed_lessons else "not_started"
                lessons_data.append({
                    "id": l_id,
                    "title": l["title"],
                    "slug": l["slug"],
                    "description": l.get("description", ""),
                    "estimatedTime": l.get("estimatedTime", "15 min"),
                    "difficulty": l.get("difficulty", "Beginner"),
                    "order": l.get("order", 0),
                    "interactiveType": l.get("interactiveType"),
                    "status": l_status,
                })

            topics_list.append({
                "id": t_id,
                "title": t["title"],
                "slug": t_slug,
                "description": t.get("description", ""),
                "order": t.get("order", 0),
                "lesson_count": len(lessons_data),
                "lessons": lessons_data,
            })

        return SubjectDetailResponse(
            id=str(subject["_id"]),
            name=subject["name"],
            slug=subject["slug"],
            description=subject.get("description", ""),
            icon=subject.get("icon", "BookOpen"),
            order=subject.get("order", 0),
            difficulty=subject.get("difficulty", "Beginner to Advanced"),
            isPublished=subject.get("isPublished", True),
            topic_count=len(topics_list),
            lesson_count=total_lessons,
            topics=topics_list,
            createdAt=subject.get("createdAt"),
            updatedAt=subject.get("updatedAt"),
        )
