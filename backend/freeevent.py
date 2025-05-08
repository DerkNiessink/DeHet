from datetime import datetime
from dataclasses import dataclass


@dataclass
class FreeEvent:
    starttime: datetime
    endtime: datetime

    def duration(self):
        """Calculates the duration between starttime and endtime."""
        return self.endtime - self.starttime
