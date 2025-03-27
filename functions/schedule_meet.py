from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime, timedelta

from datetime import datetime, timedelta
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def schedule_meet(date, starttime, endtime, purpose):
    try:
        # Combine date with start and end times
        start_datetime = datetime.fromisoformat(f"{date}T{starttime}")
        end_datetime = datetime.fromisoformat(f"{date}T{endtime}")

        creds = Credentials.from_service_account_file(
            '/Users/arunkaul/Desktop/ai-call/functions/cred/sql-db-454217-6d8b6753df48.json',
            scopes=['https://www.googleapis.com/auth/calendar']
        )
        service = build('calendar', 'v3', credentials=creds)
        
        event = {
            'summary': purpose,
            'start': {
                'dateTime': start_datetime.isoformat(),
                'timeZone': 'UTC'
            },
            'end': {
                'dateTime': end_datetime.isoformat(),
                'timeZone': 'UTC'
            },
            'reminders': {
                'useDefault': True
            }
        }
        
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


