from icalendar import Calendar as iCalendar

from models.event import Event
from models.custom_time import CustomTime


class Calendar:
    """
    Class to parse and extract events from an iCalendar file.
    """

    def __init__(self, fn: str):
        with open(fn, "rb") as f:
            self.components = iCalendar.from_ical(f.read())
        self.events = self._extract_events()

    def _extract_events(self) -> list[Event]:
        events = []
        for component in self.components.walk():
            if component.name == "VEVENT":
                dtstart, dtend = component.get("dtstart"), component.get("dtend")
                if not dtstart or not dtend:
                    continue
                starttime = CustomTime.from_datetime(component.get("dtstart").dt)
                endtime = CustomTime.from_datetime(component.get("dtend").dt)
                if endtime and starttime.time() and endtime.time():
                    events.append(Event(starttime, endtime))
        return events

    def get_free_events(
        self, start_time: CustomTime, end_time: CustomTime
    ) -> list[Event]:
        """
        Get free events inside the given time range.

        Args:
            start_day (datetime): Start day to check for free events.
            end_day (datetime): End day to check for free events.

        Returns:
            list[Event]: List of free events between `start_day` and `end_day`.
        """

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
