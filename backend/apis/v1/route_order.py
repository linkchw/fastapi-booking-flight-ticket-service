import httpx
from core.config import setting
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.order import OrderCreate
from schemas.order import OrderResponse
from sqlalchemy.orm import Session


router = APIRouter()


@router.post(
    "/order-flight/{airline}/",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED,
)
async def book_flight(airline: str, order: OrderCreate):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"{setting.FLIGHT_SERVICE_URL}/{airline}/",
                json={
                    "origin": order.origin,
                    "destination": order.destination,
                    "price": order.price,
                },
            )
            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/flight-lists/")
async def list_flights():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{setting.FLIGHT_SERVICE_URL}/flights/")
            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/flight-lists/{airline}/{flight_id}")
async def get_flight(airline: str, flight_id: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                f"{setting.FLIGHT_SERVICE_URL}/{airline}/{flight_id}"
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.put("/update-flight/{airline}/{flight_id}")
async def update_flight(airline: str, flight_id: str, flight: OrderCreate):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(
                f"{setting.FLIGHT_SERVICE_URL}/{airline}/{flight_id}",
                json={
                    "origin": flight.origin,
                    "destination": flight.destination,
                    "price": flight.price,
                },
            )
            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
