from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field



class UserBase(BaseModel):
    username: str = Field(..., max_length=100)
    email: EmailStr
    role: str = Field(..., max_length=50)



class UserCreate(UserBase):
    password: str = Field(..., min_length=8)



class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    role: Optional[str] = Field(None, max_length=50)



class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }