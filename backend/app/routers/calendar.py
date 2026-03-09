from fastapi import APIRouter
from datetime import datetime

from app.services.calendar_service import CalendarService

router = APIRouter(prefix="/calendar", tags=["Calendar"])

@router.post("/schedule-workout")
def schedule_workout(access_token: str):

    calendar = CalendarService(access_token)

    event = calendar.create_workout_event(
        "ArogyaMitra Workout Session",
        datetime.now()
    )

    return event