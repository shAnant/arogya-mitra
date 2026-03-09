def analyze_progress(records):

    total_workouts = sum(r.workout_completed for r in records)

    avg_weight = sum(r.weight for r in records) / len(records)

    return {

        "total_workouts": total_workouts,

        "average_weight": round(avg_weight,2),

        "progress": "Improving"
    }