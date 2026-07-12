from sqlalchemy import Column, String
from .base import BaseModel


class Client(BaseModel):
    __tablename__ = "clients"

    company_name = Column(String(255), nullable=False)
    contact_person = Column(String(100), nullable=False)
    email = Column(String(255), unique=True)
    phone = Column(String(20))
    status = Column(String(50), default="Active")