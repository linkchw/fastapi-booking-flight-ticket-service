def test_create_user(client):
    data = {
        "username": "testuser",
        "password": "securepassword123",
        "name": "Test User",
        "phone_number": "1234567890",
    }
    response = client.post("/", json=data)

    assert response.status_code == 201
    response_data = response.json()
    assert response_data["username"] == data["username"]
    assert response_data["name"] == data["name"]
    assert response_data["phone_number"] == data["phone_number"]
    assert "password" not in response_data
