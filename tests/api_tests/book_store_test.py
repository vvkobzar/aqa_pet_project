import random
from base.base_api import BaseAPI
import pytest


class TestBookStore(BaseAPI):

    def test_added_book_in_the_profile(self, account_setup):
        user_id, token = account_setup

        random_book_from_list = random.choice(self.api_book_store.get_isbn_books_list())
        response_book = self.api_book_store.added_books_in_the_profile(random_book_from_list, user_id, token)[0]
        book_in_the_profile = self.api_account.get_user(user_id, token)[0]

        assert random_book_from_list == book_in_the_profile, "the book has not been added to the profile"
        assert response_book == book_in_the_profile, "the books in the profile don't match the books in the response"

    @pytest.mark.xfail(
        reason="books from get_user query do not match the added books. In the ui profile the books match"
    )
    def test_added_books_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = set(self.api_book_store.get_isbn_books_list())
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        books_in_the_profile = set(self.api_account.get_user(user_id, token))

        assert isbn_books == books_in_the_profile, "added books do not match the books in the profile"

    def test_delete_all_books_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = self.api_book_store.get_isbn_books_list()
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        before_books_is_the_profile = self.api_account.get_user(user_id, token)
        self.api_book_store.delete_books(user_id, token)
        after_books_is_the_profile = self.api_account.get_user(user_id, token).books

        assert before_books_is_the_profile != after_books_is_the_profile, (
            "the books haven't been deleted from the profile"
        )
        assert after_books_is_the_profile == [], (
            "there are books in the profile. "
        )

    def test_delete_book_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = self.api_book_store.get_isbn_books_list()
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        before_books_in_profile = self.api_account.get_user(user_id, token)
        book = random.choice(before_books_in_profile)
        self.api_book_store.delete_book(book, user_id, token)
        after_books_in_profile = self.api_account.get_user(user_id, token)

        assert book in before_books_in_profile, (
            "the book hasn't been added to the profile"
        )
        assert book not in after_books_in_profile, (
            "the book hasn't been deleted from the profile"
        )

    def test_comparing_book_information_from_get_request_and_book_list(self, account_setup):
        user_id, token = account_setup

        book_information_from_list = random.choice(self.api_book_store.get_information_books_list())
        isbn_book = book_information_from_list.isbn
        book_information_from_get = self.api_book_store.get_book(isbn_book, token)

        assert book_information_from_list == book_information_from_get, (
            "book information from get request does not match information from book list"
        )
