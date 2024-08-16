HOST = "https://demoqa.com"


class Endpoints:

    authorized = f"{HOST}/Account/v1/Authorized"
    generate_token = f"{HOST}/Account/v1/GenerateToken"
    create_user = f"{HOST}/Account/v1/User"
    delete_user = lambda self, user_id: f"{HOST}/Account/v1/User/{user_id}"
    get_user = lambda self, user_id: f"{HOST}/Account/v1/User/{user_id}"
