from driver.driver import Driver

def test_open_heroku_page(browser):
    browser.get(Driver.URL)