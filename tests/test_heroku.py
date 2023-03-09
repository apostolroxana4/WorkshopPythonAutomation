from driver.driver import Driver

def test_open_page(browser):
    browser.get(Driver.URL)