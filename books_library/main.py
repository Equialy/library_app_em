import uvicorn
from fastapi import FastAPI
from books_library.authors.router import router as router_authors
from books_library.books.router import router as router_books
from books_library.borrows.router import router as router_borrows

app = FastAPI()

app.include_router(router_authors)
app.include_router(router_books)
app.include_router(router_borrows)










if __name__ == "__main__":
    uvicorn.run("books_library.main:app", reload=True)
