from pydantic import BaseModel


class PassengerBase(BaseModel):
    name: str
    national_id: str
    age: int
    gender: str
class PassengerCreate(PassengerBase):
    pass
class Passenger(PassengerBase):
    id: int

    class Config:
        orm_mode = True