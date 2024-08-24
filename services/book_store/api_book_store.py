import allure
import requests
from utils.helper import Helper
from config.headers import Headers
from services.book_store.payloads import Payloads
from services.book_store.endpoints import Endpoints
from generator.generator import random_selection_of_isbn_from_the_book_list
from services.book_store.models.book_store_model import GetBooksResponse, PostBooksResponse, Book


class BookStoreAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Get isbn books list")
    def get_isbn_books_list(self):
        response = requests.get(
            url=self.endpoints.get_books
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
        with allure.step("Validation get books model"):
            model = GetBooksResponse(**response.json())
        isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
        return isbn_books

    @allure.step("Get information books list")
    def get_information_books_list(self):
        response = requests.get(
            url=self.endpoints.get_books
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
        with allure.step("Validation get books model"):
            model = GetBooksResponse(**response.json())
        return model.books

    @allure.step("Added books in the profile")
    def added_books_in_the_profile(self, isbn, user_id, token):
        response = requests.post(
            url=self.endpoints.post_books,
            headers=self.headers.basic(token),
            json=self.payloads.post_books(user_id, isbn)
        )
        self.assert_response_status_code(response, 201)
        self.attach_response(response.json())
        with allure.step("Validation post books model"):
            model = PostBooksResponse(**response.json())
        isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
        return isbn_books

    @allure.issue("no json comes in the response")
    @allure.step("Delete books")
    def delete_books(self, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_books(user_id),
            headers=self.headers.basic(token)
        )
        self.assert_response_status_code(response, 204)

    @allure.issue("no json comes in the response")
    @allure.step("Delete book")
    def delete_book(self, isbn, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_book,
            headers=self.headers.basic(token),
            json=self.payloads.delete_book(isbn, user_id)
        )
        self.assert_response_status_code(response, 204)

    @allure.step("Getting information about the book")
    def get_book(self, isbn, token):
        response = requests.get(
            url=self.endpoints.get_book(isbn),
            headers=self.headers.basic(token)
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
        with allure.step("Validation book model"):
            model = Book(**response.json())
        return model

    @allure.issue("502 status code")
    @allure.step("Changing the book in the profile")
    def put_books(self, old_isbn, new_isbn, user_id, token):
        response = requests.put(
            url=self.endpoints.put_book(old_isbn),
            headers=self.headers.basic(token),
            json=self.payloads.put_books(user_id, new_isbn)
        )
        self.assert_response_status_code(response, 200)
        self.attach_response(response.json())
