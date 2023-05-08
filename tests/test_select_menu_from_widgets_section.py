import pytest
from actions.actions_widgets import Actions


@pytest.mark.usefixtures("browser")
class TestSelectMenuFromWidgetsSection:
    actions = Actions()

    def test_click_on_widgets_from_main_page(self):
        self.actions.select_widgets_from_main_page(self.driver)
        assert self.driver.current_url == "https://demoqa.com/widgets"

    def test_click_on_select_menu_subsection(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.actions.click_select_menu_subsection(self.driver)
        assert self.actions.check_select_menu_subsection(self.driver)

    def test_click_select_value(self):
        self.actions.click_select_value(self.driver)

    def test_verify_selected_value(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        value = self.actions.get_select_value_text(self.driver)
        print(value)
        assert "Another root option" == value

    def test_click_select_one(self):
        self.actions.click_select_one(self.driver)

    def test_verify_selected_one_value(self):
        value = self.actions.get_select_one_value_text(self.driver)
        print(value)
        assert "Prof." == value

    def test_click_old_style_select_menu(self):
        self.actions.select_old_style_select_menu(self.driver)

    def test_verify_old_style_value(self):
        value = self.actions.get_old_style_select_menu_value(self.driver)
        print(value)

    def test_click_multiselect_dropdown(self):
        self.actions.select_multiselect_dropdown(self.driver)
