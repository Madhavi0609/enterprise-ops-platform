from pydantic import BaseModel
from datetime import datetime


class ProjectBase(BaseModel):
    name: str
    description: str | None = None
    status: str = "Pending"
    priority: str = "Medium"


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    status: str | None = None
    priority: str | None = None


class ProjectResponse(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }