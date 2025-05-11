from icalendar import Calendar as iCalendar
from datetime import datetime
from datetime import timezone
from dateutil import tz

from event import Event


class Calendar:
    def __init__(self, fn: str):
        with open(fn, "rb") as f:
            self.components = iCalendar.from_ical(f.read())
        self.events = self._get_events()

    def _get_events(self) -> list[Event]:
        """
        Get all events from the calendar.

        Returns:
            list[Event]: List of events in the calendar.
        """
        events = []
        for component in self.components.walk():
            if component.name == "VEVENT":
                starttime, endtime = component.get("dtstart"), component.get("dtend")
                if endtime:
                    events.append(Event(starttime.dt, endtime.dt))
        return events

    def get_free_events(self, event: Event) -> list[Event]:
        """
        Get free events inside the given event.

        Args:
            start_day (datetime): Start day to check for free events.
            end_day (datetime): End day to check for free events.

        Returns:
            list[Event]: List of free events between `start_day` and `end_day`.
        """

        free_events = []
        current = start_day
        for event in self.events:

            try:
                if event.endtime.date() != start_day.date():
                    continue
            except AttributeError:
                continue

            event_start = max(event.starttime, start_day)
            event_end = min(event.endtime, end_day)
            if event_start > current:
                free_events.append(Event(current, event_start))

            current = max(current, event_end)

        if current < end_day:
            free_events.append(Event(current, end_day))

        return free_events


if __name__ == "__main__":
    calendar = Calendar("ics/sacha@wearebit.com.ics")
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()

    start_day = datetime(2025, 5, 7).replace(tzinfo=from_zone)
    start_day = start_day.astimezone(to_zone)
    end_day = datetime(2025, 5, 7, 23, 59).replace(tzinfo=from_zone)
    end_day = end_day.astimezone(to_zone)

    free_slots = calendar.get_free_events(start_day, end_day)
    print(free_slots)
