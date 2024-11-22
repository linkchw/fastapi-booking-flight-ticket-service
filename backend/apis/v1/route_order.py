import httpx
from core.config import setting
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.order import OrderCreate
from schemas.order import OrderResponse
from sqlalchemy.orm import Session
from typing import Union


router = APIRouter()


@router.get("/flights")
async def list_flights():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{setting.FLIGHT_SERVICE_URL}/")
            response.raise_for_status()

            return response.json()

        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{airline}/{flight_id}")
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


@router.get("/search-flights")
async def search_flights(
    origin: str,
    destination: str,
    date: Union[str, None] = None,
):
    params = {
        "origin": origin,
        "destination": destination,
    }
    if date:
        params["date"] = date

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{setting.FLIGHT_SERVICE_URL}/search/", params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
