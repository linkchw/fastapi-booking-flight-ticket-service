from pydantic import BaseModel

class TicketBase(BaseModel):
    ticket_number: str
    passenger_id: int
    order_id: int

class TicketCreate(TicketBase):
    pass

class Ticket(TicketBase):
    id: int

    class Config:
        orm_mode = True