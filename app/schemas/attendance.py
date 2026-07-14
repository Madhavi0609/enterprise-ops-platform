from datetime import date, time, datetime
from pydantic import BaseModel


class AttendanceBase(BaseModel):
    attendance_date: date
    check_in: time | None = None
    check_out: time | None = None
    status: str = "Present"


class AttendanceCreate(AttendanceBase):
    pass


class AttendanceUpdate(BaseModel):
    attendance_date: date | None = None
    check_in: time | None = None
    check_out: time | None = None
    status: str | None = None


class AttendanceResponse(AttendanceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }