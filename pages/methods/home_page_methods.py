from selenium.webdriver.common.by import By
from pages.elements.home_page import HomePage


class HomePageMethods:
    def click_elements_button(self, browser):
        elements_button = browser.find_element(By.XPATH, HomePage.btnElements)
        browser.execute_script("arguments[0].scrollIntoView();", elements_button)
        elements_button.click()

    def click_forms_button(self, browser):
        forms_button = browser.find_element(By.XPATH, HomePage.btnForms)
        browser.execute_script("arguments[0].scrollIntoView();", forms_button)
        forms_button.click()
