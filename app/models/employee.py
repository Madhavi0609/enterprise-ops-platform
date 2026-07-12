from sqlalchemy import Column, String, Integer, ForeignKey

from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = "employees"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    designation = Column(String(100))

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )