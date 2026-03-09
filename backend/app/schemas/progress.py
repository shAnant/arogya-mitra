from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProgressBase(BaseModel):

    weight: Optional[float] = None
    body_fat: Optional[float] = None
    workout_completed: Optional[int] = 0


class ProgressCreate(ProgressBase):
    pass


class ProgressResponse(ProgressBase):

    id: int
    created_at: datetime

    class Config:
        from_attributes = True