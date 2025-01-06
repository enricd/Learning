from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "publisher": "Bloomsbury",
        "published_date": "1997-06-26",
        "page_count": 223,
        "language": "English",
    },
    {
        "id": 2,
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "publisher": "George Allen & Unwin",
        "published_date": "1937-09-21",
        "page_count": 310,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Charles Scribner's Sons",
        "published_date": "1925-04-10",
        "page_count": 218,
        "language": "English",
    },
    {
        "id": 4,
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count": 277,
        "language": "English",
    },
    {
        "id": 5,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J.B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count": 281,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


@app.get("/books", response_model=List[Book])
async def get_all_books():
    return books


@app.post("/books")
async def create_a_book() -> dict:
    ...


@app.get("/books/{book_id}")
async def get_book(book_id: int) -> dict:
    ...


@app.put("/books/{book_id}")
async def update_book(book_id: int) -> dict:
    ...