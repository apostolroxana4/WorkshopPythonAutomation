import pytest
from selenium.webdriver.common.by import By
from pages.practice_form.elements import Elements
from pages.practice_form.methods import FormMethods


# mutat link-urile in variabile + variabile gen label
# de redus utilizarea la browser


@pytest.skip(allow_module_level=True)
@pytest.mark.usefixtures("browser")
class TestFillForm:
    form_methods = FormMethods()

    def test_click_on_forms(self, browser):
        self.form_methods.click_element(browser, By.XPATH, Elements.forms_category)
        assert self.form_methods.verify_url(browser, "https://demoqa.com/forms")

    def test_click_on_practice_form(self, browser):
        self.form_methods.click_element(browser, By.XPATH, Elements.form_subcategory)
        assert self.form_methods.verify_url(browser, "https://demoqa.com/automation-practice-form")

    def test_fill_name(self, browser):
        self.form_methods.fill(browser, By.ID, Elements.first_name, 'Bob')
        assert self.form_methods.validate_field(browser, By.ID, Elements.first_name, "Bob")

        self.form_methods.fill(browser, By.ID, Elements.last_name, 'The Builder')
        assert self.form_methods.validate_field(browser, By.ID, Elements.last_name, 'The Builder')

    def test_select_gender(self, browser):
        self.form_methods.click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.gender_male}']")
        assert self.form_methods.is_element_selected(browser, By.ID, Elements.gender_male)

    def test_fill_mobile_nr(self, browser):
        # make a function that encapsulates the insertion of a wrong number

        self.form_methods.click_element(browser, By.ID, Elements.mobile_number)
        self.form_methods.fill(browser, By.ID, Elements.mobile_number, 'wrong number')
        self.form_methods.clear_field(browser, By.ID, Elements.mobile_number)
        self.form_methods.fill(browser, By.ID, Elements.mobile_number, '0722333446')
        assert self.form_methods.validate_field(browser, By.ID, Elements.mobile_number, '0722333446')

    def test_fill_calendar(self, browser):
        self.form_methods.clear_calendar_date(browser, By.ID, Elements.date_of_birth)
        self.form_methods.fill(browser, By.ID, Elements.date_of_birth, "3 Sep 2023")
        assert self.form_methods.validate_field(browser, By.ID, Elements.date_of_birth, "23 Sep 2023")

    def test_select_hobbies(self, browser):
        self.form_methods.click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.hobbies_sports}']")
        assert self.form_methods.is_element_selected(browser, By.ID, Elements.hobbies_sports)

        self.form_methods.click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.hobbies_music}']")
        assert self.form_methods.is_element_selected(browser, By.ID, Elements.hobbies_music)

    def test_scroll_to_the_bottom(self, browser):
        self.form_methods.scroll_to_the_bottom(browser)
        assert self.form_methods.is_element_displayed(browser, By.ID, Elements.state)

    def test_select_state(self, browser):
        self.form_methods.click_element(browser, By.ID, Elements.state)
        self.form_methods.click_element(browser, By.XPATH, Elements.haryana)
        # assert Methods().validate_field(browser, By.XPATH, Elements.haryana, "Haryana")

    def test_select_city(self, browser):
        self.form_methods.click_element(browser, By.ID, Elements.city)
        self.form_methods.click_element(browser, By.ID, Elements.karnal)

    def test_submit_form(self, browser):
        self.form_methods.submit_form(browser, By.ID, Elements.form)
        self.form_methods.maximize_window(browser)
        assert self.form_methods.is_element_displayed(browser, By.CSS_SELECTOR, Elements.modal_form_result)

    def test_close_modal(self, browser):
        self.form_methods.close_modal(browser, By.ID, Elements.close_modal)
        assert self.form_methods.verify_url(browser, 'https://demoqa.com/automation-practice-form')
