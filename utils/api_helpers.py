import requests
import os
from dotenv import load_dotenv
import csv

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

def get_users(page=1):
    return requests.get(f"{BASE_URL}/api/users?page={page}")

def get_single_user(user_id):
    return requests.get(f"{BASE_URL}/api/users/{user_id}")

def create_user(payload, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.post(f"{BASE_URL}/api/users", json=payload, headers=headers)

def login_and_get_token():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = requests.post(f"{BASE_URL}/api/login", json=payload)
    response.raise_for_status()
    return response.json()["token"]


def load_user_data_from_csv(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def transform_flat_to_nested(data):
    return {
        "id": int(data["id"]),
        "name": data["name"],
        "username": data["username"],
        "email": data["email"],
        "address": {
            "street": data["address_street"],
            "suite": data["address_suite"],
            "city": data["address_city"],
            "zipcode": data["address_zipcode"],
            "geo": {
                "lat": data["address_geo_lat"],
                "lng": data["address_geo_lng"]
            }
        },
        "phone": data["phone"],
        "website": data["website"],
        "company": {
            "name": data["company_name"],
            "catchPhrase": data["company_catchPhrase"],
            "bs": data["company_bs"]
        }
    }
