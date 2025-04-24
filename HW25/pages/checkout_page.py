from selenium.webdriver.common.by import By
from HW25.pages.base_page import BasePage


class CheckoutPage(BasePage):
    first_name_field = (By.ID, "first-name")
    last_name_field = (By.ID, "last-name")
    postal_code_field = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    get_message_button = (By.CLASS_NAME, "complete-header")

    def checkout_info(self, first, last, zip_code):
        self.send_text(self.first_name_field, first)
        self.send_text(self.last_name_field, last)
        self.send_text(self.postal_code_field, zip_code)
        self.click(self.continue_button)

    def click_finish(self):
        self.click(self.finish_button)

    def get_message(self):
        return self.get_text(self.get_message_button)
