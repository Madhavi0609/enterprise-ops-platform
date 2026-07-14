from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
)


class AttendanceRepository:

    @staticmethod
    def create(
        db: Session,
        attendance: AttendanceCreate,
    ):
        db_attendance = Attendance(
            **attendance.model_dump()
        )

        db.add(db_attendance)
        db.commit()
        db.refresh(db_attendance)

        return db_attendance

    @staticmethod
    def get_all(db: Session):
        return db.query(Attendance).all()

    @staticmethod
    def get_by_id(
        db: Session,
        attendance_id: int,
    ):
        return (
            db.query(Attendance)
            .filter(Attendance.id == attendance_id)
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        attendance_id: int,
        data: AttendanceUpdate,
    ):
        attendance = (
            db.query(Attendance)
            .filter(Attendance.id == attendance_id)
            .first()
        )

        if attendance:

            for key, value in data.model_dump(
                exclude_unset=True
            ).items():
                setattr(attendance, key, value)

            db.commit()
            db.refresh(attendance)

        return attendance

    @staticmethod
    def delete(
        db: Session,
        attendance_id: int,
    ):
        attendance = (
            db.query(Attendance)
            .filter(Attendance.id == attendance_id)
            .first()
        )

        if attendance:
            db.delete(attendance)
            db.commit()

        return attendance