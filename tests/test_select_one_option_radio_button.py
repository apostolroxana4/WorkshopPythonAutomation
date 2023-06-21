import pytest
from actions.actions_form import Actions


@pytest.mark.usefixtures("browser")
class TestSelectOneOptionRadioButton:
    actions = Actions()

    def test_click_on_forms_from_main_page(self, browser):
        self.actions.forms_from_main_page(browser)
        assert browser.current_url == "https://demoqa.com/forms"

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

    def test_insert_email(self, browser):
        self.actions.enter_email(browser)
        assert self.actions.email_visibility(browser)

    def test_select_gender_female(self, browser):
        self.actions.select_gender_female(browser)



