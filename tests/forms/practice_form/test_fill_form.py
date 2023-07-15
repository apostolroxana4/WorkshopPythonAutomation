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


# @pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestFillForm:

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

    def test_fill_mobile_nr(self, form_methods, elements):
        form_methods.insert_wrong_number(By.ID, elements.mobile_number)
        form_methods.fill(By.ID, elements.mobile_number, elements.mobile_number_value)
        assert form_methods.validate_field(By.ID, elements.mobile_number, elements.mobile_number_value)

    def test_fill_calendar(self, form_methods, elements):
        form_methods.click_element(By.ID, elements.date_of_birth)
        form_methods.pick_date(By.CSS_SELECTOR, elements.date_day, By.CSS_SELECTOR)
        assert form_methods.validate_date(By.ID, elements.date_of_birth)

    def test_select_hobbies(self, form_methods, elements):
        form_methods.click_element(By.CSS_SELECTOR, elements.hobbies_sports_value)
        assert form_methods.is_element_selected(By.ID, elements.hobbies_sports)

        form_methods.click_element(By.CSS_SELECTOR, elements.hobbies_music_value)
        assert form_methods.is_element_selected(By.ID, elements.hobbies_music)

    def test_scroll_to_the_bottom(self, form_methods, elements):
        form_methods.maximize_window()
        assert form_methods.is_element_displayed(By.ID, elements.state)

    def test_select_state(self, form_methods, elements):
        form_methods.click_element(By.ID, elements.state)
        form_methods.click_element(By.XPATH, elements.haryana)

    def test_select_city(self, form_methods, elements):
        form_methods.click_element(By.ID, elements.city)
        form_methods.click_element(By.ID, elements.karnal)

    def test_submit_form(self, form_methods, elements):
        form_methods.submit_form(By.ID, elements.form)
        form_methods.maximize_window()
        form_methods.wait_for_modal(By.CSS_SELECTOR, elements.modal_form_result)
        assert form_methods.is_element_displayed(By.CSS_SELECTOR, elements.modal_form_result)

    def test_close_modal(self, form_methods, elements):
        form_methods.close_modal(By.ID, elements.close_modal)
        assert form_methods.verify_url(elements.form_subcategory_url)
