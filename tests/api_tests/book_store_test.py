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
