import pytest
from actions.actions_text_box import Actions


@pytest.mark.usefixtures("browser")
class TestCheckboxOffice:
    actions = Actions()

    def test_click_on_elements(self):
        self.actions.elements_from_main_page(self.driver)

    def test_click_on_checkbox_subsection(self):
        self.actions.click_checkbox_subsection(self.driver)
        assert self.actions.check_checkbox_subsection(self.driver)

    def test_expand_home_item(self):
        self.actions.expand_home_item(self.driver)
        assert self.actions.check_home_item(self.driver)

    def test_expand_documents_item(self):
        self.actions.expand_documents_item(self.driver)
        assert self.actions.check_office(self.driver)

    def test_click_on_office(self):
        self.actions.click_office(self.driver)
        assert self.actions.check_documents_office_public(self.driver)

    def test_click_on_workspace(self):
        self.actions.click_office(self.driver)
        self.actions.click_workspace(self.driver)
        assert self.actions.check_documents_workspace_angular(self.driver)

