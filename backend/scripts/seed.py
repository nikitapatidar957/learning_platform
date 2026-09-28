#!/usr/bin/env python3
"""
Database Seed & Migration Script for the Learning Platform.
Idempotent script to create indexes and populate subjects, topics, and lessons
incorporating all notes from the python_interview collection.
"""
import sys
import os
from datetime import datetime, timezone

# Ensure backend root is on sys.path
backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if backend_root not in sys.path:
    sys.path.insert(0, backend_root)

from dotenv import load_dotenv
load_dotenv(os.path.join(backend_root, ".env"))
load_dotenv(os.path.join(backend_root, "..", ".env"))

from app.core.config import settings
from app.database.mongodb import db_manager
from scripts.seed_data import ALL_SUBJECTS, ALL_TOPICS, ALL_LESSONS


def seed_database():
    host_display = settings.MONGODB_URI.split("@")[-1] if "@" in settings.MONGODB_URI else settings.MONGODB_URI
    print(f"Connecting to MongoDB at: {host_display}")
    
    db = db_manager.connect()
    db_manager.create_indexes()
    now = datetime.now(timezone.utc).isoformat()

    # =========================================================================
    # 1. SEED SUBJECTS
    # =========================================================================
    print(f"\n--- Seeding {len(ALL_SUBJECTS)} Subjects ---")
    subject_id_map = {}
    for sub in ALL_SUBJECTS:
        res = db.subjects.find_one_and_update(
            {"slug": sub["slug"]},
            {
                "$set": {
                    **sub,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        subject_id_map[sub["slug"]] = res["_id"]
        print(f"  ✓ Subject: {sub['name']} ({sub['slug']})")

    # =========================================================================
    # 2. SEED TOPICS
    # =========================================================================
    print(f"\n--- Seeding {len(ALL_TOPICS)} Topics ---")
    topic_id_map = {}
    for top in ALL_TOPICS:
        subj_id = subject_id_map.get(top["subjectSlug"])
        if not subj_id:
            print(f"  ⚠️ Skipping topic '{top['slug']}': Subject '{top['subjectSlug']}' not found in map.")
            continue

        res = db.topics.find_one_and_update(
            {"slug": top["slug"]},
            {
                "$set": {
                    **top,
                    "subjectId": subj_id,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        topic_id_map[top["slug"]] = res["_id"]
        print(f"  ✓ Topic: {top['title']} ({top['slug']}) under [{top['subjectSlug']}]")

    # =========================================================================
    # 3. SEED LESSONS
    # =========================================================================
    print(f"\n--- Seeding {len(ALL_LESSONS)} Lessons ---")
    seeded_count = 0
    for les in ALL_LESSONS:
        top_id = topic_id_map.get(les["topicSlug"])
        if not top_id:
            print(f"  ⚠️ Skipping lesson '{les['slug']}': Topic '{les['topicSlug']}' not found in map.")
            continue

        db.lessons.find_one_and_update(
            {"slug": les["slug"]},
            {
                "$set": {
                    **les,
                    "topicId": top_id,
                    "updatedAt": now,
                },
                "$setOnInsert": {"createdAt": now}
            },
            upsert=True,
            return_document=True
        )
        seeded_count += 1
        print(f"  ✓ Lesson: {les['title']} ({les['slug']}) [Interactive: {les.get('interactiveType')}]")

    print("\n" + "=" * 65)
    print(f"Successfully seeded:")
    print(f"  • {len(ALL_SUBJECTS)} Subjects")
    print(f"  • {len(ALL_TOPICS)} Topics")
    print(f"  • {seeded_count} Lessons")
    print(f"Target Database: '{db.name}' on {db_manager.connection_type.upper()}")
    print("=" * 65)


if __name__ == "__main__":
    seed_database()
