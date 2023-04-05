import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

class TextBox:

    def test_insert_value_for_username_field(self, browser):
        username_field = browser.find_element(By.ID, 'userName')
        username_field.send_keys("user")
        time.sleep(3)

    def test_insert_value_for_email_field(self, browser):
        email_field = browser.find_element(by=By.XPATH, value='//*[@id="userEmail"]')
        email_field.send_keys("andra15@yahoo.com")
        time.sleep(3)

    def test_insert_value_for_current_address(self, browser):
        current_address_field = browser.find_element(By.CSS_SELECTOR, '#currentAddress')
        current_address_field.send_keys("Bd. Chimiei, nr. 10")
        time.sleep(3)

    def test_insert_value_for_permanent_address(self, browser):
        permanent_address_field = browser.find_element(By.ID, 'permanentAddress')
        permanent_address_field.send_keys("Str. Mihai Viteazul")
        time.sleep(3)

    def test_click_submit_button(self, browser):
        submit_button = browser.find_element(By.ID, 'submit')
        submit_button.click()

