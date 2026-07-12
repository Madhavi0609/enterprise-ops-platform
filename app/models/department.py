from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import BaseModel


class Department(BaseModel):
    __tablename__ = "departments"

    organization_id = Column(
        ForeignKey("organizations.id"),
        nullable=False
    )

    name = Column(String(100), nullable=False)

    code = Column(String(20), unique=True, nullable=False)

    description = Column(String(255))

    status = Column(String(20), default="Active")

    organization = relationship(
        "Organization",
        back_populates="departments"
    )

    employees = relationship(
        "Employee",
        back_populates="department"
    )