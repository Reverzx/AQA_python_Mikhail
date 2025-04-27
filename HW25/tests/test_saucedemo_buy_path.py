from HW25.pages.login_page import LoginPage
from HW25.pages.inventory_page import InventoryPage
from HW25.pages.cart_page import CartPage
from HW25.pages.checkout_page import CheckoutPage
from HW25.test_data.creds import UserCredentials
import pytest


@pytest.mark.smoke
def test_saucedemo_by_path(driver):
    LoginPage(driver).login(UserCredentials.standart_user,
                            UserCredentials.standart_password)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    checkout.checkout_info(UserCredentials.buyer_first_name,
                           UserCredentials.buyer_last_name, UserCredentials.buyer_postal_code)
    checkout.click_finish()

    assert checkout.get_message() == "Thank you for your order!"
