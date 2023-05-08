import pytest
from actions.actions_elements import Actions


@pytest.mark.usefixtures("browser")
class TestCheckboxDownloads:
    actions = Actions()

    def test_click_on_elements(self):
        self.actions.elements_from_main_page(self.driver)

    def test_click_on_checkbox_subsection(self):
        self.actions.click_checkbox_subsection(self.driver)
        assert self.actions.check_checkbox_subsection(self.driver)

    def test_expand_home_item(self):
        self.actions.expand_home_item(self.driver)
        assert self.actions.check_downloads_item(self.driver)

    def test_click_on_downloads_item(self):
        self.actions.click_downloads_item(self.driver)
        assert self.actions.check_downloads_word_file(self.driver)



