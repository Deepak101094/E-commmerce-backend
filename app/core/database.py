from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine
)

from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings



class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    settings.DATABASE_URL,
)

SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)

async def get_db():
    async with SessionLocal() as session:
        yield session


async def check_database_connection() ->bool:
    try: 
       async with engine.connect() as connection:
              result = await connection.execute(text("SELECT 1"))

              return result.scalar_one() == 1
    except SQLAlchemyError:
        return False