import os
from dotenv import load_dotenv

load_dotenv()


class Payloads:

    username_password = {
        "userName": os.getenv('USERNAME'),
        "password": os.getenv('PASSWORD')
    }
