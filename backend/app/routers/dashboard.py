from fastapi import APIRouter

router = APIRouter()

@router.get("/dashboard")
def get_dashboard():
    return {
        "calories_burned": 450,
        "workout_streak": 5,
        "charity_points": 120,
        "next_workout": "Push Ups",
        "message": "Welcome to ArogyaMitra Dashboard"
    }