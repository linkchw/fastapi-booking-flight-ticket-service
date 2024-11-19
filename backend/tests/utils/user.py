from db.repository.user import create_new_user
from faker import Faker
from schemas.user import UserCreate
from sqlalchemy.orm import Session

fake = Faker()


def create_random_user(db: Session) -> UserCreate:
    user_data = UserCreate(
        username=fake.user_name(),
        password=fake.password(),
        name=fake.name(),
        phone_number=fake.phone_number(),
    )
    user = create_new_user(user=user_data, db=db)

    return user
