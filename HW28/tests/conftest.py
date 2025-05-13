import pytest

from HW28.api.auth_requests import get_token
from HW28.test_data.auth_data import auth_payload_valid, auth_payload_invalid
from HW28.test_data.booking_data import create_booking_payload


@pytest.fixture
def get_token_valid_response():
    return get_token(auth_payload_valid)


@pytest.fixture
def get_auth_token_valid(get_token_valid_response):
    return get_token_valid_response.json().get("token")


@pytest.fixture
def get_token_invalid_response():
    return get_token(auth_payload_invalid)


@pytest.fixture
def get_auth_token_invalid(get_token_invalid_response):
    return get_token_invalid_response.json().get("token")


@pytest.fixture
def create_booking_valid_response():
    return get_token(create_booking_payload)


@pytest.fixture
def create_booking(create_booking_valid_response):
    booking_id = create_booking_valid_response.json().get("bookingid")
    return booking_id
