from typing import List
from uuid import UUID

from pydantic import BaseModel


class Seat(BaseModel):
    seat_label: str


class CheckInSeat(Seat):
    show_id: UUID
    is_free: bool


class SeatsToReserve(BaseModel):
    seats: List[Seat]
