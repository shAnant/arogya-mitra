from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class WorkoutPlan(Base):

    __tablename__ = "workout_plans"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    title = Column(String)
    description = Column(String)

    user = relationship("User", back_populates="workouts")

    exercises = relationship("Exercise", back_populates="workout_plan")


class Exercise(Base):

    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)

    workout_id = Column(Integer, ForeignKey("workout_plans.id"))

    name = Column(String)

    sets = Column(Integer)
    reps = Column(Integer)

    rest_seconds = Column(Integer)

    workout_plan = relationship("WorkoutPlan", back_populates="exercises")