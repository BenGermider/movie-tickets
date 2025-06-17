from uuid import uuid4

from sqlalchemy import Column, UUID, String

from backend.database.settings.base import Base


class Movie(Base):

    __tablename__ = "movie"

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    image_id = Column(String, nullable=False, unique=True)
