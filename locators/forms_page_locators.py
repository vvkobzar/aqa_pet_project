import random


class PracticeFormPageLocators:
    # name
    FIRST_NAME_FIELD = ("xpath", "//input[@id='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@id='lastName']")
    # email
    EMAIL_FIELD = ("xpath", "//input[@id='userEmail']")
    # gender
    GENDER_RADIO_BUTTON = ("xpath", "//div[@class='custom-control custom-radio custom-control-inline']/label")
    # mobile
    MOBILE_NUMBER_FIELD = ("xpath", "//input[@id='userNumber']")
    # date of birth
    DATE_OF_BIRTH_CALENDAR = ("xpath", "//input[@id='dateOfBirthInput']")
    CALENDAR_MONTH_SELECT = ("xpath", "//select[@class='react-datepicker__month-select']")
    GET_MONTH_AND_YEAR = ("xpath", "//div[@class='react-datepicker__current-month "
                                   "react-datepicker__current-month--hasYearDropdown "
                                   "react-datepicker__current-month--hasMonthDropdown']")
    SELECTED_MONTH_CALENDAR = ("xpath", "//select[@class='react-datepicker__month-select']/option")
    CALENDAR_YEAR_SELECT = ("xpath", "//select[@class='react-datepicker__year-select']")
    CALENDAR_DAY = ("xpath", "//div[@role='option']")
    # subjects
    SUBJECTS_FIELD = ("xpath", "//input[@id='subjectsInput']")
    # hobbies
    HOBBIES_CHECK_BOX = ("xpath", "//div[@class='custom-control custom-checkbox custom-control-inline']//label")
    READING_CHECK_BOX = ("xpath", "//input[@id='hobbies-checkbox-2']")
    MUSIC_CHECK_BOX = ("xpath", "//input[@id='hobbies-checkbox-3']")
    # picture
    PICTURE_CHOOSE_FILE_BUTTON = ("xpath", "//input[@id='uploadPicture']")
    # current address
    CURRENT_ADDRESS_FIELD = ("xpath", "//textarea[@id='currentAddress']")
    # state and city
    SELECT_STATE = ("xpath", "//input[@id='react-select-3-input']")
    SELECT_CITY = ("xpath", "//input[@id='react-select-4-input']")

    SUBMIT_REGISTRATION_FORM_BUTTON = ("xpath", "//button[@id='submit']")

    # table results
    RESULT_TABLE = ("xpath", "//tr/td[2]")
