from sqlalchemy import Table, Column, ForeignKey
from backend.database.settings.base import Base

reservation_seat_association = Table(
    "reservation_seat_association",
    Base.metadata,
    Column("reservation_id", ForeignKey("reservation.id"), primary_key=True),
    Column("seat_id", ForeignKey("seat.id"), primary_key=True)
)