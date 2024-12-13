from sqlalchemy import Integer, Column, String, ForeignKey
from books_library.database import Base

class Books(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    describe = Column(String, nullable=False)
    id_author = Column(ForeignKey("authors.id"))
    quantity = Column(Integer, nullable=False)