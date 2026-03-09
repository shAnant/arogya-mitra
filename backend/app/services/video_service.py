import httpx
from app.utils.config import settings


YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


async def search_exercise_video(query: str):

    params = {
        "part": "snippet",
        "q": f"{query} exercise tutorial",
        "key": settings.YOUTUBE_API_KEY,
        "type": "video",
        "maxResults": 1
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(YOUTUBE_SEARCH_URL, params=params)

        data = response.json()

        if "items" not in data or len(data["items"]) == 0:
            return None

        video = data["items"][0]

        video_id = video["id"]["videoId"]

        return {
            "title": video["snippet"]["title"],
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "thumbnail": video["snippet"]["thumbnails"]["high"]["url"]
        }