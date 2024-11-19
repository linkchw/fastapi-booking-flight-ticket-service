from database.in_memory_db import all_flights
from database.in_memory_db import find_flight
from fastapi import APIRouter
from fastapi import HTTPException
from schemas import Flight
from schemas import FlightCreate

router = APIRouter()


@router.post("/{airline}/", response_model=Flight)
def create_flight(airline: str, flight: FlightCreate):
    airline_data = all_flights.get(airline)
    if not airline_data:
        raise HTTPException(status_code=404, detail="Airline not found")

    flight_id = f"flight_{len(airline_data) + 1}"
    airline_data[flight_id] = flight.dict()
    return {"airline": airline, "id": flight_id, **flight.dict()}


@router.get("/", response_model=list[Flight])
def read_flights():
    flights = []
    for airline, flight_data in all_flights.items():
        for flight_id, details in flight_data.items():
            flights.append({"airline": airline, "id": flight_id, **details})
    return flights


@router.get("/{airline}/{flight_id}", response_model=Flight)
def read_flight(airline: str, flight_id: str):
    flight = find_flight(airline, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {"airline": airline, "id": flight_id, **flight}


@router.put("/{airline}/{flight_id}", response_model=Flight)
def update_flight(airline: str, flight_id: str, flight: FlightCreate):
    existing_flight = find_flight(airline, flight_id)
    if not existing_flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    all_flights[airline][flight_id] = flight.dict()
    return {"airline": airline, "id": flight_id, **flight.dict()}
