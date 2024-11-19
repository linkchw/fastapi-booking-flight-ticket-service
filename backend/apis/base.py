from apis.v1 import route_order
from apis.v1 import route_user
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_order.router, prefix="", tags=["orders"])
