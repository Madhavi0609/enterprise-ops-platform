from pydantic import BaseModel
from datetime import datetime


class DocumentBase(BaseModel):
    title: str
    file_name: str
    file_path: str
    description: str | None = None


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    title: str | None = None
    file_name: str | None = None
    file_path: str | None = None
    description: str | None = None


class DocumentResponse(DocumentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }