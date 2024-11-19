from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


class TicketCreate(BaseModel):
    ticket_number: str
    passenger_id: int
    order_id: int

    class Config:
        orm_mode = True


class TicketResponse(BaseModel):
    id: int
    ticket_number: str
    passenger_id: int
    order_id: int

    class Config:
        orm_mode = True
