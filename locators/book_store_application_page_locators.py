class LoginPageLocators:
    USER_NAME_INPUT = ("xpath", "//input[@id='userName']")
    PASSWORD_INPUT = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//button[@id='login']", )
    LOG_OUT = ("xpath", "//button[@id='submit']")
    PROFILE_USER_NAME_TEXT = ("xpath", "//label[@id='userName-value']")
    LOGIN_ERROR_NOTIFICATION = ("xpath", "//p[text()='Invalid username or password!']")


class RegisterPageLocators:
    NEW_USER_BUTTON = ("xpath", "//button[@id='newUser']")
    REGISTER_BUTTON = ("xpath", "//button[@id='register']")
    BACK_TO_LOGIN_BUTTON = ("xpath", "//button[@id='gotologin']")
    FIRST_NAME_INPUT = ("xpath", "//input[@id='firstname']")
    LAST_NAME_INPUT = ("xpath", "//input[@id='lastname']")
    USER_NAME_INPUT = ("xpath", "//input[@id='userName']")
    PASSWORD_INPUT = ("xpath", "//input[@id='password']")
    RECAPTCHA_IFRAME = ("xpath", "//iframe[@title='reCAPTCHA']")
    RECAPTCHA_CHECKBOX = ("xpath", "//div[@class='recaptcha-checkbox-border']")
    DELETE_ACCOUNT_BUTTON = ("xpath", "//button[text()='Delete Account']")
    MODAL_DELETE_ACCOUNT_BUTTON = ("xpath", "//button[@id='closeSmallModal-ok']")
