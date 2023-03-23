import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Widgets:

    def scroll_down(self, browser):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(1)

    def scroll_up(self, browser):
        browser.execute_script("window.scrollTo(0,0)")
        time.sleep(1)

    def click_dropdown_widgets(self, browser):
        dropdown_widgets = browser.find_elements(By.CLASS_NAME, "element-group")[3]
        dropdown_widgets.click()

    def click_autocomplete(self, browser):
        autocomplete = browser.find_elements(By.ID, 'item-1')[2]
        autocomplete.click()

    def select_and_send(self, browser,word):
        first_field = browser.find_element(By.ID, 'autoCompleteMultipleInput')
        first_field.click()
        time.sleep(1)
        first_field.send_keys(word)
        first_field.send_keys(Keys.ENTER)