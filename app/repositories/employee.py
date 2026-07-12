from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeRepository:

    @staticmethod
    def create(db: Session, employee: EmployeeCreate):
        db_employee = Employee(**employee.model_dump())
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee

    @staticmethod
    def get_all(db: Session):
        return db.query(Employee).all()

    @staticmethod
    def get_by_id(db: Session, employee_id: int):
        return db.query(Employee).filter(Employee.id == employee_id).first()

    @staticmethod
    def update(db: Session, employee_id: int, employee: EmployeeUpdate):
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

        if not db_employee:
            return None

        for key, value in employee.model_dump(exclude_unset=True).items():
            setattr(db_employee, key, value)

        db.commit()
        db.refresh(db_employee)
        return db_employee

    @staticmethod
    def delete(db: Session, employee_id: int):
        db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

        if not db_employee:
            return None

        db.delete(db_employee)
        db.commit()
        return db_employee