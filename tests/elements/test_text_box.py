from driver.driver import Driver
from pages.elements.methods import Elements


class TestTextBox:

    @staticmethod
    def test_text_box(browser):
        browser.get(Driver.URL_demoqa)

        Elements().click_checkbox(browser)
        Elements().click_expand_home(browser)
        Elements().click_documents(browser)
        assert Elements().check_documents(browser)
