from apis.v1 import route_ticket
from apis.v1 import route_order
from apis.v1 import route_user
from apis.v1 import route_login
from apis.v1 import route_passenger

from fastapi import APIRouter

api_router = APIRouter()


api_router.include_router(route_ticket.router, prefix="", tags=["tickets"])
api_router.include_router(route_order.router, prefix="", tags=["orders"])
api_router.include_router(route_user.router, prefix="", tags=["users"])
api_router.include_router(route_passenger.router, prefix="", tags=["passengers"])
api_router.include_router(route_login.router, prefix="", tags=["login"])
