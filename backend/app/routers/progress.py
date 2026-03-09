from fastapi import APIRouter, Depends

from app.dependencies.auth_dependency import get_current_user

router = APIRouter(
    prefix="/progress",
    tags=["Progress"]
)

@router.get("/stats")
def get_progress(user = Depends(get_current_user)):

    return {
        "user": user,
        "weight_change": "-2kg",
        "workouts_completed": 18
    }