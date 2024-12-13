from books_library.database import async_session_maker
from sqlalchemy import select, delete
from books_library.exceptions import  RecordNotFound


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
        return result.scalars().all()

    @classmethod
    async def find_by_id(cls, record_id: int):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=record_id)
            execute_query = await session.execute(query)
            result = execute_query.scalar_one_or_none()
            if result == None:
                raise RecordNotFound
        return result

    @classmethod
    async def delete_record(cls, record_id: int):
        async with async_session_maker() as session:
            query = delete(cls.model).where(cls.model.id == record_id)
            result = await session.execute(query)
            await session.commit()
            if result.rowcount == 0:
                raise RecordNotFound
