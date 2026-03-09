from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class ProgressRecord(Base):

    __tablename__ = "progress_records"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    weight = Column(Float)

    body_fat = Column(Float)

    workout_completed = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="progress_records")