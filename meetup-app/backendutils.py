import requests
from uuid import uuid4

def fetch_random_users(count: int):
    url = f"https://randomuser.me/api/?results={count}"
    res = requests.get(url).json()
    users = []

    for item in res["results"]:
        users.append({
            "uid": str(uuid4()),
            "email": item["email"],
            "first_name": item["name"]["first"],
            "last_name": item["name"]["last"],
            "gender": item["gender"],
            "latitude": float(item["location"]["coordinates"]["latitude"]),
            "longitude": float(item["location"]["coordinates"]["longitude"]),
        })

    return users
