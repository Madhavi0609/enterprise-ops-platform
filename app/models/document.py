from sqlalchemy import Column, String, Text
from .base import BaseModel


class Document(BaseModel):
    __tablename__ = "documents"

    title = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    description = Column(Text)