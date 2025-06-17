from fastapi import APIRouter

from backend.api.schemas.reservation import Reservation
from backend.api.schemas.seat import ReservedSeats

router = APIRouter()


@router.post(
    "/seats/{movie_id}/reserve",
    tags=["seats"],
    description="Saves seats for the user",
)
async def reserve_seats(movie_id: str, seats: ReservedSeats):
    pass


@router.post(
    "/seats/{movie_id}/pay",
    tags=["seats"],
    description="Execute a payment for the movie tickets."
)
async def pay_tickets(movie_id: str, reservation: Reservation):
    pass