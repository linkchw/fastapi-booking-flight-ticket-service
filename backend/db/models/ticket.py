from db.base import Base
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Ticket(Base):
    id = Column(Integer, primary_key=True, index=True)
    ticket_number = Column(String, unique=True, nullable=False)

    passenger_id = Column(Integer, ForeignKey("passenger.id"))
    order_id = Column(Integer, ForeignKey("order.id"))

    passenger = relationship("Passenger", back_populates="ticket")
    order = relationship("Order", back_populates="ticket")
