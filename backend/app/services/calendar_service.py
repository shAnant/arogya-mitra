from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta


class CalendarService:

    def __init__(self, access_token):

        self.creds = Credentials(token=access_token)

        self.service = build(
            "calendar",
            "v3",
            credentials=self.creds
        )

    # Create workout event
    def create_workout_event(self, title, start_time):

        end_time = start_time + timedelta(hours=1)

        event = {
            "summary": title,
            "description": "Workout session scheduled by ArogyaMitra",
            "start": {
                "dateTime": start_time.isoformat(),
                "timeZone": "Asia/Kolkata",
            },
            "end": {
                "dateTime": end_time.isoformat(),
                "timeZone": "Asia/Kolkata",
            },
            "reminders": {
                "useDefault": False,
                "overrides": [
                    {"method": "popup", "minutes": 30},
                    {"method": "email", "minutes": 60},
                ],
            },
        }

        event = self.service.events().insert(
            calendarId="primary",
            body=event
        ).execute()

        return event