from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from config import get_db
from dtos.request import AuthorRequest
from dtos.response import AuthorResponse
from services.author import AuthorService


def get_router() -> APIRouter:
    router = APIRouter(tags=["Ressource des auteurs"])
    service = AuthorService()

    @router.post("/", response_model=AuthorResponse)
    def create(author: AuthorRequest, db: Session = Depends(get_db)):
        return service.create(author, db)

    @router.get("/", response_model=list[AuthorResponse])
    def get_all(db: Session = Depends(get_db)):
        return service.get_all(db)

    @router.get("/{id}", response_model=AuthorResponse)
    def get_by_id(id: int, db: Session = Depends(get_db)):
        author = service.get_by_id(id, db)
        if not author:
            raise HTTPException(status_code=404, detail=f"L'auteur d'id {id} n'existe pas dans le système")
        return author

    return router
