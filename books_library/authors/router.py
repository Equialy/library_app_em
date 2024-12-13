from datetime import datetime
from fastapi import APIRouter
from books_library.authors.dao import AuthorsDAO
from books_library.authors.schemas import SAuthors, SCreateAuthors
from books_library.exceptions import NotValidBirthday, RecordNotFound

router = APIRouter(
    prefix="/authors",
    tags=["Авторы"],
)


@router.get("", summary="Возвращает список всех авторов", )
async def get_authors() -> list[SAuthors]:
    return await AuthorsDAO.find_all()



@router.get("/{id}", summary="Получить автора по ID")
async def get_authors_id(id: int) -> SAuthors:
    return await AuthorsDAO.find_by_id(id)


@router.post("", summary="Создать нового автора")
async def create_authors(data: SCreateAuthors):
    if data.birthday >= datetime.now().date():
        raise NotValidBirthday
    return await AuthorsDAO.create_record(name=data.name, second_name=data.second_name, birthday=data.birthday)



@router.put("/{id}", summary="Обновить данные автора")
async def update_authors(id: int, data: SCreateAuthors):
    if data.birthday >= datetime.now().date():
        raise NotValidBirthday
    return await AuthorsDAO.update_record_by_id(record_id=id, name=data.name, second_name=data.second_name, birthday=data.birthday)



@router.delete("/{id}", summary="Удалить автора")
async def delete_authors(id: int):
    return await AuthorsDAO.delete_record(record_id=id)

