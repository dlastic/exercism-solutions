def flatten(iterable: list, flattened=None) -> list:
    """Return a flattened list from a nested list, skipping None values."""
    if flattened is None:
        flattened = []
    if isinstance(iterable, list):
        for i in iterable:
            flatten(i, flattened)
    elif iterable is not None:
        flattened.append(iterable)
    return flattened
