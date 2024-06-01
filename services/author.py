from sqlalchemy.orm import Session

from dtos.request import AuthorRequest
from models import Author


class AuthorService:
    @staticmethod
    def create(author: AuthorRequest, db: Session) -> Author:
        db_author = Author(
            firstname=author.firstname,
            lastname=author.lastname,
            email=author.email
        )
        # db_author = Author(*author.model_dump())
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        return db_author

    @staticmethod
    def get_by_id(id: int, db: Session) -> Author | None:
        return db.get(Author, id)

    @staticmethod
    def get_all(db: Session) -> list[Author]:
        return db.query(Author).all()
