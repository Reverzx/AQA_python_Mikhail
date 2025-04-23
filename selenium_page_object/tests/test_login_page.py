from selenium_page_object.pages.login_page import LoginPage
from selenium_page_object.test_data.creds import UserCredentials
from selenium_page_object.test_data.env import Env

import pytest


@pytest.mark.login
@pytest.mark.smoke
def test_login_w_right_creds(driver):
    lp = LoginPage(driver, Env.URL)
    lp.open()
    lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    assert lp.is_login_successful()


@pytest.mark.smoke
@pytest.mark.add_item
def test_add_item_to_bucket(driver):
    lp = LoginPage(driver, Env.URL)
    lp.open()
    plp = lp.complete_login(UserCredentials.standart_user, UserCredentials.standart_password)
    assert lp.is_login_successful()

