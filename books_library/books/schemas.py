from pydantic import BaseModel



class SBooks(BaseModel):
    id: int
    name: str
    describe: str
    id_author: int
    quantity: int

class CreateBooks(BaseModel):
    name: str
    describe: str
    id_author: int
    quantity: int