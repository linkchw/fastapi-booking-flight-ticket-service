from db.base import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String, unique=True, nullable=False)
    passenger_id = Column(Integer, ForeignKey("passengers.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))

    passenger = relationship("Passenger", back_populates="tickets")
    order = relationship("Order", back_populates="tickets")
