from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete
from models.user import User as UserModel
from schemas.user import UserCreate, UserUpdate


async def create_user(db: AsyncSession, user: UserCreate):
    user = UserModel(**user.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(UserModel.__table__.select().where(UserModel.id == user_id))
    user = result.fetchone()
    return user


async def update_user(db: AsyncSession, user_id: int, user_data: UserUpdate):
    try:
        user_dict = user_data.dict()
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
        raise HTTPException(
            status_code=400,
            detail=dict(error_message=f"{ex}")
        )


async def delete_user(db: AsyncSession, user_id: int):
    try:
        deleted_stmt = (
            delete(UserModel.__table__)
            .where(UserModel.id == user_id)
        )

        await db.execute(deleted_stmt)
        await db.commit()
    except Exception as ex:
        raise HTTPException(
            status_code=400,
            detail=dict(error_message=f"{ex}")
        )


async def list_users(db: AsyncSession, skip: int = 0, limit: int = 10):
    try:
        query = await db.execute(UserModel.__table__.select().offset(skip).limit(limit))
        users = query.fetchall()
        return users
    except Exception as ex:
        print(f"{ex}")
        return list()
