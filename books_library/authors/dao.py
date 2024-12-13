from books_library.dao.base import BaseDAO
from books_library.database import async_session_maker
from sqlalchemy import select, insert, update
from books_library.authors.models import Authors
from books_library.exceptions import  NotValidID, RecordNotFound, NotValidBirthday, NotValidName


class AuthorsDAO(BaseDAO):
    model = Authors

    @classmethod
    async def create_record(cls, **data):
        if "id_author" in data and data["id_author"] < 1:
            raise NotValidID
        if "birthday"  in data and data["birthday"] == None:
            raise NotValidBirthday
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
    @classmethod
    async def update_record_by_id(cls, record_id: int, **data):
        if "second_name" in data and data["second_name"] == ""  :
            raise NotValidName
        if data["name"] == "" or type(data["name"]) == int:
            raise NotValidName
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=record_id)
            execute_query = await session.execute(query)
            result = execute_query.scalar_one_or_none()
            if result == None:
                raise RecordNotFound
            query = update(cls.model).where(cls.model.id == record_id).values(**data).execution_options(
                synchronize_session="fetch")
            result = await session.execute(query)
            await session.commit()
            if result.rowcount == 0:
                raise RecordNotFound