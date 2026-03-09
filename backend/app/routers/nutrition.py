from fastapi import APIRouter, Depends
from app.services.ai_agent import ArogyaMitraAgent
from app.dependencies.auth_dependency import get_current_user

router = APIRouter(prefix="/nutrition", tags=["Nutrition"])

agent = ArogyaMitraAgent()


@router.get("/ai-meal-plan")
async def generate_meal_plan(user=Depends(get_current_user)):

    plan = await agent.generate_nutrition_plan(user)

    return plan