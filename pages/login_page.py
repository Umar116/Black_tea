import time

from configure import base_login, base_password, prod_login
from datas.locators import login, password, sign_in
from pages.base_page import BasePage
from pages.tools import Tools


class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.tool = Tools(browser)

    def login(self):
        self.tool.input(login, text=base_login)
        self.tool.input(password, text=base_password)
        time.sleep(1)
        self.tool.click(sign_in)
        time.sleep(3)
