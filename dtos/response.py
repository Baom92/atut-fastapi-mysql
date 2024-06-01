from pydantic import ConfigDict

from dtos.base import AuthorBase, BookBase


class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class AuthorResponse(AuthorBase):
    id: int
    books: list[BookResponse]
    model_config = ConfigDict(from_attributes=True)
