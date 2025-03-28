from datetime import datetime, timedelta
import pytz
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def schedule_meet(date, starttime, endtime, purpose):
    try:
        # Define timezones
        local_tz = pytz.timezone('Asia/Kolkata')
        utc_tz = pytz.utc

        # Handle relative date inputs
        if date.lower() == "today":
            date = datetime.now(local_tz).strftime('%Y-%m-%d')
        elif date.lower() == "tomorrow":
            date = (datetime.now(local_tz) + timedelta(days=1)).strftime('%Y-%m-%d')
        elif date.lower() in ["day after", "day after tomorrow"]:
            date = (datetime.now(local_tz) + timedelta(days=2)).strftime('%Y-%m-%d')

        # Convert local time to UTC
        start_datetime = local_tz.localize(datetime.fromisoformat(f"{date}T{starttime}")).astimezone(utc_tz)
        end_datetime = local_tz.localize(datetime.fromisoformat(f"{date}T{endtime}")).astimezone(utc_tz)

        # Load Google Calendar API credentials
        creds = Credentials.from_service_account_file(
            '/Users/arunkaul/Desktop/ai-call/functions/cred/sql-db-454217-6d8b6753df48.json',
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        service = build('calendar', 'v3', credentials=creds)

        # Create the event
        event = {
            'summary': purpose,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': 'Asia/Kolkata'
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': 'Asia/Kolkata'
            },
            'reminders': {
                'useDefault': True
            }
        }

        # Insert event into the calendar
        event = service.events().insert(calendarId='aryankaul539@gmail.com', body=event).execute()
        print(event)
        return {
            'status': 'Successfully scheduled',
            'event_id': event['id'],
            'event_link': event['htmlLink']
        }

    except Exception as e:
        return {
            'status': 'Error',
            'message': str(e)
        }
