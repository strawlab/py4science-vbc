
# ....
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from apgooglelayer.oauth import get_calendar_service
from apgooglelayer.calendar import GoogleCalendar


secrets = "./client-secrets.json"
service = get_calendar_service(secrets, "py4science-example04")

Calendar = GoogleCalendar(service)


for cal in Calendar.list_calendars():
    print cal['summary']
    for i, ev in enumerate(Calendar.iter_events(calendarId=cal['id'])):
        if i > 4: break
        if ev['status'] != "cancelled":
            START = ev['start']['date'] if 'date' in ev['start'].keys() else ev['start']['dateTime']
            print "    ", START, ev.get('summary', 'N/A')

