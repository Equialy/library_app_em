

from sqlalchemy import Integer, Date, Column, String


from books_library.database import Base

class Authors(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)