from sqlalchemy import Column, String, Integer, ForeignKey, Date, Numeric
from sqlalchemy.orm import relationship

from .base import BaseModel


class Employee(BaseModel):
    __tablename__ = "employees"

    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(20))
    designation = Column(String(100))

    salary = Column(Numeric(10, 2), nullable=False)
    hire_date = Column(Date, nullable=False)
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

    organization = relationship(
        "Organization",
        back_populates="employees"
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )