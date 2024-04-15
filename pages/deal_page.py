from datas.locators import DealsPageLocators
from pages.base_page import BasePage
from pages.tools import Tools


class DealPage(BasePage):
    deal_locators = DealsPageLocators

    def open_customer_add_window(self):
        elements = Tools(self.browser)
        elements.click(*self.deal_locators.open_customer)
