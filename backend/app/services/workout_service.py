from app.models.user import FitnessGoal, WorkoutPreference
from app.services.video_service import search_exercise_video


def generate_workout_plan(user):

    goal = user.fitness_goal
    preference = user.workout_preference

    if goal == FitnessGoal.WEIGHT_LOSS:

        plan = [
            "Jump Rope - 10 minutes",
            "Squats - 3x15",
            "Mountain Climbers - 3x20",
            "Plank - 60 sec"
        ]

    elif goal == FitnessGoal.MUSCLE_GAIN:

        plan = [
            "Push Ups - 4x12",
            "Pull Ups - 4x8",
            "Bench Press - 4x10",
            "Deadlift - 4x8"
        ]

    else:

        plan = [
            "Jogging - 20 min",
            "Bodyweight Squats - 3x12",
            "Plank - 45 sec"
        ]

    return {
        "goal": goal,
        "preference": preference,
        "workout_plan": plan
    }
    


async def enrich_workout_with_videos(workout_plan: list):

    enriched = []

    for exercise in workout_plan:

        video = await search_exercise_video(exercise)

        enriched.append({
            "exercise": exercise,
            "video": video
        })

    return enriched