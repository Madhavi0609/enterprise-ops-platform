from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseModel


class Client(BaseModel):
    __tablename__ = "clients"

    company_name = Column(String(255), nullable=False)
    contact_person = Column(String(100), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(20))
    status = Column(String(50), default="Active")

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    organization = relationship("Organization", back_populates="clients")