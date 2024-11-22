from pydantic import BaseModel 
from typing import List
from schemas.ticket import Ticket, TicketCreate 

class OrderBase(BaseModel):
    code: str
    price: float
    user_id: int

class OrderCreate(OrderBase):
    tickets: List[TicketCreate]

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
