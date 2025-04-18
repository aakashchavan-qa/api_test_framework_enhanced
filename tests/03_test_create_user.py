import pytest
import json

def test_create_users_success(playwright):
    request_context = playwright.request.new_context()

    payload = {
        "name": "John Doe",
        "username": "johndoe",
        "email": "john.doe@example.com"
    }

    response = request_context.post(
        "https://jsonplaceholder.typicode.com/users",
        data=payload
    )

    assert response.status == 201

    data = response.json()
    print("\nCreated User Response:")
    print(json.dumps(data, indent=2))

    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]
    assert "id" in data

    request_context.dispose()
