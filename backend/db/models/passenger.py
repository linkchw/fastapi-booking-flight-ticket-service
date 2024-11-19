from db.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Passenger(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    national_id = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)

    tickets = relationship("Ticket", back_populates="passenger")
