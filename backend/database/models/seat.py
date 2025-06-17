from uuid import uuid4

from sqlalchemy import UUID, Column, String, Boolean, ForeignKey

from backend.database.settings.base import Base


class Seat(Base):

    __tablename__ = "seat"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    seat_label = Column(String, nullable=False)
    is_taken = Column(Boolean, default=False)
    show_id = Column(UUID(as_uuid=True), ForeignKey("show.id"))
