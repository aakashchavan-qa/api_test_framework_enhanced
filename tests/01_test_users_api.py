import pytest
from utils.api_helpers import get_users, get_single_user, create_user, login_and_get_token
from jsonschema import validate
from schemas.user_list_schema import user_list_schema

# ✅ Positive Test: Get users list
def test_get_users_success():
    response = get_users()
    assert response.status_code == 200
    json_data = response.json()
    assert "data" in json_data and isinstance(json_data["data"], list)
    assert len(json_data["data"]) > 0
    for user in json_data["data"]:
        assert "id" in user and isinstance(user["id"], int)
        assert "email" in user and "@" in user["email"]

    response = get_users()
    validate(instance=response.json(), schema=user_list_schema)

# ✅ Data-Driven Test for multiple user IDs
@pytest.mark.parametrize("user_id", [1, 2, 3, 10])
def test_user_exists(user_id):
    response = get_single_user(user_id)
    assert response.status_code == 200
    assert "data" in response.json()

# 🔁 Retry Test
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_create_user_retry():
    token = login_and_get_token()
    response = create_user({"name": "RetryUser", "job": "QA"}, token)
    assert response.status_code == 201