from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from config import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    summary = Column(String)
    note = Column(Integer)
    price = Column(Integer)
    publication_date = Column(Date)
    category = Column(String)

    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True)

    books = relationship("Book", back_populates="author")
