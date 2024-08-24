class Payloads:

    post_books = lambda self, user_id, isbn: {
        "userId": user_id,
        "collectionOfIsbns": [
            {
                "isbn": isbn
            }
        ]
    }

    delete_book = lambda self, isbn, user_id: {
        "isbn": isbn,
        "userId": user_id
    }

    put_books = lambda self, user_id, new_isbn: {
        "userId": user_id,
        "isbn": new_isbn
    }
