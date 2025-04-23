from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def send_text(self, locator, text):
        input_field = self.driver.find_element(*locator)
        input_field.clear()
        input_field.send_keys(text)

    def is_url_correct(self, url):
        return self.driver.current_url == url, f"Expected to get {url} but got {self.driver.current_url}"

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
