from config.links import BookStoreApplicationPageLink
from generator.generator import generated_person
from locators.book_store_application_page_locators import LoginPageLocators, RegisterPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = BookStoreApplicationPageLink.LOGIN
    login_locators = LoginPageLocators()
    register_locators = RegisterPageLocators()

    def fill_fields_register_form(self):
        person = next(generated_person())
        self.element_is_visible(self.register_locators.NEW_USER_BUTTON).click()
        self.element_is_visible(self.register_locators.FIRST_NAME_INPUT).send_keys(person.firstname)
        self.element_is_visible(self.register_locators.LAST_NAME_INPUT).send_keys(person.lastname)
        self.element_is_visible(self.register_locators.USER_NAME_INPUT).send_keys(person.username)
        self.element_is_visible(self.register_locators.PASSWORD_INPUT).send_keys(person.password)
        self.passing_captcha_in_the_register_form()
        self.element_is_visible(self.register_locators.REGISTER_BUTTON).click()
        return person.username, person.password

    def passing_captcha_in_the_register_form(self):
        captcha_frame = self.element_is_present(self.register_locators.RECAPTCHA_IFRAME)
        self.switch_to_frame(captcha_frame)
        self.element_is_visible(self.register_locators.RECAPTCHA_CHECKBOX).click()
        self.driver.switch_to.default_content()

    def check_register_success(self):
        success_alert = self.alert_is_present()
        success_alert_text = success_alert.text
        success_alert.accept()
        self.driver.switch_to.default_content()
        return success_alert_text

    def check_login_success(self):
        profile_user_name_text = self.element_is_visible(self.login_locators.PROFILE_USER_NAME_TEXT, timeout=10).text
        url_page = self.get_url_page()
        return url_page, profile_user_name_text

    def delete_user(self):
        self.driver.get(BookStoreApplicationPageLink.PROFILE)
        self.element_is_visible(self.register_locators.DELETE_ACCOUNT_BUTTON).click()
        self.element_is_visible(self.register_locators.MODAL_DELETE_ACCOUNT_BUTTON).click()
        delite_alert = self.alert_is_present()
        delite_alert_text = delite_alert.text
        delite_alert.accept()
        return delite_alert_text

    def login_to_book_store(self, username, password):
        self.element_is_visible(self.login_locators.USER_NAME_INPUT).send_keys(username)
        self.element_is_visible(self.login_locators.PASSWORD_INPUT).send_keys(password)
        self.element_is_visible(self.login_locators.LOGIN_BUTTON).click()
