import pytest
from selenium.webdriver.common.by import By
from pages.practice_form.elements import Elements
from pages.practice_form.methods import FormMethods


# @pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestRefreshForm:
    form_methods = FormMethods()

    def test_click_on_forms(self):
        self.form_methods.click_element(self.driver, By.XPATH, Elements.forms_category)
        assert self.form_methods.verify_url(self.driver, "https://demoqa.com/forms")

    def test_click_on_practice_form(self):
        self.form_methods.click_element(self.driver, By.XPATH, Elements.form_subcategory)
        assert self.form_methods.verify_url(self.driver, "https://demoqa.com/automation-practice-form")

    def test_fill_name(self):
        self.form_methods.fill(self.driver, By.ID, Elements.first_name, 'Bob')
        assert self.form_methods.validate_field(self.driver, By.ID, Elements.first_name, "Bob")

        self.form_methods.fill(self.driver, By.ID, Elements.last_name, 'The Builder')
        assert self.form_methods.validate_field(self.driver, By.ID, Elements.last_name, 'The Builder')

    def test_select_gender(self):
        self.form_methods.click_element(self.driver, By.CSS_SELECTOR, f"label[for='{Elements.gender_male}']")
        assert self.form_methods.is_element_selected(self.driver, By.ID, Elements.gender_male)

    def test_refresh_and_confirm(self):
        self.form_methods.refresh_page(self.driver)
        assert self.driver.find_element(By.ID, "firstName").get_attribute("value") == ''
        assert not self.driver.find_element(By.ID, "gender-radio-1").is_selected()
