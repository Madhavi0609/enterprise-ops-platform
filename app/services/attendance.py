from sqlalchemy.orm import Session

from app.repositories.attendance import AttendanceRepository
from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
)


class AttendanceService:

    @staticmethod
    def create(
        db: Session,
        attendance: AttendanceCreate,
    ):
        return AttendanceRepository.create(
            db,
            attendance,
        )

    @staticmethod
    def get_all(db: Session):
        return AttendanceRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db: Session,
        attendance_id: int,
    ):
        return AttendanceRepository.get_by_id(
            db,
            attendance_id,
        )

    @staticmethod
    def update(
        db: Session,
        attendance_id: int,
        data: AttendanceUpdate,
    ):
        return AttendanceRepository.update(
            db,
            attendance_id,
            data,
        )

    @staticmethod
    def delete(
        db: Session,
        attendance_id: int,
    ):
        return AttendanceRepository.delete(
            db,
            attendance_id,
        )