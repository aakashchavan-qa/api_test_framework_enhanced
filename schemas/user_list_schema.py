user_list_schema = {
    "type": "object",
    "properties": {
        "page": {"type": "number"},
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "email": {"type": "string"},
                    "first_name": {"type": "string"},
                    "last_name": {"type": "string"}
                },
                "required": ["id", "email"]
            }
        }
    },
    "required": ["data"]
}
