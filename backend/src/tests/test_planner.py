from models.event import Event
from models.custom_calendar import Calendar
from models.calendar_combiner import CalendarCombiner
from models.custom_time import CustomTime


# Example input (Calendars with events that last at least 2 hours and have overlaps)
calendar1 = Calendar.from_events(
    [
        Event(CustomTime(2025, 5, 8, 7, 0), CustomTime(2025, 5, 8, 9, 30)),
        Event(CustomTime(2025, 5, 8, 10, 0), CustomTime(2025, 5, 8, 12, 0)),
        Event(CustomTime(2025, 5, 8, 13, 0), CustomTime(2025, 5, 8, 15, 0)),
        Event(CustomTime(2025, 5, 8, 15, 30), CustomTime(2025, 5, 8, 17, 30)),
        Event(CustomTime(2025, 5, 8, 18, 0), CustomTime(2025, 5, 8, 20, 0)),
    ]
)

calendar2 = Calendar.from_events(
    [
        Event(CustomTime(2025, 5, 8, 6, 30), CustomTime(2025, 5, 8, 8, 30)),
        Event(CustomTime(2025, 5, 8, 9, 0), CustomTime(2025, 5, 8, 11, 30)),
        Event(CustomTime(2025, 5, 8, 13, 0), CustomTime(2025, 5, 8, 15, 30)),
        Event(CustomTime(2025, 5, 8, 16, 0), CustomTime(2025, 5, 8, 18, 0)),
        Event(CustomTime(2025, 5, 8, 18, 30), CustomTime(2025, 5, 8, 20, 0)),
    ]
)


calendar3 = Calendar.from_events(
    [
        Event(CustomTime(2025, 5, 8, 6, 45), CustomTime(2025, 5, 8, 9, 0)),
        Event(CustomTime(2025, 5, 8, 9, 15), CustomTime(2025, 5, 8, 11, 0)),
        Event(CustomTime(2025, 5, 8, 13, 0), CustomTime(2025, 5, 8, 14, 30)),
        Event(CustomTime(2025, 5, 8, 14, 45), CustomTime(2025, 5, 8, 16, 30)),
        Event(CustomTime(2025, 5, 8, 17, 0), CustomTime(2025, 5, 8, 19, 30)),
    ]
)

# List of calendars
calendars = [calendar1, calendar2, calendar3]


print("CalendarAnalyzer:")
cal_analyzer = CalendarCombiner(calendars)
cal_analyzer.get_ranking()
cal_analyzer.print_ranking()
