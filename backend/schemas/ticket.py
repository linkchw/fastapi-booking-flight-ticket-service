from pydantic import BaseModel
from schemas.passenger import Passenger
from schemas.order import Order

class TicketBase(BaseModel):
    ticket_number: str

class TicketCreate(TicketBase):
    passenger_id: int
    order_id: int

class Ticket(TicketBase):
    id: int
    passenger: Passenger
    order: Order

    class Config:
        orm_mode = True