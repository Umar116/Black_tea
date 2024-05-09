from datas.locators import deal_list_l, open_customer_l, add_new_customer_l, create_button_l, first_name_l, last_name_l, \
    email_l, \
    phone_l, chat_field, send_message, first_name_field_error, search_customer_field, customer_name_in_customer_list, \
    deal_notification
from pages.base_page import BasePage
from pages.tools import Tools


class DealPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.elements = Tools(browser)

    def open_customer_add_window(self):
        self.elements.click(open_customer_l)

    def open_customer_create_window(self):
        self.elements.click(add_new_customer_l)

    def click_create_button(self):
        self.elements.click(create_button_l)

    def get_deal_list(self):
        self.browser.find_elements(deal_list_l)

    def input_full_customer_dates(self, name, last_name, phone, email):
        self.elements.input(first_name_l, text=name)
        self.elements.input(last_name_l, text=last_name)
        self.elements.input(phone_l, text=phone)
        self.elements.input(email_l, text=email)

    def input_mandatory_customer_dates(self, first_name):
        self.elements.input(first_name_l, text=first_name)

    def get_deals_name(self):
        return self.elements.get_items_list(deal_list_l)

    def input_text_in_chat(self, text):
        self.elements.input(chat_field, text=text)

    def click_send_message_in_chat(self):
        self.elements.click(send_message)

    def first_name_error(self):
        return self.elements.get_item(first_name_field_error)

    def input_customer_date_in_search_field(self, text):
        self.elements.input(search_customer_field, text=text)

    def get_customer_name_in_customer_list(self):
        return self.elements.get_items_list(customer_name_in_customer_list)

    def get_deal_notification(self):
        return self.elements.get_item(deal_notification)
