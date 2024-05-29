import pytest
from selenium import webdriver

from pages.base_page import BasePage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")

    options = webdriver.FirefoxOptions()
    options.set_preference("intl.accept_languages", "en")
    options.page_load_strategy = 'normal'
    browser = webdriver.Firefox(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def authorization(browser):
    base = BasePage(browser)
    login = LoginPage(browser)
    base.go_to('login')
    login.login()
