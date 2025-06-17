from typing import List
from uuid import UUID

from pydantic import BaseModel


class Seat(BaseModel):
    show_id: UUID
    seat_label: str
    is_free: bool


class ReservedSeats(BaseModel):
    movie_id: UUID
    seats: List[Seat]
