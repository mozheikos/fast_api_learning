from pydantic import BaseModel, validator, constr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    id: Optional[str] = None
    username: str
    name: str
    lastname: str
    hashed_password: str
    created_at: datetime
    updated_at: datetime


class UserIn(BaseModel):
    username: str
    name: str
    lastname: str
    password: constr(min_length=8)
    password2: str
    created_at: datetime
    updated_at: datetime

    @validator("password2")
    def password_validate(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v
