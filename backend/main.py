from fastapi import FastAPI
from app.database import Base, engine
from app.routers import google_auth
from fastapi.middleware.cors import CORSMiddleware


from app.routers import (
    auth,
    workouts,
    nutrition,
    progress,
    health_assessment,
    ai_coach,
    calendar,
    admin,
    dashboard
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ArogyaMitra API",
    version="1.0"
)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(google_auth.router)
app.include_router(dashboard.router)
app.include_router(workouts.router)
app.include_router(nutrition.router)
app.include_router(progress.router)
app.include_router(health_assessment.router)
app.include_router(ai_coach.router)
app.include_router(calendar.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"message": "ArogyaMitra Backend Running"}