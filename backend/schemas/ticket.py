from pydantic import BaseModel
from typing import Optional
from schemas.passenger import PassengerCreate

class TicketBase(BaseModel):
    ticket_number: str
    passenger_id: int
    order_id: int

class TicketCreate(BaseModel):
    ticket_number: str
    passenger: PassengerCreate

    class Config:
        orm_mode = True

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True