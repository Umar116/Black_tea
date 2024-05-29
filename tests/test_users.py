import time

import pytest
from selenium.webdriver.common.by import By

from pages.users_page import UsersPage


class TestUsers:

    @pytest.mark.parametrize('dates', ["Ethan",
                                       "senivis Test",
                                       "+49 1522 2617485",
                                       "+49 1573 9311111",
                                       "senivis250@amankro.com",
                                       "test@test.com"])
    def test_users_find_by_dates(self, browser, authorization, dates):
        users = UsersPage(browser)

        users.open_users_page()
        title = users.get_users_page_title()
        assert title.text == "Users"

        users.input_search_field(dates)
        time.sleep(3)
        text = users.get_users_list()
        assert dates in text[0].text

    @pytest.mark.parametrize('roles', ["tenant-admin", "user"])
    def test_users_sorted_by_role(self, browser, authorization, roles):
        users = UsersPage(browser)

        users.open_users_page()
        title = users.get_users_page_title()
        assert title.text == "Users"

        users.choose_user_role_in_filter(roles)
        text = users.get_users_role()

        for i in text:
            assert i.text in roles

    @pytest.mark.parametrize('statuses', ["active", "inactive", "invited"])
    def test_users_sorted_by_status(self, browser, authorization, statuses):
        users = UsersPage(browser)

        users.open_users_page()
        title = users.get_users_page_title()
        assert title.text == "Users"

        users.choose_user_status_in_filter(statuses)

        text = users.get_users_status()

        for i in text:
            assert i.text in statuses
