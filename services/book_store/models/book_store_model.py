from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import List


class Book(BaseModel):

    isbn: str
    title: str
    subTitle: str
    author: str
    publish_date: datetime
    publisher: str
    pages: int
    description: str
    website: HttpUrl


class GetBooksResponse(BaseModel):

    books: List[Book]


class PostBooks(BaseModel):
    isbn: str


class PostBooksResponse(BaseModel):

    books: List[PostBooks]


