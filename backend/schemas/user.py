from typing import List

from pydantic import BaseModel
from pydantic import EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr
    name: str
    phone_number: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    orders: List["Order"] = []

    class Config:
        orm_mode = True

