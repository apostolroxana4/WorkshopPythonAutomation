import pytest
from selenium.webdriver.common.by import By
from pages.practice_form.elements import Elements
from pages.practice_form.methods import FormMethods


# mutat link-urile in variabile + variabile gen label
# de redus utilizarea la browser


# @pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestFillForm:
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

    def test_fill_mobile_nr(self):
        # make a function that encapsulates the insertion of a wrong number

        self.form_methods.insert_wrong_number(self.driver, By.ID, self.elements.mobile_number)
        self.form_methods.fill(self.driver, By.ID, self.elements.mobile_number, self.elements.mobile_number_value)
        assert self.form_methods.validate_field(self.driver, By.ID,
                                                self.elements.mobile_number, self.elements.mobile_number_value)

    def test_fill_calendar(self):
        self.form_methods.clear_calendar_date(self.driver, By.ID, self.elements.date_of_birth)
        self.form_methods.fill(self.driver, By.ID, self.elements.date_of_birth, self.elements.date_of_birth_value)
        assert self.form_methods.validate_field(self.driver, By.ID,
                                                self.elements.date_of_birth, self.elements.date_of_birth_result)

    def test_select_hobbies(self):
        self.form_methods.click_element(self.driver, By.CSS_SELECTOR, self.elements.hobbies_sports_value)
        assert self.form_methods.is_element_selected(self.driver, By.ID, self.elements.hobbies_sports)

        self.form_methods.click_element(self.driver, By.CSS_SELECTOR, self.elements.hobbies_music_value)
        assert self.form_methods.is_element_selected(self.driver, By.ID, self.elements.hobbies_music)

    def test_scroll_to_the_bottom(self):
        self.form_methods.scroll_to_the_bottom(self.driver)
        assert self.form_methods.is_element_displayed(self.driver, By.ID, self.elements.state)

    def test_select_state(self):
        self.form_methods.click_element(self.driver, By.ID, self.elements.state)
        self.form_methods.click_element(self.driver, By.XPATH, self.elements.haryana)
        # assert Methods().validate_field(browser, By.XPATH, Elements.haryana, "Haryana")

    def test_select_city(self):
        self.form_methods.click_element(self.driver, By.ID, self.elements.city)
        self.form_methods.click_element(self.driver, By.ID, self.elements.karnal)

    def test_submit_form(self):
        self.form_methods.submit_form(self.driver, By.ID, self.elements.form)
        self.form_methods.maximize_window(self.driver)
        assert self.form_methods.is_element_displayed(self.driver, By.CSS_SELECTOR, self.elements.modal_form_result)

    def test_close_modal(self):
        self.form_methods.close_modal(self.driver, By.ID, self.elements.close_modal)
        assert self.form_methods.verify_url(self.driver, self.elements.form_subcategory_url)
