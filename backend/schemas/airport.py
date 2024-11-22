from pydantic import BaseModel


class AirportBase(BaseModel):
    name: str
    code: str

class AirportCreate(AirportBase):
    pass

class Airport(AirportBase):
    id: int

    class Config:
        orm_mode = True
