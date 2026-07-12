from sqlalchemy import Column, String, Integer, ForeignKey

from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = "employees"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    designation = Column(String(100))

    # Add these three lines here
    salary = Column(Integer, nullable=False)
    hire_date = Column(String(50), nullable=False)
    status = Column(String(50), default="Active")

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )