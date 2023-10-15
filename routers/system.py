"""
Routers for system enpoints
"""
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db_config import get_db
from models.user import User as UserModel

router = APIRouter(
    tags=["System"],
)


@router.get("/health/check", tags=["System"])
def health_check():
    """
    Simple health check
    :return:
    """
    return {"status": True, "message": "Success"}


@router.get("/health/check/db")
async def db_check_health(db: AsyncSession = Depends(get_db)):
    """
    health check: DB connection is OK?
    :param db:
    :return:
    """
    try:
        await db.execute(UserModel.__table__.select())
        return {"status": True, "message": "DB connection is: OK"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection error") from e
