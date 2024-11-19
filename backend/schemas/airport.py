from pydantic import BaseModel


class AirportCreate(BaseModel):
    name: str
    code: str

    class Config:
        orm_mode = True


class AirportResponse(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        orm_mode = True
