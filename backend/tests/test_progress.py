def test_progress_unauthorized(client):
    response = client.get("/api/progress")
    assert response.status_code == 401


def test_progress_get_and_update(client, auth_headers):
    # 1. Start lesson
    update_res = client.post(
        "/api/progress/what-is-an-array",
        json={"status": "in_progress", "progress_percentage": 50},
        headers=auth_headers
    )
    assert update_res.status_code == 200
    prog_data = update_res.json()
    assert prog_data["status"] == "in_progress"
    assert prog_data["progress_percentage"] == 50

    # 2. Get lesson progress
    get_res = client.get("/api/progress/what-is-an-array", headers=auth_headers)
    assert get_res.status_code == 200
    assert get_res.json()["status"] == "in_progress"

    # 3. Mark completed
    patch_res = client.patch(
        "/api/progress/what-is-an-array",
        json={"status": "completed", "progress_percentage": 100},
        headers=auth_headers
    )
    assert patch_res.status_code == 200
    assert patch_res.json()["status"] == "completed"
    assert patch_res.json()["progress_percentage"] == 100

    # 4. Check overall dashboard stats
    overall_res = client.get("/api/progress", headers=auth_headers)
    assert overall_res.status_code == 200
    overall = overall_res.json()
    assert overall["total_completed"] >= 1
    assert overall["overall_percentage"] > 0
