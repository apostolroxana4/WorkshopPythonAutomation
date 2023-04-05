from driver.driver import Driver
from actions.actions_text_box import Actions
from pages.elements import StepsElements


class TestTextBox:

    actions = Actions()
    browser = Driver.open_browser()
    steps_elements = StepsElements()

    def test_insert_username(self):
        self.actions.insert_value_for_username_field(self.browser, "username")

    def test_insert_email(self):
        self.actions.insert_value_for_email_field(self.browser, "email")

    def test_insert_current_address(self):
        self.actions.insert_value_for_current_address(self.browser, "current_address")

    def test_insert_permanent_address(self):
        self.actions.insert_value_for_permanent_address(self.browser, "permanent_address")
        assert self.steps_elements.fill_credentials(self.browser, "username", "email", "current_address",
                                                    "permanent_address")

    def test_click_submit(self):
        self.actions.click_submit_button(self.browser)





