import json

import pytest
from utils.api_helpers import load_user_data_from_csv, transform_flat_to_nested


@pytest.mark.parametrize("user_data", load_user_data_from_csv("../data/users.csv"))
def test_create_user_from_flat_csv(playwright, user_data):
    request_context = playwright.request.new_context()

    # Convert flat row into nested JSON
    nested_payload = transform_flat_to_nested(user_data)
    print(nested_payload)
    response = request_context.post(
        "https://jsonplaceholder.typicode.com/users",
        json=nested_payload
    )

    assert response.status == 201
    print(json.dumps(response.json(), indent=2))

    request_context.dispose()
