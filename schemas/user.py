from pydantic import BaseModel, Field, validator


class UserBase(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    email: str = Field(..., min_length=4, max_length=50)
    full_name: str = Field(..., min_length=5, max_length=50)

    @validator("username", "email", "full_name")
    def validate_no_sql_injection(cls, value):
        if "delete from" in value:
            raise ValueError("Our terms strictly prohobit SQLInjection Attacks")
        return value


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: int
