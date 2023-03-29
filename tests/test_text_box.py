from driver.driver import Driver
from actions.actions_text_box import Actions


class TestTextBox:

    actions = Actions()
    browser = Driver.open_browser()

    def test_insert_username(self):
        self.actions.insert_value_for_username_field(self.browser)
        #assert self.actions.insert_value_for_username_field(self.browser)

    def test_insert_email(self):
        self.actions.insert_value_for_email_field(self.browser)

    def test_insert_current_address(self):
        self.actions.insert_value_for_current_address(self.browser)

    def test_insert_permanent_address(self):
        self.actions.insert_value_for_permanent_address(self.browser)

    def test_click_submit(self):
        self.actions.click_submit_button(self.browser)



