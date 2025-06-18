from scripts.regsetup import description
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.api.crud.basic_service import Service
from backend.database.models import Movie as SQLMovie
from backend.api.schemas.movie import Movie as SchemaMovie


class MovieService(Service):

    def __init__(self, db_session):
        super().__init__(db_session)


    async def get_upcoming_movies(self):
        query = select(SQLMovie).options(selectinload(SQLMovie.shows))
        result = await self.db_session.execute(query)
        movies = result.scalars().all()

        return [
            SchemaMovie(
                name=movie.name,
                description=movie.description,
                image_id=movie.image_id,
                times = [show.time for show in movie.shows]
            )
            for movie in movies
        ]
