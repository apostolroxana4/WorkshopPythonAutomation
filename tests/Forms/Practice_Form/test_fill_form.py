import pytest
from selenium.webdriver.common.by import By
from pages.Practice_Form.elements import Elements
from pages.Practice_Form.methods import Methods


# @pytest.skip(allow_module_level=True)
def test_click_on_forms(browser):
    Methods().click_element(browser, By.XPATH, Elements.forms_category)
    assert Methods().verify_url(browser, "https://demoqa.com/forms")


def test_click_on_practice_form(browser):
    Methods().click_element(browser, By.XPATH, Elements.form_subcategory)
    assert Methods().verify_url(browser, "https://demoqa.com/automation-practice-form")


def test_fill_name(browser):
    Methods().fill(browser, By.ID, Elements.first_name, 'Bob')
    assert Methods().validate_field(browser, By.ID, Elements.first_name, "Bob")

    Methods().fill(browser, By.ID, Elements.last_name, 'The Builder')
    assert Methods().validate_field(browser, By.ID, Elements.last_name, 'The Builder')


def test_select_gender(browser):
    Methods().click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.gender_male}']")
    assert Methods().is_element_selected(browser, By.ID, Elements.gender_male)


def test_fill_mobile_nr(browser):
    Methods().click_element(browser, By.ID, Elements.mobile_number)
    Methods().fill(browser, By.ID, Elements.mobile_number, 'wrong number')
    Methods().clear_field(browser, By.ID, Elements.mobile_number)
    Methods().fill(browser, By.ID, Elements.mobile_number, '0722333446')
    assert Methods().validate_field(browser, By.ID, Elements.mobile_number, '0722333446')


def test_fill_calendar(browser):
    Methods().clear_calendar_date(browser, By.ID, Elements.date_of_birth)
    Methods().fill(browser, By.ID, Elements.date_of_birth, "3 Sep 2023")
    assert Methods().validate_field(browser, By.ID, Elements.date_of_birth, "23 Sep 2023")


def test_select_hobbies(browser):
    Methods().click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.hobbies_sports}']")
    assert Methods().is_element_selected(browser, By.ID, Elements.hobbies_sports)

    Methods().click_element(browser, By.CSS_SELECTOR, f"label[for='{Elements.hobbies_music}']")
    assert Methods().is_element_selected(browser, By.ID, Elements.hobbies_music)


def test_scroll_to_the_bottom(browser):
    Methods().scroll_to_the_bottom(browser)
    assert Methods().is_element_displayed(browser, By.ID, Elements.state)


def test_select_state(browser):
    Methods().click_element(browser, By.ID, Elements.state)
    Methods().click_element(browser, By.XPATH, Elements.haryana)
    # assert Methods().validate_field(browser, By.XPATH, Elements.haryana, "Haryana")


def test_select_city(browser):
    Methods().click_element(browser, By.ID, Elements.city)
    Methods().click_element(browser, By.ID, Elements.karnal)


def test_submit_form(browser):
    Methods().submit_form(browser, By.ID, Elements.form)
    Methods().maximize_window(browser)
    assert Methods().is_element_displayed(browser, By.CSS_SELECTOR, Elements.modal_form_result)


def test_close_modal(browser):
    Methods().close_modal(browser, By.ID, Elements.close_modal)
    assert Methods().verify_url(browser, 'https://demoqa.com/automation-practice-form')