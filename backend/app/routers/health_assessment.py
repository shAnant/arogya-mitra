from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health Assessment"]
)

@router.get("/bmi")
def calculate_bmi(weight: float, height: float):

    bmi = weight / (height * height)

    return {
        "BMI": round(bmi,2)
    }