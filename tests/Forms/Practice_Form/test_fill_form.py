import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.Practice_Form.elements import Elements
from pages.Practice_Form.methods import Methods


# @pytest.mark.usefixtures("browser")
# @pytest.skip(allow_module_level=True)
def test_refresh_form(browser):
    Methods().click_element(browser, By.XPATH, Elements.forms_category)
    Methods().click_element(browser, By.XPATH, Elements.form_subcategory)

    Methods().fill(browser, By.ID, Elements.first_name, 'Bob')
    Methods().fill(browser, By.ID, Elements.last_name, 'The Builder')
    assert Methods().validate_field(browser, By.ID, Elements.first_name, "Bob")
    # assert browser.find_element(By.ID, Elements.first_name).get_attribute("value") == "Bob"

    browser.find_element(By.CSS_SELECTOR, f"label[for='{Elements.gender_male}']").click()
    assert browser.find_element(By.ID, Elements.gender_male).is_selected()

    browser.find_element(By.ID, Elements.mobile_number).click()
    assert browser.find_element(By.ID, Elements.mobile_number).is_enabled()
    browser.find_element(By.ID, Elements.mobile_number).send_keys('wrong number')
    browser.find_element(By.ID, Elements.mobile_number).clear()
    browser.find_element(By.ID, Elements.mobile_number).send_keys('0722333446')

    for i in range(len(browser.find_element(By.ID, "dateOfBirthInput").get_attribute('value'))-1):
        browser.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.BACKSPACE)

    browser.find_element(By.ID, Elements.date_of_birth).send_keys("3 Sep 2023")
    assert browser.find_element(By.ID, Elements.date_of_birth).get_attribute('value') == "23 Sep 2023"

    browser.find_element(By.CSS_SELECTOR, f"label[for='{Elements.hobbies_sports}']").click()
    assert browser.find_element(By.ID, Elements.hobbies_sports).is_selected()

    browser.find_element(By.CSS_SELECTOR, f"label[for='{Elements.hobbies_music}']").click()
    assert browser.find_element(By.ID, Elements.hobbies_music).is_selected()


    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    browser.find_element(By.ID, Elements.state).click()
    browser.find_element(By.ID, Elements.haryana).click()

    browser.find_element(By.ID, Elements.city).click()
    browser.find_element(By.ID, Elements.karnal).click()

    browser.find_element(By.ID, Elements.form).submit()
    browser.fullscreen_window()
    time.sleep(5)
    browser.find_element(By.ID, Elements.close_modal).click()
