import allure
from base.base_api import BaseAPI
from allure_commons.types import Severity


@allure.epic("API Tests")
@allure.feature("Account")
class TestAccount(BaseAPI):

    @allure.title("User authorization status")
    def test_authorized(self):
        self.api_account.authorized()

    @allure.severity(Severity.CRITICAL)
    @allure.title("Information about the user and books in his profile")
    def test_get_user(self, account_setup):
        user_id, token = account_setup
        model = self.api_account.get_user(user_id, token)

        with allure.step("Check that the user id in the response matches the user id when the user was created"):
            assert model.userId == user_id, "user id don't match"
        with allure.step("Checking that there are no books in the profile when creating a user"):
            assert model.books == [], "there are books in the created account"
