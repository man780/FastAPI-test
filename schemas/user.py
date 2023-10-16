"""
User schemas
"""
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """User base schema"""
    username: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=4, max_length=50)
    full_name: str = Field(..., min_length=5, max_length=50)


class UserCreate(UserBase):
    """from User base schema"""


class UserUpdate(UserBase):
    """from User base schema"""


class User(UserBase):
    """from User base schema then add id field"""
    id: int


class UserInDB(User):
    """User log in with hashed password"""
    hashed_password: str
