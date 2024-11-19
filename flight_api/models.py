lufthansa_flights = {
    "flight_1": {
        "flight_number": "LH101",
        "origin": "Frankfurt",
        "destination": "Tehran",
        "departure_time": "2024-06-15 10:00",
        "arrival_time": "2024-06-15 15:30",
        "total_seats": 180,
        "available_seats": 120,
        "price": 450.50,
        "aircraft_type": "Airbus A320",
        "pilot": "Michael Schmidt",
        "status": "scheduled",
    },
    "flight_2": {
        "flight_number": "LH202",
        "origin": "Munich",
        "destination": "Istanbul",
        "departure_time": "2024-06-16 14:45",
        "arrival_time": "2024-06-16 16:15",
        "total_seats": 200,
        "available_seats": 85,
        "price": 320.75,
        "aircraft_type": "Boeing 787",
        "pilot": "Klaus Weber",
        "status": "scheduled",
    },
}

turkish_airlines_flights = {
    "flight_1": {
        "flight_number": "TK301",
        "origin": "Istanbul",
        "destination": "Dubai",
        "departure_time": "2024-06-15 08:30",
        "arrival_time": "2024-06-15 11:00",
        "total_seats": 220,
        "available_seats": 150,
        "price": 275.90,
        "aircraft_type": "Airbus A330",
        "pilot": "Mehmet Yılmaz",
        "status": "scheduled",
    },
    "flight_2": {
        "flight_number": "TK402",
        "origin": "Ankara",
        "destination": "London",
        "departure_time": "2024-06-16 12:15",
        "arrival_time": "2024-06-16 14:45",
        "total_seats": 180,
        "available_seats": 100,
        "price": 425.60,
        "aircraft_type": "Boeing 777",
        "pilot": "Ahmet Demir",
        "status": "scheduled",
    },
}

all_flights = {
    "lufthansa": lufthansa_flights,
    "turkish_airlines": turkish_airlines_flights,
}
