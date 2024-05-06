from selenium.webdriver.support.wait import WebDriverWait

from configure import base_url


class BasePage:

    def __init__(self, browser, timeout=5000):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)
        self.url = base_url

    def go_to(self, path):
        self.browser.get(self.url + path)
