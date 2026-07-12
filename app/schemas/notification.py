from pydantic import BaseModel
from datetime import datetime


class NotificationBase(BaseModel):
    title: str
    message: str
    notification_type: str = "INFO"
    is_read: bool = False


class NotificationCreate(NotificationBase):
    pass


class NotificationUpdate(BaseModel):
    title: str | None = None
    message: str | None = None
    notification_type: str | None = None
    is_read: bool | None = None


class NotificationResponse(NotificationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }