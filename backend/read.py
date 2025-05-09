from icalendar import Calendar
from datetime import datetime

from event import Event


def read_ics(fn: str) -> Calendar:
    """Reads an ICS file and returns its content."""
    with open(fn, "rb") as f:
        return Calendar.from_ical(f.read())


def get_events(fn="ics/sacha@wearebit.com.ics") -> list[Event]:
    cal = read_ics(fn)
    events = []
    for component in cal.walk():
        if component.name == "VEVENT":
            starttime, endtime = component.get("dtstart"), component.get("dtend")
            if endtime:
                events.append(Event(starttime.dt, endtime.dt))
    return events


def find_free_slots(
    events: list[Event], start_day: datetime, end_day: datetime
) -> list[Event]:

    free_events = []
    current = start_day
    for event in events:

        try:
            if event.endtime.date() != start_day.date():
                continue
        except AttributeError:
            continue

        print(event.starttime, start_day)
        event_start = max(event.starttime, start_day)
        event_end = min(event.endtime, end_day)
        if event_start > current:
            free_events.append(Event(current, event_start))

        current = max(current, event_end)

    if current < end_day:
        free_events.append(Event(current, end_day))

    return free_events


if __name__ == "__main__":
    events = get_events()
    start_day = datetime(2025, 5, 7)
    end_day = datetime(2025, 5, 7)
    free_slots = find_free_slots(events, start_day, end_day)
