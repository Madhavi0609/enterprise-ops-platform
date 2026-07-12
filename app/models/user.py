from sqlalchemy import Column, String
from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    username = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)