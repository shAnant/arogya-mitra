from pydantic import BaseModel
from typing import List, Optional


class MealBase(BaseModel):

    meal_type: str
    description: str
    calories: Optional[int] = None


class MealCreate(MealBase):
    pass


class MealResponse(MealBase):

    id: int

    class Config:
        from_attributes = True


class NutritionPlanBase(BaseModel):

    goal: Optional[str] = None


class NutritionPlanCreate(NutritionPlanBase):

    meals: List[MealCreate]


class NutritionPlanResponse(NutritionPlanBase):

    id: int
    meals: List[MealResponse]

    class Config:
        from_attributes = True