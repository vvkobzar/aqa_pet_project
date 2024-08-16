from services.account.api_account import AccountAPI
from services.book_store.api_book_store import BookStoreAPI


class BaseAPI:

    def setup_method(self):
        self.api_account = AccountAPI()
        self.api_book_store = BookStoreAPI()
