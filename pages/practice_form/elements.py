class Elements:
    forms_category = "//*[contains(text(),'Forms')]"
    forms_category_url = "https://demoqa.com/forms"
    form_subcategory = "//*[contains(text(),'Practice')]"
    form_subcategory_url = "https://demoqa.com/automation-practice-form"

    first_name = "firstName"
    first_name_value = 'Bob'
    last_name = "lastName"
    last_name_value = "The Builder"

    gender_male = "gender-radio-1"
    gender_male_value = f"label[for='{gender_male}']"

    mobile_number = "userNumber"
    mobile_number_value = '0722333446'

    date_of_birth = "dateOfBirthInput"
    date_day = ".react-datepicker__day--013"
    date_month_year = ".react-datepicker__current-month"
    month_dict = {'January': 'Jan ', 'February': 'Feb ', 'March': 'Mar ', 'April': 'Apr ', 'May': 'May ',
                  'June': 'Jun ',
                  'July': 'Jul '
                  }

    hobbies_sports = "hobbies-checkbox-1"
    hobbies_sports_value = f"label[for='{hobbies_sports}']"
    hobbies_music = "hobbies-checkbox-3"
    hobbies_music_value = f"label[for='{hobbies_music}']"

    state = 'state'
    haryana = "//*[contains(text(),'Haryana')]"
    city = 'city'
    karnal = 'react-select-4-option-0'

    form = "userForm"
    close_modal = 'closeLargeModal'

    modal_form_result = '.modal-content'
