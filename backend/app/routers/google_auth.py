from fastapi import APIRouter
from app.utils.config import settings
from urllib.parse import urlencode
import httpx


router = APIRouter(prefix="/auth/google", tags=["Google Auth"])


@router.get("/login")
def google_login():

    params = {
        "client_id": settings.GOOGLE_CALENDAR_CLIENT_ID,
        "redirect_uri": settings.GOOGLE_CALENDAR_REDIRECT_URI,
        "response_type": "code",
        "scope": "https://www.googleapis.com/auth/calendar",
        "access_type": "offline",
        "prompt": "consent",
    }

    auth_url = "https://accounts.google.com/o/oauth2/v2/auth"

    return {
        "auth_url": f"{auth_url}?{urlencode(params)}"
    }
    
@router.get("/callback")
async def google_callback(code: str):

    token_url = "https://oauth2.googleapis.com/token"

    data = {
        "code": code,
        "client_id": settings.GOOGLE_CALENDAR_CLIENT_ID,
        "client_secret": settings.GOOGLE_CALENDAR_CLIENT_SECRET,
        "redirect_uri": settings.GOOGLE_CALENDAR_REDIRECT_URI,
        "grant_type": "authorization_code",
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(token_url, data=data)

        token_data = response.json()

    return token_data