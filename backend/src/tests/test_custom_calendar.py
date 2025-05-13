from models.custom_calendar import Calendar

calendar = Calendar.from_ics("ics/sacha@wearebit.com.ics")

for slot in calendar.free_events:
    print(f"Free slot: {slot.starttime} - {slot.endtime}")
