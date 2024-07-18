class TextBoxPageLocators:
    # form fields
    FULL_NAME = ("xpath", "//input[@id='userName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    CURRENT_ADDRESS = ("xpath", "//textarea[@id='currentAddress']")
    PERMANENT_ADDRESS = ("xpath", "//textarea[@id='permanentAddress']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    # created from
    CREATED_FULL_NAME = ("xpath", "//p[@id='name']")
    CREATED_EMAIL = ("xpath", "//p[@id='email']")
    CREATED_CURRENT_ADDRESS = ("xpath", "//p[@id='currentAddress']")
    CREATED_PERMANENT_ADDRESS = ("xpath", "//p[@id='permanentAddress']")


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = ("xpath", "//button[@aria-label='Expand all']")
    ITEMS_LIST = ("xpath", "//span[@class='rct-checkbox']")
    CHECKED_ITEMS = ("css selector", "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ("xpath", ".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULT = ("xpath", "//span[@class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO_ACTIVE = ("xpath", "//label[@for='yesRadio']")
    IMPRESSIVE_RADIO_ACTIVE = ("xpath", "//label[@for='impressiveRadio']")
    NO_RADIO_ACTIVE = ("xpath", "//label[@for='noRadio']")

    YES_RADIO_STATUS = ("xpath", "//input[@id='yesRadio']")
    IMPRESSIVE_RADIO_STATUS = ("xpath", "//input[@id='impressiveRadio']")
    NO_RADIO_STATUS = ("xpath", "//input[@id='noRadio']")


class WebTablesPageLocators:
    # add person form
    ADD_BUTTON = ("xpath", "//button[@id='addNewRecordButton']")
    FIRST_NAME = ("xpath", "//input[@id='firstName']")
    LAST_NAME = ("xpath", "//input[@id='lastName']")
    EMAIL = ("xpath", "//input[@id='userEmail']")
    AGE = ("xpath", "//input[@id='age']")
    SALARY = ("xpath", "//input[@id='salary']")
    DEPARTMENT = ("xpath", "//input[@id='department']")
    SUBMIT_BUTTON = ("xpath", "//button[@id='submit']")

    # table
    FULL_PEOPLE_LIST = ("xpath", "//div[@class='rt-tr-group']")
    SEARCH_FIELD = ("xpath", "//input[@id='searchBox']")
    DELETE_PERSON_BUTTON = ("xpath", "//span[@title='Delete']")
    NO_ROWS_FOUND = ("xpath", "//div[@class='rt-noData']")
    ROW_PERSON = ("xpath", "//div[@class='rt-tr-group']")
    COUNT_ROW_LIST = ("xpath", "//select[@aria-label='rows per page']")

    # update
    UPDATE_BUTTON = ("xpath", "//span[@title='Edit']")


class ButtonsPageLocators:
    DOUBLE_CLICK_ME_BUTTON = ("xpath", "//button[@id='doubleClickBtn']")
    RIGHT_CLICK_ME_BUTTON = ("xpath", "//button[@id='rightClickBtn']")
    CLICK_ME_BUTTON = ("xpath", "//button[text()='Click Me']")

    DOUBLE_CLICK_MESSAGE = ("xpath", "//p[@id='doubleClickMessage']")
    RIGHT_CLICK_MESSAGE = ("xpath", "//p[@id='rightClickMessage']")
    CLICK_ME_MESSAGE = ("xpath", "//p[@id='dynamicClickMessage']")


class LinksPageLocators:
    # following links will open new tab
    HOME_LINK = ("xpath", "//a[@id='simpleLink']")
    DYNAMIC_HOME_LINK = ("xpath", "//a[@id='dynamicLink']")


class UploadAndDownloadPageLocators:
    DOWNLOAD_BUTTON = ("xpath", "//a[@id='downloadButton']")
    CHOOSE_FILE_BUTTON = ("xpath", "//input[@id='uploadFile']")
    UPLOADED_FILE_PATH = ("xpath", "//p[@id='uploadedFilePath']")


class DynamicPropertiesPageLocators:
    WILL_ENABLE_5_SECONDS_BUTTON = ("xpath", "//button[@id='enableAfter']")
    COLOR_CHANGE_BUTTON = ("xpath", "//button[@id='colorChange']")
