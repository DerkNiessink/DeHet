from models.event import Event


def find_pairwise_overlaps(
    calendars: list[list[Event]],
) -> (
    dict[tuple[int, int], list[Event]]
    | dict[tuple[tuple[int, ...], tuple[int, ...]], list[Event]]
):
    """
    Find overlapping events between each pair of calendars.
    Returns a dictionary mapping calendar index pairs to lists of their overlapping events.
    """
    overlaps = {}
    for i in range(len(calendars)):
        for j in range(i + 1, len(calendars)):
            for event1 in calendars[i]:
                for event2 in calendars[j]:
                    if event1.overlaps(event2):
                        overlap = event1.return_overlap(event2)
                        overlaps.setdefault((i, j), []).append(overlap)
    return overlaps


def merge_overlaps(
    overlaps: dict[tuple[int, ...], list[Event]],
) -> dict[tuple[int, ...], list[Event]]:
    """
    Merge overlapping events across multiple overlapping pairs to find common free slots.
    """
    # create a list of lists from all values in the dictionary
    overlaps_list = list(overlaps.values())
    new_overlaps = find_pairwise_overlaps(overlaps_list)
    merged_overlaps = {}

    for (key1, key2), value in new_overlaps.items():
        keys_list = list(overlaps.keys())
        new_key = tuple(set(keys_list[key1] + keys_list[key2]))
        merged_overlaps[new_key] = value

    return merged_overlaps


def find_all_overlaps(
    calendars: list[list[Event]],
) -> list[dict[tuple[int, ...], list[Event]]]:
    """
    Iteratively find all common overlapping time slots across all calendars.
    Returns a list of overlap dictionaries at each level of merging.
    """
    overlaps = [find_pairwise_overlaps(calendars)]

    # while not empty dict
    while overlaps[-1]:
        overlaps.append(merge_overlaps(overlaps[-1]))

    return overlaps[:-1]
