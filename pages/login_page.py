import time

from selenium.webdriver.common.by import By

from datas.locators import LoginPageLocators
from pages.base_page import BasePage

from configure import base_login, base_password
from pages.tools import Tools


class LoginPage(BasePage):
    login_locators = LoginPageLocators

    def login(self):
        tool = Tools(self.browser)
        tool.input(*self.login_locators.login, text=base_login)
        tool.input(*self.login_locators.password, text=base_password)
        tool.click(*self.login_locators.sign_in)
