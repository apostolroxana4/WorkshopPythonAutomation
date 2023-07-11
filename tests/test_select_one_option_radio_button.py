import pytest
from selenium.webdriver.common.by import By
from actions.actions_form import Actions
from actions.general_actions import GeneralActions
from pages.items import ItemsFormsSection


@pytest.mark.usefixtures("browser")
class TestSelectOneOptionRadioButton(ItemsFormsSection):
    actions = Actions()
    general_actions = GeneralActions()
    items_forms = ItemsFormsSection()

    def test_click_on_forms_from_main_page(self, browser):
        self.actions.click_forms_section(browser)
        self.general_actions.maximize_window(browser)
        #self.general_actions.scroll_down(browser)
        assert self.general_actions.check_url(browser, self.items_forms.form_url)

    def test_click_on_practice_form_subsection(self, browser):
        self.actions.click_subsection_practice_form(browser)
        assert self.actions.check_subsection_practice_form(browser)

    def test_insert_first_name(self, browser):
        self.actions.enter_first_name(browser)
        assert self.actions.first_name_field_visibility(browser)

    def test_insert_wrong_last_name(self, browser):
        self.actions.enter_wrong_last_name(browser)

    def test_insert_correctly_last_name(self, browser):
        self.actions.enter_correctly_last_name(browser)
        assert browser.find_element(By.ID, self.last_name_item).get_attribute("value") == self.last_name_value_correctly

    def test_insert_email(self, browser):
        self.actions.enter_email(browser)
        assert self.actions.email_visibility(browser)

    def test_select_gender_female(self, browser):
        self.actions.select_gender_female(browser)
        assert browser.find_element(By.ID, self.female_item).is_selected()
        assert not browser.find_element(By.ID, self.male_item).is_selected()
        assert not browser.find_element(By.ID, self.other_item).is_selected()



