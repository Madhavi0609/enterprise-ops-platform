from sqlalchemy.orm import Session

from app.repositories.department import DepartmentRepository
from app.schemas.department import DepartmentCreate


class DepartmentService:

    @staticmethod
    def create(db: Session, department: DepartmentCreate):
        return DepartmentRepository.create(db, department)

    @staticmethod
    def get_all(db: Session):
        return DepartmentRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, department_id: int):
        return DepartmentRepository.get_by_id(db, department_id)