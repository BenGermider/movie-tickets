from typing import List

from fastapi import APIRouter

from backend.api.schemas import Movie, MovieShow, CheckInSeat

router = APIRouter(prefix="/movies", tags=["movies"])


@router.get(
    "/",
    description="Get all upcoming movies",
    response_model=List[Movie]
)
async def upcoming_movies() -> List[Movie]:
    pass


@router.get(
    "/{movie_id}",
    description="Get the times of an upcoming movie",
    response_model=List[MovieShow]
)
async def get_movie(movie_id: str):
    pass


@router.get(
    "/{movie_id}/{time_id}/seats",
    description="The seats of the hall of the movie.",
    response_model=List[CheckInSeat]
)
async def get_seats_for_movie(movie_id: str, time_id: str):
    pass
