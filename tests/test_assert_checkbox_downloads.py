import pytest
from driver.driver import Driver
from actions.actions_text_box import Actions
from pages.elements import StepsElements


@pytest.mark.usefixtures("browser")
class TestAssertCheckboxDownloads:
    actions = Actions()
    steps_elements = StepsElements()

    def test_click_on_elements(self):
        self.actions.click_elements_section(self.driver)
        assert self.actions.check_elements_section(self.driver)

    def test_click_on_checkbox_subsection(self):
        self.actions.click_checkbox_subsection(self.driver)
        assert self.actions.check_checkbox_subsection(self.driver)

    def test_expand_home_item(self):
        self.actions.expand_home_item(self.driver)
        assert self.actions.check_home_item()

    def test_
