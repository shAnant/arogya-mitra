from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserRegister, UserLogin

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        (User.email == user.email) |
        (User.username == user.username)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already exists"
        )

    hashed = hash_password(user.password)

    new_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed,
        full_name=user.full_name,
        age=user.age,
        gender=user.gender,
        height=user.height,
        weight=user.weight,
        fitness_level=user.fitness_level,
        fitness_goal=user.fitness_goal,
        workout_preference=user.workout_preference,
        diet_preference=user.diet_preference
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = None

    if user.email:
        db_user = db.query(User).filter(
            User.email == user.email
        ).first()

    elif user.username:
        db_user = db.query(User).filter(
            User.username == user.username
        ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Wrong password"
        )

    token = create_access_token(
        {"sub": db_user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }