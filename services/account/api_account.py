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

    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            json=self.payloads.username_password
        )
        assert response.status_code == 201
        self.attach_response(response.json())
        model = CreateUserResponse(**response.json())
        return model.userID

    def generate_user_token(self):
        response = requests.post(
            url=self.endpoints.generate_token,
            json=self.payloads.username_password
        )
        assert response.status_code == 200
        self.attach_response(response.json())
        model = TokenResponse(**response.json())
        return model.token

    def delete_user(self, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_user(user_id),
            headers=self.headers.basic(token)
        )
        try:
            assert response.status_code == 204
        except AssertionError as e:
            raise AssertionError(f"Expected status code 200 but got {response.status_code}.") from e

    def authorized(self):
        response = requests.post(
            url=self.endpoints.authorized,
            json=self.payloads.username_password
        )
        assert response.status_code == 200, response.status_code
        assert response.json() is True
        self.attach_response(response.json())

    def get_user(self, user_id, token):
        response = requests.get(
            url=self.endpoints.get_user(user_id),
            headers=self.headers.basic(token),
        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = User(**response.json())
        if len(model.books) >= 1:
            isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
            return isbn_books
        return model
