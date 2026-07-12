from sqlalchemy import Column, Date, Time, String
from .base import BaseModel


class Attendance(BaseModel):
    __tablename__ = "attendance"

    attendance_date = Column(Date, nullable=False)
    check_in = Column(Time)
    check_out = Column(Time)
    status = Column(String(50), default="Present")