from jsonschema import validate
from loguru import logger
from HW28.api.booking_requests import delete_booking, create_booking
from HW28.api.booking_requests import get_booking
from HW28.schemas.booking_schema import schema
from HW28.test_data.booking_data import (create_booking_payload_negative, invalid_booking_id)


def test_get_booking_positive(create_booking_id):
    # Проверяем ответ
    get_resp = get_booking(create_booking_id)
    assert get_resp.status_code == 200
    validate(instance=get_resp.json(), schema=schema)
    logger.info("JSON response matches the schema")


def test_get_booking_negative():
    # Проверяем ответ с невалидным айди
    get_resp = get_booking(invalid_booking_id)
    assert get_resp.status_code == 404
    logger.info(f"Status code: {get_resp.status_code}")


def test_create_booking_negative_payload():
    # Проверяем ответ с невалидным телом АПИ
    response = create_booking(create_booking_payload_negative)
    assert response.status_code == 500, f"Expected 500, got {response.status_code}"
    logger.info(f"Status code: {response.status_code}")


def test_delete_booking_positive(auth_token_valid, create_booking_id):
    # Удаляем бронирование
    response = delete_booking(create_booking_id, auth_token_valid)
    assert response.status_code == 201, f"Unexpected status code: {response.status_code}"
    logger.info(f"Status code: {response.status_code}")


def test_delete_booking_negative(auth_token_valid):
    # Проверяем удаление с негативным айди
    response = delete_booking(invalid_booking_id, auth_token_valid)
    assert response.status_code in [404, 405], f"Unexpected status code: {response.status_code}"
    logger.info(f"Status code: {response.status_code}")
