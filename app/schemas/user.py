from datetime import datetime, date
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    full_name: str
    username: str
    dob: date


class UserLogin(BaseModel):
    username: str
    password: str


class UserOut(UserBase):
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True


class UserLoginResponse(UserOut):
    email: EmailStr


class UserCreate(UserBase):
    email: EmailStr
    password: str
