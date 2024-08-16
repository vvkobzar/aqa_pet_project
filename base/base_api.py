from services.account.api_account import AccountAPI


class BaseAPI:
    def setup_method(self):
        self.api_account = AccountAPI()
