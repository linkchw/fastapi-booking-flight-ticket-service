from db.models.passenger import Passenger
from db.models.ticket import Ticket
from db.models.user import User
from db.repository.order import create_new_order
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from schemas.order import Order
from schemas.order import OrderCreate
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session


router = APIRouter()


@router.post("/submit-order", response_model=Order)
async def submit_order(order: OrderCreate, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.id == order.user_id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="User not found"
            )

        new_order = create_new_order(order=order, db=db)

        for ticket_data in order.tickets:
            passenger_data = ticket_data.passenger

            passenger = (
                db.query(Passenger)
                .filter(Passenger.national_id == passenger_data.national_id)
                .first()
            )

            if not passenger:
                passenger = Passenger(
                    name=passenger_data.name,
                    national_id=passenger_data.national_id,
                    age=passenger_data.age,
                    gender=passenger_data.gender,
                )
                db.add(passenger)
                db.commit()
                db.refresh(passenger)

            ticket = Ticket(
                ticket_number=ticket_data.ticket_number,
                passenger_id=passenger.id,
                order_id=new_order.id,
            )
            db.add(ticket)

        db.commit()

        return new_order

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Order code or ticket number must be unique",
        )
