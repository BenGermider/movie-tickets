from datetime import datetime
from typing import List

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.api.crud.basic_service import Service
from backend.api.schemas import Seat as SchemaSeat, CheckInSeat
from backend.database.models import Seat as SQLSeat
from backend.database.models import Movie as SQLMovie, Show
from backend.api.schemas.movie import Movie as SchemaMovie


class MovieService(Service):

    def __init__(self, db_session):
        super().__init__(db_session)


    async def get_upcoming_movies(self):
        movies = await self._get_movies()
        return [
            SchemaMovie(
                name=movie.name,
                description=movie.description,
                image_id=movie.image_id,
                times = [show.time for show in movie.shows]
            )
            for movie in movies
        ]

    async def get_show_times(self, movie_id: str) -> List[datetime]:
        query = select(Show).where(Show.movie_id == movie_id)
        res = await self.db_session.execute(query)
        return [show.time for show in res.scalars().all()]


    async def _get_movies(self) -> List[SQLMovie]:
        query = select(SQLMovie).options(selectinload(SQLMovie.shows))  # selectinload prevents the N+1 problem.
        result = await self.db_session.execute(query)
        return result.scalars().all()

    async def get_show_seats(self, movie_id: str, time: datetime) -> List[CheckInSeat]:
        show_query = select(Show).where(Show.movie_id == movie_id, Show.time == time)
        show = await self.db_session.execute(show_query)
        show_id = show.scalar_one_or_none().time
        seats_query = select(SQLSeat).where(SQLSeat.show_id == show_id)
        seats = await self.db_session.execute(seats_query)
        res = seats.scalars().all()
        return [
            CheckInSeat(
                seat_label=seat.seat_label,
                show_id=seat.show_id,
                is_free=seat.is_taken
            ) for seat in res
        ]

