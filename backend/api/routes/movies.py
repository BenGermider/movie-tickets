from datetime import datetime
from typing import List

from fastapi import APIRouter

from backend.api.crud.movie_service import MovieService
from backend.api.schemas import Movie, CheckInSeat
from backend.database.settings.session import get_db

router = APIRouter(prefix="/movies", tags=["movies"])

movies_service = MovieService(db_session=get_db())

@router.get(
    "/",
    description="Get all upcoming movies",
    response_model=List[Movie]
)
async def upcoming_movies() -> List[Movie]:
    return await movies_service.get_upcoming_movies()


@router.get(
    "/{movie_id}",
    description="Get the times of an upcoming movie",
    response_model=List[datetime]
)
async def get_movie(movie_id: str):
    return await movies_service.get_show_times(movie_id)


@router.get(
    "/{movie_id}/{time_id}/seats",
    description="The seats of the hall of the movie.",
    response_model=List[CheckInSeat]
)
async def get_seats_for_movie(movie_id: str, time_id: datetime):
    return await movies_service.get_show_seats(movie_id, time_id)
