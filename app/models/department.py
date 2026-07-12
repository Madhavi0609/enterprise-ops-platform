from sqlalchemy import Column, String, ForeignKey

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