from app.core.auth import upsert_user


def test_upsert_user(mock_db):
    user1 = upsert_user(
        clerk_user_id="user_clerk_test_abc",
        email="test@example.com",
        name="Test Learner"
    )
    assert user1.clerk_user_id == "user_clerk_test_abc"
    assert user1.email == "test@example.com"
    assert user1.name == "Test Learner"
    assert user1.subscription_status == "free"

    # Upsert again with the same clerk_user_id
    user2 = upsert_user(
        clerk_user_id="user_clerk_test_abc",
        name="Test Learner Updated"
    )
    assert user2.id == user1.id

    # Verify no duplicate records exist in the users collection
    count = mock_db.users.count_documents({"clerk_user_id": "user_clerk_test_abc"})
    assert count == 1


def test_auth_sync_endpoint(client, mock_db):
    response = client.post(
        "/api/auth/sync",
        json={
            "clerk_user_id": "user_sync_test_999",
            "email": "syncuser@example.com",
            "name": "Sync User",
            "profile_image": "https://img.clerk.com/test.png"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["clerk_user_id"] == "user_sync_test_999"
    assert data["email"] == "syncuser@example.com"
    assert data["name"] == "Sync User"
    assert "_id" in data
    assert data["_id"] != ""

    # Verify user exists in mock_db
    saved = mock_db.users.find_one({"clerk_user_id": "user_sync_test_999"})
    assert saved is not None
    assert str(saved["_id"]) == data["_id"]

