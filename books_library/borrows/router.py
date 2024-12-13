from fastapi import APIRouter

from books_library.borrows.dao import BorrowsDAO
from books_library.borrows.schemas import SBorrows, InfoBorrows, UpdateBorrows

router = APIRouter(
    prefix="/borrows",
    tags=["Выдача"]
)


@router.get("", summary="Получить список всех выдач")
async def get_borrows() -> list[SBorrows]:
    return await BorrowsDAO.find_all()


@router.get("/{id}", summary="Получить запись о выдаче по ID")
async def get_borrows_by_id(id: int) -> SBorrows:
    return await BorrowsDAO.find_by_id(record_id=id)


@router.post("", summary="Создать запись о выдаче книги")
async def create_borrows(data: InfoBorrows):
    return await BorrowsDAO.create_record(**data.dict())


@router.delete("/{id}", summary="Удалить запись о выдаче")
async def delete_borrows(id: int):
    return await BorrowsDAO.delete_record(record_id=id)


@router.patch("/{id}/return", summary="Отметить возврат книги")
async def return_borrows(id: int, date_return: UpdateBorrows):
    return await BorrowsDAO.return_borrows_by_id(record_id=id, return_date=date_return)
