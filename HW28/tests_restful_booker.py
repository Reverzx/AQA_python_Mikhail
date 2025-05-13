import requests
import pytest
from jsonschema import validate
from loguru import logger

url = "https://restful-booker.herokuapp.com"

schema = {
    "type": "object",
    "properties": {
        "firstname": {"type": "string"},
        "lastname": {"type": "string"},
        "totalprice": {"type": "integer"},
        "depositpaid": {"type": "boolean"},
        "bookingdates": {
            "type": "object",
            "properties": {
                "checkin": {"type": "string"},
                "checkout": {"type": "string"},
            },
            "required": ["checkin", "checkout"]
        },
        "additionalneeds": {"type": "string"}
    },
    "required": ["firstname", "lastname", "totalprice", "depositpaid",
                 "bookingdates", "additionalneeds"]
}


@pytest.fixture
def get_auth_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{url}/auth", json=payload)
    assert response.status_code == 200, (f"Expected to have status code 200, "
                                         f"got {response.status_code}")
    return response.json().get("token")


@pytest.fixture
def create_booking():
    payload = {
        "firstname": "Misha",
        "lastname": "Zakhodin",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(f"{url}/booking", json=payload)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    return booking_id


def test_login_positive(get_auth_token):
    assert get_auth_token is not None
    logger.info(f"The auth token: {get_auth_token}")


def test_get_booking_positive(create_booking):
    response = requests.get(f"{url}/booking/{create_booking}")
    assert response.status_code == 200
    try:
        validate(response.json(), schema)
        logger.info("JSON response matches the schema")
    except Exception as e:
        logger.error("JSON response does not match schema:", e)


def test_delete_booking_negative(get_auth_token):
    headers = {"Cookie": f"token={get_auth_token}"}
    invalid_booking_id = "invalid_id"
    response = requests.delete(f"{url}/booking/{invalid_booking_id}", headers=headers)
    assert response.status_code in [404, 405]
    logger.info(f"Status code: {response.status_code}")


def test_create_booking_negative_payload():
    response = requests.post(f"{url}/booking", json={"invalid": "data"})
    assert response.status_code == 500
    logger.info(f"Status code: {response.status_code}")


def test_get_booking_negative():
    invalid_booking_id = "invalid_id"
    response = requests.get(f"{url}/booking/{invalid_booking_id}")
    assert response.status_code == 404
    logger.info(f"Status code: {response.status_code}")
