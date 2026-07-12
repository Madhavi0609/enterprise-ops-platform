from sqlalchemy import Column, String, Boolean, Text
from .base import BaseModel


class Notification(BaseModel):
    __tablename__ = "notifications"

    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    notification_type = Column(String(50), default="INFO")
    is_read = Column(Boolean, default=False)