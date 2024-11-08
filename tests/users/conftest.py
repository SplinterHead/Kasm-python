import json

from pytest import fixture


@fixture
def user_object():
    return json.dumps(
        {
            "users": [
                {
                    "kasms": [],
                    "company": {},
                    "username": "user@kasm.local",
                    "locked": False,
                    "realm": "local",
                    "phone": None,
                    "first_name": None,
                    "notes": None,
                    "user_id": "57e8fc1a-fa86-4ff4-9474-60d9831f42d5",
                    "last_session": "2020-11-12 14:29:25.808258",
                    "groups": [
                        {
                            "name": "All Users",
                            "group_id": "68d557ac4cac42cca9f31c7c853de0f3",
                        }
                    ],
                    "disabled": True,
                    "organization": None,
                    "last_name": None,
                },
                {
                    "kasms": [],
                    "company": {},
                    "username": "admin@kasm.local",
                    "locked": False,
                    "realm": "local",
                    "phone": None,
                    "first_name": None,
                    "notes": None,
                    "user_id": "4acb13bf-1215-4972-9f0d-8c537d17f2da",
                    "last_session": "2020-11-12 14:35:19.700863",
                    "groups": [
                        {
                            "name": "All Users",
                            "group_id": "68d557ac4cac42cca9f31c7c853de0f3",
                        },
                        {
                            "name": "Administrators",
                            "group_id": "31aa063c670648589533d3c42092d02a",
                        },
                    ],
                    "disabled": False,
                    "organization": None,
                    "last_name": None,
                },
            ]
        }
    )
