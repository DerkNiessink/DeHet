from event import Event

from overlap_finder import find_all_overlaps


def get_sorted_overlaps(overlap: dict[tuple[int, ...], list[Event]]) -> list[Event]:
    flattened = [event for sublist in overlap.values() for event in sublist]
    return sorted(flattened, key=lambda x: x.duration, reverse=True)


def find_event_owners(
    overlap: dict[tuple[int, ...], list[Event]], events: list[Event]
) -> list[tuple[int, ...]]:
    return [key for event in events for key, val in overlap.items() if event in val]


def format_ranking(
    overlaps: list[dict[tuple[int, ...], list[Event]]],
) -> list[tuple[tuple[int, ...], Event]]:
    overlaps.reverse()
    ranking = []
    for overlap in overlaps:
        sorted_events = get_sorted_overlaps(overlap)
        participants_list = find_event_owners(overlap, sorted_events)

        for participants, event in zip(participants_list, sorted_events):
            ranking.append((participants, event))
    return ranking


def print_ranking(ranking: list[tuple[tuple[int, ...], Event]]) -> None:
    if not ranking:
        print("No overlapping events found.")
        return

    current_level = len(ranking[0][0])
    print("-" * 20)
    print(f"Ranking of calendars with {current_level} participants:")
    for participants, event in ranking:
        print(
            f"Participants: {participants}, Duration: {event.duration}, "
            f"Start: {event.starttime}, End: {event.endtime}"
        )
        print("-" * 5)


def return_ranking(calendars: list[list[Event]]) -> list[tuple[tuple[int, ...], Event]]:
    """
    Return and print a ranking of calendars based on overlapping event duration.
    """
    overlaps = find_all_overlaps(calendars)
    ranking = format_ranking(overlaps)
    print_ranking(ranking)
    return ranking
