import os
import re
from pathlib import Path
from typing import List, Optional, Dict, Any
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

class ContentSaveRequest(BaseModel):
    content: str

class ContentCreateRequest(BaseModel):
    fileSlug: str
    content: str
    title: Optional[str] = None

router = APIRouter(prefix="/api/content", tags=["Content"])

CONTENT_ROOT = Path(__file__).resolve().parents[3] / "content"

SUBJECT_TITLES: Dict[str, str] = {
    "python": "Python & Data Engineering",
    "git": "Git & Version Control",
    "aws": "AWS & Cloud Computing",
    "dsa": "Data Structures & Algorithms",
    "machine-learning": "Machine Learning",
    "sql": "SQL & Relational Databases",
    "mongodb": "MongoDB & NoSQL",
    "llm": "Large Language Models",
    "generative-ai": "Generative AI & RAG",
    "agentic-ai": "Agentic AI",
    "deep-learning": "Deep Learning",
    "statistics": "Statistics & Probability",
    "nlp": "Natural Language Processing",
    "deployment": "Model Deployment & MLOps",
}

SUBJECT_ORDER: List[str] = [
    "python",
    "statistics",
    "git",
    "aws",
    "dsa",
    "machine-learning",
    "sql",
    "mongodb",
    "llm",
    "generative-ai",
    "agentic-ai",
    "deep-learning",
    "nlp",
    "deployment",
]



def _format_title_from_slug(slug: str) -> str:
    words = slug.replace("-", " ").replace("_", " ").split()
    capitalized = []
    acronyms = {
        "ai", "ml", "dl", "dsa", "sql", "aws", "rag", "llm", "gil", "oop",
        "crud", "bcnf", "1nf", "2nf", "3nf", "io", "api", "cte", "mae", "mse",
        "rmse", "dag", "vcs", "ec2", "s3", "iam", "vpc", "nlp", "ner", "pos",
        "bow", "tfidf", "bert", "rnn", "lstm", "gru", "cnn", "ann", "eda", "cicd", "wsgi"
    }
    for w in words:
        if w.lower() in acronyms:
            capitalized.append(w.upper())
        else:
            capitalized.append(w.capitalize())
    return " ".join(capitalized)


def _extract_headings(markdown_text: str) -> List[Dict[str, Any]]:
    headings = []
    lines = markdown_text.splitlines()
    for line in lines:
        match = re.match(r"^(#{1,4})\s+(.+)$", line.strip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            # Clean formatting characters
            clean_title = re.sub(r"[*_`]", "", title)
            slug = re.sub(r"[^a-zA-Z0-9]+", "-", clean_title.lower()).strip("-")
            headings.append({
                "level": level,
                "title": clean_title,
                "slug": slug
            })
    return headings


@router.get("/tree")
def get_content_tree():
    """
    Returns hierarchical listing of all verbatim content files organized by subject and topic.
    """
    if not CONTENT_ROOT.exists():
        raise HTTPException(status_code=404, detail="Content directory not found")

    subjects_data = []

    for subject_slug in SUBJECT_ORDER:
        subject_dir = CONTENT_ROOT / subject_slug
        if not subject_dir.exists() or not subject_dir.is_dir():
            continue

        files_info = []
        for file_path in sorted(subject_dir.glob("*.md")):
            file_slug = file_path.stem
            size_bytes = file_path.stat().st_size
            title = _format_title_from_slug(file_slug)
            
            # Read first line to see if it has an H1 title
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    first_lines = [f.readline().strip() for _ in range(5)]
                for line in first_lines:
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
            except Exception:
                pass

            files_info.append({
                "slug": file_slug,
                "title": title,
                "subjectSlug": subject_slug,
                "sizeBytes": size_bytes,
                "estimatedReadTime": f"{max(5, round(size_bytes / 2500))} mins",
            })

        subjects_data.append({
            "subjectSlug": subject_slug,
            "subjectName": SUBJECT_TITLES.get(subject_slug, _format_title_from_slug(subject_slug)),
            "files": files_info,
        })

    return subjects_data


@router.get("/file/{subject_slug}/{file_slug}")
def get_content_file(subject_slug: str, file_slug: str):
    """
    Returns the verbatim markdown content of a specific note file with extracted navigation headings.
    """
    target_file = CONTENT_ROOT / subject_slug / f"{file_slug}.md"
    if not target_file.exists():
        raise HTTPException(status_code=404, detail=f"Content file {subject_slug}/{file_slug} not found")

    try:
        with open(target_file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to read content: {str(e)}")

    headings = _extract_headings(content)
    title = _format_title_from_slug(file_slug)
    if headings and headings[0]["level"] == 1:
        title = headings[0]["title"]

    return {
        "subjectSlug": subject_slug,
        "subjectName": SUBJECT_TITLES.get(subject_slug, _format_title_from_slug(subject_slug)),
        "fileSlug": file_slug,
        "title": title,
        "sizeBytes": len(content.encode("utf-8")),
        "headings": headings,
        "content": content,
    }


@router.put("/file/{subject_slug}/{file_slug}")
def save_content_file(subject_slug: str, file_slug: str, payload: ContentSaveRequest):
    """
    Save / update markdown content directly to its respective file under content/<subject_slug>/<file_slug>.md.
    """
    clean_subj = re.sub(r'[^a-zA-Z0-9_-]', '', subject_slug)
    clean_file = re.sub(r'[^a-zA-Z0-9_-]', '', file_slug)

    if not clean_subj or not clean_file:
        raise HTTPException(status_code=400, detail="Invalid subject or file slug")

    subject_dir = CONTENT_ROOT / clean_subj
    subject_dir.mkdir(parents=True, exist_ok=True)

    target_file = subject_dir / f"{clean_file}.md"
    try:
        target_file.write_text(payload.content, encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to write file: {str(e)}")

    headings = _extract_headings(payload.content)
    title = _format_title_from_slug(clean_file)
    if headings and headings[0]["level"] == 1:
        title = headings[0]["title"]

    return {
        "subjectSlug": clean_subj,
        "subjectName": SUBJECT_TITLES.get(clean_subj, _format_title_from_slug(clean_subj)),
        "fileSlug": clean_file,
        "title": title,
        "sizeBytes": len(payload.content.encode("utf-8")),
        "headings": headings,
        "content": payload.content,
        "message": f"Successfully saved to {clean_file}.md",
    }


@router.post("/file/{subject_slug}")
def create_content_file(subject_slug: str, payload: ContentCreateRequest):
    """
    Create a new markdown note file under content/<subject_slug>/<file_slug>.md.
    """
    clean_subj = re.sub(r'[^a-zA-Z0-9_-]', '', subject_slug)
    raw_slug = payload.fileSlug or payload.title or "new-note"
    clean_file = re.sub(r'[^a-zA-Z0-9_-]', '', raw_slug.lower().replace(" ", "-")).strip("-_")
    if not clean_file:
        clean_file = "custom-note"

    if not clean_subj:
        raise HTTPException(status_code=400, detail="Invalid subject slug")

    subject_dir = CONTENT_ROOT / clean_subj
    subject_dir.mkdir(parents=True, exist_ok=True)

    target_file = subject_dir / f"{clean_file}.md"
    
    file_content = payload.content
    if payload.title and not file_content.strip().startswith("#"):
        file_content = f"# {payload.title}\n\n{file_content}"

    try:
        target_file.write_text(file_content, encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create file: {str(e)}")

    headings = _extract_headings(file_content)
    title = payload.title or _format_title_from_slug(clean_file)
    if headings and headings[0]["level"] == 1:
        title = headings[0]["title"]

    return {
        "subjectSlug": clean_subj,
        "subjectName": SUBJECT_TITLES.get(clean_subj, _format_title_from_slug(clean_subj)),
        "fileSlug": clean_file,
        "title": title,
        "sizeBytes": len(file_content.encode("utf-8")),
        "headings": headings,
        "content": file_content,
        "message": f"Successfully created {clean_file}.md",
    }


@router.get("/search")
def search_content(q: str = Query(..., min_length=2)):
    """
    Full-text search across all verbatim content files for interview questions, concepts, and key terms.
    """
    query = q.strip().lower()
    results = []

    for subject_slug in SUBJECT_ORDER:
        subject_dir = CONTENT_ROOT / subject_slug
        if not subject_dir.exists():
            continue

        for file_path in sorted(subject_dir.glob("*.md")):
            file_slug = file_path.stem
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue

            lines = content.splitlines()
            matches = []
            for i, line in enumerate(lines):
                if query in line.lower():
                    # Get surrounding context
                    start = max(0, i - 1)
                    end = min(len(lines), i + 2)
                    context_snippet = "\n".join(lines[start:end]).strip()
                    matches.append({
                        "lineNumber": i + 1,
                        "line": line.strip(),
                        "snippet": context_snippet[:300]
                    })
                    if len(matches) >= 5:
                        break

            if matches:
                results.append({
                    "subjectSlug": subject_slug,
                    "subjectName": SUBJECT_TITLES.get(subject_slug, _format_title_from_slug(subject_slug)),
                    "fileSlug": file_slug,
                    "fileTitle": _format_title_from_slug(file_slug),
                    "matchCount": len(matches),
                    "matches": matches,
                })

    return {
        "query": q,
        "totalFilesMatched": len(results),
        "results": results,
    }
