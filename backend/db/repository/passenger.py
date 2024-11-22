from db.models.passenger import Passenger
from schemas.passenger import PassengerCreate
from sqlalchemy.orm import Session



def create_new_passenger(passenger_data: PassengerCreate, db: Session):
    passenger = Passenger(
        name=passenger_data.name,
        national_id=passenger_data.national_id,
        age=passenger_data.age,
        gender=passenger_data.gender,
    )

    db.add(passenger)
    db.commit()
    db.refresh(passenger)