import pytest
from driver.driver import Driver
from actions.actions_elements import Actions
from pages.items import StepsElements


#@pytest.mark.skipif(sys.platform != "win32", reason="just win32 platform available")
@pytest.mark.usefixtures("browser")
class TestUsernameEmptyFieldOnTestBox:
    actions = Actions()
    steps_elements = StepsElements()

    def test_insert_username(self):
        username = self.actions.insert_value_for_username_field(self.driver, "")
        if not username:
            pytest.xfail("Username field is empty")

    def test_insert_email(self):
        self.actions.insert_value_for_email_field(self.driver, "email")
        assert self.actions.email_field_visibility(self.driver)

    def test_insert_current_address(self):
        self.actions.insert_value_for_current_address(self.driver, "current_address")
        assert self.actions.current_address_visibility(self.driver)

    def test_insert_permanent_address(self):
        self.actions.insert_value_for_permanent_address(self.driver, "permanent_address")
        assert self.actions.permanent_address_visibility(self.driver)

    def test_click_submit(self):
        self.actions.click_submit_button(self.driver)