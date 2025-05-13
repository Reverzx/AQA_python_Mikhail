from loguru import logger
from HW28.api.booking_requests import get_booking, delete_booking, create_booking_invalid_payload


def test_delete_booking_negative(get_auth_token_valid):
    invalid_booking_id = "invalid_id"
    response = delete_booking(invalid_booking_id, get_auth_token_valid)
    assert response.status_code in [404, 405], f"Unexpected status code: {response.status_code}"
    logger.info(f"Status code: {response.status_code}")


def test_create_booking_negative_payload():
    response = create_booking_invalid_payload()
    assert response.status_code == 500, f"Expected 500, got {response.status_code}"
    logger.info(f"Status code: {response.status_code}")


def test_get_booking_negative():
    invalid_booking_id = "invalid_id"
    response = get_booking(invalid_booking_id)
    assert response.status_code == 404
    logger.info(f"Status code: {response.status_code}")