from db.models.order import Order
from schemas.order import OrderCreate
from sqlalchemy.orm import Session


def create_new_order(order: OrderCreate, db: Session):
    new_order = Order(
        code=order.code,
        price=order.price, 
        user_id=order.user_id
        )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order