from typing import List

from fastapi import APIRouter

from backend.api.schemas.movie import Movie, MovieShow
from backend.api.schemas.seat import Seat

router = APIRouter()


@router.get(
    "/movies",
    tags=["movies"],
    description="Get all upcoming movies",
    response_model=List[Movie]
)
async def upcoming_movies() -> List[Movie]:
    pass


@router.get(
    "/movies/{movie_id}",
    tags=["movies"],
    description="Get the times of an upcoming movie",
    response_model=List[MovieShow]
)
async def get_movie(movie_id: str):
    pass


@router.get(
    "/movies/{movie_id}/{time_id}/seats",
    tags=["movies"],
    description="The seats of the hall of the movie.",
    response_model=List[Seat]
)
async def get_seats_for_movie(movie_id: str, time_id: str):
    pass
