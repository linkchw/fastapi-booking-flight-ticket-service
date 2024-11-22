from database.in_memory_db import all_flights
from database.in_memory_db import find_flight
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Query
from schemas import Flight

router = APIRouter()


@router.get("/list", response_model=list[Flight])
async def read_flights():
    flights = []
    for airline, flight_data in all_flights.items():
        for flight_id, details in flight_data.items():
            flights.append({"airline": airline, "id": flight_id, **details})
    return flights


@router.get("/{airline}/{flight_id}", response_model=Flight)
async def read_flight(airline: str, flight_id: str):
    flight = find_flight(airline, flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return {"airline": airline, "id": flight_id, **flight}


@router.get("/search/", response_model=list[Flight])
async def search_flights(
    origin: str,
    destination: str,
    date: str | None = Query(None, description="Format: YYYY-MM-DD")
):
    results = []
    for airline, flight_data in all_flights.items():
        for flight_id, details in flight_data.items():
            if details["origin"].lower() == origin.lower() and details["destination"].lower() == destination.lower():
                if date:
                    flight_date = details["departure_time"].split(" ")[0]
                    if flight_date == date:
                        results.append({"airline": airline, "id": flight_id, **details})
                else:
                    results.append({"airline": airline, "id": flight_id, **details})
    
    if not results:
        raise HTTPException(status_code=404, detail="No flights found matching the criteria.")
    
    return results
