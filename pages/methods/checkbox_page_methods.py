from selenium.webdriver.common.by import By
from pages.elements.checkbox_page import CheckBoxPage


class CheckBoxPageMethods:
    def click_arrow(self, browser, name):
        browser.find_element(By.XPATH, "//span[text()='" + name + "']/ancestor::*[@class='rct-text']/descendant::button").click()

    def click_checkbox(self, browser, name):
        browser.find_element(By.XPATH, "//span[text()='" + name + "']/preceding-sibling::span[@class='rct-checkbox']").click()

    def get_message(self, browser):
        elements = browser.find_elements(By.XPATH, CheckBoxPage.message_element)
        text = ' '.join([element.text for element in elements])
        return text
