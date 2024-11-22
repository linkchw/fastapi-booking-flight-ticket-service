from db.base import Base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, nullable=False)
    price = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="orders")
    tickets = relationship("Ticket", back_populates="order")
