import csv
from event import Event


# SAME CODE AS IN OVERLAP FINDER AND RANKER
class CalendarAnalyzer:
    """
    Analyzes multiple calendars to find overlapping events and rank them based on duration and participation.

    Attributes:
        calendars (list[list[Event]]): A list of calendars, each containing a list of Event objects.
        overlaps (list[dict]): Stores overlapping events found at each level of merging.
        ranking (list): Ranked list of overlapping events with participant information.
    """

    def __init__(self, calendars: list[list[Event]]):
        """
        Initialize the analyzer with calendars to compare.

        This constructor computes all overlaps and generates a ranking of events.

        Args:
            calendars (list[list[Event]]): A list of event lists, one for each calendar.
        """
        self.calendars = calendars
        self.overlaps = []

        self.compute_all_overlaps()
        self.ranking = self._format_ranking()

    def get_ranking(self) -> None:
        """
        Return the ranking of overlapping events.
        """
        return self.ranking

    def print_ranking(self) -> None:
        """
        Print the current ranking of overlapping events to the console,
        grouped by number of participants.
        """
        if not self.ranking:
            print("No overlapping events found.")
            return

        current_level = None
        print("-" * 20)

        for participants, event in self.ranking:
            level = len(participants)
            if level != current_level:
                current_level = level
                print(f"\nRanking of calendars with {current_level} participants:")
                print("-" * 20)

            print(
                f"Participants: {participants}, Duration: {event.duration}, "
                f"Start: {event.starttime}, End: {event.endtime}"
            )
            print("-" * 5)

    def export_ranking(self, filepath: str) -> None:
        """
        Export the current ranking to a CSV file.

        Args:
            filepath (str): Path to the output CSV file.
        """
        with open(filepath, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Participants", "Start", "End", "Duration"])
            for participants, event in self.ranking:
                writer.writerow(
                    [participants, event.starttime, event.endtime, event.duration]
                )

    def find_pairwise_overlaps(
        self, calendars_subset: list[list[Event]] = None
    ) -> dict[tuple[int, int], list[Event]]:
        """
        Identify overlapping events between each pair of calendars.

        Args:
            calendars_subset (optional): If provided, use this instead of self.calendars.

        Returns:
            dict: Mapping of calendar index pairs to lists of overlapping events.
        """
        if calendars_subset is None:
            calendars_subset = self.calendars
        overlaps = {}
        for i in range(len(calendars_subset)):
            for j in range(i + 1, len(calendars_subset)):
                for event1 in calendars_subset[i]:
                    for event2 in calendars_subset[j]:
                        if event1.overlaps(event2):
                            overlap = event1.return_overlap(event2)
                            overlaps.setdefault((i, j), []).append(overlap)
        return overlaps

    def merge_overlaps(self) -> dict[tuple[int, ...], list[Event]]:
        """
        Merge pairwise overlaps to find multi-calendar overlaps.

        Returns:
            dict: Merged dictionary with participant group tuples as keys and overlapping events as values.
        """
        overlaps_list = list(self.overlaps[-1].values())
        new_overlaps = self.find_pairwise_overlaps(overlaps_list)
        merged_overlaps = {}

        for (key1, key2), value in new_overlaps.items():
            keys_list = list(self.overlaps[-1].keys())
            new_key = tuple(set(keys_list[key1] + keys_list[key2]))
            merged_overlaps[new_key] = value

        return merged_overlaps

    def compute_all_overlaps(self) -> None:
        """
        Iteratively compute all levels of overlapping events across the calendars.
        Updates self.overlaps with the result.
        """
        self.overlaps.append(self.find_pairwise_overlaps())

        while self.overlaps[-1]:
            self.overlaps.append(self.merge_overlaps())

        self.overlaps = self.overlaps[:-1]

    def _format_ranking(self) -> list[tuple[tuple[int, ...], Event]]:
        """
        Internal method to generate a ranked list of events from overlaps.

        Returns:
            list: List of (participants, event) tuples, sorted by duration.
        """
        ranking = []
        for overlap in reversed(self.overlaps):
            sorted_events = self._get_sorted_overlaps(overlap)
            participants_list = self._find_event_owners(overlap, sorted_events)

            for participants, event in zip(participants_list, sorted_events):
                ranking.append((participants, event))
        return ranking

    def _get_sorted_overlaps(self, overlap: dict) -> list[Event]:
        """
        Flatten and sort overlapping events by duration (descending).

        Args:
            overlap (dict): Dictionary of overlapping events.

        Returns:
            list: Sorted list of Event objects.
        """
        flattened = [event for sublist in overlap.values() for event in sublist]
        return sorted(flattened, key=lambda x: x.duration, reverse=True)

    def _find_event_owners(
        self, overlap: dict, events: list[Event]
    ) -> list[tuple[int, ...]]:
        """
        Match events to the participant groups they belong to.

        Args:
            overlap (dict): Dictionary mapping participant tuples to events.
            events (list): Events to find owners for.

        Returns:
            list: Participant tuples matching each event.
        """
        return [key for event in events for key, val in overlap.items() if event in val]
