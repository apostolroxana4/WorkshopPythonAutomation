from selenium.webdriver.common.by import By


class ItemsElementsSection:
    main_page_elements = "div[class='card mt-4 top-card']"
    section_elements = "//*[contains(text(),'Elements')]"
    subsection_checkbox = "//*[@id='item-1']"
    home_item = "//*[contains(text(),'Home')]"
    expand_home = "svg[class='rct-icon rct-icon-expand-close']"
    downloads_item = "//*[contains(text(),'Downloads')]"
    downloads_result = "span[class='text-success']"
    downloads_word = "result"
    expand_documents = "svg[class='rct-icon rct-icon-expand-close']"
    documents_item = "//*[contains(text(),'Documents')"
    office_item = "//*[contains(text(),'Office')]"
    workspace_item = "//*[contains(text(),'Workspace')]"
    documents_office_result = "result"
    documents_workspace_result = "result"
    documents_office_public_result = "span[class='text-success']"
    documents_workspace_angular_result = "span[class='text-success']"
    username_field = "//label[@id='userName-label']"
    username = "userName"
    email_field = "//label[@id='userEmail-label']"
    email = "//*[@id='userEmail']"
    current_address_field = "//label[@id='currentAddress-label']"
    current_address = "#currentAddress"
    permanent_address_field = "//label[@id='permanentAddress-label']"
    permanent_address = "permanentAddress"
    submit_button = "submit"


class ItemsWidgetsSection:
    widgets_from_main = "div[class='card mt-4 top-card']"
    widgets_section = "//*[contains(text(),'Widgets')]"
    subsection_select_menu = "//*[@id='item-8']"
    select_value_item = "div[class=' css-2b097c-container']"
    another_root_option_item = "//*[@id='react-select-2-option-3']"
    select_one_item = "//*[@id='selectOne']"
    prof_option_item = "//*[@id='react-select-3-option-0-4']"
    old_style_select_menu_item = "//*[@id='oldSelectMenu']"
    multiselect_dropdown_item = "div[class=' css-2b097c-container']"


class ItemsFormsSection:
    forms_from_main = "//*[contains(text(),'Forms')]"
    forms_subsection = "//*[contains(text(),'Practice')]"
    first_name_item = "firstName"
    last_name_item = "lastName"
    email_item = "userEmail"
    gender_male_radio_button = "//label[@for='gender-radio-1']"
    gender_female_radio_button = "//label[@for='gender-radio-2']"
    gender_other_radio_button = "//label[@for='gender-radio-3']"
    male_item = "gender-radio-1"
    female_item = "gender-radio-2"
    other_item = "gender-radio-3"
    form_url = "https://demoqa.com/forms"
    first_name_value = 'Jack'
    last_name_value_wrong = 'Taylor'
    last_name_value_correctly = 'Maylor'
    email_value = "jackmaylor@gmail.com"

class StepsElements(ItemsElementsSection):

    def fill_credentials(self, browser, username, email, permanent_address):
        if (
                (not browser.find_element(By.ID, self.username).is_displayed())
                or (not browser.find_element(By.XPATH, self.email).is_displayed())
                #or (not browser.find_element(By.CSS_SELECTOR, self.current_address).is_displayed())
                or (not browser.find_element(By.ID, self.permanent_address).is_displayed())
        ):
            raise ValueError("Fields are not visible")

        return (
                (browser.find_element(By.ID, self.username) == username)
                and (browser.find_element(By.XPATH, self.email) == email)
                #and (browser.find_element(By.CSS_SELECTOR, self.current_address) == current_address)
                and (browser.find_element(By.ID, self.permanent_address) == permanent_address)
                     )
