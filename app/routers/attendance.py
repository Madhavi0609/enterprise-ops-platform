from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse,
)
from app.services.attendance import AttendanceService


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AttendanceResponse)
def create_attendance(
    attendance: AttendanceCreate,
    db: Session = Depends(get_db),
):
    return AttendanceService.create(
        db,
        attendance,
    )


@router.get("/", response_model=list[AttendanceResponse])
def get_attendance(
    db: Session = Depends(get_db),
):
    return AttendanceService.get_all(db)


@router.get("/{attendance_id}", response_model=AttendanceResponse)
def get_attendance_by_id(
    attendance_id: int,
    db: Session = Depends(get_db),
):
    attendance = AttendanceService.get_by_id(
        db,
        attendance_id,
    )

    if not attendance:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found",
        )

    return attendance


@router.put("/{attendance_id}", response_model=AttendanceResponse)
def update_attendance(
    attendance_id: int,
    attendance: AttendanceUpdate,
    db: Session = Depends(get_db),
):
    updated = AttendanceService.update(
        db,
        attendance_id,
        attendance,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found",
        )

    return updated


@router.delete("/{attendance_id}")
def delete_attendance(
    attendance_id: int,
    db: Session = Depends(get_db),
):
    deleted = AttendanceService.delete(
        db,
        attendance_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Attendance not found",
        )

    return {
        "message": "Attendance deleted successfully"
    }