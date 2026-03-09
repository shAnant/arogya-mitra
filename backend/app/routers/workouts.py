from fastapi import APIRouter

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.get("/plan")
def get_workout_plan():
    return {
        "plan": [
            {
                "name": "Push Ups",
                "sets": 3,
                "reps": 12,
                "video": "https://www.w3schools.com/html/mov_bbb.mp4"
            },
            {
                "name": "Squats",
                "sets": 3,
                "reps": 15,
                "video": "https://www.w3schools.com/html/mov_bbb.mp4"
            },
            {
                "name": "Plank",
                "sets": 3,
                "reps": 30,
                "video": "https://www.w3schools.com/html/mov_bbb.mp4"
            }
        ]
    }


@router.post("/start")
def start_workout(data: dict):
    return {"message": "Workout started"}


@router.post("/complete")
def complete_workout(data: dict):
    return {"message": "Workout completed"}