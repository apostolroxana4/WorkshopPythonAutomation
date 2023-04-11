from driver.driver import Driver
from pages.elements_box_page import ElementsBoxPage
from pages.elements.elements_text_box import ElementFromTextBox


class TestElementsTextBoxComplete:
    elements_box_page = ElementsBoxPage()
    elements_text_box = ElementFromTextBox()
    browser = Driver.open_page()

    # still work in progress, maybe I will finish it this year

    def test_click_test_box(self):
        self.elements_box_page.click_test_box(self.browser)
        assert self.elements_box_page.text_box_text_visibility(self.browser)

    def test_insert_full_name(self):
        assert self.elements_box_page.full_name_field_visibility(self.browser)
        self.elements_box_page.insert_full_name(self.browser)
        full_name_placeholder = str(self.elements_text_box.full_name_field.get_attribute())
        assert full_name_placeholder in str("Jose Armando")

    def test_insert_email(self):
        assert self.elements_box_page.email_field_visibility(self.browser)
        self.elements_box_page.insert_email(self.browser)
        assert self.elements_box_page.insert_email(self.browser).get_attribute() == str("aaaaa@gmail.com")

    def test_insert_current_address(self):
        assert self.elements_box_page.current_address_field_visibility(self.browser)
        self.elements_box_page.insert_current_address(self.browser)
        assert self.elements_box_page.insert_current_address(self.browser) == str("str.Sorcova")

    def test_insert_permanent_address(self):
        assert self.elements_box_page.permanent_address_field_visibility(self.browser)
        self.elements_box_page.insert_permanent_address(self.browser)
        assert self.elements_box_page.insert_permanent_address(self.browser) == str("str.Sorvoca, nr.10")

    def test_close_page(self):
        self.browser.quit()
