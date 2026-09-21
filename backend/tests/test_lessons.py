def test_get_lessons_for_topic(client):
    response = client.get("/api/topics/arrays/lessons")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    slugs = [l["slug"] for l in data]
    assert "what-is-an-array" in slugs


def test_get_lesson_by_slug(client):
    response = client.get("/api/lessons/what-is-an-array")
    assert response.status_code == 200
    data = response.json()
    assert data["slug"] == "what-is-an-array"
    assert data["interactiveType"] == "ArrayVisualizer"
    assert "content" in data
    assert "sections" in data["content"]
    assert len(data["content"]["sections"]) > 0


def test_get_lesson_not_found(client):
    response = client.get("/api/lessons/unknown-lesson-slug")
    assert response.status_code == 404
