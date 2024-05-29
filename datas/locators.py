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
               "MuiTypography-root.MuiTypography-body2.MuiTypography-noWrap.css-1n4xcnw")
chat_field = (By.NAME, "msg")
send_message = (By.CSS_SELECTOR, 'button[aria-label="Send"]')
first_name_field_error = (By.XPATH, '//p[text()=\'"firstName" is required\']')

search_customer_field = (By.CSS_SELECTOR, 'input[placeholder="Enter phone number, email, or name"]')
deal_notification = (By.CSS_SELECTOR, 'div[class="MuiAlert-message css-1xsto0d"]')

customer_name_in_customer_list = (By.CLASS_NAME,
                                  'MuiTypography-root.MuiTypography-body1.css-1bbjwv7')

users_button = (By.CSS_SELECTOR, 'a[href="/users"]')
users_page_title = (By.CSS_SELECTOR, 'h4[class="MuiTypography-root MuiTypography-h4 css-6x0aek"]')
users_input_field = (By.CSS_SELECTOR, 'input[type="text"]')
users_date_list = (By.CSS_SELECTOR, 'div[class="MuiDataGrid-row MuiDataGrid-row--lastVisible"]')
users_role = (By.CSS_SELECTOR, 'div[data-field="role"]')
all_user_roles = (By.XPATH, '//p[text()="all roles"]')
role_list_dropdown = lambda roles: (By.XPATH, f'//p[text()="{roles}"]')

all_user_statuses = (By.XPATH, '//p[text()="all statuses"]')
status_drop_down = lambda statuses: (By.XPATH, f'//p[text()="{statuses}"]')
user_statuses = (By.CSS_SELECTOR, 'span[class="MuiChip-label MuiChip-labelMedium css-14vsv3w"]')

catalog = (By.CSS_SELECTOR, 'a[href="/catalog"]')
add_product_button = (By.CSS_SELECTOR, 'button[class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-yvjl6n"]')
add_category_button = (By.XPATH, '//span[text()="Category"]')
input_category_name_field = (By.XPATH, "//input[href*=':r']")
create_category_button = (By.XPATH, '//p[text()="Create"]')
