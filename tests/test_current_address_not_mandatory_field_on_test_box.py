import sys
import pytest
import conftest
from actions.actions_text_box import Actions
from pages.elements import StepsElements


@pytest.mark.skipif(sys.platform != "win32", reason="just win32 platform available")
class TestTextBox:
    actions = Actions()
    browser = conftest.setup()
    steps_elements = StepsElements()

    def test_insert_username(self):
        self.actions.insert_value_for_username_field(self.browser, "username")
        assert self.actions.username_field_visibility(self.browser)

    def test_insert_email(self):
        self.actions.insert_value_for_email_field(self.browser, "email")

    @pytest.mark.skip(reason="not mandatory field")
    def test_insert_current_address(self):
        self.actions.insert_value_for_current_address(self.browser, "current_address")
        assert self.actions.current_address_visibility(self.browser)

    def test_insert_permanent_address(self):
        self.actions.insert_value_for_permanent_address(self.browser, "permanent_address")
        assert self.steps_elements.fill_credentials(self.browser, "username", "email", "current_address",
                                                    "permanent_address")
       
    def test_click_submit(self):
        self.actions.click_submit_button(self.browser)

