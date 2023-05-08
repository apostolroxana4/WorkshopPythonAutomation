from selenium.webdriver.support.select import Select

from pages.items import ItemsWidgetsSection
from selenium.webdriver.common.by import By


class Actions(ItemsWidgetsSection):

    def select_widgets_from_main_page(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.widgets_from_main)[3].click()

    def check_widgets_section(self, browser):
        return browser.find_element(By.XPATH, self.widgets_section).is_displayed()

    def click_widgets_section(self, browser):
        browser.find_element(By.XPATH, self.widgets_section).click()

    def check_select_menu_subsection(self, browser):
        return browser.find_element(By.XPATH, self.subsection_select_menu).is_displayed()

    def click_select_menu_subsection(self, browser):
        browser.find_element(By.XPATH, self.subsection_select_menu).click()

    def click_select_value(self, browser):
        browser.find_element(By.CSS_SELECTOR, self.select_value_item)[0].click()

    def get_select_value_text(self, browser):
        return browser.find_element(By.CSS_SELECTOR, self.select_value_item).get_property("innerText")

    def select_another_root_option_item(self, browser):
        browser.find_element(By.XPATH, self.another_root_option_item).click()

    def click_select_one(self, browser):
        browser.find_element(By.XPATH, self.select_one_item).click()

    def get_select_one_value_text(self, browser):
        return browser.find_element(By.XPATH, self.select_one_item).get_property("innerText")

    def select_prof_option(self, browser):
        browser.find_element(By.XPATH, self.prof_option_item).click()

    def select_old_style_select_menu(self, browser):
        browser.find_element(By.XPATH, self.old_style_select_menu_item).click()

    def get_old_style_select_menu_value(self, browser):
        value_old_style = browser.find_element(By.XPATH, self.select_old_style_select_menu)
        value = Select(value_old_style)
        value.select_by_value("9")

    def select_multiselect_dropdown(self, browser):
        browser.find_element(By.XPATH, self.multiselect_dropdown_item)[2].click()


