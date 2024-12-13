from sqlalchemy import Integer, Column, String, ForeignKey, Date


from books_library.database import Base

class Borrows(Base):
    __tablename__ = "borrows"

    id = Column(Integer, primary_key=True)
    id_book = Column(ForeignKey("books.id"))
    name_reader = Column(String, nullable=True)
    date_borrow = Column(Date, nullable=True)
    date_return = Column(Date, nullable=True)
