from fastapi import FastAPI

from config import Base, engine
from controllers.author import get_router as get_author_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(get_author_router(), prefix="/api/v1/authors")


@app.get("/hello")
def hello():
    return {"message": "Hello World !"}


@app.get("/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name} ! Welcome to the World !"}
