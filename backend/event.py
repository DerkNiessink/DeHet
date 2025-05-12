from custom_time import CustomTime


class Event:
    def __init__(self, starttime: CustomTime, endtime: CustomTime):
        self.starttime = starttime.to_local_time()
        self.endtime = endtime.to_local_time()

    def __repr__(self):
        return f"Event({self.starttime}, {self.endtime})"

    @property
    def duration(self):
        """Calculates the duration between starttime and endtime."""
        return self.endtime - self.starttime

    def overlaps(self, other: "Event") -> bool:
        """Checks if two events overlap. Returns the overlapping event if they do."""
        return self.starttime < other.endtime and other.starttime < self.endtime

    def return_overlap(self, other: "Event") -> bool:
        """Returns the overlapping event if two events overlap."""
        start_overlap = max(self.starttime, other.starttime)
        end_overlap = min(self.endtime, other.endtime)
        return Event(start_overlap, end_overlap)
