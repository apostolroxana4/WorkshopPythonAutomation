from driver.driver import Driver

def test_open_herokuapp_page(browser):
    browser.get(Driver.URL)

    btnDropdown = browser.find_element('xpath', )