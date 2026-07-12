from pydantic import BaseModel, EmailStr
from datetime import datetime


class EmployeeBase(BaseModel):
    organization_id: int
    department_id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str | None = None
    designation: str
    salary: float
    hire_date: datetime
    status: str = "Active"


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    organization_id: int | None = None
    department_id: int | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    designation: str | None = None
    salary: float | None = None
    hire_date: datetime | None = None
    status: str | None = None


class EmployeeResponse(EmployeeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }