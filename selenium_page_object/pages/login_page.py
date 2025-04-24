from selenium_page_object.pages.base_page import BasePage
from selenium_page_object.pages.product_list_page import ProductListPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    user_name = (By.ID, "user-name")
    user_password = (By.ID, "password")
    login_button = (By.CLASS_NAME, "btn_action")
    error_message = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver, url):
        super().__init__(driver, url)

    def complete_login(self, user_name, password):
        self.send_text(self.user_name, user_name)
        self.send_text(self.user_password, password)
        self.click_button(self.login_button)
        return ProductListPage(self.driver, self.url)

    def is_login_successful(self):
        return not self.is_element_present(self.error_message)