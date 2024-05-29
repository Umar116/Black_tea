from pages.base_page import BasePage
from pages.tools import Tools
from datas.locators import users_button, users_page_title, users_input_field, users_date_list, users_role, role_list_dropdown, \
    all_user_roles, all_user_statuses, status_drop_down, user_statuses


class UsersPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser
        self.elements = Tools(browser)

    def open_users_page(self):
        self.elements.click(users_button)

    def get_users_page_title(self):
        return self.elements.get_item(users_page_title)

    def input_search_field(self, text):
        self.elements.input(users_input_field, text=text)

    def get_users_list(self):
        return self.elements.get_items_list(users_date_list)

    def get_users_role(self):
        return self.elements.get_items_list(users_role)[1:]

    def get_users_status(self):
        return self.elements.get_items_list(user_statuses)

    def choose_user_role_in_filter(self, roles):
        self.elements.click(all_user_roles)
        self.elements.click(role_list_dropdown(roles))

    def choose_user_status_in_filter(self, statuses):
        self.elements.click(all_user_statuses)
        self.elements.click(status_drop_down(statuses))
