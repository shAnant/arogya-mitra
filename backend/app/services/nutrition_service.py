import httpx
from app.utils.config import settings


BASE_URL = "https://api.spoonacular.com/mealplanner/generate"


async def generate_meal_plan(calories: int, diet: str = None):

    params = {
        "apiKey": settings.SPOONACULAR_API_KEY,
        "timeFrame": "week",
        "targetCalories": calories
    }

    if diet:
        params["diet"] = diet

    async with httpx.AsyncClient() as client:

        response = await client.get(BASE_URL, params=params)

        data = response.json()

        return data
    
def parse_meal_plan(data):

    week_plan = []

    for day, details in data["week"].items():

        meals = []

        for meal in details["meals"]:

            meals.append({
                "title": meal["title"],
                "id": meal["id"],
                "readyInMinutes": meal["readyInMinutes"],
                "servings": meal["servings"],
                "sourceUrl": meal["sourceUrl"]
            })

        week_plan.append({
            "day": day,
            "meals": meals,
            "nutrients": details["nutrients"]
        })

    return week_plan

def generate_grocery_list(week_plan):

    grocery_items = []

    for day in week_plan:

        for meal in day["meals"]:
            grocery_items.append(meal["title"])

    return list(set(grocery_items))