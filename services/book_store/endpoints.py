HOST = "https://demoqa.com"


class Endpoints:

    get_books = f"{HOST}/BookStore/v1/Books"
    post_books = f"{HOST}/BookStore/v1/Books"
    delete_books = lambda self, user_id: f"{HOST}/BookStore/v1/Books?UserId={user_id}"
    get_book = lambda self, isbn: f"{HOST}/BookStore/v1/Book?ISBN={isbn}"
    delete_book = f"{HOST}/BookStore/v1/Book"
    put_book = lambda self, isbn: f"{HOST}/BookStore/v1/Books/{isbn}"
