import allure
import pytest
import random
from base.base_api import BaseAPI
from allure_commons.types import Severity


@allure.epic("API Tests")
@allure.feature("Book Store")
class TestBookStore(BaseAPI):

    @allure.title("Added book in the user profile")
    def test_added_book_in_the_profile(self, account_setup):
        user_id, token = account_setup

        random_book_from_list = random.choice(self.api_book_store.get_isbn_books_list())
        response_book = self.api_book_store.added_books_in_the_profile(random_book_from_list, user_id, token)[0]
        book_in_the_profile = self.api_account.get_user(user_id, token)[0]

        with allure.step("Check if a book has been added to the profile"):
            assert random_book_from_list == book_in_the_profile, (
                "the book has not been added to the profile"
            )
        with allure.step("Checking that the response from adding a book matches the book in the profile"):
            assert response_book == book_in_the_profile, (
                "the books in the profile don't match the books in the response"
            )

    @allure.severity(Severity.CRITICAL)
    @allure.title("Added books in the user profile")
    @pytest.mark.xfail(
        reason="books from get_user query do not match the added books. In the ui profile the books match"
    )
    def test_added_books_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = set(self.api_book_store.get_isbn_books_list())
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        books_in_the_profile = set(self.api_account.get_user(user_id, token))

        with allure.step("Checking that all books have been added to the profile"):
            assert isbn_books == books_in_the_profile, "added books do not match the books in the profile"

    @allure.title("Delete all books in the user profile")
    def test_delete_all_books_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = self.api_book_store.get_isbn_books_list()
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        before_books_is_the_profile = self.api_account.get_user(user_id, token)
        self.api_book_store.delete_books(user_id, token)
        after_books_is_the_profile = self.api_account.get_user(user_id, token).books

        with allure.step("Checking that the books has been deleted from the profile"):
            assert before_books_is_the_profile != after_books_is_the_profile, (
                "the books haven't been deleted from the profile"
            )
        with allure.step("Checking that there are no books in the profile"):
            assert after_books_is_the_profile == [], (
                "there are books in the profile."
            )

    @allure.title("Delete book in the user profile")
    def test_delete_book_in_the_profile(self, account_setup):
        user_id, token = account_setup

        isbn_books = self.api_book_store.get_isbn_books_list()
        for book in isbn_books:
            self.api_book_store.added_books_in_the_profile(book, user_id, token)
        before_books_in_profile = self.api_account.get_user(user_id, token)
        book = random.choice(before_books_in_profile)
        self.api_book_store.delete_book(book, user_id, token)
        after_books_in_profile = self.api_account.get_user(user_id, token)

        with allure.step("Checking that the book has been added to the profile"):
            assert book in before_books_in_profile, "the book hasn't been added to the profile"
        with allure.step(
                "Check that the book has been removed from the list of books and is not contained in the profile"
        ):
            assert book not in after_books_in_profile, "the book hasn't been deleted from the profile"

    @allure.title("Checking if the book information from the get request matches the books in the list")
    def test_comparing_book_information_from_get_request_and_book_list(self, account_setup):
        user_id, token = account_setup

        book_information_from_list = random.choice(self.api_book_store.get_information_books_list())
        isbn_book = book_information_from_list.isbn
        book_information_from_get = self.api_book_store.get_book(isbn_book, token)

        with allure.step(
                "Checking that the book information from the get request matches the information from the book list"
        ):
            assert book_information_from_list == book_information_from_get, (
                "book information from get request does not match information from book list"
            )

    @allure.severity(Severity.BLOCKER)
    @allure.title("Replacing a book from the profile by a new book request ")
    @pytest.mark.skip(reason="502 error occurs and the user cannot be deleted")
    def test_replace_the_book_in_your_profile_with_another_book(self, account_setup):
        user_id, token = account_setup

        old_isbn_book = random.choices(self.api_book_store.get_isbn_books_list())
        self.api_book_store.added_books_in_the_profile(old_isbn_book, user_id, token)
        before_book_in_the_profile = self.api_account.get_user(user_id, token)[0]
        new_isbn_book = random.choices(self.api_book_store.get_isbn_books_list())
        self.api_book_store.put_books(before_book_in_the_profile, new_isbn_book, user_id, token)
        after_book_in_the_profile = self.api_account.get_user(user_id, token)

        with allure.step("Checking that the book in the profile has been replaced with a new book"):
            assert before_book_in_the_profile != after_book_in_the_profile, (
                "the book hasn't changed to the new one in the profile"
            )
