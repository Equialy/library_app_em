
from datetime import date

from pydantic import BaseModel, Field


class SAuthors(BaseModel):
    id: int
    name: str
    second_name: str
    birthday: date

class SCreateAuthors(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    second_name: str = Field(..., min_length=2, max_length=100 )
    birthday: date