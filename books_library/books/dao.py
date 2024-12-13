from sqlalchemy import select, insert, update

from books_library.authors.models import Authors
from books_library.books.models import Books
from books_library.dao.base import BaseDAO
from books_library.database import async_session_maker
from books_library.exceptions import ExceptionQuantity, NotValidID, BooksAuthorNotFound, NotValidName, RecordNotFound


class BooksDAO(BaseDAO):
    model = Books

    @classmethod
    async def create_record(cls, **data):
        if "quantity" in data and data["quantity"] < 0:
            raise ExceptionQuantity
        if not isinstance(data.get("name"), str) or not data["name"].strip():
            raise NotValidName

        async with async_session_maker() as session:
            query_author = select(Authors).where(Authors.id == data["id_author"])
            books_result = await session.execute(query_author)
            books_instance = books_result.scalar_one_or_none()
            if not books_instance:
                raise BooksAuthorNotFound
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_record_by_id(cls, record_id: int, **data):
        if "quantity" in data and data["quantity"] < 0:
            raise ExceptionQuantity
        async with async_session_maker() as session:
            query_select = select(cls.model).filter_by(id=record_id)
            execute_query = await session.execute(query_select)
            result = execute_query.scalar_one_or_none()
            if result == None:
                raise RecordNotFound
            query_author = select(Authors).filter_by(id=data["id_author"])
            execute_author = await session.execute(query_author)
            result_author = execute_author.scalar_one_or_none()
            if result_author == None:
                raise RecordNotFound

            query = update(cls.model).where(cls.model.id == record_id).values(**data).execution_options(
                synchronize_session="fetch")
            result = await session.execute(query)
            await session.commit()
            if result.rowcount == 0:
                raise RecordNotFound