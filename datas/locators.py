from selenium.webdriver.common.by import By

login = (By.CSS_SELECTOR, 'input[type="email"]')
password = (By.CSS_SELECTOR, 'input[type="password"]')
sign_in = (By.CSS_SELECTOR, 'button[type="submit"]')

open_customer_l = (By.XPATH, '//*[@id="root"]//div[2]/div/div[1]/button[2]')
add_new_customer_l = (By.XPATH, '//button[text() = "Add new contact"]')
create_button_l = (By.XPATH, '//button[text() = "Create"]')
first_name_l = (By.CSS_SELECTOR, 'input[name="firstName"]')
last_name_l = (By.CSS_SELECTOR, 'input[name="lastName"]')
phone_l = (By.CSS_SELECTOR, 'input[name="phone"]')
email_l = (By.CSS_SELECTOR, 'input[name="email"]')
deal_list_l = (By.CLASS_NAME,
               "MuiTypography-root.MuiTypography-body2.MuiTypography-noWrap.css-fsltt8")
chat_field = (By.NAME, "msg")
send_message = (By.CSS_SELECTOR, 'button[aria-label="Send"]')
