from selenium.webdriver.common.by import By
from HW25.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        self.click(self.ADD_TO_CART)

    def go_to_cart(self):
        self.click(self.CART_ICON)
