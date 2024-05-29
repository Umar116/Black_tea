import time

from pages.base_page import BasePage
from pages.tools import Tools
from datas.locators import catalog, add_product_button, add_category_button, input_category_name_field, \
    create_category_button


class CatalogPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.elements = Tools(browser)

    def open_catalog_page(self):
        self.elements.click(catalog)

    def open_add_products_window(self):
        self.elements.click(add_product_button)

    def open_add_category_window(self):
        self.elements.click(add_category_button)

    def input_category_name(self, text):
        self.elements.input(input_category_name_field, text=text)

    def click_create_category(self):
        self.elements.click(create_category_button)

    def create_category(self) -> None:
        self.open_add_products_window()
        self.open_add_category_window()

