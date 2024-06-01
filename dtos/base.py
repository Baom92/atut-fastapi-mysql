from datetime import date

from pydantic import BaseModel


class AuthorBase(BaseModel):
    firstname: str
    lastname: str
    email: str


class BookBase(BaseModel):
    title: str
    summary: str
    note: int
    price: int
    publication_date: date
    category: str
