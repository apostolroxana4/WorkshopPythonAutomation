from selenium.webdriver.common.by import By
from pages.elements.select_menu_page import SelectMenuPage


class SelectMenuPageMethods:
    @staticmethod
    def select_dropdown_value(browser):
        browser.find_element(By.ID, SelectMenuPage.ddSelectValue).click()
        browser.find_element(By.ID, SelectMenuPage.ddSelectValueGroup2Item2).click()

    @staticmethod
    def get_ddSelectValueText(browser):
        return browser.find_element(By.ID, SelectMenuPage.ddSelectValue).get_property("textContent")


