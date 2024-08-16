from pydantic import BaseModel, HttpUrl, field_validator
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


class CreateUserResponse(BaseModel):

    userID: str
    username: str
    books: List[Book]

    @field_validator("userID")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class TokenResponse(BaseModel):

    token: str
    expires: datetime
    status: str
    result: str

    @field_validator("token")
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class DeleteUserResponse(BaseModel):

    code: int
    message: str


class AuthorizedResponse(BaseModel):

    status: bool


class User(BaseModel):

    userId: str
    username: str
    books: List[Book]
