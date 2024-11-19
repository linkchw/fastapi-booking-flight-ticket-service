from typing import List

from pydantic import BaseModel


class PassengerCreate(BaseModel):
    name: str
    national_id: str
    age: int
    gender: str

    class Config:
        orm_mode = True


class PassengerResponse(BaseModel):
    id: int
    name: str
    national_id: str
    age: int
    gender: str
    tickets: List["TicketResponse"] = []

    class Config:
        orm_mode = True
