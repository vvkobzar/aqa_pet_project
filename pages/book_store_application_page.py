import allure

from config.links import BookStoreApplicationPageLink
from generator.generator import generated_person
from locators.book_store_application_page_locators import LoginPageLocators, RegisterPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_URL = BookStoreApplicationPageLink.LOGIN
    login_locators = LoginPageLocators()
    register_locators = RegisterPageLocators()

    @allure.step("Fill registration fields")
    def fill_fields_register_form(self):
        person = next(generated_person())
        with allure.step(f"Click new user button"):
            self.element_is_visible(self.register_locators.NEW_USER_BUTTON).click()
        with allure.step(f"Enter first name: {person.firstname}"):
            self.element_is_visible(self.register_locators.FIRST_NAME_INPUT).send_keys(person.firstname)
        with allure.step(f"Enter last name: {person.lastname}"):
            self.element_is_visible(self.register_locators.LAST_NAME_INPUT).send_keys(person.lastname)
        with allure.step(f"Enter username: {person.username}"):
            self.element_is_visible(self.register_locators.USER_NAME_INPUT).send_keys(person.username)
        with allure.step(f"Enter password"):
            self.element_is_visible(self.register_locators.PASSWORD_INPUT).send_keys(person.password)
        with allure.step("Pass captcha"):
            self.passing_captcha_in_the_register_form()
        with allure.step("Click register button"):
            self.element_is_visible(self.register_locators.REGISTER_BUTTON).click()
        return person.username, person.password

    @allure.step("Pass captcha in the registration form")
    def passing_captcha_in_the_register_form(self):
        with allure.step("Switch to captcha iframe and click checkbox"):
            captcha_frame = self.element_is_present(self.register_locators.RECAPTCHA_IFRAME)
            self.switch_to_frame(captcha_frame)
            self.element_is_visible(self.register_locators.RECAPTCHA_CHECKBOX).click()
        with allure.step("Switch back to default content"):
            self.driver.switch_to.default_content()

    @allure.step("Check registration success")
    def check_register_success(self):
        with allure.step("Get and accept success alert"):
            success_alert = self.alert_is_present()
            success_alert_text = success_alert.text
            success_alert.accept()
            self.driver.switch_to.default_content()
        return success_alert_text

    @allure.step("Check login success")
    def check_login_success(self):
        try:
            with allure.step("Retrieve profile user name text"):
                profile_user_name_text = self.element_is_visible(self.login_locators.PROFILE_USER_NAME_TEXT).text
            with allure.step("Get current URL page"):
                url_page = self.get_url_page()
            return url_page, profile_user_name_text
        except Exception:
            with allure.step("Retrieve login error notification text"):
                login_error_notification = self.element_is_visible(self.login_locators.LOGIN_ERROR_NOTIFICATION)
                error_message = login_error_notification.text
            raise RuntimeError(error_message)

    @allure.step("Delete user")
    def delete_user(self):
        with allure.step("Navigate to profile page and click delete account button"):
            self.driver.get(BookStoreApplicationPageLink.PROFILE)
            self.element_is_visible(self.register_locators.DELETE_ACCOUNT_BUTTON).click()
            self.element_is_visible(self.register_locators.MODAL_DELETE_ACCOUNT_BUTTON).click()
        with allure.step("Get and accept delete account alert"):
            delite_alert = self.alert_is_present()
            delite_alert_text = delite_alert.text
            delite_alert.accept()
        return delite_alert_text

    @allure.step("Login to book store with username: {username}")
    def login_to_book_store(self, username, password):
        with allure.step("Enter username"):
            self.element_is_visible(self.login_locators.USER_NAME_INPUT).send_keys(username)
        with allure.step("Enter password"):
            self.element_is_visible(self.login_locators.PASSWORD_INPUT).send_keys(password)
        with allure.step("Click login button"):
            self.element_is_visible(self.login_locators.LOGIN_BUTTON).click()
