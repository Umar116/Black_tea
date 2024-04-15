from conftest import browser
from pages.login_page import LoginPage
from pages.main_page import MainPage


class TestLogin:

    def test_user_login(self, browser):
        page = MainPage(browser)
        auth = LoginPage(browser)
        page.go_to('login')
        page.should_be_login_link()
        auth.login()
