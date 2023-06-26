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


def test_refresh_and_confirm(browser):
    Methods().refresh_page(browser)
    assert browser.find_element(By.ID, "firstName").get_attribute("value") == ''
    assert not browser.find_element(By.ID, "gender-radio-1").is_selected()
