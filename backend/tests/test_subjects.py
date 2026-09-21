def test_get_subjects(client):
    response = client.get("/api/subjects")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 8
    # Check DSA exists
    slugs = [s["slug"] for s in data]
    assert "dsa" in slugs
    assert "machine-learning" in slugs
    assert "deep-learning" in slugs
    assert "sql" in slugs
    assert "mongodb" in slugs
    assert "llm" in slugs
    assert "generative-ai" in slugs
    assert "agentic-ai" in slugs


def test_get_subject_by_slug(client):
    response = client.get("/api/subjects/dsa")
    assert response.status_code == 200
    data = response.json()
    assert data["slug"] == "dsa"
    assert data["name"] == "Data Structures & Algorithms"
    assert "topics" in data
    assert len(data["topics"]) > 0


def test_get_subject_not_found(client):
    response = client.get("/api/subjects/non-existent-subject")
    assert response.status_code == 404
