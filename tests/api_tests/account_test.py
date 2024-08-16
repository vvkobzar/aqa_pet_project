from base.base_api import BaseAPI


class TestAccount(BaseAPI):

    def test_authorized(self):
        self.api_account.authorized()

    def test_get_user(self, account_setup):
        user_id, token = account_setup
        model = self.api_account.get_user(user_id, token)

        assert model.userId == user_id, "user id don't match"
        assert model.books == [], "there are books in the created account"
