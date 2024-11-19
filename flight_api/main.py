from fastapi import FastAPI
from routes.flight_routes import router as flight_router

app = FastAPI(title="Flight Service API")

app.include_router(flight_router, prefix="/flights", tags=["Flights"])
