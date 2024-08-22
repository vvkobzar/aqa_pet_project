import os
import allure
import pytest

from dotenv import load_dotenv
from pages.book_store_application_page import LoginPage

load_dotenv()


@allure.epic("UI Tests")
@allure.feature("Book Store Application")
class TestBookStoreApplication:

    @allure.story("Login")
    class TestLoginPage:

        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')

        @allure.title("Register to book store")
        @pytest.mark.xfail(reason="It's not going through because of the captcha.")
        # @pytest.fixture(scope='function', autouse=True)
        def register_to_book_store(self, driver):
            login_page = LoginPage(driver)
            login_page.open()

            self.username, self.password = login_page.fill_fields_register_form()
            success_alert = login_page.check_register_success()

            with allure.step("Check registration success"):
                assert success_alert == "User Register Successfully.", (
                    "error during user registration"
                )

            yield

            with allure.step("Delete user"):
                delite_alert = login_page.delete_user()
                assert delite_alert == "User Deleted.", (
                    "failed to delete a user"
                )

        @allure.title("Login to book store")
        def test_login_to_book_store(self, driver):
            login_page = LoginPage(driver)
            login_page.open()

            login_page.login_to_book_store(self.username, self.password)
            url_page, profile_user_name_text = login_page.check_login_success()

            with allure.step(f"Assert URL is correct: {url_page}"):
                assert url_page == "https://demoqa.com/profile", (
                    "the profile page didn't open"
                )
            with allure.step(f"Assert profile user name matches: {profile_user_name_text}"):
                assert self.username == profile_user_name_text, (
                    "user name does not match the name in the profile"
                )
