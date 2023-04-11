import time

import pytest
from driver.driver import Driver
from pages.elements.methods import Elements

'''
This method uses conftest, to get the browser fixture as a parameter
'''

# # method 1
# class TestTextBox:
#
#     @staticmethod
#     def test_text_box(browser):
#         browser.get(Driver.URL_demoqa)
#
#         Elements().click_checkbox(browser)
#         Elements().click_expand_home(browser)
#         Elements().click_documents(browser)
#         assert Elements().check_documents(browser)


'''
This method uses browser_initialization function from driver, while skipping conftest
It also closes the browser as a last step, since we can't do that with browser function within conftest
'''

# method 2
# class TestTextBox:
#     browser = Driver.browser_initialization()
#
#     def test_select_checkbox(self):
#         assert Elements().check_checkbox(self.browser)
#         Elements().click_checkbox(self.browser)
#
#     def test_expand_home(self):
#         assert Elements().check_home_title(self.browser)
#         Elements().click_expand_home(self.browser)
#
#     def test_click_documents(self):
#         assert Elements().check_documents_title(self.browser)
#         Elements().click_documents(self.browser)
#
#     def test_check_results(self):
#         assert Elements().check_documents(self.browser)
#
#     def test_teardown(self):
#         self.browser.quit()


'''
This method uses conftest and splits each action into a test
check this for future reminders
https://www.seleniumeasy.com/python/webdriver-tests-in-pytest-using-fixtures-and-conftest
'''


# method 3
@pytest.mark.usefixtures("browser")
class TestTextBox:

    def test_verify_checkbox_visibility(self):
        assert Elements().check_elements(self.driver)

        if Elements().check_checkbox(self.driver):
            pytest.skip()

        Elements().click_elements(self.driver)

    def test_select_checkbox(self):
        assert Elements().check_checkbox(self.driver)
        Elements().click_checkbox(self.driver)

    def test_expand_home(self):
        assert Elements().check_home_title(self.driver)
        Elements().click_expand_home(self.driver)

    @pytest.mark.xfail(reason='Documents is not visible after you refresh the page')
    def test_preemptive_fail(self):
        self.driver.refresh()
        Elements().click_expand_home(self.driver)

    def test_click_documents(self):
        assert Elements().check_documents_title(self.driver)
        Elements().click_documents(self.driver)

    def test_check_results(self):
        assert Elements().check_documents(self.driver)
