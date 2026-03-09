import asyncio
from typing import Dict, Any

from groq import Groq
from app.utils.config import settings

from app.models.user import (
    FitnessGoal,
    WorkoutPreference,
    DietPreference
)

from app.services.workout_service import enrich_workout_with_videos
from app.services.nutrition_service import generate_meal_plan, parse_meal_plan

class ArogyaMitraAgent:
    """
    🤖 ArogyaMitra AI Agent (AROMI)

    Responsible for:
    - Workout plan generation
    - Nutrition planning
    - AI chat coaching
    - Adaptive plan adjustments
    """

    def __init__(self):

        self.client = None
        self.initialize_ai_clients()

    # ----------------------------------------
    # Initialize Groq client
    # ----------------------------------------

    def initialize_ai_clients(self):

        try:

            if settings.GROQ_API_KEY:

                self.client = Groq(
                    api_key=settings.GROQ_API_KEY
                )

                print("✅ Groq AI client initialized")

            else:

                print("⚠️ GROQ_API_KEY missing")

        except Exception as e:

            print("AI initialization error:", e)

    # ----------------------------------------
    # Generic AI call
    # ----------------------------------------

    async def _ask_ai(self, prompt: str):

        try:

            completion = self.client.chat.completions.create(

                model="llama3-70b-8192",

                messages=[
                    {
                        "role": "system",
                        "content": "You are AROMI, a professional AI fitness coach."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],

                temperature=0.7
            )

            return completion.choices[0].message.content

        except Exception as e:

            return f"AI Error: {str(e)}"

    # ----------------------------------------
    # Workout plan generator
    # ----------------------------------------

    async def generate_workout_plan(self, user) -> Dict[str, Any]:

        prompt = f"""
        Generate a weekly workout plan.

        User details:
        Goal: {user.fitness_goal}
        Workout preference: {user.workout_preference}
        Age: {user.age}
        Weight: {user.weight}
        Height: {user.height}

        Provide:
        - 5 day workout schedule
        - exercises
        - sets and reps
        """

        response = await self._ask_ai(prompt)

        return {

            "type": "workout_plan",
            "plan": response
        }

    # ----------------------------------------
    # Nutrition plan generator
    # ----------------------------------------

    async def generate_nutrition_plan(self, user) -> Dict[str, Any]:

        prompt = f"""
        Create a healthy daily nutrition plan.

        User details:
        Goal: {user.fitness_goal}
        Diet preference: {user.diet_preference}
        Weight: {user.weight}

        Include:
        breakfast
        lunch
        dinner
        snacks
        calories
        """

        response = await self._ask_ai(prompt)

        return {

            "type": "nutrition_plan",
            "plan": response
        }

    # ----------------------------------------
    # AI coach chat
    # ----------------------------------------

    async def chat_coach(self, message: str):

        prompt = f"""
        You are AROMI AI fitness coach.

        Respond to this message in a friendly and helpful way.

        Message:
        {message}
        """

        response = await self._ask_ai(prompt)

        return {

            "type": "chat",
            "response": response
        }

    # ----------------------------------------
    # Dynamic plan adjustment
    # ----------------------------------------

    async def adjust_plan(self, reason: str, user_data: Dict):

        prompt = f"""
        Adjust the user's workout and nutrition plan.

        Reason:
        {reason}

        User data:
        {user_data}

        Provide modified recommendations.
        """

        response = await self._ask_ai(prompt)

        return {

            "type": "adjusted_plan",
            "recommendation": response
        }
        
    async def generate_workout_plan(self, user):

        prompt = f"""
        Generate a list of exercises for:
        Goal: {user.fitness_goal}
        Preference: {user.workout_preference}

        Return 5 exercises only.
        """

        response = await self._ask_ai(prompt)

        exercises = [x.strip() for x in response.split("\n") if x.strip()]

        exercises = exercises[:5]

        enriched = await enrich_workout_with_videos(exercises)

        return {
            "exercises": enriched
        }
        
    async def generate_nutrition_plan(self, user):

        calories = 2000

        if user.fitness_goal == "weight_loss":
            calories = 1600

        elif user.fitness_goal == "muscle_gain":
            calories = 2500

        diet = None

        if user.diet_preference:
            diet = user.diet_preference.value

        data = await generate_meal_plan(calories, diet)

        parsed = parse_meal_plan(data)

        return {
            "type": "nutrition_plan",
            "week_plan": parsed
        }
        
    async def aromi_coach(self, user, message: str, history: list):

        history_text = ""

        for h in history[-5:]:
            history_text += f"User: {h.message}\nAROMI: {h.response}\n"

        prompt = f"""
    You are AROMI, an intelligent AI fitness coach.

    User profile:
    Goal: {user.fitness_goal}
    Diet: {user.diet_preference}
    Workout preference: {user.workout_preference}

    Conversation history:
    {history_text}

    User message:
    {message}

    Instructions:
    - If user mentions travel → suggest portable workouts
    - If injury → suggest safe alternatives
    - If busy schedule → give quick routines
    - If tired or low motivation → give encouragement
    - Suggest hydration and recovery tips

    Respond clearly and briefly.
    """

        response = await self._ask_ai(prompt)

        return response