from models import all_flights


def find_flight(airline: str, flight_id: str) -> dict:
    """Utility function to find a flight."""
    return all_flights.get(airline, {}).get(flight_id)
