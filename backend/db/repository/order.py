from db.models.order import Order
from schemas.order import OrderCreate
from sqlalchemy.orm import Session


def create_new_order(order: OrderCreate, db: Session, code: str, price: int):
    order = Order(code=code, price=price)
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
