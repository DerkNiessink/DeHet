import datetime
from dateutil import tz


class CustomTime(datetime.datetime):
    """
    Custom datetime class to handle time-related operations.
    """

    def __gt__(self, other: "CustomTime") -> bool:
        """Custom implementation for the > operator."""
        return self.time() > other.time()

    def __lt__(self, other: "CustomTime") -> bool:
        """Custom implementation for the < operator."""
        return self.time() < other.time()

    @classmethod
    def from_datetime(cls, dt: datetime.datetime) -> "CustomTime":
        """Convert a datetime to a CustomTime object."""

        if (
            not hasattr(dt, "hour")
            or not hasattr(dt, "minute")
            or not hasattr(dt, "second")
        ):
            dt = datetime.datetime(dt.year, dt.month, dt.day, 0, 0, 0)

        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    def to_local_time(self):
        """Convert a UTC datetime to local time."""
        if self.tzinfo is None:
            utc_time = self.replace(tzinfo=tz.tzutc())
        else:
            utc_time = self.astimezone(tz.tzutc())
        return utc_time.astimezone(tz.tzlocal())
