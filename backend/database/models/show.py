from uuid import uuid4

from sqlalchemy import UUID, Column, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from backend.database.settings.base import Base


class Show(Base):

    __tablename__ = "show"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    movie_id = Column(UUID(as_uuid=True), ForeignKey('movie.id'))
    time = Column(DateTime, nullable=False)

    movie = relationship("Movie", back_populates="show")