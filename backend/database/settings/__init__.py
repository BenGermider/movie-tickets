import asyncio
from backend.database.models import (
    Movie,
    Reservation,
    Show,
    Seat
)
# Python
from backend.database.settings.session import engine
from backend.database.settings.base import Base  # adjust import as needed

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())