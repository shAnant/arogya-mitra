from sqlalchemy import Column, Integer, String, Float, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum

from app.database import Base


class UserRole(str, enum.Enum):
    USER = "user"
    ADMIN = "admin"


class FitnessGoal(str, enum.Enum):
    WEIGHT_LOSS = "weight_loss"
    WEIGHT_GAIN = "weight_gain"
    MUSCLE_GAIN = "muscle_gain"
    MAINTENANCE = "maintenance"
    ENDURANCE = "endurance"


class WorkoutPreference(str, enum.Enum):
    HOME = "home"
    GYM = "gym"
    OUTDOOR = "outdoor"
    HYBRID = "hybrid"


class DietPreference(str, enum.Enum):
    VEGETARIAN = "vegetarian"
    NON_VEGETARIAN = "non_vegetarian"
    VEGAN = "vegan"
    KETO = "keto"
    PALEO = "paleo"


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)

    hashed_password = Column(String)

    full_name = Column(String)

    age = Column(Integer)
    gender = Column(String)

    height = Column(Float)
    weight = Column(Float)

    role = Column(Enum(UserRole), default=UserRole.USER)

    fitness_goal = Column(Enum(FitnessGoal))
    workout_preference = Column(Enum(WorkoutPreference))
    diet_preference = Column(Enum(DietPreference))

    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    workouts = relationship("WorkoutPlan", back_populates="user")
    nutrition_plans = relationship("NutritionPlan", back_populates="user")
    assessments = relationship("HealthAssessment", back_populates="user")
    progress_records = relationship("ProgressRecord", back_populates="user")
    chat_sessions = relationship("ChatSession", back_populates="user")