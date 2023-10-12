from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

DATABASE_URL = "sqlite+aiosqlite:///./ax_technology.db"
engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
