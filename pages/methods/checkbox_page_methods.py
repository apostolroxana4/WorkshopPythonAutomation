from selenium.webdriver.common.by import By
from pages.elements.checkbox_page import CheckBoxPage


class CheckBoxPageMethods:
    @staticmethod
    def click_arrow(browser, name):
        browser.find_element(By.XPATH, CheckBoxPage.tree_element_part1 +
                             name
                             + CheckBoxPage.tree_element_part2_arrow).click()

    @staticmethod
    def click_checkbox(browser, name):
        browser.find_element(By.XPATH, CheckBoxPage.tree_element_part1 +
                             name
                             + CheckBoxPage.tree_element_part2_checkbox).click()

    @staticmethod
    def get_message(browser):
        elements = browser.find_elements(By.XPATH, CheckBoxPage.message_element)
        text = ' '.join([element.text for element in elements])
        return text
