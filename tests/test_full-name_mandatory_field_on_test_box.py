import pytest
from driver.driver import Driver
from pages.elements_box_page import ElementsBoxPage


class TestElementsTextBoxComplete:
    elements_box_page = ElementsBoxPage()
    browser = Driver.open_page()

    def test_click_test_box(self):
        self.elements_box_page.click_test_box(self.browser)
        assert self.elements_box_page.text_box_text_visibility(self.browser)

    def test_insert_full_name(self):
        assert self.elements_box_page.full_name_field_visibility(self.browser)
        self.elements_box_page.insert_full_name(self.browser)

    @pytest.mark.skip(reason="not mandatory field")
    def test_insert_email(self):
        assert self.elements_box_page.email_field_visibility(self.browser)
        self.elements_box_page.insert_email(self.browser)

    @pytest.mark.skip(reason="not mandatory field")
    def test_insert_current_address(self):
        assert self.elements_box_page.current_address_field_visibility(self.browser)
        self.elements_box_page.insert_current_address(self.browser)
        assert self.elements_box_page.insert_current_address(self.browser) == str("str.Sorcova")

    @pytest.mark.skip(reason="not mandatory field")
    def test_insert_permanent_address(self):
        assert self.elements_box_page.permanent_address_field_visibility(self.browser)
        self.elements_box_page.insert_permanent_address(self.browser)

    def test_click_submit_button(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.elements_box_page.click_submit_button(self.browser)
        assert self.elements_box_page.check_submit_content(self.browser)

    def test_close_page(self):
        self.browser.quit()



