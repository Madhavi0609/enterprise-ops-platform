from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import DepartmentCreate


class DepartmentRepository:

    @staticmethod
    def create(db: Session, department: DepartmentCreate):
        db_department = Department(**department.model_dump())

        db.add(db_department)
        db.commit()
        db.refresh(db_department)

        return db_department

    @staticmethod
    def get_all(db: Session):
        return db.query(Department).all()

    @staticmethod
    def get_by_id(db: Session, department_id: int):
        return (
            db.query(Department)
            .filter(Department.id == department_id)
            .first()
        )