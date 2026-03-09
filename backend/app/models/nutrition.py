from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class NutritionPlan(Base):

    __tablename__ = "nutrition_plans"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    goal = Column(String)

    user = relationship("User", back_populates="nutrition_plans")

    meals = relationship("Meal", back_populates="nutrition_plan")


class Meal(Base):

    __tablename__ = "meals"

    id = Column(Integer, primary_key=True)

    plan_id = Column(Integer, ForeignKey("nutrition_plans.id"))

    meal_type = Column(String)

    description = Column(String)

    calories = Column(Integer)

    nutrition_plan = relationship("NutritionPlan", back_populates="meals")