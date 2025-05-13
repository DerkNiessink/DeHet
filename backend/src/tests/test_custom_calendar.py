from src.models.custom_time import CustomTime
from src.models.custom_calendar import Calendar

calendar = Calendar("ics/sacha@wearebit.com.ics")

start_day = CustomTime(2025, 5, 2, 7).to_local_time()
end_day = CustomTime(2025, 5, 2, 15).to_local_time()
free_slots = calendar.get_free_events(start_day, end_day)
for slot in free_slots:
    print(f"Free slot: {slot.starttime} - {slot.endtime}")
