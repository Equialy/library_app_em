from typing import Optional

from pydantic import BaseModel
from datetime import date

class SBorrows(BaseModel):
    id: int
    id_book: int
    name_reader: str
    date_borrow: date
    date_return: Optional[date]

class InfoBorrows(BaseModel):
    id_book: int
    name_reader: str
    date_borrow: date


class UpdateBorrows(BaseModel):
    date_return: Optional[date]