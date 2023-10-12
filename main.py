from typing import List, Annotated

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from database import async_session, engine, Base
from crud.user import create_user, get_user, delete_user, update_user, list_users
from schemas.user import UserCreate, UserUpdate, User


async def get_db():
    async_db = async_session()
    try:
        yield async_db
    finally:
        await async_db.close()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


description = """
Ax Technology API helps you do awesome stuff. 🚀

## Users CRUD and List via APIs

You can: 
- create user
- read user
- update user
- delete user
- see user list
"""

app = FastAPI(
    title="Ax Technology test",
    version="1.0.0",
    description=description,
    contact={
        "name": "Tatibaev Murat",
        "email": "tatibaevmurod@gmail.com",
    },
    openapi_url="/api/v1/openapi.json"
)


@app.get("/health/check", tags=["System"])
def root():
    return {"success": True}


@app.post("/users/", response_model=User)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: int, user_data: UserUpdate, db: AsyncSession = Depends(get_db)):
    user = await update_user(db, user_id, user_data)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}")
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    await delete_user(db, user_id)
    raise HTTPException(status_code=404, detail="User has deleted")


@app.get("/users/", response_model=List[User])
async def users_list(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    users = await list_users(db, skip, limit)
    return users


if __name__ == "__main__":
    import uvicorn

    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_tables())

    uvicorn.run("main:app", host="0.0.0.0", port=8008, reload=True)
