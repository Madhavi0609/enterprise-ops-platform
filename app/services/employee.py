from sqlalchemy.orm import Session

from app.repositories.employee import EmployeeRepository
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


class EmployeeService:

    @staticmethod
    def create(db: Session, employee: EmployeeCreate):
        return EmployeeRepository.create(db, employee)

    @staticmethod
    def get_all(db: Session):
        return EmployeeRepository.get_all(db)

    @staticmethod
    def get_by_id(db: Session, employee_id: int):
        return EmployeeRepository.get_by_id(db, employee_id)

    @staticmethod
    def update(db: Session, employee_id: int, employee: EmployeeUpdate):
        return EmployeeRepository.update(db, employee_id, employee)

    @staticmethod
    def delete(db: Session, employee_id: int):
        return EmployeeRepository.delete(db, employee_id)