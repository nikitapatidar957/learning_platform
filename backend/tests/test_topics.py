def test_get_topics_for_subject(client):
    response = client.get("/api/subjects/dsa/topics")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    slugs = [t["slug"] for t in data]
    assert "arrays" in slugs


def test_get_topic_by_slug(client):
    response = client.get("/api/topics/arrays")
    assert response.status_code == 200
    data = response.json()
    assert data["slug"] == "arrays"
    assert "lessons" in data
    assert len(data["lessons"]) > 0


def test_get_topic_not_found(client):
    response = client.get("/api/topics/non-existent-topic")
    assert response.status_code == 404
