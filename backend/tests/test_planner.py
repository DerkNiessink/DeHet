from datetime import datetime
import sys
import os


one_dir_up = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(one_dir_up)
from event import Event
from planner import find_pairwise_overlaps, find_all_overlaps

# Example input (Calendars with events that last at least 2 hours and have overlaps)
calendar1 = [
    Event(datetime(2025, 5, 8, 7, 0), datetime(2025, 5, 8, 9, 30)),
    Event(datetime(2025, 5, 8, 10, 0), datetime(2025, 5, 8, 12, 0)),
    Event(datetime(2025, 5, 8, 13, 0), datetime(2025, 5, 8, 15, 0)),
    Event(datetime(2025, 5, 8, 15, 30), datetime(2025, 5, 8, 17, 30)),
    Event(datetime(2025, 5, 8, 18, 0), datetime(2025, 5, 8, 20, 0)),
]

calendar2 = [
    Event(datetime(2025, 5, 8, 6, 30), datetime(2025, 5, 8, 8, 30)),
    Event(datetime(2025, 5, 8, 9, 0), datetime(2025, 5, 8, 11, 30)),
    Event(datetime(2025, 5, 8, 13, 0), datetime(2025, 5, 8, 15, 30)),
    Event(datetime(2025, 5, 8, 16, 0), datetime(2025, 5, 8, 18, 0)),
    Event(datetime(2025, 5, 8, 18, 30), datetime(2025, 5, 8, 20, 0)),
]

calendar3 = [
    Event(datetime(2025, 5, 8, 6, 45), datetime(2025, 5, 8, 9, 0)),
    Event(datetime(2025, 5, 8, 9, 15), datetime(2025, 5, 8, 11, 0)),
    Event(datetime(2025, 5, 8, 13, 0), datetime(2025, 5, 8, 14, 30)),
    Event(datetime(2025, 5, 8, 14, 45), datetime(2025, 5, 8, 16, 30)),
    Event(datetime(2025, 5, 8, 17, 0), datetime(2025, 5, 8, 19, 30)),
]

# List of calendars
calendars = [calendar1, calendar2, calendar3]


print("Overlapping events:")
overlaps = find_pairwise_overlaps(calendars)
print(overlaps)

print("Merged overlapping events:")
for cal in find_all_overlaps(calendars):
    print(cal)
    print("-----")


print(find_all_overlaps(calendars))
