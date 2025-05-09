from datetime import datetime
import sys

sys.path.append("..")
from event import Event
from planner import find_overlaps

# Example input (Calendars with events that last at least 2 hours and have overlaps)
calendar1 = [
    Event(
        starttime=datetime(2025, 5, 8, 9, 0), endtime=datetime(2025, 5, 8, 11, 0)
    ),  # Event lasting 2 hours
    Event(
        starttime=datetime(2025, 5, 8, 13, 0), endtime=datetime(2025, 5, 8, 15, 0)
    ),  # Event lasting 2 hours
]

calendar2 = [
    Event(
        starttime=datetime(2025, 5, 8, 10, 0), endtime=datetime(2025, 5, 8, 12, 0)
    ),  # Event lasting 2 hours, overlaps with calendar1[0]
    Event(
        starttime=datetime(2025, 5, 8, 16, 0), endtime=datetime(2025, 5, 8, 18, 0)
    ),  # Event lasting 2 hours
]

calendar3 = [
    Event(
        starttime=datetime(2025, 5, 8, 7, 0), endtime=datetime(2025, 5, 8, 9, 30)
    ),  # Event lasting 2 hours, overlaps with calendar1[0]
    Event(
        starttime=datetime(2025, 5, 8, 14, 0), endtime=datetime(2025, 5, 8, 16, 0)
    ),  # Event lasting 2 hours, overlaps with calendar2[0]
]

# List of calendars
calendars = [calendar1, calendar2, calendar3]


print("Overlapping events:")
overlaps = find_overlaps(calendars)
print(overlaps)
