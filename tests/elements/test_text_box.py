from driver.driver import Driver
from pages.elements import Elements


def test_open_elements_checkbox(browser):
    browser.get(Driver.URL_demoqa)

    Elements().click_checkbox(browser)
    Elements().click_expand_home(browser)
    Elements().click_documents(browser)
    assert Elements().check_documents(browser).is_displayed()
