def test_search_content(client):
    response = client.get("/api/search?q=array")
    assert response.status_code == 200
    data = response.json()
    assert "query" in data
    assert data["query"] == "array"
    assert data["total"] > 0
    assert len(data["results"]) > 0


def test_search_empty_query(client):
    response = client.get("/api/search?q=")
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 0
    assert len(data["results"]) == 0
