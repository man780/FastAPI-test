from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username: str
    email: str
    full_name: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int


class UserList(BaseModel):
    users: list[User]
