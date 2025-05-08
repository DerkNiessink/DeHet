from datetime import datetime
from event import Event


def find_overlaps(calendars: list[list[Event]]) -> dict[tuple[int, int], Event]:
    """
    Check if calendars overlap.
    """
    overlaps = {}
    for i in range(len(calendars)):
        for j in range(i + 1, len(calendars)):
            if i == j:
                continue
            for event1 in calendars[i]:
                for event2 in calendars[j]:
                    if event1.overlaps(event2):
                        overlaps[(i, j)] = event1.return_overlap(event2)
    return overlaps
