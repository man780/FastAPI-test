"""
Routers for user CRUD
"""
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from crud.user import create_user, get_user, delete_user, update_user, list_users
from schemas.user import UserCreate, UserUpdate, User
from db_config import get_db

router = APIRouter(tags=["Users"], prefix="/user")


@router.post("/create", response_model=User)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Create new user
    :param user:
    :param db:
    :return:
    """
    return await create_user(db, user)


@router.get("/get/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Retrieve existing user by user_id
    :param user_id:
    :param db:
    :return:
    """
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/update/{user_id}", response_model=User)
async def update_existing_user(
    user_id: int, user_data: UserUpdate, db: AsyncSession = Depends(get_db)
):
    """
    Update existing user by user_id
    :param user_id:
    :param user_data:
    :param db:
    :return:
    """
    user = await update_user(db, user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/delete/{user_id}")
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Delete existing user by user_id
    :param user_id:
    :param db:
    :return:
    """
    await delete_user(db, user_id)
    raise HTTPException(status_code=404, detail="User has deleted")


@router.get("/list/", response_model=List[User],
            name="Users list with filter and sorting",
            description="Users list, filter by username limit 10, sort by `username` or `email`")
async def users_list(
    skip: int = 0, limit: int = 10,
    username: str = Query(None, description="Filter by username"),
    sort_by: str = Query(None, description="Sort by 'username' or 'email'"),
    db: AsyncSession = Depends(get_db),
):
    """
    Get users list
    :param skip:
    :param limit:
    :param db:
    :param username:
    :param sort_by:
    :return:
    """
    users = await list_users(db, skip, limit, username, sort_by)
    return users
