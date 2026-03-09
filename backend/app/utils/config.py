from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL:str
    SECRET_KEY:str
    
    ENVIRONMENT:str
    DEBUG:str
    CORS_ORIGIN:str
    
    GROQ_API_KEY: str
    OPENAI_API_KEY:str
    GEMINI_API_KEY:str
    
    
    GOOGLE_CALENDAR_CLIENT_ID: str
    GOOGLE_CALENDAR_CLIENT_SECRET: str
    GOOGLE_CALENDAR_REDIRECT_URI: str
    YOUTUBE_SERVICE_ACCOUNT_ID:str
    YOUTUBE_API_KEY: str     
    
    SPOONACULAR_API_KEY: str
    
    class Config:
        env_file = ".env"


settings = Settings()