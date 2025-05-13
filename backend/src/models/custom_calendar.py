from icalendar import Calendar as iCalendar

from models.event import Event
from models.custom_time import CustomTime


class Calendar:
    """
    Class to parse and extract events from an iCalendar file.
    """

    def __init__(self, events: list[Event]):
        """
        Initialize the Calendar with a list of events.

        Args:
            events (list[Event]): List of events to initialize the calendar.
        """
        self.events = events
        self.free_events = self._get_free_events()

    @classmethod
    def from_ics(cls, fn: str) -> "Calendar":
        """
        Load an iCalendar file and extract events.

        Args:
            fn (str): Path to the iCalendar file.
        """
        with open(fn, "rb") as f:
            components = iCalendar.from_ical(f.read())

        events = []
        for component in components.walk():
            if component.name == "VEVENT":
                dtstart, dtend = component.get("dtstart"), component.get("dtend")
                if not dtstart or not dtend:
                    continue
                starttime = CustomTime.from_datetime(component.get("dtstart").dt)
                endtime = CustomTime.from_datetime(component.get("dtend").dt)
                if endtime and starttime.time() and endtime.time():
                    events.append(Event(starttime, endtime))

        return cls(events)

    @classmethod
    def from_events(cls, events: list[Event]) -> "Calendar":
        """
        Load events from a list.

        Args:
            events (list[Event]): List of events to load.
        """
        return cls(events)

    def _get_free_events(self, time_range: Event = None) -> list[Event]:
        """
        Get free events inside the given time range. A free event is defined as a
        time slot that is not occupied by any event.

        Args:
            time_range (Event, optional): The time range to check for free events.
                If not provided, the default is from 2025-05-02 07:00 to 2025-05-02 15:00.

        Returns:
            list[Event]: List of free events within the specified time range.
        """
        start_time = CustomTime(2025, 5, 2, 7).to_local_time()
        end_time = CustomTime(2025, 5, 2, 15).to_local_time()

        free_events = []
        current = start_time
        for event in self.events:
            if event.starttime.date() == start_time.date():
                event_start = max(event.starttime, start_time)
                event_end = min(event.endtime, end_time)
                if event_start > current:

                    begin_free_time = current

                    end_free_time = min(event_start, end_time)
                    free_events.append(Event(begin_free_time, end_free_time))

                current = max(current, event_end)

            if current > end_time:
                break

        return free_events
