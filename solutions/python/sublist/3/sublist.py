SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one: list, list_two: list) -> int:
    """Return the integer representing relation of two lists."""

    if list_one == list_two:
        return EQUAL
    if is_sublist(list_one, list_two):
        return SUBLIST
    if is_sublist(list_two, list_one):
        return SUPERLIST
    return UNEQUAL


def is_sublist(candidate: list, container: list) -> bool:
    """Return True if the first list is a contiguous sublist of the second."""

    candidate_len = len(candidate)
    container_len = len(container)

    return any(
        container[i : i + candidate_len] == candidate
        for i in range(0, container_len - candidate_len + 1)
    )
