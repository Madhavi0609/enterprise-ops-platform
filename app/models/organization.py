from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseModel


class Organization(BaseModel):
    __tablename__ = "organizations"

    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(20))
    address = Column(String(255))

    departments = relationship("Department", back_populates="organization")
    employees = relationship("Employee", back_populates="organization")
    clients = relationship("Client", back_populates="organization")