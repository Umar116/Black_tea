from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):

    def should_be_login_link(self):
        assert self.browser.find_element(By.XPATH, '//h3[text()="Welcome!"]')
