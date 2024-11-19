from db.base import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String


class Airport(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    code = Column(String, unique=True, nullable=False)
