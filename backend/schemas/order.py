from typing import List
from schemas.user import User

from pydantic import BaseModel

class OrderBase(BaseModel):
    code: str
    price: float

class OrderCreate(OrderBase):
    code: str
    price: float
    user_id: int
    tickets: List = []

class Order(OrderBase):
    id: int
    user: User
    tickets: List = []

    class Config:
        orm_mode = True
