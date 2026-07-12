from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.department import (
    DepartmentCreate,
    DepartmentResponse,
)
from app.services.department import DepartmentService

router = APIRouter(
    prefix="/departments",
    tags=["Departments"],
)


@router.post("/", response_model=DepartmentResponse)
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db),
):
    print(department.model_dump())
    return DepartmentService.create(db, department)


@router.get("/", response_model=list[DepartmentResponse])
def get_departments(
    db: Session = Depends(get_db),
):
    return DepartmentService.get_all(db)


@router.get("/{department_id}", response_model=DepartmentResponse)
def get_department(
    department_id: int,
    db: Session = Depends(get_db),
):
    return DepartmentService.get_by_id(db, department_id)