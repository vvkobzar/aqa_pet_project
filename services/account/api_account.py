import allure
import requests
from config.headers import Headers
from services.account.payloads import Payloads
from services.account.endpoints import Endpoints
from utils.helper import Helper
from generator.generator import random_selection_of_isbn_from_the_book_list
from services.account.models.account_model import CreateUserResponse, TokenResponse, User


class AccountAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            json=self.payloads.username_password
        )
        self.assert_response_status_code(response, 201)
        self.attach_response(response.json())
        with allure.step("Validation create user model"):
            model = CreateUserResponse(**response.json())
        return model.userID

    @allure.step("Generate user token")
    def generate_user_token(self):
        response = requests.post(
            url=self.endpoints.generate_token,
            json=self.payloads.username_password
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
        with allure.step("Validation generate user token model"):
            model = TokenResponse(**response.json())
        return model.token

    @allure.step("Delete user")
    def delete_user(self, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_user(user_id),
            headers=self.headers.basic(token)
        )
        self.assert_response_status_code(response, 204)

    @allure.step("Authorized user status")
    def authorized(self):
        response = requests.post(
            url=self.endpoints.authorized,
            json=self.payloads.username_password
        )
        self.assert_response_status_code(response, 200)
        assert response.json() is True
        self.attach_response(response.json())

    @allure.step("Get information about the user and books in his profile")
    def get_user(self, user_id, token):
        response = requests.get(
            url=self.endpoints.get_user(user_id),
            headers=self.headers.basic(token),
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
        with allure.step("Validation user model"):
            model = User(**response.json())
        if len(model.books) >= 1:
            isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
            return isbn_books
        return model
