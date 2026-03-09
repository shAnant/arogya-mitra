from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base


class HealthAssessment(Base):

    __tablename__ = "health_assessments"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    bmi = Column(Float)

    body_fat = Column(Float)

    resting_heart_rate = Column(Integer)

    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="assessments")