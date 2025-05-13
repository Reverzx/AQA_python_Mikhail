from loguru import logger


def test_login_positive(get_auth_token_valid):
    assert get_auth_token_valid is not None
    logger.info(f"The auth token: {get_auth_token_valid}")


def test_login_negative(get_auth_token_invalid):
    assert get_auth_token_invalid is None
    logger.info(f"The auth token none: {get_auth_token_invalid}")
