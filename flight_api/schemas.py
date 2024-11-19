from pydantic import BaseModel


class FlightBase(BaseModel):
    origin: str
    destination: str
    departure_time: str
    arrival_time: str
    total_seats: int
    available_seats: int
    price: float
    aircraft_type: str
    pilot: str
    status: str


class FlightCreate(FlightBase):
    flight_number: str


class Flight(FlightCreate):
    airline: str
