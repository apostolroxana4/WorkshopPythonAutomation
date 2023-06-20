import pytest
from actions.actions_form import Actions


@pytest.mark.usefixtures("browser")
class TestSelectOneOptionRadioButton:
    actions = Actions()

    def test_click_on_forms_from_main_page(self):
        self.actions.forms_from_main_page(self.driver)
        assert self.driver.current_url == "https://demoqa.com/forms"

    def test_click_on_practice_form_subsection(self):
        self.actions.click_subsection_practice_form(self.driver)
        assert self.actions.check_subsection_practice_form(self.driver)

    def test_insert_first_name(self):
        self.actions.enter_first_name(self.driver)
        assert self.actions.first_name_field_visibility(self.driver)

    def test_insert_wrong_last_name(self):
        self.actions.enter_wrong_last_name(self.driver)

    def test_insert_correctly_last_name(self):
        self.actions.enter_correctly_last_name(self.driver)

    def test_insert_email(self):
        self.actions.enter_email(self.driver)
        assert self.actions.email_visibility(self.driver)

    def test_select_gender_female(self):
        self.actions.select_gender_female(self.driver)



