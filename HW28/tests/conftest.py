import pytest
from HW28.api.auth_requests import get_token
from HW28.api.booking_requests import create_booking
from HW28.test_data.auth_data import auth_payload_valid, auth_payload_invalid
from HW28.test_data.booking_data import create_booking_payload
import requests
from HW28.test_data.env import url


@pytest.fixture
def auth_token_valid():
    # Dозвращает валидный токен
    return get_token(auth_payload_valid)


@pytest.fixture
def create_booking_id():
    # Создает бронь и возвращает ее айди
    response = create_booking(create_booking_payload)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")
    return booking_id
