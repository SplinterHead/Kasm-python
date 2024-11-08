import requests_mock
from pytest import fixture

from kasm_python.kasm import Kasm


@fixture
def kasm():
    return Kasm(
        url="https://localhost.com", api_key="abcd123", api_key_secret="abcdef12345678"
    )


def test_can_get_current_users(requests_mock, kasm, user_object):
    requests_mock.post("https://localhost.com/api/public/get_users", json=user_object)
    users = kasm.get_users()
    print(users)
    assert len(users["users"]) == 2
