import pytest
from selenium.webdriver.common.by import By
from pages.practice_form.elements import Elements
from pages.practice_form.methods import FormMethods


@pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestRefreshForm:
    form_methods = FormMethods()
    elements = Elements

    def test_click_on_forms(self):
        self.form_methods.click_element(self.driver, By.XPATH, self.elements.forms_category)
        assert self.form_methods.verify_url(self.driver, self.elements.forms_category_url)

    def test_click_on_practice_form(self):
        self.form_methods.click_element(self.driver, By.XPATH, self.elements.form_subcategory)
        assert self.form_methods.verify_url(self.driver, self.elements.form_subcategory_url)

    def test_fill_name(self):
        self.form_methods.fill(self.driver, By.ID, self.elements.first_name, self.elements.first_name_value)
        assert self.form_methods.validate_field(self.driver, By.ID,
                                                self.elements.first_name, self.elements.first_name_value)

        self.form_methods.fill(self.driver, By.ID, self.elements.last_name, self.elements.last_name_value)
        assert self.form_methods.validate_field(self.driver, By.ID,
                                                self.elements.last_name, self.elements.last_name_value)

    def test_select_gender(self):
        self.form_methods.click_element(self.driver, By.CSS_SELECTOR, self.elements.gender_male_value)
        assert self.form_methods.is_element_selected(self.driver, By.ID, self.elements.gender_male)

    def test_refresh_and_confirm(self):
        self.form_methods.refresh_page(self.driver)
        assert self.form_methods.validate_after_refresh(self.driver, By.ID,
                                                        self.elements.first_name, self.elements.gender_male)
