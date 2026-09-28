import os
import sys

backend_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, backend_root)

from scripts.seed_data.genai_llm_agentic_data import ADVANCED_LESSONS

for les in ADVANCED_LESSONS:
    subj = les["subjectSlug"]
    slug = les["slug"]
    path = os.path.join(backend_root, "..", "content", subj, f"{slug}.md")
    path = os.path.abspath(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {les['title']}\n\n")
        f.write(f"{les['description']}\n\n---\n\n")
        for sec in les["content"]["sections"]:
            if sec.get("title"):
                f.write(f"## {sec['title']}\n\n")
            if sec.get("content"):
                f.write(f"{sec['content']}\n\n")
            if sec.get("code"):
                lang = sec.get("language", "python")
                code_text = sec["code"]
                f.write(f"```{lang}\n{code_text}\n```\n\n")
    print(f"Generated {path} ({os.path.getsize(path)} bytes)")
