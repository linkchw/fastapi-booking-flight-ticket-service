from typing import List

from pydantic import BaseModel


class OrderCreate(BaseModel):
    code: str
    price: float
    user_id: int

    class Config:
        orm_mode = True


class OrderResponse(BaseModel):
    id: int
    code: str
    price: float
    user_id: int
    tickets: List = []

    class Config:
        orm_mode = True
