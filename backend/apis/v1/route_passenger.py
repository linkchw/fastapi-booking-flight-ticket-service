from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from schemas.passenger import Passenger, PassengerBase
from db.session import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from db.models.user import User
from db.models.ticket import Ticket
from db.models.order import Order
from db.models.passenger import Passenger


router = APIRouter()


@router.get("/user/{user_id}/passengers", response_model=list[PassengerBase])
def get_user_passengers(user_id: int,
                        db: Session = Depends(get_db)
                    ):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
            )
    
    passengers = (
        db.query(Passenger)
        .join(Ticket, Ticket.passenger_id == Passenger.id)
        .join(Order, Order.id == Ticket.order_id)
        .filter(Order.user_id == user_id)
        .distinct()
        .all()
    )

    return passengers
