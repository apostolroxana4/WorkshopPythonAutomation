from selenium.webdriver.common.by import By
from pages.elements.home_page import HomePage


class HomePageMethods:
    @staticmethod
    def click_elements_button(browser):
        elements_button = browser.find_element(By.XPATH, HomePage.btnElements)
        browser.execute_script("arguments[0].scrollIntoView();", elements_button)
        elements_button.click()

    @staticmethod
    def click_forms_button(browser):
        forms_button = browser.find_element(By.XPATH, HomePage.btnForms)
        browser.execute_script("arguments[0].scrollIntoView();", forms_button)
        forms_button.click()

    @staticmethod
    def click_widgets_button(browser):
        widgets_button = browser.find_element(By.XPATH, HomePage.btnWidgets)
        browser.execute_script("arguments[0].scrollIntoView();", widgets_button)
        widgets_button.click()
