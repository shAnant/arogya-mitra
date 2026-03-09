from pydantic import BaseModel
from typing import List, Optional


class ExerciseBase(BaseModel):

    name: str
    sets: int
    reps: int
    rest_seconds: Optional[int] = 60


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):

    id: int

    class Config:
        from_attributes = True


class WorkoutPlanBase(BaseModel):

    title: str
    description: Optional[str] = None


class WorkoutPlanCreate(WorkoutPlanBase):

    exercises: List[ExerciseCreate]


class WorkoutPlanResponse(WorkoutPlanBase):

    id: int
    exercises: List[ExerciseResponse]

    class Config:
        from_attributes = True