import json

import pytest

def test_get_users_success(playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")

    assert response.status == 200
    headers = response.headers
    print("\nHEADERS: ", json.dumps(headers, indent=2))
    assert headers["content-type"] == "application/json; charset=utf-8"
    data = response.json()
    print("\nResponse Data:")
    print(json.dumps(data, indent=2))  # Pretty prints JSON with new lines and indentation
    assert data["id"] == 1
    assert "name" in data
    assert isinstance(data["name"], str)

    request_context.dispose()
