import pytest
from actions.actions_elements import Actions
from pytest_bdd import scenario, when, then


@pytest.mark.usefixtures("browser")


    @scenario('myfeatures/checkbox.feature', 'Check angular file and public file from Documents category')
    def test_checkbox(self):
        pass

    @when("I click to Elements section")
    def click_on_elements():
        selactions.elements_from_main_page(self.driver)

    @then("I should enter into Elements section")
    def main_page_visibility(self):
        assert self.driver.current_url == "https://demoqa.com/elements"

    @when("I click Checkbox subsection")
    def click_on_checkbox_subsection(self):
        self.actions.click_checkbox_subsection(self.driver)

    @then("I should enter into Checkbox subsection")
    def check_on_checkbox_subsection(self):
        assert self.actions.check_checkbox_subsection(self.driver)

    @when("I expand Home button")
    def expand_home_item(self):
        self.actions.expand_home_item(self.driver)

    @then("I should enter into Home")
    def home_item_visibility(self):
        assert self.actions.check_home_item(self.driver)

    @when("I expand Documents category")
    def expand_documents_item(self):
        self.actions.expand_documents_item(self.driver)

    @then("I should enter into Documents category")
    def documents_category_visibility(self):
        assert self.actions.check_office(self.driver)

    @when("I click Office")
    def click_on_office(self):
        self.actions.click_office(self.driver)

    @then("Check public file from Office")
    def check_public_file_from_office(self):
        assert self.actions.check_documents_office_public(self.driver)

    @when("I click Workspace")
    def click_on_workspace(self):
        self.actions.click_office(self.driver)
        self.actions.click_workspace(self.driver)

    @then("Check angular file from Workspace")
    def check_angular_file_from_workspace(self):
        assert self.actions.check_documents_workspace_angular(self.driver)

