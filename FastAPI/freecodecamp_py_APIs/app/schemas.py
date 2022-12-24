from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

# Schema by pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True


class Post(PostBase):
    # inheriting title, content and published from PostBase
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    # necessary to properly transform the ORM object to a dictionary
    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None
