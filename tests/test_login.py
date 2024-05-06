import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from conftest import browser, authorization
from datas.fake import first_name, last_name, phone, email
from pages.deal_page import DealPage


class TestLogin:

    def test_deal_created(self, browser, authorization):
        deal = DealPage(browser)
        f_name = first_name()
        l_name = last_name()

        deal.open_customer_add_window()
        deal.open_customer_create_window()
        deal.input_full_customer_dates(
            name=f_name,
            last_name=l_name,
            email=email(),
            phone=phone())
        deal.click_create_button()
        time.sleep(5)
        name = f_name + " " + l_name
        deals = deal.get_deals_name()
        assert deals[0].text == name, "Deal Not found"

    def test_deal_created_by_mandatory_field(self, browser, authorization):
        deal = DealPage(browser)
        f_name = first_name()

        deal.open_customer_add_window()
        deal.open_customer_create_window()
        deal.input_mandatory_customer_dates(
            first_name=f_name)
        deal.click_create_button()
        time.sleep(3)
        deals = deal.get_deals_name()
        assert f_name in deals[0].text, "Deal Not found"

    def test_chat_is_top_up(self, browser, authorization):
        deal = DealPage(browser)
        browser.refresh()
        text = email()
        deal_name = deal.get_deals_name()
        s_name = deal_name[1].text
        deal_name[1].click()
        browser.switch_to.frame(0)
        deal.input_text_in_chat(text)
        deal.click_send_message_in_chat()
        time.sleep(5)
        browser.switch_to.parent_frame()
        f_as = deal.get_deals_name()
        time.sleep(5)
        assert f_as[0].text == s_name, f'{f_as[0].text} is not equal {s_name}'

