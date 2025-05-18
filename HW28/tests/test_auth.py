from loguru import logger
from HW28.test_data.auth_data import auth_payload_valid, auth_payload_invalid
from HW28.api.auth_requests import get_token


def test_login_positive():
    token = get_token(auth_payload_valid)
    assert token is not None
    logger.info(f"The auth token: {token}")


def test_login_negative():
    token = get_token(auth_payload_invalid)
    assert token is None
    logger.info(f"The auth token none: {token}")
