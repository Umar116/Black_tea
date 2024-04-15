from selenium.common import NoSuchElementException
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class Tools(BasePage):

    def click(self, *element):
        try:
            self.browser.find_element(*element).click()
        except NoSuchElementException:
            return False
        return True

    def input(self, *element, text):
        try:
            self.browser.find_element(*element).send_keys(text)
        except NoSuchElementException:
            return False
        return True
