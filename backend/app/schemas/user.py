from pydantic import BaseModel, EmailStr
from typing import Optional
from app.models.user import FitnessGoal, WorkoutPreference, DietPreference


class UserBase(BaseModel):

    email: EmailStr
    username: str
    full_name: Optional[str] = None

    age: Optional[int] = None
    gender: Optional[str] = None

    height: Optional[float] = None
    weight: Optional[float] = None

    fitness_goal: Optional[FitnessGoal] = None
    workout_preference: Optional[WorkoutPreference] = None
    diet_preference: Optional[DietPreference] = None


class UserRegister(UserBase):

    password: str


class UserLogin(BaseModel):

    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: str


class UserResponse(UserBase):

    id: int

    class Config:
        from_attributes = True