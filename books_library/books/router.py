from fastapi import APIRouter
from books_library.books.dao import BooksDAO
from books_library.books.schemas import SBooks, CreateBooks

router = APIRouter(
    prefix="/books",
    tags=["Книги"],

)


@router.get("", summary="Получить список всех книг")
async def get_books() -> list[SBooks]:
    return await BooksDAO.find_all()


@router.get("/{id}", summary="Получить книгу по ID")
async def get_books_by_id(id: int) -> SBooks:
    return await BooksDAO.find_by_id(record_id=id)


@router.post("", summary="Добавить новую книгу")
async def create_books(data: CreateBooks):
    return await BooksDAO.create_record(**data.dict())


@router.put("/{id}", summary="Обновить данные книги")
async def update_books(id: int, data: CreateBooks):
    return await BooksDAO.update_record_by_id(record_id=id, **data.dict())


@router.delete("/{id}", summary="Удалить книгу")
async def delete_books(id: int):
    return await BooksDAO.delete_record(record_id=id)
