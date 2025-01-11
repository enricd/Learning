from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.books.routes import book_router
from src.db.main import init_db


@asynccontextmanager
async def life_span(app: FastAPI):
    print("Server is starting...")
    await init_db()

    yield

    print("Server is been stopped")



version = "v1"

app = FastAPI(
    title="Book API",
    description="A REST API to manage books",
    version=version,
    lifespan=life_span,
)

app.include_router(
    book_router, 
    prefix=f"/api/{version}/books", 
    tags=["Books"]
)

