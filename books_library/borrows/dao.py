from datetime import datetime

from books_library.books.models import Books
from books_library.borrows.models import Borrows
from books_library.dao.base import BaseDAO
from books_library.database import async_session_maker
from sqlalchemy import update, insert, select

from books_library.exceptions import NotValidID, WrongQuantity, WrongeDate, BookNotFound, \
    BorrowIDNotFound, BookReturn


class BorrowsDAO(BaseDAO):
    model = Borrows

    @classmethod
    async def find_by_id(cls, record_id: int):
        async with async_session_maker() as session:
            query_select = select(cls.model).where(cls.model.id == record_id)
            book = await session.execute(query_select)
            book_instance = book.scalar_one_or_none()
            if not book_instance:
                raise BorrowIDNotFound

        return book_instance

    @classmethod
    async def return_borrows_by_id(cls, record_id: int, return_date):
        if record_id < 1:
            raise NotValidID
        if return_date.date_return > datetime.now().date():
            raise WrongeDate

        async with async_session_maker() as session:
            query_borrow = select(cls.model).where(cls.model.id == record_id)
            borrow_result = await session.execute(query_borrow)
            borrow_instance = borrow_result.scalar_one_or_none()

            if not borrow_instance:
                raise BorrowIDNotFound

            if borrow_instance.date_return is not None:
                raise BookReturn
            if return_date.date_return < borrow_instance.date_borrow:
                raise WrongeDate

            query_update_borrow = (
                update(cls.model)
                .where(cls.model.id == record_id)
                .values(date_return=return_date.date_return)
            )

            query_update_books = (
                update(Books)
                .where(Books.id == borrow_instance.id_book)
                .values(quantity=Books.quantity + 1)
            )

            await session.execute(query_update_borrow)
            await session.execute(query_update_books)
            await session.commit()

    @classmethod
    async def create_record(cls, **data):
        if datetime.now().date() < data["date_borrow"]:
            raise WrongeDate
        async with async_session_maker() as session:
            query_insert = insert(cls.model).values(**data)
            query_select = select(Books).where(Books.id == data["id_book"])
            book = await session.execute(query_select)
            book_instance = book.scalar_one_or_none()
            if not book_instance:
                raise BookNotFound

            if book_instance.quantity < 1:
                raise WrongQuantity

            query_decrease = update(Books).where(Books.id == data["id_book"]).values(
                quantity=book_instance.quantity - 1)
            await session.execute(query_decrease)
            await session.execute(query_insert)
            await session.commit()
