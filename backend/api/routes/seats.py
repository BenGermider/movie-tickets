from fastapi import APIRouter

from backend.api.schemas.reservation import Reservation
from backend.api.schemas.seat import SeatsToReserve

router = APIRouter(prefix="/seats", tags=["seats"])


@router.post(
    "/{movie_id}/reserve",
    description="Saves seats for the user",
)
async def reserve_seats(movie_id: str, seats: SeatsToReserve):
    pass


@router.post(
    "/{movie_id}/pay",
    description="Execute a payment for the movie tickets."
)
async def pay_tickets(movie_id: str, reservation: Reservation):
    pass