from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class Tools(BasePage):

    def __init__(self, browser, time=10):
        super().__init__(browser)
        self.browser = browser

    def click(self, *element):
        button = self.wait.until(
            EC.element_to_be_clickable(*element)
        )
        button.click()

    def input(self, *element, text):
        input_value = self.wait.until(
            EC.visibility_of_element_located(*element)
        )
        input_value.send_keys(text)

    def get_items_list(self, *element):
        value = self.wait.until(
            EC.visibility_of_all_elements_located(*element)
        )
        return value
