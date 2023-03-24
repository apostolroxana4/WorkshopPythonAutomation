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
class TestTextBox:

    browser = Driver.browser_initialization()

    def test_select_checkbox(self):
        Elements().click_checkbox(self.browser)

    def test_expand_home(self):
        Elements().click_expand_home(self.browser)

    def test_click_documents(self):
        Elements().click_documents(self.browser)

    def test_check_results(self):
        assert Elements().check_documents(self.browser)

    def test_teardown(self):
        self.browser.quit()
