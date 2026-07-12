from pydantic import BaseModel, EmailStr
from datetime import datetime


class ClientBase(BaseModel):
    organization_id: int
    company_name: str
    contact_person: str
    email: EmailStr
    phone: str | None = None
    status: str = "Active"


class ClientCreate(ClientBase):
    pass


class ClientUpdate(BaseModel):
    organization_id: int | None = None
    company_name: str | None = None
    contact_person: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    status: str | None = None


class ClientResponse(ClientBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }