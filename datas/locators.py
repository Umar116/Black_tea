from selenium.webdriver.common.by import By


class LoginPageLocators:
    login = (By.CSS_SELECTOR, 'input[type="email"]')
    password = (By.CSS_SELECTOR, 'input[type="password"]')
    sign_in = (By.CSS_SELECTOR, 'button[type="submit"]')


class DealsPageLocators:
    open_customer = (By.CSS_SELECTOR, 'button[type = "button"][8]')
    add_new_customer = (By.XPATH, '//span[text() = "Add new contact"]')
