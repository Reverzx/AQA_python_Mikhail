from selenium.webdriver.common.by import By
from HW25.pages.base_page import BasePage


class CartPage(BasePage):
    checkout_button = (By.ID, "checkout")
    item_name = (By.CLASS_NAME, "inventory_item_name")
    remove_button = (By.ID, "remove-sauce-labs-bolt-t-shirt")

    def click_checkout(self):
        self.click(self.checkout_button)

    def get_item_name(self):
        return self.get_text(self.item_name)

    def remove_item(self):
        self.click(self.remove_button)
