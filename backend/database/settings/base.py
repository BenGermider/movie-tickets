import asyncio
from sqlalchemy.orm import declarative_base
from .session import engine
from backend.database.models import (
    Movie,
    Reservation,
    Show,
    Seat
)

Base = declarative_base()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all(bind=engine))


if __name__ == "__main__":
    asyncio.run(init_db())