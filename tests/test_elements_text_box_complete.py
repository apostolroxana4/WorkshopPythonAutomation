from driver.driver import Driver
from pages.elements_box_page import ElementsBoxPage


class TestElementsTextBoxComplete:
    elements_box_page = ElementsBoxPage()
    browser = Driver.open_page()

    def test_click_test_box(self):
        self.elements_box_page.click_test_box(self.browser)

    def test_insert_fields(self):
        self.elements_box_page.insert_full_name(self.browser)
        self.elements_box_page.insert_email(self.browser)
        self.elements_box_page.insert_current_address(self.browser)
        self.elements_box_page.insert_permanent_address(self.browser)

    def test_click_submit_button(self):
        self.elements_box_page.click_submit_button(self.browser)

    def test_close_page(self):
        self.browser.quit()







