from HW25.pages.login_page import LoginPage
from HW25.pages.inventory_page import InventoryPage
from HW25.pages.cart_page import CartPage
from HW25.test_data.creds import UserCredentials
import pytest


@pytest.mark.smoke
def test_saucedemo_add_and_remove(driver):
    LoginPage(driver).login(UserCredentials.standart_user, UserCredentials.standart_password)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_item_name() == "Sauce Labs Bolt T-Shirt"
    cart.remove_item()
