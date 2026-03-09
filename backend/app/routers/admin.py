from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/stats")
def system_stats():

    return {
        "total_users": 120,
        "active_today": 48
    }