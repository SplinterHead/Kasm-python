import json

import requests


def get_users(url: str, auth: dict):
    api_url = f"{url}/api/public/get_users"
    res = requests.post(api_url, json=auth).json()
    return json.loads(res)
