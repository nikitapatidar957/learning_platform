from datetime import datetime, timezone
from typing import Optional, List, Dict
from bson import ObjectId
from pymongo.database import Database
from app.database.mongodb import get_db
from app.schemas.progress import (
    ProgressResponse,
    OverallProgressResponse,
    SubjectProgressSummary,
)


class ProgressService:
    def __init__(self, db: Database = None):
        self.db = db or get_db()

    def get_lesson_progress(self, user_id: str, lesson_id: str) -> ProgressResponse:
        # Match by ObjectId, id string, or lesson slug
        prog = self.db.progress.find_one({
            "user_id": user_id,
            "$or": [{"lesson_id": lesson_id}, {"lesson_slug": lesson_id}]
        })
        if not prog:
            return ProgressResponse(
                id="",
                user_id=user_id,
                lesson_id=lesson_id,
                status="not_started",
                progress_percentage=0,
            )
        return ProgressResponse(
            id=str(prog["_id"]),
            user_id=prog["user_id"],
            lesson_id=prog["lesson_id"],
            lesson_slug=prog.get("lesson_slug"),
            subject_slug=prog.get("subject_slug"),
            topic_slug=prog.get("topic_slug"),
            status=prog.get("status", "not_started"),
            progress_percentage=prog.get("progress_percentage", 0),
            started_at=prog.get("started_at"),
            last_accessed_at=prog.get("last_accessed_at"),
            completed_at=prog.get("completed_at"),
        )

    def update_progress(
        self,
        user_id: str,
        lesson_id: str,
        status: str = "in_progress",
        progress_percentage: int = 50,
    ) -> ProgressResponse:
        now = datetime.now(timezone.utc).isoformat()
        
        if not lesson_id or lesson_id in ("undefined", "null"):
            raise ValueError("Invalid lesson identifier")

        # Look up lesson details to enrich progress record
        lesson_filter = {"_id": ObjectId(lesson_id)} if ObjectId.is_valid(lesson_id) else {"slug": lesson_id}
        lesson = self.db.lessons.find_one(lesson_filter)
        if not lesson:
            raise ValueError(f"Lesson '{lesson_id}' not found")
        
        lesson_id_str = str(lesson["_id"])
        lesson_slug = lesson["slug"]
        subject_slug = lesson.get("subjectSlug", "")
        topic_slug = lesson.get("topicSlug", "")

        existing = self.db.progress.find_one({
            "user_id": user_id,
            "$or": [{"lesson_id": lesson_id_str}, {"lesson_slug": lesson_slug}]
        })

        update_data = {
            "user_id": user_id,
            "lesson_id": lesson_id_str,
            "lesson_slug": lesson_slug,
            "subject_slug": subject_slug,
            "topic_slug": topic_slug,
            "status": status,
            "progress_percentage": progress_percentage,
            "last_accessed_at": now,
        }

        if status == "completed":
            update_data["completed_at"] = now
            update_data["progress_percentage"] = 100

        if not existing:
            update_data["started_at"] = now
            res = self.db.progress.insert_one(update_data)
            update_data["_id"] = str(res.inserted_id)
        else:
            self.db.progress.update_one(
                {"_id": existing["_id"]},
                {"$set": update_data}
            )
            update_data["_id"] = str(existing["_id"])
            update_data["started_at"] = existing.get("started_at", now)

        return ProgressResponse(
            id=update_data["_id"],
            user_id=user_id,
            lesson_id=lesson_id_str,
            lesson_slug=lesson_slug,
            subject_slug=subject_slug,
            topic_slug=topic_slug,
            status=status,
            progress_percentage=update_data["progress_percentage"],
            started_at=update_data.get("started_at"),
            last_accessed_at=now,
            completed_at=update_data.get("completed_at"),
        )

    def get_user_overall_progress(self, user_id: str) -> OverallProgressResponse:
        total_published_lessons = self.db.lessons.count_documents({"isPublished": True})

        user_progress_docs = list(self.db.progress.find({"user_id": user_id}))
        
        completed_count = sum(1 for p in user_progress_docs if p.get("status") == "completed")
        in_progress_count = sum(1 for p in user_progress_docs if p.get("status") == "in_progress")

        overall_percentage = int((completed_count / total_published_lessons * 100)) if total_published_lessons > 0 else 0

        # Calculate per-subject breakdown
        subjects = list(self.db.subjects.find({"isPublished": True}).sort("order", 1))
        subject_summaries: List[SubjectProgressSummary] = []

        completed_lesson_ids = {p["lesson_id"] for p in user_progress_docs if p.get("status") == "completed"}
        completed_lesson_slugs = {p.get("lesson_slug") for p in user_progress_docs if p.get("status") == "completed"}

        for s in subjects:
            s_slug = s["slug"]
            s_lessons = list(self.db.lessons.find({"subjectSlug": s_slug, "isPublished": True}, {"_id": 1, "slug": 1}))
            total_s_lessons = len(s_lessons)
            completed_s_lessons = sum(
                1 for l in s_lessons
                if str(l["_id"]) in completed_lesson_ids or l.get("slug") in completed_lesson_slugs
            )
            pct = int((completed_s_lessons / total_s_lessons * 100)) if total_s_lessons > 0 else 0
            
            subject_summaries.append(
                SubjectProgressSummary(
                    subject_slug=s_slug,
                    subject_name=s["name"],
                    completed_lessons=completed_s_lessons,
                    total_lessons=total_s_lessons,
                    percentage=pct
                )
            )

        # Recently viewed lessons
        recent_sorted = sorted(
            user_progress_docs,
            key=lambda x: x.get("last_accessed_at", ""),
            reverse=True
        )[:10]

        recently_viewed = []
        for r in recent_sorted:
            l_slug = r.get("lesson_slug")
            l_id = r.get("lesson_id")
            if not l_slug or l_slug in ("undefined", "null") or not l_id or l_id in ("undefined", "null"):
                continue

            l_filter = {"slug": l_slug} if l_slug else ({"_id": ObjectId(l_id)} if ObjectId.is_valid(l_id) else None)
            l_info = self.db.lessons.find_one(l_filter) if l_filter else None

            subject_slug = r.get("subject_slug") or (l_info.get("subjectSlug") if l_info else "")
            topic_slug = r.get("topic_slug") or (l_info.get("topicSlug") if l_info else "")
            title = (l_info.get("title") if l_info else None) or r.get("lesson_title") or l_slug

            # Only accept fully routable lessons with valid slugs
            if subject_slug and topic_slug and l_slug:
                recently_viewed.append({
                    "lesson_id": str(l_id),
                    "lesson_slug": l_slug,
                    "lesson_title": title,
                    "subject_slug": subject_slug,
                    "topic_slug": topic_slug,
                    "status": r.get("status", "in_progress"),
                    "progress_percentage": r.get("progress_percentage", 0),
                    "last_accessed_at": r.get("last_accessed_at"),
                })
                if len(recently_viewed) >= 5:
                    break

        current_lesson = recently_viewed[0] if recently_viewed else None

        return OverallProgressResponse(
            total_completed=completed_count,
            total_in_progress=in_progress_count,
            total_lessons=total_published_lessons,
            overall_percentage=overall_percentage,
            subjects_progress=subject_summaries,
            recently_viewed=recently_viewed,
            current_lesson=current_lesson,
        )
