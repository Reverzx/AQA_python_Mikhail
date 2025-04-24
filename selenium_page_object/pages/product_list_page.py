from selenium_page_object.pages.base_page import BasePage


class ProductListPage(BasePage):
  def __init__(self, driver, url):
    super().__init__(driver, url)