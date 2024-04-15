from configure import base_url


class BasePage:

    def __init__(self, browser, timeout=10):
        self.browser = browser
        self.browser.implicitly_wait(timeout)
        self.url = base_url

    def go_to(self, path):
        self.browser.get(self.url + path)
