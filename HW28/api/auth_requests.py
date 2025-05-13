import requests
from HW28.test_data.env import url


def get_token(auth_payload_valid):
    response = requests.post(f"{url}/auth", json=auth_payload_valid)
    assert response.status_code == 200, (f"Expected to have status code 200, "
                                         f"got {response.status_code}")
    return response


def not_get_token(auth_payload_invalid):
    response = requests.post(f"{url}/auth", json=auth_payload_invalid)
    return response
