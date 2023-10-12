from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db_config import get_db

router = APIRouter(
    tags=["System"],
)


@router.get("/health/check", tags=["System"])
def health_check():
    return {
        "status": True,
        "message": "Success"
    }


@router.get("/health/check/db")
async def db_check_health(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute("SELECT 1")
        return {
            "status": True,
            "message": "DB connection is: OK"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection error") from e
