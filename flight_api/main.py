from fastapi import FastAPI
from routes.flight_routes import router as flight_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Flight Service API")

origins = [
    "http://127.0.0.1:5090",
    "http://localhost:5090",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(flight_router, prefix="", tags=["Flights"])


@app.get("/")
async def root():
    return {"message": "Hello World"}