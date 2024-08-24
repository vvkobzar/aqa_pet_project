import pytest
from services.account.api_account import AccountAPI


@pytest.fixture(scope='function', autouse=True)
def account_setup():
    account_api = AccountAPI()
    user_id = account_api.create_user()
    token = account_api.generate_user_token()
    yield user_id, token
    account_api.delete_user(user_id, token)
