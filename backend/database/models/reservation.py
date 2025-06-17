from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, UUID, DateTime, String
from sqlalchemy.orm import relationship

from backend.database.models.reservation_seat_association import reservation_seat_association
from backend.database.settings.base import Base


class Reservation(Base):

    __tablename__ = "reservation"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    seats = relationship('Seat', secondary=reservation_seat_association)
    owner = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


