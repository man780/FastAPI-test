"""User CRUD operations"""
import logging
from logging.handlers import RotatingFileHandler
from typing import Any, Sequence

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete, Row
from models.user import User as UserModel
from schemas.user import UserCreate, UserUpdate


file_handler = RotatingFileHandler("logs/crud.log", maxBytes=1024000, backupCount=3)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_handler)
logger = logging.getLogger(__name__)


async def create_user(db: AsyncSession, user: UserCreate) -> Row:
    """
    Create user

    :param db:
    :param user:
    :return: user Row
    """
    try:
        user = UserModel(**user.model_dump())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user
    except Exception as ex:
        logger.error("Error on user create: %s", ex)
        raise HTTPException(status_code=400, detail={"error_message": f"{ex}"}) from ex


async def get_user(db: AsyncSession, user_id: int) -> Row[Any] | None:
    """
    Get user by id

    :param db:
    :param user_id:
    :return: user Row
    """
    result = await db.execute(
        UserModel.__table__.select().where(UserModel.id == user_id)
    )
    user = result.fetchone()
    return user


async def update_user(db: AsyncSession, user_id: int, user_data: UserUpdate):
    """
    Update user by id

    :param db:
    :param user_id:
    :param user_data:
    :return: user Row
    """
    try:
        user_dict = user_data.model_dump()
        update_stmt = (
            update(UserModel.__table__)
            .where(UserModel.id == user_id)
            .values(**user_dict)
        )

        await db.execute(update_stmt)
        await db.commit()

        user = await get_user(db=db, user_id=user_id)
        return user
    except Exception as ex:
        logger.error("Error on user update: %s", ex)
        raise HTTPException(status_code=400, detail={"error_message": f"{ex}"}) from ex


async def delete_user(db: AsyncSession, user_id: int) -> None:
    """
    Delete user by id

    :param db:
    :param user_id:
    :return:
    """
    try:
        deleted_stmt = delete(UserModel.__table__).where(UserModel.id == user_id)

        await db.execute(deleted_stmt)
        await db.commit()
    except Exception as ex:
        logger.error("Error on user delete: %s", ex)
        raise HTTPException(status_code=400, detail={"error_message": f"{ex}"}) from ex


async def list_users(
    db: AsyncSession, skip: int = 0, limit: int = 10
) -> Sequence[Row[Any]]:
    """
    Get users list

    :param db:
    :param skip:
    :param limit:
    :return:
    """
    try:
        query = await db.execute(UserModel.__table__.select().offset(skip).limit(limit))
        users = query.fetchall()
        return users
    except Exception as ex:
        logger.error("Error on getting users list: %s", ex)
        raise HTTPException(status_code=400, detail={"error_message": f"{ex}"}) from ex
