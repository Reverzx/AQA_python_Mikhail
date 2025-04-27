from HW25.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    user_name = (By.ID, "user-name")
    user_password = (By.ID, "password")
    login_button = (By.CLASS_NAME, "btn_action")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, user_name, password):
        self.send_text(self.user_name, user_name)
        self.send_text(self.user_password, password)
        self.click(self.login_button)
