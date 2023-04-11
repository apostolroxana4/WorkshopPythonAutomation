from selenium.webdriver.common.by import By
from driver.driver import Driver
from pages.elements_box_page import ElementsBoxPage
from pages.elements.elements_text_box import ElementFromTextBox


class TestElementsTextBoxComplete:
    __EXPECTED_COLOR = "rgba(255, 0, 0, 1)"
    elements_box_page = ElementsBoxPage()
    browser = Driver.open_page()
    elements_from_text_box = ElementFromTextBox()

    def test_click_test_box(self):
        self.elements_box_page.click_test_box(self.browser)
        assert self.elements_box_page.text_box_text_visibility(self.browser)

    def test_insert_fields(self):
        assert self.elements_box_page.full_name_field_visibility(self.browser)
        self.elements_box_page.insert_full_name(self.browser)
        assert self.elements_box_page.email_field_visibility(self.browser)
        self.elements_box_page.insert_incorrect_email(self.browser)
        assert self.elements_box_page.current_address_field_visibility(self.browser)
        self.elements_box_page.insert_current_address(self.browser)
        assert self.elements_box_page.permanent_address_field_visibility(self.browser)
        self.elements_box_page.insert_permanent_address(self.browser)

    def test_click_submit_button(self):
        self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.elements_box_page.click_submit_button(self.browser)

        email = self.browser.find_element(By.XPATH, self.elements_from_text_box.email_field)
        if "error" in email.get_attribute('outerHTML'):
            obtained_color = email.value_of_css_property('border-bottom-color')
            if not self.elements_box_page.check_color(obtained_color, "rgba(222, 20, 33, 1)"):
                raise ValueError(f"expected color is {self.__EXPECTED_COLOR} and got {obtained_color}")

    def test_close_page(self):
        self.browser.quit()


