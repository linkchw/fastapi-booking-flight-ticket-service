from typing import List

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=4)
    username: str
    name: str
    phone_number: str

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    name: str
    phone_number: str
    orders: List = []

    class Config:
        orm_mode = True
