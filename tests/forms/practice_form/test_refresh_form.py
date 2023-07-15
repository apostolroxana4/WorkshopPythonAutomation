import pytest
from selenium.webdriver.common.by import By
from pages.practice_form.elements import Elements
from pages.practice_form.methods import FormMethods


@pytest.fixture
def form_methods(browser):
    return FormMethods(browser)


@pytest.fixture
def elements():
    return Elements()


@pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestRefreshForm:

    def test_click_on_forms(self, form_methods, elements):
        form_methods.click_element(By.XPATH, elements.forms_category)
        assert form_methods.verify_url(elements.forms_category_url)

    def test_click_on_practice_form(self, form_methods, elements):
        form_methods.click_element(By.XPATH, elements.form_subcategory)
        assert form_methods.verify_url(elements.form_subcategory_url)

    def test_fill_name(self, form_methods, elements):
        form_methods.fill(By.ID, elements.first_name, elements.first_name_value)
        assert form_methods.validate_field(By.ID, elements.first_name, elements.first_name_value)

        form_methods.fill(By.ID, elements.last_name, elements.last_name_value)
        assert form_methods.validate_field(By.ID, elements.last_name, elements.last_name_value)

    def test_select_gender(self, form_methods, elements):
        form_methods.click_element(By.CSS_SELECTOR, elements.gender_male_value)
        assert form_methods.is_element_selected(By.ID, elements.gender_male)

    def test_refresh_and_confirm(self, form_methods, elements):
        form_methods.refresh_page()
        form_methods.wait_for_refresh(By.ID, elements.gender_male)
        assert form_methods.validate_after_refresh(By.ID, elements.first_name, elements.gender_male)
