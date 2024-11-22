from db.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=True)
    email = Column(String, unique=True, nullable=True)
    password = Column(String, nullable=True)
    name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)

    orders = relationship("Order", back_populates="user")
