from sqlalchemy import Column, String, Text
from .base import BaseModel


class Project(BaseModel):
    __tablename__ = "projects"

    name = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(50), default="Pending")
    priority = Column(String(50), default="Medium")