from fastapi import Depends
from fastapi import status
from fastapi import HTTPException
from schemas.order import OrderCreate
from schemas.order import Order
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from db.repository.order import create_new_order
from db.session import get_db
from db.models.user import User
from db.models.passenger import Passenger
from db.models.ticket  import Ticket

from fastapi import APIRouter


router = APIRouter()


@router.post("/submit-order", response_model=Order)
async def submit_order(order: OrderCreate, db: Session = Depends(get_db)):
    print(order)
    try:
        user = db.query(User).filter(User.id == order.user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
        
        new_order = create_new_order(order=order, db=db)

        for ticket_data in order.tickets:

            passenger = db.query(Passenger).filter(Passenger.id == ticket_data.passenger_id).first()

            if not passenger:
                passenger = Passenger(
                    name=ticket_data.passenger.name,
                    national_id=ticket_data.passenger.national_id,
                    age=ticket_data.passenger.age,
                    gender=ticket_data.passenger.gender
                )
                db.add(passenger)
                db.commit()  # Commit to generate the passenger ID
                db.refresh(passenger)

            new_ticket = Ticket(
                ticket_number=ticket_data.ticket_number,
                passenger_id=ticket_data.passenger_id,
                order_id=new_order.id,
            )
            db.add(new_ticket)

        db.commit()

        return new_order

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Order code or ticket number must be unique")

