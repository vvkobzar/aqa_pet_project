import pytest
from pages.book_store_application_page import LoginPage


class TestBookStoreApplication:
    class TestLoginPage:
        username = None
        password = None

        # @pytest.fixture(scope='function', autouse=True)
        def register_to_book_store(self, driver):
            login_page = LoginPage(driver)

            self.username, self.password = login_page.fill_fields_register_form()
            success_alert = login_page.check_register_success()

            assert success_alert == "User Register Successfully."

            yield

            delite_alert = login_page.delete_user()
            assert delite_alert == "User Deleted."

        def test_login_to_book_store(self, driver):
            login_page = LoginPage(driver)
            login_page.open()

            login_page.check_login_to_book_store(self.username, self.password)
            url_page, profile_user_name_text = login_page.check_login_success()

            assert url_page == "https://demoqa.com/profile"
            assert self.username == profile_user_name_text
