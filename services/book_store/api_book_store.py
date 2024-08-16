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

    def get_isbn_books_list(self):
        response = requests.get(
            url=self.endpoints.get_books
        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = GetBooksResponse(**response.json())
        isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
        return isbn_books

    def get_information_books_list(self):
        response = requests.get(
            url=self.endpoints.get_books
        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = GetBooksResponse(**response.json())
        return model.books

    def added_books_in_the_profile(self, isbn, user_id, token):
        response = requests.post(
            url=self.endpoints.post_books,
            headers=self.headers.basic(token),
            json=self.payloads.post_books(user_id, isbn)
        )
        assert response.status_code == 201, response.status_code
        self.attach_response(response.json())
        model = PostBooksResponse(**response.json())
        isbn_books = random_selection_of_isbn_from_the_book_list(model.books)
        return isbn_books

    def delete_books(self, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_books(user_id),
            headers=self.headers.basic(token)
        )
        assert response.status_code == 204, response.status_code
        # bug: no json comes in the response

    def delete_book(self, isbn, user_id, token):
        response = requests.delete(
            url=self.endpoints.delete_book,
            headers=self.headers.basic(token),
            json=self.payloads.delete_book(isbn, user_id)
        )
        assert response.status_code == 204, response.status_code
        # bug: no json comes in the response

    def get_book(self, isbn, token):
        response = requests.get(
            url=self.endpoints.get_book(isbn),
            headers=self.headers.basic(token)
        )
        assert response.status_code == 200, response.status_code
        self.attach_response(response.json())
        model = Book(**response.json())
        return model