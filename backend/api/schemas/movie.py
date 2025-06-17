from datetime import datetime
from typing import List
from uuid import UUID

from pydantic import BaseModel

from backend.api.schemas.seat import Seat


class Movie(BaseModel):
    description: str
    image_id: str
    times: List[datetime]


class MovieShow(BaseModel):
    movie_id: UUID
    seats: List[Seat]
    show_time: datetime
